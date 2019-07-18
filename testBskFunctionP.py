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
<<<<<<< HEAD
            sdA = bsk.sd.home
            sdH = bsk.sd.away
            if sdA not in ('0', '0.0', ''):
                sd = testCutOneP.cutOne(sdA, sdH)
                bsk.sd.home = sd[0]
                bsk.sd.away = sd[1]

=======
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
>>>>>>> 5e03a538acddc71e24d57275273e6c3be14560b2

            if '_' in league:
                noCal = testCutOneP.justCutOne_fun([bsk])
                enData = APHDC_noDB_pb2.ApHdcArr()
                enData.ParseFromString(noCal)
                noCalData = enData.aphdc
            else:
<<<<<<< HEAD
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
=======
                zfBK = testBKzf.calBKzf(source, gameType, homeL, awayL, homeO, awayO, homeDe, awayDe)
                bsk.twZF.homeZF.line = zfBK[0]
                bsk.twZF.awayZF.line = zfBK[1]
                if homeDe in('0', '0.0', ''):
                    # bsk.de.home = '0'
                    # bsk.de.away = '0'
                    if homeO in ('0', '0.0') or zfBK[0] == '0+0':
                        bsk.twZF.homeZF.odds = "0"
                        bsk.twZF.awayZF.odds = "0"
>>>>>>> 5e03a538acddc71e24d57275273e6c3be14560b2
                    else:
                        # 獨贏0或空不理
                        pass
                else:
<<<<<<< HEAD
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
=======
                    try:
                        homeDe
                        bsk.de.home = zfBK[2]
                        bsk.de.away = zfBK[3]
                    except:
                        pass
                    if homeO in ('0', '0.0') or zfBK[0] == '0+0':
                        bsk.twZF.homeZF.odds = '0'
                        bsk.twZF.awayZF.odds = '0'
>>>>>>> 5e03a538acddc71e24d57275273e6c3be14560b2
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
<<<<<<< HEAD
        print(str(e))
        # telegramBot("BSK錯誤")
=======
        # print(e)
        telegramBot("BSK錯誤")
>>>>>>> 5e03a538acddc71e24d57275273e6c3be14560b2


## 找錯誤用 
## testData 後面請填入錯誤的data 執行即可印出錯誤

<<<<<<< HEAD
# testData = 
# enData = APHDC_noDB_pb2.ApHdcArr()
# enData.ParseFromString(testData)
# Data = enData.aphdc
# out = basketball(Data)

