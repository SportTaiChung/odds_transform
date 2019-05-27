import copy
import APHDC_pb2
import testBSzf
import testBSds
import testBSde
import testCutOneP
import newBSds
import newBSzf
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
                #上半場
                if gameType == '1st half':
                    zfBShalf = testBSzf.calBSzf(source, gameClass, gameType, homeL, awayL, homeO, awayO, homeDe, awayDe)
                    bs.de.home = zfBShalf[2]
                    bs.de.away = zfBShalf[3]
                    bs.twZF.homeZF.line = zfBShalf[0]
                    bs.twZF.awayZF.line = zfBShalf[1]
                    if homeO == '0' or zfBShalf[0] == '0+0':
                        bs.twZF.homeZF.odds = "0"
                        bs.twZF.awayZF.odds = "0"
                    else:
                        bs.twZF.homeZF.odds = "0.95"
                        bs.twZF.awayZF.odds = "0.95"

                    dsBS = testBSds.calBSds(source, gameClass, gameType, line, over, under)
                    bs.twDS.line = dsBS
                    if over == '0' or over == "0.0" or dsBS == '0+0':
                        bs.twDS.over = "0"
                        bs.twDS.under = "0"
                    else:
                        bs.twDS.over = "0.94"
                        bs.twDS.under = "0.94"
                #全場
                else:
                    # 讓分兩盤口
                    if ',' in homeL :
                        zfBS = newBSzf.calBSzf(source,gameClass,gameType,homeL,awayL,homeO,awayO)
                        bs.twZF.homeZF.line = zfBS[0]
                        bs.twZF.awayZF.line = zfBS[1]
                        if zfBS[0] == '0+0':
                            bs.usZF.homeZF.line = homeL.split(',')[0]
                            bs.usZF.awayZF.line = awayL.split(',')[0]
                            bs.usZF.homeZF.odds = homeO.split(',')[0]
                            bs.usZF.awayZF.odds = awayO.split(',')[0]
                            bs.twZF.homeZF.odds = "0"
                            bs.twZF.awayZF.odds = "0"
                        else:
                            bs.twZF.homeZF.odds = "0.95"
                            bs.twZF.awayZF.odds = "0.95"
                            bs.de.home = str(round((float(homeDe)-1),2))
                            bs.de.away = str(round((float(awayDe)-1),2))
                            bs.usZF.homeZF.line = homeL.split(',')[0]
                            bs.usZF.awayZF.line = awayL.split(',')[0]
                            bs.usZF.homeZF.odds = str(round((float(zfBS[2])+1),2))
                            bs.usZF.awayZF.odds = str(round((float(zfBS[3])+1),2))
                        ## 一輸二贏 (美盤讓分盤口減一)
                        bs.esre.let = 1 if "-" in homeL else 2
                        bs.esre.home = zfBS[2]
                        bs.esre.away = zfBS[3]
                    # 讓分單一盤口
                    else:
                        # 若 沒讓分 有獨贏 用獨贏算讓分的算法
                        if homeDe != '0':
                            if homeO in ('0', '', '0.0'): #沒讓分有獨贏
                                zfBSde = testBSde.calBSde(source, gameClass, gameType, homeDe, awayDe)
                                bs.twZF.homeZF.line = zfBSde[0]
                                bs.twZF.awayZF.line = zfBSde[1]
                                if  float(zfBSde[3]) <= 0.0 or homeDe == '0' or zfBSde[0] == '0+0':
                                    bs.twZF.homeZF.line = '0+0'
                                    bs.twZF.awayZF.line = '0+0'
                                    bs.twZF.homeZF.odds = "0"
                                    bs.twZF.awayZF.odds = "0"
                                    bs.de.home = '0'
                                    bs.de.away = '0'
                                else:
                                    bs.twZF.homeZF.odds = "0.95"
                                    bs.twZF.awayZF.odds = "0.95"
                                    bs.de.home = zfBSde[2]
                                    bs.de.away = zfBSde[3]
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
                # 大小兩盤口
                if ',' in line :
                    dsBS = newBSds.calBSds(source, gameClass, line, over, under)
                    bs.twDS.line = dsBS[0]
                    bs.usDS.line = dsBS[1]
                    bs.usDS.over = str(round((float(dsBS[2])+1),2))
                    bs.usDS.under = str(round((float(dsBS[3])+1),2))
                    if over == '0' or over == "0.0" or dsBS == '0+0':
                        bs.usDS.line = line.split(',')[0]
                        bs.usDS.over = over.split(',')[0]
                        bs.usDS.under = under.split(',')[0]
                        bs.twDS.over = "0"
                        bs.twDS.under = "0"
                    else:
                        bs.twDS.over = "0.94"
                        bs.twDS.under = "0.94"
                # 大小單一盤口
                else :
                    dsBS = testBSds.calBSds(source, gameClass, gameType, line, over, under)
                    bs.twDS.line = dsBS
                    if over == '0' or over == "0.0" or dsBS == '0+0':
                        bs.twDS.over = "0"
                        bs.twDS.under = "0"
                    else:
                        bs.twDS.over = "0.94"
                        bs.twDS.under = "0.94"

            sendData.append(copy.deepcopy(bs))
        # print(sendData)
        datas = APHDC_pb2.ApHdcArr()
        datas.aphdc.extend(sendData)
        data = datas.SerializeToString()  #變成byte
        return data

    except Exception as e:
        # print(bs)
        pass
        telegramBot("BS錯誤")
        datas = APHDC_pb2.ApHdcArr()
        datas.aphdc.extend(Data)
        data = datas.SerializeToString()
        BSfile = open('bs.log','a')
        BSfile.write(str(data)+'\n'+str(e)+'\n'+dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')+'\n')




## 找錯誤用 
## testData 後面請填入錯誤的data 執行即可印出錯誤

# testData = 
# enData = APHDC_pb2.ApHdcArr()
# enData.ParseFromString(testData)
# Data = enData.aphdc
# baseballMix(Data)