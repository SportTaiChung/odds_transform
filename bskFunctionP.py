# -*- coding:utf-8 -*-
import numpy as np
import APHDC_pb2
import io
import sys
import json
import copy
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')
import testBKzf
import testBKds
import cutOneP


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
        homeDe= bsk.de.home
        awayDe= bsk.de.away
        
        dsline = bsk.usDS.line
        over = bsk.usDS.over
        under = bsk.usDS.under
        
        # ## 主客隊總得分
        # if '隊總得分' in league :
        #     dsBK = BKDS.calBKds(dsline,over,under)
        #     bsk.twDS.line=dsBK
        #     if over ==  '0' or over ==  "0.0" :
        #         bsk.twDS.over="0"
        #         bsk.twDS.under="0"
        #     else :
        #         bsk.twDS.over="0.94"
        #         bsk.twDS.under="0.94"

        #     sendData.append(copy.deepcopy(bsk))
        #優先得分球隊 , 最後得分球隊 , 三分球總數 ,NBA-總得分
        if '球隊' in league or '三分球總數' in league or 'NBA - 總得分' in league:
            noCal.append(bsk)
            others = cutOneP.justCutOne_fun(noCal)
            enData = APHDC_pb2.ApHdcArr()
            enData.ParseFromString(others)
            notNHLData = enData.aphdc
            for no in notNHLData :
                no
            sendData.append(copy.deepcopy(no))
        #一般比賽 夢幻配對賽 第一節~第四節 下半場
        else :
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
                bsk.de.home="0"
                bsk.de.away="0" 
                if homeO == '0' or  homeO == '0.0': 
                    bsk.twZF.homeZF.odds=zfBK[2]
                    bsk.twZF.awayZF.odds=zfBK[3] 
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
    # print(sendData)
    datas = APHDC_pb2.ApHdcArr()
    datas.aphdc.extend(sendData)
    data = datas.SerializeToString()  #變成byte
    return data
    


# enData = APHDC_pb2.ApHdcArr()
# enData.ParseFromString(f)
# Data = enData.aphdc
# basketball_fun(Data)