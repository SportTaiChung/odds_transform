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
            sdA = bsk.sd.home
            sdH = bsk.sd.away
            if sdA not in ('0', '0.0', ''):
                sd = testCutOneP.cutOne(sdA, sdH)
                bsk.sd.home = sd[0]
                bsk.sd.away = sd[1]


            if '_' in league:
                noCal = testCutOneP.justCutOne_fun([bsk])
                enData = APHDC_noDB_pb2.ApHdcArr()
                enData.ParseFromString(noCal)
                noCalData = enData.aphdc
            else:
                homeL = bsk.usZF.homeZF.line
                awayL = bsk.usZF.awayZF.line
                homeO = bsk.usZF.homeZF.odds
                awayO = bsk.usZF.awayZF.odds
                homeDe = bsk.de.home
                awayDe = bsk.de.away
            
                if homeO == '':
                    # 讓分空不理
                    pass
                elif homeO in ('0', '0.0'):
                    # 讓分要給0
                    bsk.twZF.homeZF.line = "0"
                    bsk.twZF.awayZF.line = "0"
                    bsk.twZF.homeZF.odds = "0"
                    bsk.twZF.awayZF.odds = "0"
                    if homeDe not in ('0', '0.0', ''):
                        # 獨贏有值要減1
                        de = testCutOneP.cutOne(homeDe, awayDe)
                        bsk.de.home = de[0]
                        bsk.de.away = de[1]
                    else:
                        # 獨贏0或空不理
                        pass
                else:
                    # 讓分要計算
                    zfBK = testBKzf.calBKzf(source, gameType, homeL, awayL, homeO, awayO, homeDe, awayDe)
                    bsk.twZF.homeZF.line = zfBK[0]
                    bsk.twZF.awayZF.line = zfBK[1]

                    if zfBK[2] == '0.0':
                        # 獨贏是0或空不理
                        if zfBK[0] == '0+0':
                            #讓分算錯關盤
                            bsk.twZF.homeZF.odds = "0"
                            bsk.twZF.awayZF.odds = "0"
                        else:
                            #讓分正確給0.95
                            bsk.twZF.homeZF.odds = "0.95"
                            bsk.twZF.awayZF.odds = "0.95"
                    else:
                        # 獨贏有值
                        bsk.de.home = zfBK[2]
                        bsk.de.away = zfBK[3]
                        if zfBK[0] == '0+0':
                            #讓分算錯關盤
                            bsk.twZF.homeZF.odds = '0'
                            bsk.twZF.awayZF.odds = '0'
                        else:
                            #讓分正確給0.95
                            bsk.twZF.homeZF.odds = "0.95"
                            bsk.twZF.awayZF.odds = "0.95"

                dsline = bsk.usDS.line
                over = bsk.usDS.over
                under = bsk.usDS.under

                if over in (''):
                    pass
                elif over in ('0', '0.0'):
                    bsk.twDS.line = "0"
                    bsk.twDS.over = "0"
                    bsk.twDS.under = "0"
                else:
                    dsBK = testBKds.calBKds(source, dsline, over, under)
                    bsk.twDS.line = dsBK
                    if dsBK == '0+0':
                        # 大小算錯觀盤
                        bsk.twDS.over = "0"
                        bsk.twDS.under = "0"
                    else:
                        # 大小正確給0.95
                        bsk.twDS.over = "0.94"
                        bsk.twDS.under = "0.94"

            sendData.append(copy.deepcopy(bsk))
        
        # print(sendData)
        datas = APHDC_noDB_pb2.ApHdcArr()
        datas.aphdc.extend(sendData)
        data = datas.SerializeToString()  #變成byte
        return data
    except Exception as e:
        print(str(e))
        # telegramBot("BSK錯誤")


## 找錯誤用 
## testData 後面請填入錯誤的data 執行即可印出錯誤

# testData = 
# enData = APHDC_noDB_pb2.ApHdcArr()
# enData.ParseFromString(testData)
# Data = enData.aphdc
# out = basketball(Data)

