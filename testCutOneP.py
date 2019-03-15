# -*- coding:utf-8 -*-
import numpy as np
import APHDC_pb2
import json
import copy
import mapping

def cutOne(home,away):
    if home != '0' :
        hO = str(round((float(home) -1),2))
        aO = str(round((float(away) -1),2))
    else :
        hO = str(home)
        aO = str(away)
    return str(hO),str(aO)

def justCutOne_fun(Data):
    sendData =[]
    for cut in Data:
        try :
            homeline = cut.usZF.homeZF.line
            awayline = cut.usZF.awayZF.line
            homeodds = cut.usZF.homeZF.odds
            awayodds = cut.usZF.awayZF.odds
            if homeodds != "0" :
                if cut.game_class == 'soccer' :
                    cut.twZF.homeZF.line=mapping.scMap(homeline[1:])
                    cut.twZF.awayZF.line=mapping.scMap(awayline[1:])
                else :
                    cut.twZF.homeZF.line=homeline
                    cut.twZF.awayZF.line=awayline
                zf = cutOne(homeodds,awayodds)
                cut.twZF.homeZF.odds=zf[0]
                cut.twZF.awayZF.odds=zf[1]
            else:
                cut.twZF.homeZF.line='0+0'
                cut.twZF.awayZF.line='0+0'
                cut.twZF.homeZF.odds='0'
                cut.twZF.awayZF.odds='0'
        except :
            pass

        try :
            dsline = cut.usDS.line 
            over = cut.usDS.over 
            under = cut.usDS.under
            if over != "0" :
                if cut.game_class == 'soccer' :
                    cut.twDS.line=mapping.scMap(dsline[1:])
                else :
                    cut.twDS.line=dsline
                ds = cutOne(over,under)
                cut.twDS.over=ds[0]
                cut.twDS.under=ds[1]
            else:
                cut.twDS.line='0+0'
                cut.twDS.over='0'
                cut.twDS.under='0'
        except :
            pass

        try :
            dehome = cut.de.home
            deaway = cut.de.away
            de = cutOne(dehome,deaway)
            cut.de.home = de[0]
            cut.de.away = de[1]
        except :
            pass

        try:
            sdhome = cut.sd.home
            sdaway = cut.sd.away
            sd = cutOne(sdhome,sdaway)
            cut.sd.home = sd[0]
            cut.sd.away = sd[1]
        except :
            pass
        
        
        sendData.append(copy.deepcopy(cut))
        
        datas = APHDC_pb2.ApHdcArr()
        datas.aphdc.extend(sendData)
        data = datas.SerializeToString()  #變成byte
        
    return data





# enData = APHDC_pb2.ApHdcArr()
# enData.ParseFromString(f)
# Data = enData.aphdc
# justCutOne_fun(Data)

