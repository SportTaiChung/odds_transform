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
        pass
        telegramBot("BS錯誤")
        datas = APHDC_pb2.ApHdcArr()
        datas.aphdc.extend(Data)
        data = datas.SerializeToString()
        BSfile = open('bs.log','a')
        BSfile.write(str(data)+'\n'+str(e)+'\n'+dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')+'\n')



# enData = APHDC_pb2.ApHdcArr()
# enData.ParseFromString(f)
# Data = enData.aphdc
# baseballMix(Data)