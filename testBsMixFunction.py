import APHDC_pb2 
import copy
import testBSzf
import testBSds
import testBSde
import testCutOneP

def baseballMix(Data):
    sendData = []   
    noCalList = []
    for bs in Data:
        league = bs.information.league
        gameType = bs.game_type
        gameClass = bs.game_class
        homeDe = bs.de.home
        awayDe = bs.de.away 
        if homeDe =='0.0' or homeDe == '':
            homeDe ='0'
            awayDe ='0'       
        homeL = bs.usZF.homeZF.line
        awayL = bs.usZF.awayZF.line
        homeO = bs.usZF.homeZF.odds
        awayO = bs.usZF.awayZF.odds
        line = bs.usDS.line
        over = bs.usDS.over
        under = bs.usDS.under

        if '-' in league :
            noCalList.append(bs)
            noCal = testCutOneP.justCutOne_fun(noCalList)
            enData = APHDC_pb2.ApHdcArr()
            enData.ParseFromString(noCal)
            noCalData = enData.aphdc
            for no in noCalData :
                no
        elif "總得分" in league :
            dsBS = testBSds.calBSds(gameClass,line,over,under)
            bs.twDS.line=dsBS
            if over ==  '0' or over ==  "0.0" or dsBS=='0+0':
                bs.twDS.over="0"
                bs.twDS.under="0"
            else :
                bs.twDS.over="0.94"
                bs.twDS.under="0.94"
            bs.twZF.homeZF.line = '0+0'
            bs.twZF.homeZF.odds = '0'
            bs.twZF.awayZF.line = '0+0'
            bs.twZF.awayZF.odds = '0'            

        else :
            dsBS = testBSds.calBSds(gameClass,line,over,under)
            bs.twDS.line=dsBS
            if over ==  '0' or over ==  "0.0" or dsBS=='0+0':
                bs.twDS.over="0"
                bs.twDS.under="0"
            else :
                bs.twDS.over="0.94"
                bs.twDS.under="0.94"
            # sendData.append(copy.deepcopy(bs))
        
            # 若 沒讓分 有獨贏 用獨贏算讓分的算法
            # print(bs.game_id,homeDe,homeO)
            if  homeDe != '0' :
                if homeO == '0' : #有獨贏沒讓分
                    # print(bs.information.league)
                    zfBS1 = testBSde.calBSde(gameClass,gameType,homeDe,awayDe)
                    bs.twZF.homeZF.line=zfBS1[0]
                    bs.twZF.awayZF.line=zfBS1[1]
                    if homeDe == '0'  or zfBS1[0] == '0+0':
                        bs.twZF.homeZF.odds="0"
                        bs.twZF.awayZF.odds="0" 
                        bs.de.home='0'
                        bs.de.away='0'
                    else :
                        bs.twZF.homeZF.odds="0.95"
                        bs.twZF.awayZF.odds="0.95"  
                        bs.de.home=zfBS1[2]
                        bs.de.away=zfBS1[3]

                    sendData.append(copy.deepcopy(bs))   
            # 若 有讓分 有獨贏 用讓分＋獨贏的算法
                else :  #有獨贏有讓分
                    # print(homeL,awayL,homeO,awayO,homeDe,awayDe)
                    zfBS2 = testBSzf.calBSzf(gameClass,gameType,homeL,awayL,homeO,awayO,homeDe,awayDe)
                    # print(zfBS2)
                    bs.de.home=zfBS2[2]
                    bs.de.away=zfBS2[3]
                    bs.twZF.homeZF.line=zfBS2[0]
                    bs.twZF.awayZF.line=zfBS2[1]                
                    if homeO == '0' or '0+0' == zfBS2[0] :
                        bs.twZF.homeZF.odds="0"
                        bs.twZF.awayZF.odds="0"
                    else :
                        bs.twZF.homeZF.odds="0.95"
                        bs.twZF.awayZF.odds="0.95"

                    ## 一輸二贏 (美盤讓分盤口減一)
                    bs.esre.let = 1 if "-" in homeL else 2
                    bs.esre.home = zfBS2[4]
                    bs.esre.away = zfBS2[5]
                    # print(bs)
            

        sendData.append(copy.deepcopy(bs))
  

    # print(sendData)
    datas = APHDC_pb2.ApHdcArr()
    datas.aphdc.extend(sendData)
    data = datas.SerializeToString()  #變成byte
    return data




