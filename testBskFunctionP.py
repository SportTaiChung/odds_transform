# -*- coding:utf-8 -*-
import numpy as np
import APHDC_pb2
import json
import copy
import testBKzf
import testBKds
import testCutOneP
from sendMQ import telegramBot



def basketball(Data):
    sendData =[]
    noCalList=[]
    for bsk in Data :
        try :
            source = bsk.source
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
           
            if '_' in league :
                noCalList.append(bsk)
                noCal = testCutOneP.justCutOne_fun(noCalList)
                enData = APHDC_pb2.ApHdcArr()
                enData.ParseFromString(noCal)
                noCalData = enData.aphdc
                for no in noCalData :
                    no      
            else :            
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

                zfBK = testBKzf.calBKzf(source,gameType,homeL,awayL,homeO,awayO,homeDe,awayDe)
                bsk.twZF.homeZF.line=zfBK[0]
                bsk.twZF.awayZF.line=zfBK[1]
                

                if homeDe == '0' or homeDe == '0.0'  or homeDe =='': 
                    bsk.de.home='0'
                    bsk.de.away='0'  
                    if homeO == '0'  or  homeO == '0.0' or zfBK[0]== '0+0': 
                        bsk.twZF.homeZF.odds="0"
                        bsk.twZF.awayZF.odds="0"  
                    else :
                        bsk.twZF.homeZF.odds="0.95"
                        bsk.twZF.awayZF.odds="0.95"
                else :
                    bsk.de.home=zfBK[2]
                    bsk.de.away=zfBK[3]
                    if homeO == '0' or  homeO == '0.0' or zfBK[0]== '0+0': 
                        bsk.twZF.homeZF.odds='0'
                        bsk.twZF.awayZF.odds='0' 
                    else :
                        bsk.twZF.homeZF.odds="0.95"
                        bsk.twZF.awayZF.odds="0.95"
                
                dsBK = testBKds.calBKds(source,dsline,over,under)
                bsk.twDS.line=dsBK
                if over ==  '0' or over ==  "0.0" or  dsBK == '0+0' :
                    bsk.twDS.over="0"
                    bsk.twDS.under="0"
                else :
                    bsk.twDS.over="0.94"
                    bsk.twDS.under="0.94"
                
            sendData.append(copy.deepcopy(bsk))            
        except :
            telegramBot("BSK錯誤")
            telegramBot(str(Data))
    # print(sendData)
    datas = APHDC_pb2.ApHdcArr()
    datas.aphdc.extend(sendData)
    data = datas.SerializeToString()  #變成byte
    return data
    





# enData = APHDC_pb2.ApHdcArr()
# enData.ParseFromString(f)
# Data = enData.aphdc
# basketball(Data)