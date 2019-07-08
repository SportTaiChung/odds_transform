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
                        bsk.twZF.homeZF.odds = "0"
                        bsk.twZF.awayZF.odds = "0"
                    else:
                        bsk.twZF.homeZF.odds = "0.95"
                        bsk.twZF.awayZF.odds = "0.95"
                else:
                    bsk.de.home = zfBK[2]
                    bsk.de.away = zfBK[3]
                    if homeO in ('0', '0.0') or zfBK[0] == '0+0':
                        bsk.twZF.homeZF.odds = '0'
                        bsk.twZF.awayZF.odds = '0'
                    else:
                        bsk.twZF.homeZF.odds = "0.95"
                        bsk.twZF.awayZF.odds = "0.95"

                dsBK = testBKds.calBKds(source, dsline, over, under)
                bsk.twDS.line = dsBK
                if over in('0', "0.0") or dsBK == '0+0':
                    bsk.twDS.over = "0"
                    bsk.twDS.under = "0"
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

# testData = b'\n\x93\x03\n\x03CMD\x12\x0fotherbasketball\x1a\x04full"\x08844536372\x010:\x132019-07-08 11:30:00B\x132019-07-08 11:19:36J\x05falseZ\xf4\x01\n3\xe7\xbe\x8e\xe5\x9c\x8b\xe8\x81\xb7\xe6\xa5\xad\xe7\xb1\x83\xe7\x90\x83\xe5\xa4\x8f\xe5\xad\xa3\xe8\x81\xaf\xe8\xb3\xbd (\xe5\x9c\xa8\xe6\x8b\x89\xe6\x96\xaf\xe7\xb6\xad\xe5\x8a\xa0\xe6\x96\xaf)\x123\xe7\xbe\x8e\xe5\x9b\xbd\xe8\x81\x8c\xe4\xb8\x9a\xe7\xaf\xae\xe7\x90\x83\xe5\xa4\x8f\xe5\xad\xa3\xe8\x81\x94\xe8\xb5\x9b (\xe5\x9c\xa8\xe6\x8b\x89\xe6\x96\xaf\xe7\xbb\xb4\xe5\x8a\xa0\xe6\x96\xaf)\x1a NBA SUMMER LEAGUE (IN LAS VEGAS)"/\n\x0f\xe6\xb4\x9b\xe6\x9d\x89\xe7\xa3\xaf\xe5\xbf\xab\xe8\x88\xb9\x1a\x0f\xe6\xb4\x9b\xe6\x9d\x89\xe7\x9f\xb6\xe5\xbf\xab\xe8\x88\xb9"\x0bLA Clippers*5\n\x0f\xe5\xad\x9f\xe8\x8f\xb2\xe6\x96\xaf\xe7\x81\xb0\xe7\x86\x8a\x1a\x0f\xe5\xad\x9f\xe8\x8f\xb2\xe6\x96\xaf\xe7\x81\xb0\xe7\x86\x8a"\x11Memphis Grizzliesj\x1c\n\x0c\n\x04+6.5\x12\x041.92\x12\x0c\n\x04-6.5\x12\x041.94r\x13\n\x05174.5\x12\x041.82\x1a\x042.02\x92\x01\x0c\n\x041.94\x12\x041.94\n\x86\x04\n\x03CMD\x12\x0fotherbasketball\x1a\x021q"\x08306630932\x010:\x132019-07-08 11:30:00B\x132019-07-08 11:19:36J\x05falseZ\xea\x02\n>\xe7\xbe\x8e\xe5\x9c\x8b\xe8\x81\xb7\xe6\xa5\xad\xe7\xb1\x83\xe7\x90\x83\xe5\xa4\x8f\xe5\xad\xa3\xe8\x81\xaf\xe8\xb3\xbd(\xe5\x9c\xa8\xe6\x8b\x89\xe6\x96\xaf\xe7\xb6\xad\xe5\x8a\xa0\xe6\x96\xaf) - \xe7\xac\xac\xe4\xb8\x80\xe7\xaf\x80\x12>\xe7\xbe\x8e\xe5\x9b\xbd\xe8\x81\x8c\xe4\xb8\x9a\xe7\xaf\xae\xe7\x90\x83\xe5\xa4\x8f\xe5\xad\xa3\xe8\x81\x94\xe8\xb5\x9b(\xe5\x9c\xa8\xe6\x8b\x89\xe6\x96\xaf\xe7\xbb\xb4\xe5\x8a\xa0\xe6\x96\xaf) - \xe7\xac\xac\xe4\xb8\x80\xe8\x8a\x82\x1a.NBA SUMMER LEAGUE (IN LAS VEGAS) - 1ST QUARTER"X\n\x1c\xe6\xb4\x9b\xe6\x9d\x89\xe7\xa3\xaf\xe5\xbf\xab\xe8\x88\xb9  (\xe7\xac\xac\xe4\xb8\x80\xe7\xaf\x80)\x1a\x1c\xe6\xb4\x9b\xe6\x9d\x89\xe7\x9f\xb6\xe5\xbf\xab\xe8\x88\xb9  (\xe7\xac\xac\xe4\xb8\x80\xe8\x8a\x82)"\x1aLA Clippers  (1st Quarter)*^\n\x1c\xe5\xad\x9f\xe8\x8f\xb2\xe6\x96\xaf\xe7\x81\xb0\xe7\x86\x8a  (\xe7\xac\xac\xe4\xb8\x80\xe7\xaf\x80)\x1a\x1c\xe5\xad\x9f\xe8\x8f\xb2\xe6\x96\xaf\xe7\x81\xb0\xe7\x86\x8a  (\xe7\xac\xac\xe4\xb8\x80\xe8\x8a\x82)" Memphis Grizzlies  (1st Quarter)j\x1c\n\x0c\n\x04+2.0\x12\x041.74\x12\x0c\n\x04-2.0\x12\x042.11r\x12\n\x0443.5\x12\x041.76\x1a\x042.06\x92\x01\x0c\n\x041.94\x12\x041.94'
# testData = b'\n\xb3\x02\n\x03CMD\x12\x0fotherbasketball\x1a\x082nd half"\x08980092942\x010:\x132019-08-31 23:59:00B\x132019-07-08 11:43:37J\x05falseZ\xa2\x01\n 2019\xe5\xb9\xb4\xe4\xb8\x96\xe7\x95\x8c\xe6\x9d\xaf\xe7\xb1\x83\xe7\x90\x83\xe8\xb3\xbd_\xe5\x86\xa0\xe8\xbb\x8d\x12 2019\xe5\xb9\xb4\xe4\xb8\x96\xe7\x95\x8c\xe6\x9d\xaf\xe7\xaf\xae\xe7\x90\x83\xe8\xb5\x9b_\xe5\x86\xa0\xe5\x86\x9b\x1a\x17WORLD CUP 2019 - WINNER"\x15\n\x06\xe7\xbe\x8e\xe5\x9c\x8b\x1a\x06\xe7\xbe\x8e\xe5\x9b\xbd"\x03USA*,\n\x0c\xe5\x85\xb6\xe5\xae\x83\xe9\x9a\x8a\xe4\xbc\x8d\x1a\x0c\xe5\x85\xb6\xe5\xae\x83\xe9\x98\x9f\xe4\xbc\x8d"\x0eAny Other Teamj\x18\n\x0b\n\x04-0.0\x12\x031.1\x12\t\n\x04+0.0\x12\x016r\x0b\n\x030.0\x12\x010\x1a\x010\x92\x01\x06\n\x010\x12\x010'

# enData = APHDC_noDB_pb2.ApHdcArr()
# enData.ParseFromString(testData)
# Data = enData.aphdc
# basketball(Data)