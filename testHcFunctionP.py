# -*- coding:utf-8 -*-
import testCutOneP
import APHDC_pb2
import numpy as np
# import io
# import sys
import json  
import copy
# sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')
import testHCzf
import testBSzf
import testBSds

def hockey(Data):
    sendData = []      
    notNHL =[]
    for hc in Data:
        if  "NHL美國冰球聯季後賽(含加時賽)" not in hc.information.league  and hc.game_class == "hockey":
            # print(hc.information.league)
            notNHL.append(hc)
            others = testCutOneP.justCutOne_fun(notNHL)
            enData = APHDC_pb2.ApHdcArr()
            enData.ParseFromString(others)
            notNHLData = enData.aphdc
            for no in notNHLData :
                no
            sendData.append(copy.deepcopy(no))
        elif '總得分' in hc.information.league :
            # print(hc.information.league)
            notNHL.append(hc)
            others = testCutOneP.justCutOne_fun(notNHL)
            enData = APHDC_pb2.ApHdcArr()
            enData.ParseFromString(others)
            notNHLData = enData.aphdc
            for no in notNHLData :
                no
            sendData.append(copy.deepcopy(no))
        else:
            gameType = hc.game_type
            homeL = hc.usZF.homeZF.line
            awayL = hc.usZF.awayZF.line
            homeO = hc.usZF.homeZF.odds
            awayO = hc.usZF.awayZF.odds
            homeDe = hc.de.home
            awayDe = hc.de.away
            # zfBS = testHCzf.calBSzf(gameType,homeL,awayL,homeO,awayO,homeDe,awayDe)
            zfBS = testBSzf.calBSzf(gameType,homeL,awayL,homeO,awayO,homeDe,awayDe)
            hc.twZF.homeZF.line=zfBS[0]
            hc.twZF.awayZF.line=zfBS[1]
            
            ## 如果獨贏為0 讓分獨贏都關 因為算是需要讓分及獨贏缺一不可
            if homeDe == '0' : 
                hc.twZF.homeZF.odds="0"
                hc.twZF.awayZF.odds="0" 
                hc.de.home='0'
                hc.de.away='0'
            else :
                hc.de.home=zfBS[2]
                hc.de.away=zfBS[3]
                if homeO == '0' :
                    hc.twZF.homeZF.odds="0"
                    hc.twZF.awayZF.odds="0"
                else :
                    hc.twZF.homeZF.odds="0.95"
                    hc.twZF.awayZF.odds="0.95"  


            ## 一輸二贏 (美盤讓分盤口減一)
            if homeO != '0' :
                hc.esre.let = 1 if "-" in homeL else 2
                hc.esre.home = zfBS[4]
                hc.esre.away = zfBS[5]

            ## 大小
            line = hc.usDS.line
            over = hc.usDS.over
            under = hc.usDS.under
            # if over == "0" or over == "0.0":
            #     hc.twDS.line= '0+0'
            #     hc.twDS.over= '0'
            #     hc.twDS.under= '0'
            # else :
            #     dsBS = testCutOneP.cutOne(over,under)
            #     if '.5' in str(float(line)) :
            #         line = line
            #     else :
            #         line = str(float(line)).replace('.0','+0')
            #     hc.twDS.line= line
            #     hc.twDS.over= dsBS[0]
            #     hc.twDS.under= dsBS[1]
            dsBS = testBSds.calBSds(line,over,under)
            hc.twDS.line= dsBS
            hc.twDS.over= '0.94'
            hc.twDS.under= '0.94'
       
            sendData.append(copy.deepcopy(hc))                

    # print(sendData)
    datas = APHDC_pb2.ApHdcArr()
    datas.aphdc.extend(sendData)
    data = datas.SerializeToString()  #變成byte
    return data

    


