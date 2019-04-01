import APHDC_pb2 
import copy
import testBSzf
import testBSds


def baseball(Data):
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


        ## 讓分
        zfBS = testBSzf.calBSzf(gameClass,gameType,homeL,awayL,homeO,awayO,homeDe,awayDe)
        bs.twZF.homeZF.line=zfBS[0]
        bs.twZF.awayZF.line=zfBS[1]
        ## 如果獨贏為0 讓分獨贏都關 因為算是需要讓分及獨贏缺一不可
        if homeDe == '0' : 
            bs.twZF.homeZF.odds="0"
            bs.twZF.awayZF.odds="0" 
            bs.de.home='0'
            bs.de.away='0'
        else :
            bs.de.home=zfBS[2]
            bs.de.away=zfBS[3]
            if homeO == '0' :
                bs.twZF.homeZF.odds="0"
                bs.twZF.awayZF.odds="0"
            else :
                bs.twZF.homeZF.odds="0.95"
                bs.twZF.awayZF.odds="0.95"  


        ## 一輸二贏 (美盤讓分盤口減一)
        if homeO != '0' :
            bs.esre.let = 1 if "-" in homeL else 2
            bs.esre.home = zfBS[4]
            bs.esre.away = zfBS[5]

        ## 大小
        line = bs.usDS.line
        over = bs.usDS.over
        under = bs.usDS.under
        dsBS = testBSds.calBSds(gameClass,line,over,under)
        bs.twDS.line=dsBS
        if over ==  '0' or over ==  "0.0" :
            bs.twDS.over="0"
            bs.twDS.under="0"
        else :
            bs.twDS.over="0.94"
            bs.twDS.under="0.94"

        

        sendData.append(copy.deepcopy(bs))                

    # print(sendData)
    datas = APHDC_pb2.ApHdcArr()
    datas.aphdc.extend(sendData)
    data = datas.SerializeToString()  #變成byte
    return data