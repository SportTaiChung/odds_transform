# -*- coding:utf-8 -*-
import copy
import traceback
import APHDC_noDB_pb2
import testBKzf
import testBKds
import testCutOneP
import datetime as dt


def basketball(Data):
    for bsk in Data.aphdc:
        try:
            source = bsk.source
            gameType = bsk.game_type
            league = bsk.information.league
            gameID = bsk.game_id
            sdH = bsk.sd.home
            sdA = bsk.sd.away
            deH = bsk.de.home
            deA = bsk.de.away
            homeL = bsk.usZF.homeZF.line
            awayL = bsk.usZF.awayZF.line
            homeO = bsk.usZF.homeZF.odds
            awayO = bsk.usZF.awayZF.odds
            dsline = bsk.usDS.line
            over = bsk.usDS.over
            under = bsk.usDS.under

            if (gameType == 'full' and gameID[-1] == '0') or (gameType=='1st half' and gameID[-2] == '0'):
                if sdH not in ('0', '0.0', ''):
                    sd = testCutOneP.cutOne(sdH, sdA)
                    bsk.sd.home = sd[0]
                    bsk.sd.away = sd[1]
                if '_' in league:
                    noCal = testCutOneP.justCutOne_fun(Data, single=bsk)
                    noCalData = noCal.aphdc
                else:

                    if homeO == '':
                        # 讓分空不理
                        pass
                    elif homeO in ('0', '0.0'):
                        # 讓分要給0
                        bsk.twZF.homeZF.line = "0"
                        bsk.twZF.awayZF.line = "0"
                        bsk.twZF.homeZF.odds = "0"
                        bsk.twZF.awayZF.odds = "0"
                        if deH not in ('0', '0.0', ''):
                            # 獨贏有值要減1
                            de = testCutOneP.cutOne(deH, deA)
                            bsk.de.home = de[0]
                            bsk.de.away = de[1]
                        else:
                            # 獨贏0或空不理
                            pass
                    else:
                        # 讓分要計算
                        zfBK = testBKzf.calBKzf(source, gameType, homeL, awayL, homeO, awayO, deH, deA)
                        bsk.twZF.homeZF.line = zfBK[0]
                        bsk.twZF.awayZF.line = zfBK[1]

                        if zfBK[2] == '0.0':
                            # 獨贏是0或空不理
                            if zfBK[0] == '0+0':
                                #讓分算不出關盤
                                bsk.twZF.homeZF.odds = "false"
                                bsk.twZF.awayZF.odds = "0"
                            else:
                                #讓分正確給0.95
                                bsk.twZF.homeZF.odds = "0.95"
                                bsk.twZF.awayZF.odds = "0.95"
                        else:
                            # 獨贏有值
                            bsk.de.home = zfBK[2]
                            bsk.de.away = zfBK[3]
                            if zfBK[0] == '0+0':
                                #讓分算不出關盤
                                bsk.twZF.homeZF.odds = 'false'
                                bsk.twZF.awayZF.odds = '0'
                            else:
                                #讓分正確給0.95
                                bsk.twZF.homeZF.odds = "0.95"
                                bsk.twZF.awayZF.odds = "0.95"


                    if over in (''):
                        pass
                    elif over in ('0', '0.0'):
                        bsk.twDS.line = "0"
                        bsk.twDS.over = "0"
                        bsk.twDS.under = "0"
                    else:
                        dsBK = testBKds.calBKds(source, dsline, over, under)
                        bsk.twDS.line = dsBK
                        if dsBK == '0+0':
                            # 大小算不出關盤
                            bsk.twDS.over = "false"
                            bsk.twDS.under = "0"
                        else:
                            # 大小正確給0.95
                            bsk.twDS.over = "0.94"
                            bsk.twDS.under = "0.94"
            else:
                if homeL not in ('0', '0.0', ''):
                    bsk.twZF.homeZF.line = homeL.replace('.0','+0').replace('.5','-100')
                    bsk.twZF.awayZF.line = awayL.replace('.0','+0').replace('.5','-100')
                    zfCutOne = testCutOneP.cutOne(homeO,awayO)
                    bsk.twZF.homeZF.odds, bsk.twZF.awayZF.odds = zfCutOne
                    bsk.twDS.line = dsline.replace('.0','+0').replace('.5','-100')
                    bsCutOne = testCutOneP.cutOne(over,under)
                    bsk.twDS.over, bsk.twDS.under = bsCutOne
                    if deH not in ('0', '0.0', ''):
                        # 獨贏有值要減1
                        de = testCutOneP.cutOne(deH, deA)
                        bsk.de.home = de[0]
                        bsk.de.away = de[1]
                # 籃球團隊總得分走地
                elif gameType in ('live full', '2nd half'):
                    bsk.twZF.homeZF.line = homeL.replace('.0','+0').replace('.5','-100')
                    bsk.twZF.awayZF.line = awayL.replace('.0','+0').replace('.5','-100')
                    zfCutOne = testCutOneP.cutOne(homeO,awayO)
                    bsk.twZF.homeZF.odds, bsk.twZF.awayZF.odds = zfCutOne
                    bsk.twDS.line = dsline.replace('.0','+0').replace('.5','-100')
                    bsCutOne = testCutOneP.cutOne(over,under)
                    bsk.twDS.over, bsk.twDS.under = bsCutOne
        except Exception as e:
            traceback.print_exc()
        return Data

# if __name__ == '__main__':
    # ff = open('ps38_basketball_today.bin', 'rb')
    # testData = ff.read()
    # enData = APHDC_noDB_pb2.ApHdcArr()
    # enData.ParseFromString(testData)
    # Data = enData.aphdc
    # out = basketball(Data)

