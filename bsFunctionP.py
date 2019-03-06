import APHDC_pb2 
import copy
import testBSzf


def baseball(Data):
    sendData = []   
    for bs in Data:
        gameType = bs.game_type
        homeDe = bs.de.home
        awayDe = bs.de.away
        homeL = bs.usZF.homeZF.line
        awayL = bs.usZF.awayZF.line
        homeO = bs.usZF.homeZF.odds
        awayO = bs.usZF.awayZF.odds
        zfBS = testBSzf.calBSzf(gameType,homeL,awayL,homeO,awayO,homeDe,awayDe)
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
            bs.de.home=zfBS[4]
            bs.de.away=zfBS[5]

        if homeO != '0' :
            bs.esre.let = 1 if "-" in homeL else 2
            bs.esre.home = zfBS[2]
            bs.esre.away = zfBS[3]

        sendData.append(copy.deepcopy(bs))                

    # print(sendData)
    datas = APHDC_pb2.ApHdcArr()
    datas.aphdc.extend(sendData)
    data = datas.SerializeToString()  #變成byte
    return data