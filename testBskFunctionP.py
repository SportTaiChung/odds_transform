# -*- coding:utf-8 -*-
import numpy as np
import APHDC_pb2
# import io
# import sys
import json
import copy
# sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')
import testBKzf
import testBKds
import testCutOneP


def basketball(Data):
    sendData =[]
    noCal =[]
    for bsk in Data :
        # print(bsk.game_id)
        gameType = bsk.game_type
        league = bsk.information.league
        homeL = bsk.usZF.homeZF.line
        awayL = bsk.usZF.awayZF.line
        homeO = bsk.usZF.homeZF.odds
        awayO = bsk.usZF.awayZF.odds
        try :
            homeDe= bsk.de.home
            awayDe= bsk.de.away
        except :
            homeDe= '0'
            awayDe= '0'            
        
        dsline = bsk.usDS.line
        over = bsk.usDS.over
        under = bsk.usDS.under
        
        try :
            sdA = bsk.sd.home
            sdH = bsk.sd.away
            if sdA != '0' :
                sd = testCutOneP.cutOne(sdA,sdH)
                bsk.sd.home = sd[0]
                bsk.sd.away = sd[1]
        except:
            sdA ='0'
            sdH ='0'

        # ## 主客隊總得分
        # if '隊總得分' in league :
        #     dsBK = testBKds.calBKds(dsline,over,under)
        #     bsk.twDS.line=dsBK
        #     if over ==  '0' or over ==  "0.0" :
        #         bsk.twDS.over="0"
        #         bsk.twDS.under="0"
        #     else :
        #         bsk.twDS.over="0.94"
        #         bsk.twDS.under="0.94"

        #     sendData.append(copy.deepcopy(bsk))
        #優先得分球隊 , 最後得分球隊 , 三分球總數 ,NBA-總得分

        #一般比賽 夢幻配對賽 第一節~第四節 下半場
        if "第一節" in league or "第二節" in league or "第三節" in league or "第四節" in league or "隊總得分" in league or "夢幻配對賽" in league or 'NBA 美國職業籃球聯賽' == league :
            # print(league)
            try :
                float(homeDe)
            except :
                homeDe = '0'
                awayDe = '0'
            zfBK = testBKzf.calBKzf(gameType,homeL,awayL,homeO,awayO,homeDe,awayDe)
            bsk.twZF.homeZF.line=zfBK[0]
            bsk.twZF.awayZF.line=zfBK[1]
            

            if homeDe == '0' or homeDe == '0.0'  : 
                bsk.de.home='0'
                bsk.de.away='0'  
                if homeO == '0'  or  homeO == '0.0': 
                    bsk.twZF.homeZF.odds="0"
                    bsk.twZF.awayZF.odds="0"  
                else :
                    bsk.twZF.homeZF.odds="0.95"
                    bsk.twZF.awayZF.odds="0.95"
            else :
                bsk.de.home=zfBK[2]
                bsk.de.away=zfBK[3]
                if homeO == '0' or  homeO == '0.0': 
                    bsk.twZF.homeZF.odds='0'
                    bsk.twZF.awayZF.odds='0' 
                else :
                    bsk.twZF.homeZF.odds="0.95"
                    bsk.twZF.awayZF.odds="0.95"

            dsBK = testBKds.calBKds(dsline,over,under)
            bsk.twDS.line=dsBK
            if over ==  '0' or over ==  "0.0" :
                bsk.twDS.over="0"
                bsk.twDS.under="0"
            else :
                bsk.twDS.over="0.94"
                bsk.twDS.under="0.94"
            sendData.append(copy.deepcopy(bsk))
            # print(bsk)

        # elif '球隊' in league or '三分球總數' in league or 'NBA - 總得分' or '冠軍' in league:
        else :
            # print(league)
            noCal.append(bsk)
            others = testCutOneP.justCutOne_fun(noCal)
            enData = APHDC_pb2.ApHdcArr()
            enData.ParseFromString(others)
            notNHLData = enData.aphdc
            for no in notNHLData :
                no
                sendData.append(copy.deepcopy(no))
    # # print(sendData)
    datas = APHDC_pb2.ApHdcArr()
    datas.aphdc.extend(sendData)
    data = datas.SerializeToString()  #變成byte
    return data
    




# enData = APHDC_pb2.ApHdcArr()
# enData.ParseFromString(f)
# Data = enData.aphdc
# basketball(Data)