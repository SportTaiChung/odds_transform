# -*- coding:utf-8 -*-
import numpy as np
import APHDC_pb2
import json
import copy




def justCutOne_fun(Data):
    sendData =[]
    for cut in Data:
        
        homeline = cut.usZF.homeZF.line
        awayline = cut.usZF.awayZF.line
        homeodds = cut.usZF.homeZF.odds
        awayodds = cut.usZF.awayZF.odds

        dsline = cut.usDS.line 
        over = cut.usDS.over 
        under = cut.usDS.under

        dehome = cut.de.home
        deaway = cut.de.away
        

        if homeodds != "0" :
            cut.twZF.homeZF.line=homeline
            cut.twZF.awayZF.line=awayline
            cut.twZF.homeZF.odds=str(round((float(homeodds)-1),2))
            cut.twZF.awayZF.odds=str(round((float(awayodds)-1),2))
          
        else:
            pass


        if over != "0" :
            cut.twDS.line=dsline
            cut.twDS.over=str(round((float(over)-1),2))
            cut.twDS.under=str(round((float(under)-1),2))
        
        else:
            pass
        

        sendData.append(copy.deepcopy(cut))
        
        datas = APHDC_pb2.ApHdcArr()
        datas.aphdc.extend(sendData)
        data = datas.SerializeToString()  #變成byte
        

    # print(sendData)
    # return sendData
    return data


