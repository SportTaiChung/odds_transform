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
            if homeO == '0' :
                # print(bs.game_id)
                zfBS1 = testBSde.calBSde(gameType,homeDe,awayDe)
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
            else : 
                # print(homeL,awayL,homeO,awayO,homeDe,awayDe)
                zfBS2 = testBSzf.calBSzf(gameClass,gameType,homeL,awayL,homeO,awayO,homeDe,awayDe)
                # print(zfBS2)
                bs.twZF.homeZF.line=zfBS2[0]
                bs.twZF.awayZF.line=zfBS2[1]
                bs.de.home=zfBS2[2]
                bs.de.away=zfBS2[3]
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



# f=b'\n\x9f\x02\n\x04PS38\x12\x03mlb\x1a\x04full"\t963316087*\x0c149.28.23.642\x010:\x132019-03-21 17:35:00B\x132019-03-21 17:03:24J\x05falseRq\n\x1b\xe7\xbe\x8e\xe5\x9c\x8b\xe8\x81\xb7\xe6\xa3\x92\xe5\xa4\xa7\xe8\x81\xaf\xe7\x9b\x9f (MLB)\x12\x0b0_963316087\x1a#\n\x1e\xe5\xa5\xa7\xe5\x85\x8b\xe8\x98\xad\xe9\x81\x8b\xe5\x8b\x95\xe5\xae\xb6(M. Estrada)\x12\x010" \n\x1b\xe8\xa5\xbf\xe9\x9b\x85\xe5\x9c\x96\xe6\xb0\xb4\xe6\x89\x8b(Y. Kikuchi)\x12\x010Z\x06\n\x010\x12\x010b\x1e\n\r\n\x04-1.5\x12\x053.200\x12\r\n\x04+1.5\x12\x051.404j\x13\n\x039.5\x12\x051.970\x1a\x051.934\x82\x01\x0e\n\x052.170\x12\x051.787\n\xa8\x02\n\x04PS38\x12\x03mlb\x1a\x04full"\t965665833*\x0c149.28.23.642\x010:\x132019-03-21 17:35:00B\x132019-03-21 17:03:24J\x05falseR\x80\x01\n*\xe7\xbe\x8e\xe5\x9c\x8b\xe8\x81\xb7\xe6\xa5\xad\xe6\xa3\x92\xe7\x90\x83\xe5\xa4\xa7\xe8\x81\xaf\xe7\x9b\x9f - \xe6\x9b\xbf\xe4\xbb\xa3\xe7\x9b\xa4\xe5\x8f\xa3\x12\x0b0_965665833\x1a#\n\x1e\xe5\xa5\xa7\xe5\x85\x8b\xe8\x98\xad\xe9\x81\x8b\xe5\x8b\x95\xe5\xae\xb6(M. Estrada)\x12\x010" \n\x1b\xe8\xa5\xbf\xe9\x9b\x85\xe5\x9c\x96\xe6\xb0\xb4\xe6\x89\x8b(Y. Kikuchi)\x12\x010Z\x06\n\x010\x12\x010b\x1e\n\r\n\x04+1.5\x12\x051.598\x12\r\n\x04-1.5\x12\x052.480j\x14\n\x0413.5\x12\x055.040\x1a\x051.190\x82\x01\x06\n\x010\x12\x010\n\xfb\x01\n\x04PS38\x12\x03mlb\x1a\x04full"\t965388170*\x0c149.28.23.642\x010:\x132019-03-22 01:05:00B\x132019-03-21 17:03:24J\x05falseRe\n\'\xe7\xbe\x8e\xe5\x9c\x8b\xe8\x81\xb7\xe6\xa5\xad\xe6\xa3\x92\xe7\x90\x83\xe5\xa4\xa7\xe8\x81\xaf\xe7\x9b\x9f - \xe8\xb3\xbd\xe5\xad\xa3\xe5\x89\x8d\x12\x0b0_965388170\x1a\x14\n\x0f\xe5\xba\x95\xe7\x89\xb9\xe5\xbe\x8b\xe8\x80\x81\xe8\x99\x8e\x12\x010"\x17\n\x12\xe4\xbc\x91\xe5\xa3\xab\xe9\xa0\x93\xe5\xa4\xaa\xe7\xa9\xba\xe4\xba\xba\x12\x010Z\x06\n\x010\x12\x010b\x10\n\x06\n\x010\x12\x010\x12\x06\n\x010\x12\x010j\t\n\x010\x12\x010\x1a\x010\x82\x01\x0e\n\x052.160\x12\x051.740\n\xf8\x01\n\x04PS38\x12\x03mlb\x1a\x04full"\t965388257*\x0c149.28.23.642\x010:\x132019-03-22 01:05:00B\x132019-03-21 17:03:24J\x05falseRb\n\'\xe7\xbe\x8e\xe5\x9c\x8b\xe8\x81\xb7\xe6\xa5\xad\xe6\xa3\x92\xe7\x90\x83\xe5\xa4\xa7\xe8\x81\xaf\xe7\x9b\x9f - \xe8\xb3\xbd\xe5\xad\xa3\xe5\x89\x8d\x12\x0b0_965388257\x1a\x14\n\x0f\xe8\xb2\xbb\xe5\x9f\x8e\xe8\xb2\xbb\xe5\x9f\x8e\xe4\xba\xba\x12\x010"\x14\n\x0f\xe5\xa4\x9a\xe5\x80\xab\xe5\xa4\x9a\xe8\x97\x8d\xe9\xb3\xa5\x12\x010Z\x06\n\x010\x12\x010b\x10\n\x06\n\x010\x12\x010\x12\x06\n\x010\x12\x010j\t\n\x010\x12\x010\x1a\x010\x82\x01\x0e\n\x051.719\x12\x052.190\n\xfb\x01\n\x04PS38\x12\x03mlb\x1a\x04full"\t965388232*\x0c149.28.23.642\x010:\x132019-03-22 01:05:00B\x132019-03-21 17:03:24J\x05falseRe\n\'\xe7\xbe\x8e\xe5\x9c\x8b\xe8\x81\xb7\xe6\xa5\xad\xe6\xa3\x92\xe7\x90\x83\xe5\xa4\xa7\xe8\x81\xaf\xe7\x9b\x9f - \xe8\xb3\xbd\xe5\xad\xa3\xe5\x89\x8d\x12\x0b0_965388232\x1a\x14\n\x0f\xe5\x8c\xb9\xe8\x8c\xb2\xe5\xa0\xa1\xe6\xb5\xb7\xe7\x9b\x9c\x12\x010"\x17\n\x12\xe5\xb7\xb4\xe7\x88\xbe\xe7\x9a\x84\xe6\x91\xa9\xe9\x87\x91\xe9\xb6\xaf\x12\x010Z\x06\n\x010\x12\x010b\x10\n\x06\n\x010\x12\x010\x12\x06\n\x010\x12\x010j\t\n\x010\x12\x010\x1a\x010\x82\x01\x0e\n\x051.613\x12\x052.390\n\xfb\x01\n\x04PS38\x12\x03mlb\x1a\x04full"\t965388254*\x0c149.28.23.642\x010:\x132019-03-22 01:10:00B\x132019-03-21 17:03:24J\x05falseRe\n\'\xe7\xbe\x8e\xe5\x9c\x8b\xe8\x81\xb7\xe6\xa5\xad\xe6\xa3\x92\xe7\x90\x83\xe5\xa4\xa7\xe8\x81\xaf\xe7\x9b\x9f - \xe8\xb3\xbd\xe5\xad\xa3\xe5\x89\x8d\x12\x0b0_965388254\x1a\x14\n\x0f\xe7\xb4\x90\xe7\xb4\x84\xe5\xa4\xa7\xe9\x83\xbd\xe6\x9c\x83\x12\x010"\x17\n\x12\xe9\x82\x81\xe9\x98\xbf\xe5\xaf\x86\xe9\xa6\xac\xe6\x9e\x97\xe9\xad\x9a\x12\x010Z\x06\n\x010\x12\x010b\x10\n\x06\n\x010\x12\x010\x12\x06\n\x010\x12\x010j\t\n\x010\x12\x010\x1a\x010\x82\x01\x0e\n\x051.571\x12\x052.490\n\xf8\x01\n\x04PS38\x12\x03mlb\x1a\x04full"\t965388247*\x0c149.28.23.642\x010:\x132019-03-22 04:05:00B\x132019-03-21 17:03:24J\x05falseRb\n\'\xe7\xbe\x8e\xe5\x9c\x8b\xe8\x81\xb7\xe6\xa5\xad\xe6\xa3\x92\xe7\x90\x83\xe5\xa4\xa7\xe8\x81\xaf\xe7\x9b\x9f - \xe8\xb3\xbd\xe5\xad\xa3\xe5\x89\x8d\x12\x0b0_965388247\x1a\x14\n\x0f\xe8\x8a\x9d\xe5\x8a\xa0\xe5\x93\xa5\xe5\xb0\x8f\xe7\x86\x8a\x12\x010"\x14\n\x0f\xe8\x88\x8a\xe9\x87\x91\xe5\xb1\xb1\xe5\xb7\xa8\xe4\xba\xba\x12\x010Z\x06\n\x010\x12\x010b\x10\n\x06\n\x010\x12\x010\x12\x06\n\x010\x12\x010j\t\n\x010\x12\x010\x1a\x010\x82\x01\x0e\n\x051.746\x12\x052.150\n\xfe\x01\n\x04PS38\x12\x03mlb\x1a\x04full"\t965388194*\x0c149.28.23.642\x010:\x132019-03-22 04:05:00B\x132019-03-21 17:03:24J\x05falseRh\n\'\xe7\xbe\x8e\xe5\x9c\x8b\xe8\x81\xb7\xe6\xa5\xad\xe6\xa3\x92\xe7\x90\x83\xe5\xa4\xa7\xe8\x81\xaf\xe7\x9b\x9f - \xe8\xb3\xbd\xe5\xad\xa3\xe5\x89\x8d\x12\x0b0_965388194\x1a\x1a\n\x15\xe5\xaf\x86\xe7\x88\xbe\xe7\x93\xa6\xe5\x9f\xba\xe9\x87\x80\xe9\x85\x92\xe4\xba\xba\x12\x010"\x14\n\x0f\xe6\xb4\x9b\xe6\x9d\x89\xe7\xa3\xaf\xe9\x81\x93\xe5\xa5\x87\x12\x010Z\x06\n\x010\x12\x010b\x10\n\x06\n\x010\x12\x010\x12\x06\n\x010\x12\x010j\t\n\x010\x12\x010\x1a\x010\x82\x01\x0e\n\x051.769\x12\x052.110\n\xfe\x01\n\x04PS38\x12\x03mlb\x1a\x04full"\t965388246*\x0c149.28.23.642\x010:\x132019-03-22 04:10:00B\x132019-03-21 17:03:24J\x05falseRh\n\'\xe7\xbe\x8e\xe5\x9c\x8b\xe8\x81\xb7\xe6\xa5\xad\xe6\xa3\x92\xe7\x90\x83\xe5\xa4\xa7\xe8\x81\xaf\xe7\x9b\x9f - \xe8\xb3\xbd\xe5\xad\xa3\xe5\x89\x8d\x12\x0b0_965388246\x1a\x1a\n\x15\xe4\xba\x9e\xe5\x88\xa9\xe6\xa1\x91\xe9\x82\xa3\xe9\x9f\xbf\xe5\xb0\xbe\xe8\x9b\x87\x12\x010"\x14\n\x0f\xe6\xb4\x9b\xe6\x9d\x89\xe7\xa3\xaf\xe5\xa4\xa9\xe4\xbd\xbf\x12\x010Z\x06\n\x010\x12\x010b\x10\n\x06\n\x010\x12\x010\x12\x06\n\x010\x12\x010j\t\n\x010\x12\x010\x1a\x010\x82\x01\x0e\n\x051.840\x12\x052.020\n\xd0\x02\n\x04PS38\x12\x03mlb\x1a\x04full"\t965664120*\x0c149.28.23.642\x010:\x132019-03-21 17:35:00B\x132019-03-21 17:03:24J\x05falseR\xb6\x01\n2\xe7\xbe\x8e\xe5\x9c\x8b\xe8\x81\xb7\xe6\xa5\xad\xe6\xa3\x92\xe7\x90\x83\xe5\xa4\xa7\xe8\x81\xaf\xe7\x9b\x9f - Hits + Runs + Errors\x12\x0b0_965664120\x1a:\n5\xe5\xa5\xa7\xe5\x85\x8b\xe8\x98\xad\xe9\x81\x8b\xe5\x8b\x95\xe5\xae\xb6 (\xe5\xae\x89\xe6\x89\x93+\xe7\xb8\xbd\xe5\x88\x86+\xe5\xa4\xb1\xe8\xaa\xa4)(M. Estrada)\x12\x010"7\n2\xe8\xa5\xbf\xe9\x9b\x85\xe5\x9c\x96\xe6\xb0\xb4\xe6\x89\x8b (\xe5\xae\x89\xe6\x89\x93+\xe7\xb8\xbd\xe5\x88\x86+\xe5\xa4\xb1\xe8\xaa\xa4)(Y. Kikuchi)\x12\x010Z\x06\n\x010\x12\x010b\x10\n\x06\n\x010\x12\x010\x12\x06\n\x010\x12\x010j\x14\n\x0428.5\x12\x051.943\x1a\x051.862\x82\x01\x06\n\x010\x12\x010\n\xb9\x02\n\x04PS38\x12\x03mlb\x1a\x04full"\t965664123*\x0c149.28.23.642\x010:\x132019-03-21 17:35:00B\x132019-03-21 17:03:24J\x05falseR\xa2\x01\n4\xe7\xbe\x8e\xe5\x9c\x8b\xe8\x81\xb7\xe6\xa3\x92\xe5\xa4\xa7\xe8\x81\xaf\xe7\x9b\x9f (MLB)  - To Score First \xe8\xb3\xa0\xe7\x8e\x87\x12\x0b0_965664123\x1a/\n*\xe5\xa5\xa7\xe5\x85\x8b\xe8\x98\xad\xe9\x81\x8b\xe5\x8b\x95\xe5\xae\xb6 (\xe5\x85\x88\xe5\xbe\x97\xe5\x88\x86)(M. Estrada)\x12\x010",\n\'\xe8\xa5\xbf\xe9\x9b\x85\xe5\x9c\x96\xe6\xb0\xb4\xe6\x89\x8b (\xe5\x85\x88\xe5\xbe\x97\xe5\x88\x86)(Y. Kikuchi)\x12\x010Z\x06\n\x010\x12\x010b\x10\n\x06\n\x010\x12\x010\x12\x06\n\x010\x12\x010j\t\n\x010\x12\x010\x1a\x010\x82\x01\x0e\n\x052.450\x12\x051.588'

# enData = APHDC_pb2.ApHdcArr()
# enData.ParseFromString(f)
# Data = enData.aphdc
# baseballMix(Data)