=======
# testData = b'\n\xb3\x02\n\x03CMD\x12\x0fotherbasketball\x1a\x082nd half"\x08980092942\x010:\x132019-08-31 23:59:00B\x132019-07-10 10:46:00J\x05falseZ\xa2\x01\n 2019\xe5\xb9\xb4\xe4\xb8\x96\xe7\x95\x8c\xe6\x9d\xaf\xe7\xb1\x83\xe7\x90\x83\xe8\xb3\xbd_\xe5\x86\xa0\xe8\xbb\x8d\x12 2019\xe5\xb9\xb4\xe4\xb8\x96\xe7\x95\x8c\xe6\x9d\xaf\xe7\xaf\xae\xe7\x90\x83\xe8\xb5\x9b_\xe5\x86\xa0\xe5\x86\x9b\x1a\x17WORLD CUP 2019 - WINNER"\x15\n\x06\xe7\xbe\x8e\xe5\x9c\x8b\x1a\x06\xe7\xbe\x8e\xe5\x9b\xbd"\x03USA*,\n\x0c\xe5\x85\xb6\xe5\xae\x83\xe9\x9a\x8a\xe4\xbc\x8d\x1a\x0c\xe5\x85\xb6\xe5\xae\x83\xe9\x98\x9f\xe4\xbc\x8d"\x0eAny Other Teamj\x18\n\x0b\n\x04-0.0\x12\x031.1\x12\t\n\x04+0.0\x12\x016r\x0b\n\x030.0\x12\x010\x1a\x010\x92\x01\x06\n\x010\x12\x010\n\xca\x02\n\x03CMD\x12\x0fotherbasketball\x1a\x04full"\x08523229312\x010:\x132019-07-10 19:30:00B\x132019-07-10 10:46:00J\x05falseZ\xad\x01\n\x18\xe9\xa6\xac\xe4\xbe\x86\xe8\xa5\xbf\xe4\xba\x9e\xe8\x81\xb7\xe6\xa5\xad\xe8\x81\xaf\xe8\xb3\xbd\x12\x18\xe9\xa9\xac\xe6\x9d\xa5\xe8\xa5\xbf\xe4\xba\x9a\xe8\x81\x8c\xe4\xb8\x9a\xe8\x81\x94\xe8\xb5\x9b\x1a\x13MALAYSIA PRO LEAGUE"!\n\t\xe7\xb4\x85\xe7\x94\xb7\xe7\x88\xb5\x1a\t\xe7\xba\xa2\xe7\x94\xb7\xe7\x88\xb5"\tRed Baron*?\n\x15\xe8\xbe\xb2\xe5\xa0\xb4\xe4\xbf\xae\xe9\xa3\xbe\xe7\xb1\x83\xe7\x90\x83\xe9\x9a\x8a\x1a\x15\xe5\x86\x9c\xe5\x9c\xba\xe4\xbf\xae\xe9\xa5\xb0\xe7\xaf\xae\xe7\x90\x83\xe9\x98\x9f"\x0fFarmco Touch Upj\x1c\n\x0c\n\x04-3.5\x12\x041.91\x12\x0c\n\x04+3.5\x12\x041.91r\x11\n\x05144.5\x12\x031.9\x1a\x031.9\x92\x01\x0c\n\x041.94\x12\x041.94\n\xae\x02\n\x03CMD\x12\x0fotherbasketball\x1a\x04full"\x08959344192\x010:\x132019-07-10 21:15:00B\x132019-07-10 10:46:00J\x05falseZ\x93\x01\n\x18\xe9\xa6\xac\xe4\xbe\x86\xe8\xa5\xbf\xe4\xba\x9e\xe8\x81\xb7\xe6\xa5\xad\xe8\x81\xaf\xe8\xb3\xbd\x12\x18\xe9\xa9\xac\xe6\x9d\xa5\xe8\xa5\xbf\xe4\xba\x9a\xe8\x81\x8c\xe4\xb8\x9a\xe8\x81\x94\xe8\xb5\x9b\x1a\x13MALAYSIA PRO LEAGUE"\'\n\x0bJD\xe7\x8d\xa8\xe8\xa7\x92\xe7\x8d\xb8\x1a\x0bJD\xe7\x8b\xac\xe8\xa7\x92\xe5\x85\xbd"\x0bJD Unicorns*\x1f\n\x08NS\xe7\x9f\xa9\xe9\x99\xa3\x1a\x08NS\xe7\x9f\xa9\xe9\x98\xb5"\tNS Matrixj\x1c\n\x0c\n\x04+2.5\x12\x041.91\x12\x0c\n\x04-2.5\x12\x041.91r\x0f\n\x05148.5\x12\x031.8\x1a\x012\x92\x01\x0c\n\x041.94\x12\x041.94\n\x86\x03\n\x03CMD\x12\x0fotherbasketball\x1a\x04full"\x08892446462\x010:\x132019-07-10 17:00:00B\x132019-07-10 10:46:00J\x05falseZ\xe9\x01\n-\xe4\xb8\x89\xe5\xb0\x8d\xe4\xb8\x89\xe5\xa5\xb3\xe5\xad\x90\xe4\xbf\x82\xe5\x88\x97\xe8\xb3\xbd (\xe5\x9c\xa8\xe8\x91\x89\xe5\x8d\xa1\xe6\x8d\xb7\xe7\x90\xb3\xe5\xa0\xa1)\x12-\xe4\xb8\x89\xe5\xaf\xb9\xe4\xb8\x89\xe5\xa5\xb3\xe5\xad\x90\xe7\xb3\xbb\xe5\x88\x97\xe8\xb5\x9b (\xe5\x9c\xa8\xe5\x8f\xb6\xe5\x8d\xa1\xe6\x8d\xb7\xe7\x90\xb3\xe5\xa0\xa1)\x1a"3X3 WOMEN SERIES (IN EKATERINBURG)".\n\x0f\xe4\xbf\x84\xe7\xbe\x85\xe6\x96\xaf (\xe5\xa5\xb3)\x1a\x0f\xe4\xbf\x84\xe7\xbd\x97\xe6\x96\xaf (\xe5\xa5\xb3)"\nRussia (w)*5\n\x12\xe7\xbe\x85\xe9\xa6\xac\xe5\xb0\xbc\xe4\xba\x9e (\xe5\xa5\xb3)\x1a\x12\xe7\xbd\x97\xe9\xa9\xac\xe5\xb0\xbc\xe4\xba\x9a (\xe5\xa5\xb3)"\x0bRomania (w)j\x1c\n\x0c\n\x04-4.5\x12\x041.75\x12\x0c\n\x04+4.5\x12\x042.09r\x11\n\x0431.5\x12\x032.0\x1a\x041.82\x92\x01\x0c\n\x041.94\x12\x041.94\n\xfe\x02\n\x03CMD\x12\x0fotherbasketball\x1a\x04full"\x08350545912\x010:\x132019-07-10 17:20:00B\x132019-07-10 10:46:00J\x05falseZ\xe0\x01\n-\xe4\xb8\x89\xe5\xb0\x8d\xe4\xb8\x89\xe5\xa5\xb3\xe5\xad\x90\xe4\xbf\x82\xe5\x88\x97\xe8\xb3\xbd (\xe5\x9c\xa8\xe8\x91\x89\xe5\x8d\xa1\xe6\x8d\xb7\xe7\x90\xb3\xe5\xa0\xa1)\x12-\xe4\xb8\x89\xe5\xaf\xb9\xe4\xb8\x89\xe5\xa5\xb3\xe5\xad\x90\xe7\xb3\xbb\xe5\x88\x97\xe8\xb5\x9b (\xe5\x9c\xa8\xe5\x8f\xb6\xe5\x8d\xa1\xe6\x8d\xb7\xe7\x90\xb3\xe5\xa0\xa1)\x1a"3X3 WOMEN SERIES (IN EKATERINBURG)"*\n\x0c\xe6\xbf\x9b\xe5\x8f\xa4 (\xe5\xa5\xb3)\x1a\x0c\xe8\x92\x99\xe5\x8f\xa4 (\xe5\xa5\xb3)"\x0cMongolia (w)*0\n\x0c\xe6\x8d\xb7\xe5\x89\x8b (\xe5\xa5\xb3)\x1a\x0c\xe6\x8d\xb7\xe5\x85\x8b (\xe5\xa5\xb3)"\x12Czech Republic (w)j\x1c\n\x0c\n\x04+5.5\x12\x042.06\x12\x0c\n\x04-5.5\x12\x041.78r\x12\n\x0430.5\x12\x042.08\x1a\x041.74\x92\x01\x0c\n\x041.94\x12\x041.94\n\xf0\x02\n\x03CMD\x12\x0fotherbasketball\x1a\x04full"\x08744074012\x010:\x132019-07-10 17:40:00B\x132019-07-10 10:46:00J\x05falseZ\xd3\x01\n-\xe4\xb8\x89\xe5\xb0\x8d\xe4\xb8\x89\xe5\xa5\xb3\xe5\xad\x90\xe4\xbf\x82\xe5\x88\x97\xe8\xb3\xbd (\xe5\x9c\xa8\xe8\x91\x89\xe5\x8d\xa1\xe6\x8d\xb7\xe7\x90\xb3\xe5\xa0\xa1)\x12-\xe4\xb8\x89\xe5\xaf\xb9\xe4\xb8\x89\xe5\xa5\xb3\xe5\xad\x90\xe7\xb3\xbb\xe5\x88\x97\xe8\xb5\x9b (\xe5\x9c\xa8\xe5\x8f\xb6\xe5\x8d\xa1\xe6\x8d\xb7\xe7\x90\xb3\xe5\xa0\xa1)\x1a"3X3 WOMEN SERIES (IN EKATERINBURG)"%\n\x0c\xe7\xbe\x8e\xe5\x9c\x8b (\xe5\xa5\xb3)\x1a\x0c\xe7\xbe\x8e\xe5\x9b\xbd (\xe5\xa5\xb3)"\x07USA (w)*(\n\x0c\xe6\xb3\x95\xe5\x9c\x8b (\xe5\xa5\xb3)\x1a\x0c\xe6\xb3\x95\xe5\x9b\xbd (\xe5\xa5\xb3)"\nFrance (w)j\x1c\n\x0c\n\x04+4.5\x12\x041.92\x12\x0c\n\x04-4.5\x12\x041.92r\x11\n\x0431.5\x12\x032.0\x1a\x041.82\x92\x01\x0c\n\x041.94\x12\x041.94\n\x88\x03\n\x03CMD\x12\x0fotherbasketball\x1a\x04full"\x08490934742\x010:\x132019-07-10 18:00:00B\x132019-07-10 10:46:00J\x05falseZ\xea\x01\n-\xe4\xb8\x89\xe5\xb0\x8d\xe4\xb8\x89\xe5\xa5\xb3\xe5\xad\x90\xe4\xbf\x82\xe5\x88\x97\xe8\xb3\xbd (\xe5\x9c\xa8\xe8\x91\x89\xe5\x8d\xa1\xe6\x8d\xb7\xe7\x90\xb3\xe5\xa0\xa1)\x12-\xe4\xb8\x89\xe5\xaf\xb9\xe4\xb8\x89\xe5\xa5\xb3\xe5\xad\x90\xe7\xb3\xbb\xe5\x88\x97\xe8\xb5\x9b (\xe5\x9c\xa8\xe5\x8f\xb6\xe5\x8d\xa1\xe6\x8d\xb7\xe7\x90\xb3\xe5\xa0\xa1)\x1a"3X3 WOMEN SERIES (IN EKATERINBURG)"5\n\x12\xe7\x99\xbd\xe4\xbf\x84\xe7\xbe\x85\xe6\x96\xaf (\xe5\xa5\xb3)\x1a\x12\xe7\x99\xbd\xe4\xbf\x84\xe7\xbd\x97\xe6\x96\xaf (\xe5\xa5\xb3)"\x0bBelarus (w)*/\n\x0f\xe5\x8c\x88\xe7\x89\x99\xe5\x88\xa9 (\xe5\xa5\xb3)\x1a\x0f\xe5\x8c\x88\xe7\x89\x99\xe5\x88\xa9 (\xe5\xa5\xb3)"\x0bHungary (w)j\x1c\n\x0c\n\x04+3.5\x12\x041.92\x12\x0c\n\x04-3.5\x12\x041.92r\x12\n\x0431.5\x12\x041.96\x1a\x041.86\x92\x01\x0c\n\x041.94\x12\x041.94'

# enData = APHDC_noDB_pb2.ApHdcArr()
# enData.ParseFromString(testData)
# Data = enData.aphdc
# basketball(Data)

# f = open('basketball_early.bin','rb')
# print(f.read())
>>>>>>> 5e03a538acddc71e24d57275273e6c3be14560b2
