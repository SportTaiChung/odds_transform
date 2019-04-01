# -*- coding:utf-8 -*-
import cutOneP
import APHDC_pb2
import numpy as np
import testCutOneP
import io
import sys
import json  
import copy
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')

def round_half(number):
    return round(number * 2, 1) / 2

def baseball_fun(Data):
    sendData = []      
    notNHL =[]
    for bs in Data:
        # if (bs.information.league == "NHL美國冰球聯季後賽(含加時賽)")  or (any(BS in bs.game_class for BS in("mlb","npb","cpbl","kbo"))) :
        if  "NHL美國冰球聯季後賽(含加時賽)" not in bs.information.league  and  bs.game_class == "hockey":
            # print(bs.information.league)
            notNHL.append(bs)
            others = testCutOneP.justCutOne_fun(notNHL)
            enData = APHDC_pb2.ApHdcArr()
            enData.ParseFromString(others)
            notNHLData = enData.aphdc
            for no in notNHLData :
                no
            sendData.append(copy.deepcopy(no))
        elif '總得分' in bs.information.league :
            # print(bs.information.league)
            notNHL.append(bs)
            others = testCutOneP.justCutOne_fun(notNHL)
            enData = APHDC_pb2.ApHdcArr()
            enData.ParseFromString(others)
            notNHLData = enData.aphdc
            for no in notNHLData :
                no
            sendData.append(copy.deepcopy(no))
        else: 
            # print(bs.information.league)
            # bs.usZF.homeZF.odds = '3.32'
            # bs.usZF.awayZF.odds = '1.381'
            # bs.de.home = '0.96'
            # bs.de.away = '0.94'
            # bs.usZF.homeZF.line = '-1.5'
            if  bs.usZF.homeZF.odds !="0" and bs.de.home != "0":
                # print(bs.game_id)
                line = bs.usZF.homeZF.line
                p1 = 9650
                p2 = 9850
                
                if "+" in line: #被讓方
                    
                    zf = float(bs.usZF.homeZF.odds)-1
                    pk = float(bs.de.home)-1
                    zf_let = float(bs.usZF.awayZF.odds)-1
                    pk_let = float(bs.de.away)-1
                    foo1 = (p2 - pk * p1) / (zf - pk)
                    foo2 = (p2 - pk * p1) / (zf - pk)
                    limit1 = ((p1 - foo1) * pk - foo2) / p2

                    foo1 = (zf_let * p1 - p2) / (zf_let - pk_let)
                    foo2 = (zf_let * p1 - p2) / (zf_let - pk_let)
                    limit2 = ((p1 - foo1) * zf_let - foo2) * (-1) / p2

                    

                elif "-" in line : #讓方
                    zf = float(bs.usZF.awayZF.odds)-1
                    pk = float(bs.de.away) -1
                    zf_let = float(bs.usZF.homeZF.odds)-1
                    pk_let = float(bs.de.home) -1
                    foo1 = (zf * p1 - p2) / (zf - pk)
                    foo2 = (zf * p1 - p2) / (zf - pk)
                    limit1 = ((p1 - foo1) * zf - foo2) * (-1) / p2

                    foo1 = (p2 - pk_let * p1) / (zf_let - pk_let)
                    foo2 = (p2 - pk_let * p1) / (zf_let - pk_let)
                    limit2 = ((p1 - foo1) * pk_let - foo2) / p2
                
                # print(bs.game_id)
                # print(zf,zf_let)
                if line[1:] == "1.5":
                    home_away =1 if line[0]=="-" else 2
                    bs.esre.let = home_away
                    bs.esre.home = str(round(float(bs.usZF.homeZF.odds)-1,2))
                    bs.esre.away = str(round(float(bs.usZF.awayZF.odds)-1,2))
                    

                
                
                oddsmap = {
                    2.0: "0",
                    1.95: "0-5",
                    1.9: "0-10",
                    1.95: "0-15",
                    1.8: "0-20",
                    1.75: "0-25",
                    1.65: "0-35",
                    1.6: "0-40",
                    1.55: "0-45",
                    1.5: "0-50",
                    1.45: "0-55",
                    1.4: "0-60",
                    1.35: "0-65",
                    1.3: "0-70",
                    1.25: "0-75",
                    1.2: "0-80",
                    1.15: "0-85",
                    1.1: "0-90",
                    1.05: "0-95",
                    1: "0-100",
                    0.95: "1+95",
                    0.9: "1+90",
                    0.85: "1+85",
                    0.8: "1+80",
                    0.75: "1+75",
                    0.7: "1+70",
                    0.65: "1+65",
                    0.6: "1+60",
                    0.55: "1+55",
                    0.5: "1+50",
                    0.45: "1+45",
                    0.4: "1+40",
                    0.35: "1+35",
                    0.3: "1+30",
                    0.25: "1+25",
                    0.2: "1+20",
                    0.15: "1+15",
                    0.1: "1+10",
                    0.05: "1+5",
                    0.0: "1+0",
                    -0.05: "1-5",
                    -0.1: "1-10",
                    -0.15: "1-15",
                    -0.2: "1-20",
                    -0.25: "1-25",
                    -0.3: "1-30",
                    -0.35: "1-35",
                    -0.4: "1-40",
                    -0.45: "1-45",
                    -0.5: "1-50",
                    -0.55: "1-55",
                    -0.6: "1-60",
                    -0.65: "1-65",
                    -0.7: "1-70",
                    -0.75: "1-75",
                    -0.8: "1-80",
                    -0.85: "1-85",
                    -0.9: "1-90",
                    -0.95:"1-95",
                    -1: "1-100",
                    -1.05: "2+95",
                    -1.1: "2+90",
                    -1.15: "2+85",
                    -1.2: "2+80",
                    -1.25: "2+75",
                    -1.3: "2+70",
                    -1.35: "2+65",
                    -1.4: "2+60",
                    -1.45: "2+55",
                    -1.5: "2+50",
                    -1.55: "2+45",
                    -1.6: "2+40",
                    -1.65: "2+35",
                    -1.7: "2+30",
                    -1.75: "2+25",
                    -1.8: "2+20",
                    -1.85: "2+15",
                    -1.9: "2+10",
                    -1.95: "2+5",
                    -2.0: "2+0",
                    -2.05: "2-5",
                    -2.1: "2-10",
                    -2.15: "2-15",
                    -2.2: "2-20",
                    -2.25: "2-25",
                    -2.3: "2-30",
                    -2.35: "2-35",
                    -2.4: "2-40",
                    -2.45: "2-45",
                    -2.5: "2-50",
                    -2.55: "2-55",
                    -2.6: "2-60",
                    -2.65: "2-65",
                    -2.7: "2-70",
                    -2.75: "2-75",
                    -2.8: "2-80",
                    -2.85: "2-85",
                    -2.9: "2-90",
                    -2.95:"2-95",
                    -3.0: "3-100",
                    -3.05: "3+95",
                    -3.1: "3+90",
                    -3.15: "3+85",
                    -3.2: "3+80",
                    -3.25: "3+75",
                    -3.3: "3+70",
                    -3.35: "3+65",
                    -3.4: "3+60",
                    -3.45: "3+55",
                    -3.5: "3+50",
                    -3.55: "3+45",
                    -3.6: "3+40",
                    -3.65: "3+35",
                    -3.7: "3+30"
                    }

            
                average = round((limit1 + limit2) / 2, 2)
                # print(average)
                key = round_half(average)
                ##無平手(全場)   =================================================
               
                if 'full' in bs.game_type : 
                    if 2 > key >= 1 :
                        # print(key)
                        newkey = round_half(2-key)
                        # print(newkey)
                        newline = oddsmap[newkey]
                    else :
                        newline = oddsmap[key]
                    ##客讓        
                    if float(line) > 0:  
                        homeline = "+" + str(newline)
                        awayline = "-" + str(newline)
                        homede = pk
                        awayde = pk_let
                        if str(newline) == '0':
                            if zf > zf_let :
                                homeline = "+" + str(newline) + "+0"
                                awayline = "-" + str(newline) + "+0"
                            else:
                                homeline = "-" + str(newline) + "+0"
                                awayline = "+" + str(newline) + "+0"  
                        elif 2 > key >=1 :
                            if pk > pk_let :
                                homeline = "-" + str(newline) 
                                awayline = "+" + str(newline) 
                            else:
                                homeline = "+" + str(newline) 
                                awayline = "-" + str(newline) 
                        # print(homede,awayde,homeline,awayline,newline)                                             
                    ##主讓    
                    else:  
                        homeline = "-" + str(newline)
                        awayline = "+" + str(newline)
                        awayde = pk
                        homede = pk_let
                        
                        if str(newline) == '0':
                            if zf > zf_let :
                                homeline = "-" + str(newline) + "+0"
                                awayline = "+" + str(newline) + "+0"
                            else:
                                homeline = "+" + str(newline) + "+0"
                                awayline = "-" + str(newline) + "+0"  
                        elif 2 > key >=1 :
                            if pk > pk_let :
                                homeline = "-" + str(newline) 
                                awayline = "+" + str(newline) 
                            else:
                                homeline = "+" + str(newline) 
                                awayline = "-" + str(newline) 
                        # print(homede,awayde,homeline,awayline,newline)
                ## 有平手 (半場)    =============================================           
                else :  
                    try:
                        newline = oddsmap[key]
                    except:
                        newline = 0                    
                    if float(line) > 0:  ##客讓
                        homeline = "+" + str(newline)
                        awayline = "-" + str(newline)
                        homede = pk
                        awayde = pk_let
                        if str(newline) == '0':
                            if zf > zf_let :
                                homeline = "+" + str(newline) + "+0"
                                awayline = "-" + str(newline) + "+0"
                            else:
                                homeline = "-" + str(newline) + "+0"
                                awayline = "+" + str(newline) + "+0"                           
                        # print(pk,pk_let,newline,homeline,awayline)
                    else:                ##主讓
                        homeline = "-" + str(newline)
                        awayline = "+" + str(newline)
                        awayde = pk
                        homede = pk_let
                        # print(homede,awayde,homeline,awayline,newline)
                        if str(newline) == '0':
                            if zf > zf_let :
                                homeline = "-" + str(newline) + "+0"
                                awayline = "+" + str(newline) + "+0"
                            else:
                                homeline = "+" + str(newline) + "+0"
                                awayline = "-" + str(newline) + "+0"      
                        # print(pk,pk_let,newline,homeline,awayline)       
                    
                    
                
                bs.twZF.homeZF.line=homeline
                bs.twZF.awayZF.line=awayline
                bs.twZF.homeZF.odds="0.95"
                bs.twZF.awayZF.odds="0.95"
                if bs.usDS.over != '0' :
                    bs.twDS.line=bs.usDS.line
                    bs.twDS.over= str(round(float(bs.usDS.over)-1,2))
                    bs.twDS.under = str(round(float(bs.usDS.under)-1,2))
                else :
                    bs.twDS.over ="0"
                    bs.twDS.under ="0"
                # print(homeline,awayline)
            elif  bs.usZF.homeZF.odds =="0" or bs.de.home == "0":
                
                bs.twZF.homeZF.odds ="0"
                bs.twZF.awayZF.odds ="0"
                if bs.usDS.over == "0" :
                    bs.twDS.over ="0"
                    bs.twDS.under ="0"
                else :
                    bs.twDS.line=bs.usDS.line
                    bs.twDS.over =str(round(float(bs.usDS.over)-1,2))
                    bs.twDS.under =str(round(float(bs.usDS.under)-1,2))                
            
            
            sendData.append(copy.deepcopy(bs))                

 
    
    
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