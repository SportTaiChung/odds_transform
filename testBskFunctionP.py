# -*- coding:utf-8 -*-
import copy
import APHDC_noDB_pb2
import testBKzf
import testBKds
import testCutOneP
from sendMQ import telegramBot
import datetime as dt


def basketball(Data):
    try:
        sendData = []
        for bsk in Data:
            source = bsk.source
            gameType = bsk.game_type
            league = bsk.information.league
            homeL = bsk.usZF.homeZF.line
            awayL = bsk.usZF.awayZF.line
            homeO = bsk.usZF.homeZF.odds
            awayO = bsk.usZF.awayZF.odds
            dsline = bsk.usDS.line
            over = bsk.usDS.over
            under = bsk.usDS.under
            try:
                sdA = bsk.sd.home
                sdH = bsk.sd.away
                if sdA != '0':
                    sd = testCutOneP.cutOne(sdA, sdH)
                    bsk.sd.home = sd[0]
                    bsk.sd.away = sd[1]
            except:
                pass
            try:
                homeDe = bsk.de.home
                awayDe = bsk.de.away
            except:
                pass

            if '_' in league:
                noCal = testCutOneP.justCutOne_fun([bsk])
                enData = APHDC_noDB_pb2.ApHdcArr()
                enData.ParseFromString(noCal)
                noCalData = enData.aphdc
            else:
                zfBK = testBKzf.calBKzf(source, gameType, homeL, awayL, homeO, awayO, homeDe, awayDe)
                bsk.twZF.homeZF.line = zfBK[0]
                bsk.twZF.awayZF.line = zfBK[1]
                if homeDe in('0', '0.0', ''):
                    # bsk.de.home = '0'
                    # bsk.de.away = '0'
                    if homeO in ('0', '0.0') or zfBK[0] == '0+0':
                        pass
                        # bsk.twZF.homeZF.odds = "0"
                        # bsk.twZF.awayZF.odds = "0"
                    else:
                        bsk.twZF.homeZF.odds = "0.95"
                        bsk.twZF.awayZF.odds = "0.95"
                else:
                    bsk.de.home = zfBK[2]
                    bsk.de.away = zfBK[3]
                    if homeO in ('0', '0.0') or zfBK[0] == '0+0':
                        pass
                        # bsk.twZF.homeZF.odds = '0'
                        # bsk.twZF.awayZF.odds = '0'
                    else:
                        bsk.twZF.homeZF.odds = "0.95"
                        bsk.twZF.awayZF.odds = "0.95"

                dsBK = testBKds.calBKds(source, dsline, over, under)
                bsk.twDS.line = dsBK
                if over in('0', "0.0") or dsBK == '0+0':
                    pass
                    # bsk.twDS.over = "0"
                    # bsk.twDS.under = "0"
                else:
                    bsk.twDS.over = "0.94"
                    bsk.twDS.under = "0.94"

            sendData.append(copy.deepcopy(bsk))
       
        # print(sendData)
        datas = APHDC_noDB_pb2.ApHdcArr()
        datas.aphdc.extend(sendData)
        data = datas.SerializeToString()  #變成byte
        return data
    except Exception as e:
        # print(e)
        telegramBot("BSK錯誤")


## 找錯誤用 
## testData 後面請填入錯誤的data 執行即可印出錯誤

# testData = 
# enData = APHDC_noDB_pb2.ApHdcArr()
# enData.ParseFromString(testData)
# Data = enData.aphdc
# basketball(Data)

# f = open('basketball_early.bin','rb')
# print(f.read())