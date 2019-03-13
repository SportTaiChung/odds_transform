# -*- coding:utf-8 -*-
import numpy as np
import APHDC_pb2
import io
import sys
import json
import copy
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')

def wt():
    wt = {}
    odds = [0, 25, 50, 75, -100, -75, -50, -25]
    line = np.array([0, 0, 0, 0, -1, -1, -1, -1, -1])
    odds2 = [-25, -50, -75, -100, 75, 50, 25, 0]
    line2 = np.array([0, 0, 0, 0, 1, 1, 1, 1, 1])

    line = line + 1
    line2 = line2 - 1
    number = 100
    for i in range(number):
        i2 = (i + 1) * -1
        j = i % 8
        # print(j)
        if j == 0: line = line - 1
        if j == 0: line2 = line2 + 1
        # print(line)
        # print(i,line[j] ,odds[j])
        # print(i2, line2[j], odds2[j])
        wt.update({i: {"x": line[j], "odd": odds[j]}})
        wt.update({i2: {"x": line2[j], "odd": odds2[j]}})
    # print(wt)
    return wt



def basketball_fun(Data):
    sendData =[]
    for bsk in Data :
        # print(bsk.game_id)
        gametype = bsk.game_class
        homeline = bsk.usZF.homeZF.line
        awayline = bsk.usZF.awayZF.line
        homeodds = float(bsk.usZF.homeZF.odds)
        awayodds = float(bsk.usZF.awayZF.odds)
        
        dsline = float(bsk.usDS.line)
        over = float(bsk.usDS.over)
        under = float(bsk.usDS.under)

        try :
            deH = float(bsk.de.home)
            deA = float(bsk.de.away)
        except :
            deH = '0'
            deA = '0'           
        if "+" in homeline :
            let = "away"
            line = float(homeline.replace("+",""))
            zf = float(homeodds)
            zf_let = float(awayodds)
            # let = "away"
            # line = float('+0.5'.replace("+",""))
            # zf = float(1.917)
            # zf_let = float(1.97)            
        elif "-" in homeline:
            let = "home"
            line = float(homeline.replace("-",""))
            zf = float(awayodds)
            zf_let = float(homeodds)
            # let = "home"
            # line = float('-0'.replace("-",""))
            # zf = float(1.909)
            # zf_let = float(1.961)        
        else :
            let = "equal"
            line = float(homeline)
            zf = float(homeodds)
            zf_let = float(awayodds)

        # print(let,line,zf,zf_let)
        ## 讓分zf,zf_let,line
        ## 大小under,over,dsline
        def share(zf,zf_let,line):
            wt_map = wt()
            zf = round(zf - 1.0, 4)
            zf_let = round(zf_let - 1.0, 4)
            # print(zf, zf_let)
            middle_line = (zf + zf_let) / 2
            diff = abs(zf_let - middle_line)

            index = int(diff / 0.013)
            line = abs(line)
            if zf == zf_let:
                middle = True
            else:
                middle = False
            # print("zf_let", zf_let)

            #賠率主客隊相等 盤口賠率不動
            if middle:
                if (float(line) % 1) == 0:
                    odds = 0
                    line_move = line
                else:
                    odds = -100
                    line_move = int(line)
            else:
                #賠率小於 0.95 ，所以賠率上調到0.95，盤口賠率下降
                if zf_let < middle_line:
                    if (line % 1) == 0.5:
                        index = -4 + index * -1
                    else:
                        index = index * -1
                    

                #賠率大於 0.95 ，所以賠率下調到0.95，盤口下陪率上升
                elif zf_let > middle_line:
                    if (line % 1) == 0.5:
                        index = -4 + index
                    else:
                        index = index

                

                move = wt_map[index]["x"]
                odds = wt_map[index]["odd"]
                line_move = int(line) + move
                
                return odds,line_move
            # print("line_move, odds", line_move, odds)

       
            
        try :
            # print(over,under)
            ## 0 0 0.95
            if over == under and float(over) != 0.0 :
                bsk.twDS.line=str(dsline)
                bsk.twDS.over="0.94"
                bsk.twDS.under="0.94"
            ## 0 0 0 
            elif over == under and float(dsline) == 0.0 :
                bsk.twDS.line="0"
                bsk.twDS.over="0"
                bsk.twDS.under="0"
               
                
            else : 
                odds = share(under,over,dsline)[0]
                line_move = share(under,over,dsline)[1]
            
                if "-" in str(odds) :
                    TWline = str(line_move) + str(odds).replace(" ","")
                else :
                    TWline = str(line_move) + "+" + str(odds).replace(" ","")

                bsk.twDS.line=TWline
                bsk.twDS.over="0.94"
                bsk.twDS.under="0.94"     
                
                
        except:
            bsk.twDS.line="0"
            bsk.twDS.over="0"
            bsk.twDS.under="0"
        
        
        
        try :
            ## 1.5  0.97 0.97 
            ## 0    0.95 0.95
            # print(line)
            # print(abs(float(zf)-((float(zf) + float(zf_let))/2))/0.013)
            # print(zf ,zf_let)
            if zf == zf_let and float(zf) != 0.0:
                bsk.twZF.homeZF.line=homeline
                bsk.twZF.awayZF.line=awayline
                bsk.twZF.homeZF.odds="0.95"
                bsk.twZF.awayZF.odds="0.95"
            elif zf == zf_let and float(zf) == 0.0:
                bsk.twZF.homeZF.line=homeline
                bsk.twZF.awayZF.line=awayline
                bsk.twZF.homeZF.odds="0"
                bsk.twZF.awayZF.odds="0"
            elif float(zf) == 0.0 and float(zf_let) == 0.0 and float(line) == 0.0 :
                bsk.twZF.homeZF.line="0"
                bsk.twZF.awayZF.line="0"
                bsk.twZF.homeZF.odds="0"
                bsk.twZF.awayZF.odds="0"
           
            else :
                odds = share(zf,zf_let,line)[0]
                line_move = share(zf,zf_let,line)[1]
                #處理台盤轉換中線盤 line 值 為 0 的情況
                if zf > zf_let:
                    zf_big = zf
                else:
                    zf_big = zf_let

                if odds >= 0:
                    twline = str(int(line_move)) + '+' + str(odds)
                else:
                    twline = str(int(line_move)) + str(odds)
                # print(line_move)

                        
                # print(line)
                # print(twline[0])
                if int(line) < 0 or twline[0] == "-" or twline[0] == "+":
                    twline = twline[1:]
                #     print(twline[1:])
                if let == "home":
                    # print(twline,line_move)
                    home_line = "-" + twline
                    away_line = "+" + twline
                    #籃球上半沒有 0+25的盤, 要換成 0-25
                    if line_move == 0 :
                        if "+" in twline:
                            twline = twline.replace("+","-")  
                            if zf < zf_let : 
                                home_line = "+" + twline
                                away_line = "-" + twline
                            else :
                                home_line = "-" + twline
                                away_line = "+" + twline                              
                    if zf < zf_let and twline == '0-0':
                        home_line = "+" + (twline).replace('-0','+0')
                        away_line = "-" + (twline).replace('-0','+0') 
                    elif zf > zf_let and twline == '0-0' :
                        home_line = "-" + (twline).replace('-0','+0')
                        away_line = "+" + (twline).replace('-0','+0') 
  
                                                  
                elif let == "away":
                    # print(twline,line_move)
                    home_line = "+" + twline
                    away_line = "-" + twline
                    #籃球上半沒有 0+25的盤, 要換成 0-25
                    if line_move == 0 :
                        if "+" in twline:
                            twline = twline.replace("+","-")  
                            if zf < zf_let : 
                                home_line = "-" + twline
                                away_line = "+" + twline
                            else :
                                home_line = "+" + twline
                                away_line = "-" + twline    
                    # print(zf,zf_let,home_line,away_line)
                    if zf < zf_let and twline == '0-0':
                        home_line = "-" + (twline).replace('-0','+0') 
                        away_line = "+" + (twline).replace('-0','+0') 
                    elif zf > zf_let and twline == '0-0' :
                        home_line = "+" + (twline).replace('-0','+0')
                        away_line = "-" + (twline).replace('-0','+0')
                elif let == "equal":
                    home_line = twline
                    away_line = twline  
                    if zf < zf_let and twline == 0-0:
                        home_line = "-" + (twline).replace('-0','+0') 
                        away_line = "+" + (twline).replace('-0','+0') 
                    else :
                        home_line = "+" + (twline).replace('-0','+0')
                        away_line = "-" + (twline).replace('-0','+0')                
                # print(home_line, away_line)

                bsk.twZF.homeZF.line=home_line
                bsk.twZF.awayZF.line=away_line
                bsk.twZF.homeZF.odds="0.95"
                bsk.twZF.awayZF.odds="0.95"   

            
            if deH != '0' :
                bsk.de.home = str(round(float(deH)-1,2))
                bsk.de.home = str(round(float(deA)-1,2))
            else :
                bsk.de.home = '0'
                bsk.de.home = '0'
            
            # print(bsk.de.home)
            
                # if let == 'away':
                #     print(let,line,zf,zf_let,bsk.twZF.homeZF.line,bsk.twZF.awayZF.line)
                # else : 
                #     print(let,line,zf_let,zf,bsk.twZF.homeZF.line,bsk.twZF.awayZF.line)
        except Exception as e:
            e
        
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