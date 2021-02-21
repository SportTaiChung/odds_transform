# -*- coding:utf-8 -*-
import copy
import APHDC_noDB_pb2
import testCutOneP
import testBSzf
from sendMQ import telegramBot
import datetime as dt

def hockey(Data):
    for hc in Data.aphdc:
        try:
            source = hc.source
            league = hc.information.league
            gameType = hc.game_type
            gameClass = hc.game_class


            if '總得分' in league:  # 其他冰球賽事皆不用換算 只需減掉本金
                noCal = testCutOneP.justCutOne_fun(Data, single=hc)
            elif league not in ('NHL OT Included', 'NHL美國冰球聯季後賽(含加時賽)', '國家冰球聯盟包括加時'): # 此聯盟全場賽事需換算
                noCal = testCutOneP.justCutOne_fun(Data, single=hc)
            else:
                if 'full' in gameType and '1.5' in hc.usZF.homeZF.line:
                    try:
                        homeL = hc.usZF.homeZF.line
                        awayL = hc.usZF.awayZF.line
                        homeO = hc.usZF.homeZF.odds
                        awayO = hc.usZF.awayZF.odds
                        try:
                            homeDe = hc.de.home
                            awayDe = hc.de.away
                        except:
                            homeDe = '0.0'
                            awayDe = '0.0'
                        zfBS = testBSzf.calBSzf(source, gameClass, gameType, homeL, awayL, homeO, awayO, homeDe, awayDe)
                        hc.twZF.homeZF.line = zfBS[0]
                        hc.twZF.awayZF.line = zfBS[1]

                        ## 如果獨贏為0 讓分獨贏都關 因為算是需要讓分及獨贏缺一不可
                        if homeDe == '0' or zfBS[0] == '0+0':
                            hc.twZF.homeZF.odds = "0"
                            hc.twZF.awayZF.odds = "0"
                            hc.de.home = '0'
                            hc.de.away = '0'
                        else:
                            hc.de.home = zfBS[2]
                            hc.de.away = zfBS[3]
                            if homeO == '0':
                                hc.twZF.homeZF.odds = "0"
                                hc.twZF.awayZF.odds = "0"
                            else:
                                hc.twZF.homeZF.odds = "0.95"
                                hc.twZF.awayZF.odds = "0.95"


                        ## 一輸二贏 (美盤讓分盤口減一)
                        if homeO != '0':
                            hc.esre.let = 1 if "-" in homeL else 2
                            hc.esre.home = zfBS[4]
                            hc.esre.away = zfBS[5]
                    except:
                        pass

                    ## 大小
                    try:
                        line = hc.usDS.line
                        over = hc.usDS.over
                        under = hc.usDS.under
                        if over in ('0.0', '0'):
                            hc.twDS.line = '0+0'
                            hc.twDS.over = '0'
                            hc.twDS.under = '0'
                        else:
                            dsBS = testCutOneP.cutOne(over, under)
                            if '.5' in str(float(line)):
                                line = line
                            else:
                                line = str(float(line)).replace('.0', '+0')
                            hc.twDS.line = line
                            hc.twDS.over = dsBS[0]
                            hc.twDS.under = dsBS[1]
                    except:
                        pass
                else:
                    noCal = testCutOneP.justCutOne_fun(Data, single=hc)
        except Exception as e:
            telegramBot("HC錯誤")
        return Data


# if __name__ == "__main__":
    # testData = 
    # enData = APHDC_noDB_pb2.ApHdcArr()
    # enData.ParseFromString(testData)
    # Data = enData
    # hockey(Data)