import copy
import APHDC_pb2
import testBSzf
import testBSds
import testBSde
import testCutOneP
from sendMQ import telegramBot
import datetime as dt

def baseballMix(Data):
    try:
        sendData = []
        noCalList = []
        for bs in Data:
            source = bs.source
            league = bs.information.league
            gameType = bs.game_type
            gameClass = bs.game_class
            homeDe = bs.de.home
            awayDe = bs.de.away
            if homeDe == '0.0' or homeDe == '':
                homeDe = '0'
                awayDe = '0'
            homeL = bs.usZF.homeZF.line
            awayL = bs.usZF.awayZF.line
            homeO = bs.usZF.homeZF.odds
            awayO = bs.usZF.awayZF.odds
            line = bs.usDS.line
            over = bs.usDS.over
            under = bs.usDS.under


            if '_' in league:
                noCalList.append(bs)
                noCal = testCutOneP.justCutOne_fun(noCalList)
                enData = APHDC_pb2.ApHdcArr()
                enData.ParseFromString(noCal)
                noCalData = enData.aphdc
                for no in noCalData:
                    no
            elif "總得分" in league:
                dsBS = testBSds.calBSds(source, gameClass, gameType, line, over, under)
                bs.twDS.line = dsBS
                if over == '0' or over == "0.0" or dsBS == '0+0':
                    bs.twDS.over = "0"
                    bs.twDS.under = "0"
                else:
                    bs.twDS.over = "0.94"
                    bs.twDS.under = "0.94"
                bs.twZF.homeZF.line = '0+0'
                bs.twZF.homeZF.odds = '0'
                bs.twZF.awayZF.line = '0+0'
                bs.twZF.awayZF.odds = '0'

            else:
                dsBS = testBSds.calBSds(source, gameClass, gameType, line, over, under)
                bs.twDS.line = dsBS
                if over == '0' or over == "0.0" or dsBS == '0+0':
                    bs.twDS.over = "0"
                    bs.twDS.under = "0"
                else:
                    bs.twDS.over = "0.94"
                    bs.twDS.under = "0.94"

                #上半場
                if gameType == '1st half':
                    zfBS2 = testBSzf.calBSzf(source, gameClass, gameType, homeL, awayL, homeO, awayO, homeDe, awayDe)
                    bs.de.home = zfBS2[2]
                    bs.de.away = zfBS2[3]
                    bs.twZF.homeZF.line = zfBS2[0]
                    bs.twZF.awayZF.line = zfBS2[1]
                    if homeO == '0' or zfBS2[0] == '0+0':
                        bs.twZF.homeZF.odds = "0"
                        bs.twZF.awayZF.odds = "0"
                    else:
                        bs.twZF.homeZF.odds = "0.95"
                        bs.twZF.awayZF.odds = "0.95"
                #全場
                else:
                    # 若 沒讓分 有獨贏 用獨贏算讓分的算法
                    if homeDe != '0':
                        if homeO in ('0', '', '0.0'): #沒讓分有獨贏
                            zfBS1 = testBSde.calBSde(source, gameClass, gameType, homeDe, awayDe)
                            bs.twZF.homeZF.line = zfBS1[0]
                            bs.twZF.awayZF.line = zfBS1[1]
                            if homeDe == '0' or zfBS1[0] == '0+0':
                                bs.twZF.homeZF.odds = "0"
                                bs.twZF.awayZF.odds = "0"
                                bs.de.home = '0'
                                bs.de.away = '0'
                            else:
                                bs.twZF.homeZF.odds = "0.95"
                                bs.twZF.awayZF.odds = "0.95"
                                bs.de.home = zfBS1[2]
                                bs.de.away = zfBS1[3]
                        # 若 有讓分 有獨贏 用讓分＋獨贏的算法
                        else:  #有獨贏有讓分
                            zfBS2 = testBSzf.calBSzf(source, gameClass, gameType, homeL, awayL, homeO, awayO, homeDe, awayDe)
                            bs.de.home = zfBS2[2]
                            bs.de.away = zfBS2[3]
                            bs.twZF.homeZF.line = zfBS2[0]
                            bs.twZF.awayZF.line = zfBS2[1]
                            if homeO == '0' or '0+0' == zfBS2[0]:
                                bs.twZF.homeZF.odds = "0"
                                bs.twZF.awayZF.odds = "0"
                            else:
                                bs.twZF.homeZF.odds = "0.95"
                                bs.twZF.awayZF.odds = "0.95"

                            ## 一輸二贏 (美盤讓分盤口減一)
                            bs.esre.let = 1 if "-" in homeL else 2
                            bs.esre.home = zfBS2[4]
                            bs.esre.away = zfBS2[5]
              

            sendData.append(copy.deepcopy(bs))
        # print(sendData)
        datas = APHDC_pb2.ApHdcArr()
        datas.aphdc.extend(sendData)
        data = datas.SerializeToString()  #變成byte
        return data

    except Exception as e:
        telegramBot("BS錯誤")
        datas = APHDC_pb2.ApHdcArr()
        datas.aphdc.extend(Data)
        data = datas.SerializeToString()
        BSfile = open('bs.log','a')
        BSfile.write(str(data)+'\n'+str(e)+'\n'+dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')+'\n')



# f = b'\n\xa1\x02\n\x04PS38\x12\x03mlb\x1a\x081st half"\n9824237461*\x0c149.28.23.642\x010:\x132019-05-07 00:35:00B\x132019-05-06 18:24:11J\x05falseRv\n\x1b\xe7\xbe\x8e\xe5\x9c\x8b\xe8\x81\xb7\xe6\xa3\x92\xe5\xa4\xa7\xe8\x81\xaf\xe7\x9b\x9f (MLB)\x12\x0c0_9824237461\x1a&\n!\xe8\xbe\x9b\xe8\xbe\x9b\xe9\x82\xa3\xe6\x8f\x90\xe7\xb4\x85\xe4\xba\xba(A. Desclafani)\x12\x010"!\n\x1c\xe8\x88\x8a\xe9\x87\x91\xe5\xb1\xb1\xe5\xb7\xa8\xe4\xba\xba(D. Pomeranz)\x12\x010Z\x06\n\x010\x12\x010b\x1e\n\r\n\x04-0.5\x12\x052.010\x12\r\n\x04+0.5\x12\x051.862j\x13\n\x034.5\x12\x052.010\x1a\x051.869\x82\x01\x06\n\x010\x12\x010\n\x9e\x02\n\x04PS38\x12\x03mlb\x1a\x081st half"\n9825282541*\x0c149.28.23.642\x010:\x132019-05-07 06:10:00B\x132019-05-06 18:24:11J\x05falseRs\n\x1b\xe7\xbe\x8e\xe5\x9c\x8b\xe8\x81\xb7\xe6\xa3\x92\xe5\xa4\xa7\xe8\x81\xaf\xe7\x9b\x9f (MLB)\x12\x0c0_9825282541\x1a\'\n"\xe5\x85\x8b\xe9\x87\x8c\xe5\xa4\xab\xe8\x98\xad\xe5\x8d\xb0\xe5\x9c\xb0\xe5\xae\x89\xe4\xba\xba(T. Bauer)\x12\x010"\x1d\n\x18\xe8\x8a\x9d\xe5\x8a\xa0\xe5\x93\xa5\xe7\x99\xbd\xe8\xa5\xaa(I. Nova)\x12\x010Z\x06\n\x010\x12\x010b\x1e\n\r\n\x04-1.0\x12\x051.862\x12\r\n\x04+1.0\x12\x052.000j\x13\n\x034.5\x12\x051.840\x1a\x052.040\x82\x01\x06\n\x010\x12\x010\n\x9a\x02\n\x04PS38\x12\x03mlb\x1a\x081st half"\n9825309471*\x0c149.28.23.642\x010:\x132019-05-07 06:35:00B\x132019-05-06 18:24:11J\x05falseRo\n\x1b\xe7\xbe\x8e\xe5\x9c\x8b\xe8\x81\xb7\xe6\xa3\x92\xe5\xa4\xa7\xe8\x81\xaf\xe7\x9b\x9f (MLB)\x12\x0c0_9825309471\x1a\x1e\n\x19\xe7\xb4\x90\xe7\xb4\x84\xe6\xb4\x8b\xe5\x9f\xba(C. Sabathia)\x12\x010""\n\x1d\xe8\xa5\xbf\xe9\x9b\x85\xe5\x9c\x96\xe6\xb0\xb4\xe6\x89\x8b(F. Hernandez)\x12\x010Z\x06\n\x010\x12\x010b\x1e\n\r\n\x04-0.5\x12\x051.943\x12\r\n\x04+0.5\x12\x051.925j\x13\n\x035.0\x12\x051.884\x1a\x051.990\x82\x01\x06\n\x010\x12\x010\n\x9b\x02\n\x04PS38\x12\x03mlb\x1a\x081st half"\n9825361321*\x0c149.28.23.642\x010:\x132019-05-07 07:07:00B\x132019-05-06 18:24:11J\x05falseRp\n\x1b\xe7\xbe\x8e\xe5\x9c\x8b\xe8\x81\xb7\xe6\xa3\x92\xe5\xa4\xa7\xe8\x81\xaf\xe7\x9b\x9f (MLB)\x12\x0c0_9825361321\x1a \n\x1b\xe5\xa4\x9a\xe5\x80\xab\xe5\xa4\x9a\xe8\x97\x8d\xe9\xb3\xa5(M. Stroman)\x12\x010"!\n\x1c\xe6\x98\x8e\xe5\xb0\xbc\xe8\x98\x87\xe9\x81\x94\xe9\x9b\x99\xe5\x9f\x8e(M. Perez)\x12\x010Z\x06\n\x010\x12\x010b\x1e\n\r\n\x04+0.0\x12\x051.909\x12\r\n\x04-0.0\x12\x051.980j\x13\n\x034.5\x12\x051.854\x1a\x052.020\x82\x01\x06\n\x010\x12\x010\n\xa0\x02\n\x04PS38\x12\x03mlb\x1a\x081st half"\n9825405431*\x0c149.28.23.642\x010:\x132019-05-07 07:40:00B\x132019-05-06 18:24:11J\x05falseRu\n\x1b\xe7\xbe\x8e\xe5\x9c\x8b\xe8\x81\xb7\xe6\xa3\x92\xe5\xa4\xa7\xe8\x81\xaf\xe7\x9b\x9f (MLB)\x12\x0c0_9825405431\x1a%\n \xe5\xaf\x86\xe7\x88\xbe\xe7\x93\xa6\xe5\x9f\xba\xe9\x87\x80\xe9\x85\x92\xe4\xba\xba(J. Chacin)\x12\x010"!\n\x1c\xe8\x8f\xaf\xe7\x9b\x9b\xe9\xa0\x93\xe5\x9c\x8b\xe6\xb0\x91(M. Scherzer)\x12\x010Z\x06\n\x010\x12\x010b\x1e\n\r\n\x04+0.0\x12\x052.120\x12\r\n\x04-0.0\x12\x051.793j\x13\n\x034.0\x12\x051.961\x1a\x051.909\x82\x01\x06\n\x010\x12\x010\n\x86\x02\n\x04PS38\x12\x03mlb\x1a\x081st half"\n9825444691*\x0c149.28.23.642\x010:\x132019-05-07 08:05:00B\x132019-05-06 18:24:11J\x05falseRs\n\x1b\xe7\xbe\x8e\xe5\x9c\x8b\xe8\x81\xb7\xe6\xa3\x92\xe5\xa4\xa7\xe8\x81\xaf\xe7\x9b\x9f (MLB)\x12\x0c0_9825444691\x1a\x1f\n\x1a\xe8\x8a\x9d\xe5\x8a\xa0\xe5\x93\xa5\xe5\xb0\x8f\xe7\x86\x8a(C. Hamels)\x12\x010"%\n \xe9\x82\x81\xe9\x98\xbf\xe5\xaf\x86\xe9\xa6\xac\xe6\x9e\x97\xe9\xad\x9a(S. Alcantara)\x12\x010Z\x06\n\x010\x12\x010b\x10\n\x06\n\x010\x12\x010\x12\x06\n\x010\x12\x010j\t\n\x010\x12\x010\x1a\x010\x82\x01\x06\n\x010\x12\x010\n\x9c\x02\n\x04PS38\x12\x03mlb\x1a\x081st half"\n9825444671*\x0c149.28.23.642\x010:\x132019-05-07 08:05:00B\x132019-05-06 18:24:11J\x05falseRq\n\x1b\xe7\xbe\x8e\xe5\x9c\x8b\xe8\x81\xb7\xe6\xa3\x92\xe5\xa4\xa7\xe8\x81\xaf\xe7\x9b\x9f (MLB)\x12\x0c0_9825444671\x1a \n\x1b\xe8\x81\x96\xe8\xb7\xaf\xe6\x98\x93\xe7\xb4\x85\xe9\x9b\x80(M. Mikolas)\x12\x010""\n\x1d\xe8\xb2\xbb\xe5\x9f\x8e\xe8\xb2\xbb\xe5\x9f\x8e\xe4\xba\xba(V. Velasquez)\x12\x010Z\x06\n\x010\x12\x010b\x1e\n\r\n\x04-0.5\x12\x052.070\x12\r\n\x04+0.5\x12\x051.819j\x13\n\x034.5\x12\x051.862\x1a\x052.010\x82\x01\x06\n\x010\x12\x010\n\x9b\x02\n\x04PS38\x12\x03mlb\x1a\x081st half"\n9825462391*\x0c149.28.23.642\x010:\x132019-05-07 08:10:00B\x132019-05-06 18:24:11J\x05falseRp\n\x1b\xe7\xbe\x8e\xe5\x9c\x8b\xe8\x81\xb7\xe6\xa3\x92\xe5\xa4\xa7\xe8\x81\xaf\xe7\x9b\x9f (MLB)\x12\x0c0_9825462391\x1a \n\x1b\xe4\xbc\x91\xe5\xa3\xab\xe9\xa0\x93\xe5\xa4\xaa\xe7\xa9\xba\xe4\xba\xba(G. Cole)\x12\x010"!\n\x1c\xe5\xa0\xaa\xe8\x96\xa9\xe6\x96\xaf\xe5\xb8\x82\xe7\x9a\x87\xe5\xae\xb6(J. Junis)\x12\x010Z\x06\n\x010\x12\x010b\x1e\n\r\n\x04-1.0\x12\x051.781\x12\r\n\x04+1.0\x12\x052.100j\x13\n\x034.5\x12\x051.980\x1a\x051.884\x82\x01\x06\n\x010\x12\x010\n\x9c\x02\n\x04PS38\x12\x03mlb\x1a\x081st half"\n9825677471*\x0c149.28.23.642\x010:\x132019-05-07 10:10:00B\x132019-05-06 18:24:11J\x05falseRq\n\x1b\xe7\xbe\x8e\xe5\x9c\x8b\xe8\x81\xb7\xe6\xa3\x92\xe5\xa4\xa7\xe8\x81\xaf\xe7\x9b\x9f (MLB)\x12\x0c0_9825677471\x1a#\n\x1e\xe8\x81\x96\xe5\x9c\xb0\xe7\x89\x99\xe5\x93\xa5\xe6\x95\x99\xe5\xa3\xab(C. Paddack)\x12\x010"\x1f\n\x1a\xe7\xb4\x90\xe7\xb4\x84\xe5\xa4\xa7\xe9\x83\xbd\xe6\x9c\x83(J. DeGrom)\x12\x010Z\x06\n\x010\x12\x010b\x1e\n\r\n\x04+0.5\x12\x051.751\x12\r\n\x04-0.5\x12\x052.160j\x13\n\x033.0\x12\x051.854\x1a\x052.020\x82\x01\x06\n\x010\x12\x010'


# enData = APHDC_pb2.ApHdcArr()
# enData.ParseFromString(f)
# Data = enData.aphdc
# baseballMix(Data)