# f= b'\n\x8b\x02\n\x04PS38\x12\x06hockey\x1a\tlive full"\n95195454872\x010:\x132019-02-15 09:30:00B\x132019-02-15 11:30:05J\x04trueRe\n)NHL\xe7\xbe\x8e\xe5\x9c\x8b\xe5\x86\xb0\xe7\x90\x83\xe8\x81\xaf\xe5\xad\xa3\xe5\xbe\x8c\xe8\xb3\xbd(\xe5\x90\xab\xe5\x8a\xa0\xe6\x99\x82\xe8\xb3\xbd)\x12\x0c0_9519545487\x1a\x14\n\x0f\xe8\x8a\x9d\xe5\x8a\xa0\xe5\x93\xa5\xe9\xbb\x91\xe9\xb7\xb9\x12\x010"\x14\n\x0f\xe6\x96\xb0\xe6\xbe\xa4\xe8\xa5\xbf\xe9\xad\x94\xe9\xac\xbc\x12\x010Z\x06\n\x010\x12\x010b\x1e\n\r\n\x04-1.5\x12\x052.430\x12\r\n\x04+1.5\x12\x051.505j\x13\n\x037.5\x12\x052.310\x1a\x051.561\x82\x01\x0c\n\x040.25\x12\x042.46\n\xf7\x01\n\x04PS38\x12\x06hockey\x1a\tlive full"\n95165419372\x010:\x132019-02-15 09:35:00B\x132019-02-15 11:30:05J\x04trueRe\n)NHL\xe7\xbe\x8e\xe5\x9c\x8b\xe5\x86\xb0\xe7\x90\x83\xe8\x81\xaf\xe5\xad\xa3\xe5\xbe\x8c\xe8\xb3\xbd(\xe5\x90\xab\xe5\x8a\xa0\xe6\x99\x82\xe8\xb3\xbd)\x12\x0c0_9516541937\x1a\x14\n\x0f\xe8\x8a\x9d\xe5\x8a\xa0\xe5\x93\xa5\xe9\xbb\x91\xe9\xb7\xb9\x12\x010"\x14\n\x0f\xe6\x96\xb0\xe6\xbe\xa4\xe8\xa5\xbf\xe9\xad\x94\xe9\xac\xbc\x12\x010Z\x06\n\x010\x12\x010b\x10\n\x06\n\x010\x12\x010\x12\x06\n\x010\x12\x010j\x13\n\x038.5\x12\x053.460\x1a\x051.334\x82\x01\x06\n\x010\x12\x010\n\x8b\x02\n\x04PS38\x12\x06hockey\x1a\tlive full"\n95165419272\x010:\x132019-02-15 09:35:00B\x132019-02-15 11:30:05J\x04trueRe\n)NHL\xe7\xbe\x8e\xe5\x9c\x8b\xe5\x86\xb0\xe7\x90\x83\xe8\x81\xaf\xe5\xad\xa3\xe5\xbe\x8c\xe8\xb3\xbd(\xe5\x90\xab\xe5\x8a\xa0\xe6\x99\x82\xe8\xb3\xbd)\x12\x0c0_9516541927\x1a\x14\n\x0f\xe8\x8a\x9d\xe5\x8a\xa0\xe5\x93\xa5\xe9\xbb\x91\xe9\xb7\xb9\x12\x010"\x14\n\x0f\xe6\x96\xb0\xe6\xbe\xa4\xe8\xa5\xbf\xe9\xad\x94\xe9\xac\xbc\x12\x010Z\x06\n\x010\x12\x010b\x1e\n\r\n\x04-1.5\x12\x052.290\x12\r\n\x04+1.5\x12\x051.662j\x13\n\x037.5\x12\x052.480\x1a\x051.574\x82\x01\x0c\n\x040.25\x12\x043.21\n\x88\x02\n\x04PS38\x12\x06hockey\x1a\tlive full"\n95194925172\x010:\x132019-02-15 10:00:00B\x132019-02-15 11:30:05J\x04trueRh\n)NHL\xe7\xbe\x8e\xe5\x9c\x8b\xe5\x86\xb0\xe7\x90\x83\xe8\x81\xaf\xe5\xad\xa3\xe5\xbe\x8c\xe8\xb3\xbd(\xe5\x90\xab\xe5\x8a\xa0\xe6\x99\x82\xe8\xb3\xbd)\x12\x0c0_9519492517\x1a\x17\n\x12\xe4\xba\x9e\xe5\x88\xa9\xe6\xa1\x91\xe9\x82\xa3\xe5\x9c\x9f\xe7\x8b\xbc\x12\x010"\x14\n\x0f\xe8\x81\x96\xe8\xb7\xaf\xe6\x98\x93\xe8\x97\x8d\xe8\xaa\xbf\x12\x010Z\x06\n\x010\x12\x010b\x1e\n\r\n\x04+2.5\x12\x051.980\x12\r\n\x04-2.5\x12\x051.763j\x13\n\x034.5\x12\x051.952\x1a\x051.793\x82\x01\x06\n\x010\x12\x010\n\x8e\x02\n\x04PS38\x12\x06hockey\x1a\tlive full"\n95194925072\x010:\x132019-02-15 11:00:00B\x132019-02-15 11:30:05J\x04trueRh\n)NHL\xe7\xbe\x8e\xe5\x9c\x8b\xe5\x86\xb0\xe7\x90\x83\xe8\x81\xaf\xe5\xad\xa3\xe5\xbe\x8c\xe8\xb3\xbd(\xe5\x90\xab\xe5\x8a\xa0\xe6\x99\x82\xe8\xb3\xbd)\x12\x0c0_9519492507\x1a\x17\n\x12\xe7\xb6\xad\xe5\x8a\xa0\xe6\x96\xaf\xe9\x87\x91\xe9\xa8\x8e\xe5\xa3\xab\x12\x010"\x14\n\x0f\xe5\xa4\x9a\xe5\x80\xab\xe5\xa4\x9a\xe6\xa5\x93\xe8\x91\x89\x12\x010Z\x06\n\x010\x12\x010b\x1e\n\r\n\x04+1.5\x12\x051.395\x12\r\n\x04-1.5\x12\x052.750j\x13\n\x035.5\x12\x052.310\x1a\x051.561\x82\x01\x0c\n\x040.96\x12\x040.79'

# enData = APHDC_pb2.ApHdcArr()
# enData.ParseFromString(f)
# Data = enData.aphdc
# baseball_fun(Data)