# f=b'\n\x9e\x02\n\x04PS38\x12\x03mlb\x1a\x04full"\t967652962*\x0c149.28.23.642\x010:\x132019-04-02 01:05:00B\x132019-04-01 18:29:27J\x05falseRp\n\x1b\xe7\xbe\x8e\xe5\x9c\x8b\xe8\x81\xb7\xe6\xa3\x92\xe5\xa4\xa7\xe8\x81\xaf\xe7\x9b\x9f (MLB)\x12\x0b0_967652962\x1a\x1f\n\x1a\xe5\x8c\xb9\xe8\x8c\xb2\xe5\xa0\xa1\xe6\xb5\xb7\xe7\x9b\x9c(C. Archer)\x12\x010"#\n\x1e\xe8\x81\x96\xe8\xb7\xaf\xe6\x98\x93\xe7\xb4\x85\xe9\x9b\x80(A. Wainwright)\x12\x010Z\x06\n\x010\x12\x010b\x1e\n\r\n\x04-1.5\x12\x052.680\x12\r\n\x04+1.5\x12\x051.534j\x13\n\x037.5\x12\x052.020\x1a\x051.892\x82\x01\x0e\n\x051.787\x12\x052.170\n\xa4\x02\n\x04PS38\x12\x03mlb\x1a\x04full"\t967700566*\x0c149.28.23.642\x010:\x132019-04-02 04:10:00B\x132019-04-01 18:29:27J\x05falseRv\n\x1b\xe7\xbe\x8e\xe5\x9c\x8b\xe8\x81\xb7\xe6\xa3\x92\xe5\xa4\xa7\xe8\x81\xaf\xe7\x9b\x9f (MLB)\x12\x0b0_967700566\x1a+\n&\xe5\x85\x8b\xe9\x87\x8c\xe5\xa4\xab\xe8\x98\xad\xe5\x8d\xb0\xe5\x9c\xb0\xe5\xae\x89\xe4\xba\xba(M. Clevinger)\x12\x010"\x1d\n\x18\xe8\x8a\x9d\xe5\x8a\xa0\xe5\x93\xa5\xe7\x99\xbd\xe8\xa5\xaa(I. Nova)\x12\x010Z\x06\n\x010\x12\x010b\x1e\n\r\n\x04-1.5\x12\x052.220\x12\r\n\x04+1.5\x12\x051.740j\x13\n\x037.5\x12\x052.040\x1a\x051.869\x82\x01\x0e\n\x051.598\x12\x052.540\n\x95\x02\n\x04PS38\x12\x03mlb\x1a\x04full"\t967740569*\x0c149.28.23.642\x010:\x132019-04-02 06:35:00B\x132019-04-01 18:29:27J\x05falseRg\n\x1b\xe7\xbe\x8e\xe5\x9c\x8b\xe8\x81\xb7\xe6\xa3\x92\xe5\xa4\xa7\xe8\x81\xaf\xe7\x9b\x9f (MLB)\x12\x0b0_967740569\x1a\x1c\n\x17\xe7\xb4\x90\xe7\xb4\x84\xe6\xb4\x8b\xe5\x9f\xba(D. German)\x12\x010"\x1d\n\x18\xe5\xba\x95\xe7\x89\xb9\xe5\xbe\x8b\xe8\x80\x81\xe8\x99\x8e(T. Ross)\x12\x010Z\x06\n\x010\x12\x010b\x1e\n\r\n\x04-1.5\x12\x051.925\x12\r\n\x04+1.5\x12\x051.980j\x13\n\x038.5\x12\x051.909\x1a\x052.000\x82\x01\x0e\n\x051.465\x12\x052.960\n\xa2\x02\n\x04PS38\x12\x03mlb\x1a\x04full"\t967740566*\x0c149.28.23.642\x010:\x132019-04-02 06:40:00B\x132019-04-01 18:29:27J\x05falseRt\n\x1b\xe7\xbe\x8e\xe5\x9c\x8b\xe8\x81\xb7\xe6\xa3\x92\xe5\xa4\xa7\xe8\x81\xaf\xe7\x9b\x9f (MLB)\x12\x0b0_967740566\x1a!\n\x1c\xe8\xbe\x9b\xe8\xbe\x9b\xe9\x82\xa3\xe6\x8f\x90\xe7\xb4\x85\xe4\xba\xba(T. Roark)\x12\x010"%\n \xe5\xaf\x86\xe7\x88\xbe\xe7\x93\xa6\xe5\x9f\xba\xe9\x87\x80\xe9\x85\x92\xe4\xba\xba(Z. Davies)\x12\x010Z\x06\n\x010\x12\x010b\x1e\n\r\n\x04-1.5\x12\x052.780\x12\r\n\x04+1.5\x12\x051.505j\x13\n\x038.5\x12\x051.980\x1a\x051.925\x82\x01\x0e\n\x051.900\x12\x052.030\n\x9f\x02\n\x04PS38\x12\x03mlb\x1a\x04full"\t967745908*\x0c149.28.23.642\x010:\x132019-04-02 07:07:00B\x132019-04-01 18:29:27J\x05falseRq\n\x1b\xe7\xbe\x8e\xe5\x9c\x8b\xe8\x81\xb7\xe6\xa3\x92\xe5\xa4\xa7\xe8\x81\xaf\xe7\x9b\x9f (MLB)\x12\x0b0_967745908\x1a#\n\x1e\xe5\xa4\x9a\xe5\x80\xab\xe5\xa4\x9a\xe8\x97\x8d\xe9\xb3\xa5(S. Reid Foley)\x12\x010" \n\x1b\xe5\xb7\xb4\xe7\x88\xbe\xe7\x9a\x84\xe6\x91\xa9\xe9\x87\x91\xe9\xb6\xaf(D. Hess)\x12\x010Z\x06\n\x010\x12\x010b\x1e\n\r\n\x04-1.5\x12\x052.120\x12\r\n\x04+1.5\x12\x051.813j\x13\n\x039.0\x12\x052.050\x1a\x051.862\x82\x01\x0e\n\x051.571\x12\x052.610\n\xa1\x02\n\x04PS38\x12\x03mlb\x1a\x04full"\t967745895*\x0c149.28.23.642\x010:\x132019-04-02 07:10:00B\x132019-04-01 18:29:27J\x05falseRs\n\x1b\xe7\xbe\x8e\xe5\x9c\x8b\xe8\x81\xb7\xe6\xa3\x92\xe5\xa4\xa7\xe8\x81\xaf\xe7\x9b\x9f (MLB)\x12\x0b0_967745895\x1a#\n\x1e\xe4\xba\x9e\xe7\x89\xb9\xe8\x98\xad\xe5\xa4\xa7\xe5\x8b\x87\xe5\xa3\xab(S. Newcomb)\x12\x010""\n\x1d\xe8\x8a\x9d\xe5\x8a\xa0\xe5\x93\xa5\xe5\xb0\x8f\xe7\x86\x8a(K. Hendricks)\x12\x010Z\x06\n\x010\x12\x010b\x1e\n\r\n\x04+1.5\x12\x051.595\x12\r\n\x04-1.5\x12\x052.510j\x13\n\x038.0\x12\x051.892\x1a\x052.010\x82\x01\x0e\n\x052.020\x12\x051.900\n\x9a\x02\n\x04PS38\x12\x03mlb\x1a\x04full"\t967745897*\x0c149.28.23.642\x010:\x132019-04-02 07:10:00B\x132019-04-01 18:29:27J\x05falseRl\n\x1b\xe7\xbe\x8e\xe5\x9c\x8b\xe8\x81\xb7\xe6\xa3\x92\xe5\xa4\xa7\xe8\x81\xaf\xe7\x9b\x9f (MLB)\x12\x0b0_967745897\x1a!\n\x1c\xe9\x82\x81\xe9\x98\xbf\xe5\xaf\x86\xe9\xa6\xac\xe6\x9e\x97\xe9\xad\x9a(C. Smith)\x12\x010"\x1d\n\x18\xe7\xb4\x90\xe7\xb4\x84\xe5\xa4\xa7\xe9\x83\xbd\xe6\x9c\x83(S. Matz)\x12\x010Z\x06\n\x010\x12\x010b\x1e\n\r\n\x04+1.5\x12\x051.671\x12\r\n\x04-1.5\x12\x052.350j\x13\n\x037.5\x12\x051.925\x1a\x051.980\x82\x01\x0e\n\x052.170\x12\x051.787\n\x9d\x02\n\x04PS38\x12\x03mlb\x1a\x04full"\t967752294*\x0c149.28.23.642\x010:\x132019-04-02 08:05:00B\x132019-04-01 18:29:27J\x05falseRo\n\x1b\xe7\xbe\x8e\xe5\x9c\x8b\xe8\x81\xb7\xe6\xa3\x92\xe5\xa4\xa7\xe8\x81\xaf\xe7\x9b\x9f (MLB)\x12\x0b0_967752294\x1a\x1e\n\x19\xe5\xbe\xb7\xe5\xb7\x9e\xe9\x81\x8a\xe9\xa8\x8e\xe5\x85\xb5(D. Smyly)\x12\x010"#\n\x1e\xe4\xbc\x91\xe5\xa3\xab\xe9\xa0\x93\xe5\xa4\xaa\xe7\xa9\xba\xe4\xba\xba(B. Peacock)\x12\x010Z\x06\n\x010\x12\x010b\x1e\n\r\n\x04+1.5\x12\x051.877\x12\r\n\x04-1.5\x12\x052.030j\x13\n\x039.5\x12\x052.050\x1a\x051.862\x82\x01\x0e\n\x052.380\x12\x051.671\n\x9c\x02\n\x04PS38\x12\x03mlb\x1a\x04full"\t967780779*\x0c149.28.23.642\x010:\x132019-04-02 10:07:00B\x132019-04-01 18:29:27J\x05falseRn\n\x1b\xe7\xbe\x8e\xe5\x9c\x8b\xe8\x81\xb7\xe6\xa3\x92\xe5\xa4\xa7\xe8\x81\xaf\xe7\x9b\x9f (MLB)\x12\x0b0_967780779\x1a"\n\x1d\xe5\xa5\xa7\xe5\x85\x8b\xe8\x98\xad\xe9\x81\x8b\xe5\x8b\x95\xe5\xae\xb6(A. Brooks)\x12\x010"\x1e\n\x19\xe6\xb3\xa2\xe5\xa3\xab\xe9\xa0\x93\xe7\xb4\x85\xe8\xa5\xaa(D. Price)\x12\x010Z\x06\n\x010\x12\x010b\x1e\n\r\n\x04+1.5\x12\x051.751\x12\r\n\x04-1.5\x12\x052.210j\x13\n\x038.0\x12\x051.925\x1a\x051.980\x82\x01\x0e\n\x052.240\x12\x051.746\n\x9b\x02\n\x04PS38\x12\x03mlb\x1a\x04full"\t967785502*\x0c149.28.23.642\x010:\x132019-04-02 10:10:00B\x132019-04-01 18:29:27J\x05falseRm\n\x1b\xe7\xbe\x8e\xe5\x9c\x8b\xe8\x81\xb7\xe6\xa3\x92\xe5\xa4\xa7\xe8\x81\xaf\xe7\x9b\x9f (MLB)\x12\x0b0_967785502\x1a\x1e\n\x19\xe6\xb4\x9b\xe6\x9d\x89\xe7\xa3\xaf\xe9\x81\x93\xe5\xa5\x87(J. Urias)\x12\x010"!\n\x1c\xe8\x88\x8a\xe9\x87\x91\xe5\xb1\xb1\xe5\xb7\xa8\xe4\xba\xba(D. Pomeranz)\x12\x010Z\x06\n\x010\x12\x010b\x1e\n\r\n\x04-1.5\x12\x052.040\x12\r\n\x04+1.5\x12\x051.877j\x13\n\x038.0\x12\x052.030\x1a\x051.877\x82\x01\x0e\n\x051.497\x12\x052.840\n\xa2\x02\n\x04PS38\x12\x03mlb\x1a\x04full"\t967785498*\x0c149.28.23.642\x010:\x132019-04-02 10:10:00B\x132019-04-01 18:29:27J\x05falseRt\n\x1b\xe7\xbe\x8e\xe5\x9c\x8b\xe8\x81\xb7\xe6\xa3\x92\xe5\xa4\xa7\xe8\x81\xaf\xe7\x9b\x9f (MLB)\x12\x0b0_967785498\x1a"\n\x1d\xe8\x81\x96\xe5\x9c\xb0\xe7\x89\x99\xe5\x93\xa5\xe6\x95\x99\xe5\xa3\xab(M. Strahm)\x12\x010"$\n\x1f\xe4\xba\x9e\xe5\x88\xa9\xe6\xa1\x91\xe9\x82\xa3\xe9\x9f\xbf\xe5\xb0\xbe\xe8\x9b\x87(M. Kelly)\x12\x010Z\x06\n\x010\x12\x010b\x1e\n\r\n\x04-1.5\x12\x052.360\x12\r\n\x04+1.5\x12\x051.662j\x13\n\x037.5\x12\x052.010\x1a\x051.900\x82\x01\x0e\n\x051.641\x12\x052.430\n\x9f\x02\n\x04PS38\x12\x03mlb\x1a\x04full"\t967785507*\x0c149.28.23.642\x010:\x132019-04-02 10:10:00B\x132019-04-01 18:29:27J\x05falseRq\n\x1b\xe7\xbe\x8e\xe5\x9c\x8b\xe8\x81\xb7\xe6\xa3\x92\xe5\xa4\xa7\xe8\x81\xaf\xe7\x9b\x9f (MLB)\x12\x0b0_967785507\x1a"\n\x1d\xe8\xa5\xbf\xe9\x9b\x85\xe5\x9c\x96\xe6\xb0\xb4\xe6\x89\x8b(F. Hernandez)\x12\x010"!\n\x1c\xe6\xb4\x9b\xe6\x9d\x89\xe7\xa3\xaf\xe5\xa4\xa9\xe4\xbd\xbf(C. Stratton)\x12\x010Z\x06\n\x010\x12\x010b\x1e\n\r\n\x04+1.5\x12\x051.617\x12\r\n\x04-1.5\x12\x052.460j\x13\n\x038.5\x12\x051.892\x1a\x052.020\x82\x01\x0e\n\x052.000\x12\x051.925\n\xcf\x02\n\x04PS38\x12\x03mlb\x1a\x04full"\t969950365*\x0c149.28.23.642\x010:\x132019-04-02 01:05:00B\x132019-04-01 18:29:27J\x05falseR\xb5\x01\n2\xe7\xbe\x8e\xe5\x9c\x8b\xe8\x81\xb7\xe6\xa3\x92\xe5\xa4\xa7\xe8\x81\xaf\xe7\x9b\x9f (MLB) - Hits + Runs + Errors\x12\x0b0_969950365\x1a6\n1\xe5\x8c\xb9\xe8\x8c\xb2\xe5\xa0\xa1\xe6\xb5\xb7\xe7\x9b\x9c (\xe5\xae\x89\xe6\x89\x93+\xe7\xb8\xbd\xe5\x88\x86+\xe5\xa4\xb1\xe8\xaa\xa4)(C. Archer)\x12\x010":\n5\xe8\x81\x96\xe8\xb7\xaf\xe6\x98\x93\xe7\xb4\x85\xe9\x9b\x80 (\xe5\xae\x89\xe6\x89\x93+\xe7\xb8\xbd\xe5\x88\x86+\xe5\xa4\xb1\xe8\xaa\xa4)(A. Wainwright)\x12\x010Z\x06\n\x010\x12\x010b\x10\n\x06\n\x010\x12\x010\x12\x06\n\x010\x12\x010j\x14\n\x0425.0\x12\x052.050\x1a\x051.775\x82\x01\x06\n\x010\x12\x010'

# enData = APHDC_pb2.ApHdcArr()
# enData.ParseFromString(f)
# Data = enData.aphdc
# baseballMix(Data)