# f = b'\n\xae\x02\n\x04PS38\x12\x08football\x1a\x082nd half"\x0c9378925131322\x010:\x132019-01-13 05:35:00B\x132019-01-11 10:55:13J\x05falseRz\n(\xe5\x9c\x8b\xe5\xae\xb6\xe7\xbe\x8e\xe5\xbc\x8f\xe8\xb6\xb3\xe7\x90\x83\xe8\x81\xaf\xe7\x9b\x9f_\xe4\xb8\xbb\xe9\x9a\x8a\xe7\xb8\xbd\xe5\xbe\x97\xe5\x88\x86\x12\x19\xe4\xb8\xbb\xe9\x9a\x8a\xe7\xb8\xbd\xe5\xbe\x97\xe5\x88\x86_937892513\x1a\x14\n\x12\xe5\xa0\xaa\xe8\x96\xa9\xe6\x96\xaf\xe5\x9f\x8e\xe9\x85\x8b\xe9\x95\xb7"\x1d\n\x1b\xe5\x8d\xb0\xe7\xac\xac\xe5\xae\x89\xe7\xb4\x8d\xe6\xb3\xa2\xe5\x88\xa9\xe6\x96\xaf\xe5\xb0\x8f\xe9\xa6\xacZ\x06\n\x010\x12\x010b\x10\n\x06\n\x010\x12\x010\x12\x06\n\x010\x12\x010j\x14\n\x0430.5\x12\x051.826\x1a\x052.040r\x10\n\x06\n\x010\x12\x010\x12\x06\n\x010\x12\x010z\t\n\x010\x12\x010\x1a\x010\x82\x01\x06\n\x010\x12\x010\n\x9f\x02\n\x04PS38\x12\x08football\x1a\x082nd half"\x0c9382773411322\x010:\x132019-01-13 09:15:00B\x132019-01-11 10:55:13J\x05falseRk\n(\xe5\x9c\x8b\xe5\xae\xb6\xe7\xbe\x8e\xe5\xbc\x8f\xe8\xb6\xb3\xe7\x90\x83\xe8\x81\xaf\xe7\x9b\x9f_\xe4\xb8\xbb\xe9\x9a\x8a\xe7\xb8\xbd\xe5\xbe\x97\xe5\x88\x86\x12\x19\xe4\xb8\xbb\xe9\x9a\x8a\xe7\xb8\xbd\xe5\xbe\x97\xe5\x88\x86_938277341\x1a\x11\n\x0f\xe6\xb4\x9b\xe6\x9d\x89\xe7\xa3\xaf\xe5\x85\xac\xe7\xbe\x8a"\x11\n\x0f\xe9\x81\x94\xe6\x8b\x89\xe6\x96\xaf\xe7\x89\x9b\xe4\xbb\x94Z\x06\n\x010\x12\x010b\x10\n\x06\n\x010\x12\x010\x12\x06\n\x010\x12\x010j\x14\n\x0428.5\x12\x051.900\x1a\x051.943r\x10\n\x06\n\x010\x12\x010\x12\x06\n\x010\x12\x010z\t\n\x010\x12\x010\x1a\x010\x82\x01\x06\n\x010\x12\x010\n\xa2\x02\n\x04PS38\x12\x08football\x1a\x082nd half"\x0c9382264071322\x010:\x132019-01-14 02:05:00B\x132019-01-11 10:55:13J\x05falseRn\n(\xe5\x9c\x8b\xe5\xae\xb6\xe7\xbe\x8e\xe5\xbc\x8f\xe8\xb6\xb3\xe7\x90\x83\xe8\x81\xaf\xe7\x9b\x9f_\xe4\xb8\xbb\xe9\x9a\x8a\xe7\xb8\xbd\xe5\xbe\x97\xe5\x88\x86\x12\x19\xe4\xb8\xbb\xe9\x9a\x8a\xe7\xb8\xbd\xe5\xbe\x97\xe5\x88\x86_938226407\x1a\x14\n\x12\xe6\x96\xb0\xe8\x8b\xb1\xe5\x80\xab\xe6\x84\x9b\xe5\x9c\x8b\xe8\x80\x85"\x11\n\x0f\xe6\xb4\x9b\xe6\x9d\x89\xe7\xa3\xaf\xe9\x96\x83\xe9\x9b\xbbZ\x06\n\x010\x12\x010b\x10\n\x06\n\x010\x12\x010\x12\x06\n\x010\x12\x010j\x14\n\x0426.5\x12\x051.961\x1a\x051.892r\x10\n\x06\n\x010\x12\x010\x12\x06\n\x010\x12\x010z\t\n\x010\x12\x010\x1a\x010\x82\x01\x06\n\x010\x12\x010\n\x9f\x02\n\x04PS38\x12\x08football\x1a\x082nd half"\x0c9382775231322\x010:\x132019-01-14 05:40:00B\x132019-01-11 10:55:13J\x05falseRk\n(\xe5\x9c\x8b\xe5\xae\xb6\xe7\xbe\x8e\xe5\xbc\x8f\xe8\xb6\xb3\xe7\x90\x83\xe8\x81\xaf\xe7\x9b\x9f_\xe4\xb8\xbb\xe9\x9a\x8a\xe7\xb8\xbd\xe5\xbe\x97\xe5\x88\x86\x12\x19\xe4\xb8\xbb\xe9\x9a\x8a\xe7\xb8\xbd\xe5\xbe\x97\xe5\x88\x86_938277523\x1a\x14\n\x12\xe6\x96\xb0\xe5\xa5\xa7\xe7\x88\xbe\xe8\x89\xaf\xe8\x81\x96\xe5\xbe\x92"\x0e\n\x0c\xe8\xb2\xbb\xe5\x9f\x8e\xe8\x80\x81\xe9\xb7\xb9Z\x06\n\x010\x12\x010b\x10\n\x06\n\x010\x12\x010\x12\x06\n\x010\x12\x010j\x14\n\x0429.5\x12\x051.757\x1a\x052.130r\x10\n\x06\n\x010\x12\x010\x12\x06\n\x010\x12\x010z\t\n\x010\x12\x010\x1a\x010\x82\x01\x06\n\x010\x12\x010'

# import requests
# enData = APHDC_pb2.ApHdcArr()
# enData.ParseFromString(f)
# Data = enData.aphdc
# print(justCutOne_fun(Data))
# headers = {
#     'content-type': "text/html;charset=utf-8",
#     'cache-control': "no-cache",
#     }
# url = "http://jvapi.iq168.net:56788/asia"
# res = requests.post(url, headers=headers, data=justCutOne_fun(Data))