# -*- coding:utf-8 -*-
import copy
import APHDC_noDB_pb2
import testCutOneP
import testBSzf
from sendMQ import telegramBot
import datetime as dt

def hockey(Data):
    try:
        sendData = []
        for hc in Data:
            source = hc.source
            league = hc.information.league
            gameType = hc.game_type
            gameClass = hc.game_class
            homeL = hc.usZF.homeZF.line
            awayL = hc.usZF.awayZF.line
            homeO = hc.usZF.homeZF.odds
            awayO = hc.usZF.awayZF.odds
            line = hc.usDS.line
            over = hc.usDS.over
            under = hc.usDS.under
            try:
                homeDe = hc.de.home
                awayDe = hc.de.away
                if homeDe in ('0.0', ''):
                    homeDe = '0'
                    awayDe = '0'
            except:
                pass

            if  "NHL美國冰球聯季後賽(含加時賽)" not in league:
                noCal = testCutOneP.justCutOne_fun([hc])
                enData = APHDC_noDB_pb2.ApHdcArr()
                enData.ParseFromString(noCal)
                noCalData = enData.aphdc
            elif '總得分' in league:
                noCal = testCutOneP.justCutOne_fun([hc])
                enData = APHDC_noDB_pb2.ApHdcArr()
                enData.ParseFromString(noCal)
                noCalData = enData.aphdc
            else:
                if 'full' in gameType:
                    zfBS = testBSzf.calBSzf(source, gameClass, gameType, homeL, awayL, homeO, awayO, homeDe, awayDe)
                    hc.twZF.homeZF.line = zfBS[0]
                    hc.twZF.awayZF.line = zfBS[1]

                    ## 如果獨贏為0 讓分獨贏都關 因為算是需要讓分及獨贏缺一不可
                    if homeDe == '0' or zfBS[0] == '0+0':
                        pass
                        # hc.twZF.homeZF.odds = "0"
                        # hc.twZF.awayZF.odds = "0"
                        # hc.de.home = '0'
                        # hc.de.away = '0'
                    else:
                        hc.de.home = zfBS[2]
                        hc.de.away = zfBS[3]
                        if homeO == '0':
                            pass
                            # hc.twZF.homeZF.odds = "0"
                            # hc.twZF.awayZF.odds = "0"
                        else:
                            hc.twZF.homeZF.odds = "0.95"
                            hc.twZF.awayZF.odds = "0.95"


                    ## 一輸二贏 (美盤讓分盤口減一)
                    if homeO != '0':
                        hc.esre.let = 1 if "-" in homeL else 2
                        hc.esre.home = zfBS[4]
                        hc.esre.away = zfBS[5]

                    ## 大小
                    if over in ('0.0', '0'):
                        pass
                        # hc.twDS.line = '0+0'
                        # hc.twDS.over = '0'
                        # hc.twDS.under = '0'
                    else:
                        dsBS = testCutOneP.cutOne(over, under)
                        if '.5' in str(float(line)):
                            line = line
                        else:
                            line = str(float(line)).replace('.0', '+0')
                        hc.twDS.line = line
                        hc.twDS.over = dsBS[0]
                        hc.twDS.under = dsBS[1]
            sendData.append(copy.deepcopy(hc))

        # print(sendData)
        datas = APHDC_noDB_pb2.ApHdcArr()
        datas.aphdc.extend(sendData)
        data = datas.SerializeToString()  #變成byte
        return data
    except Exception as e:
        telegramBot("HC錯誤")

## 找錯誤用 
## testData 後面請填入錯誤的data 執行即可印出錯誤

# testData = 
# enData = GAMEDB_pb2.GdHdcArr()
# enData.ParseFromString(testData)
# Data = enData.gdhdc
# hockey(Data)