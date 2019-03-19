import APHDC_pb2 
import copy
import testBSzf
import testBSds
import testBSde


def baseballMix(Data):
    sendData = []   
    for bs in Data:
        gameType = bs.game_type
        gameClass = bs.game_class
        homeDe = bs.de.home
        awayDe = bs.de.away
        homeL = bs.usZF.homeZF.line
        awayL = bs.usZF.awayZF.line
        homeO = bs.usZF.homeZF.odds
        awayO = bs.usZF.awayZF.odds


        ## 大小
        line = bs.usDS.line
        over = bs.usDS.over
        under = bs.usDS.under
        # print(line,over,under)
        dsBS = testBSds.calBSds(gameClass,line,over,under)
        bs.twDS.line=dsBS
        if over ==  '0' or over ==  "0.0" :
            bs.twDS.over="0"
            bs.twDS.under="0"
        else :
            bs.twDS.over="0.94"
            bs.twDS.under="0.94"

        # 若 沒讓分 有獨贏 用獨贏算讓分的算法
        if  homeDe != '0' :
            if homeO == '0' :
                zfBS = testBSde.calBSde(gameType,homeDe,awayDe)
                bs.twZF.homeZF.line=zfBS[0]
                bs.twZF.awayZF.line=zfBS[1]
                if homeDe == '0' : 
                    bs.twZF.homeZF.odds="0"
                    bs.twZF.awayZF.odds="0" 
                    bs.de.home='0'
                    bs.de.away='0'
                else :
                    bs.twZF.homeZF.odds="0.95"
                    bs.twZF.awayZF.odds="0.95"  
                    bs.de.home=zfBS[2]
                    bs.de.away=zfBS[3]

                # sendData.append(copy.deepcopy(bs))   
        # 若 有讓分 有獨贏 用讓分＋獨贏的算法
            else : 
                zfBS = testBSzf.calBSzf(gameType,homeL,awayL,homeO,awayO,homeDe,awayDe)
                bs.twZF.homeZF.line=zfBS[0]
                bs.twZF.awayZF.line=zfBS[1]
                bs.de.home=zfBS[2]
                bs.de.away=zfBS[3]
                bs.twZF.homeZF.odds="0.95"
                bs.twZF.awayZF.odds="0.95"

                ## 一輸二贏 (美盤讓分盤口減一)
                bs.esre.let = 1 if "-" in homeL else 2
                bs.esre.home = zfBS[4]
                bs.esre.away = zfBS[5]

        sendData.append(copy.deepcopy(bs))



    # print(sendData)
    datas = APHDC_pb2.ApHdcArr()
    datas.aphdc.extend(sendData)
    data = datas.SerializeToString()  #變成byte
    return data



# f =b'\n\xe5\x01\n\x06testPS\x12\x03mlb\x1a\x04full"\t9630291042\x010:\x132019-03-19 10:05:00B\x132019-03-19 09:58:51J\x05falseRP\n\x15\xe7\xbe\x8e\xe5\x9c\x8b\xe8\x81\xb7\xe6\xa3\x92\xe5\xa4\xa7\xe8\x81\xaf\xe7\x9b\x9f\x12\x0b0_963029104\x1a\x14\n\x0f\xe5\xbe\xb7\xe5\xb7\x9e\xe9\x81\x8a\xe9\xa8\x8e\xe5\x85\xb5\x12\x010"\x14\n\x0f\xe6\xb4\x9b\xe6\x9d\x89\xe7\xa3\xaf\xe9\x81\x93\xe5\xa5\x87\x12\x010Z\x06\n\x010\x12\x010b\x10\n\x06\n\x010\x12\x010\x12\x06\n\x010\x12\x010j\x14\n\x0410.5\x12\x051.862\x1a\x051.961\x82\x01\x0e\n\x051.793\x12\x052.080'

# enData = APHDC_pb2.ApHdcArr()
# enData.ParseFromString(f)
# Data = enData.aphdc
# baseballMix(Data)