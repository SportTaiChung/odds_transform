import traceback
import APHDC_noDB_pb2
import testBSzf
import testBSds
import testBSde
import testCutOneP
import newBSds
import newBSzf
import datetime as dt

def baseballMix(Data):
    for bs in Data.aphdc:
        try:
            source = bs.source
            league = bs.information.league
            gameType = bs.game_type
            gameClass = bs.game_class

            if '總得分' in league and gameClass == 'mlb' or '_' in league:
                handicaps = APHDC_noDB_pb2.ApHdcArr()
                handicaps.aphdc.append(bs)
                noCal = testCutOneP.justCutOne_fun(handicaps)
                noCalData = noCal.aphdc
            else:
                homeDe = bs.de.home
                awayDe = bs.de.away
                homeL = bs.usZF.homeZF.line
                awayL = bs.usZF.awayZF.line
                homeO = bs.usZF.homeZF.odds
                awayO = bs.usZF.awayZF.odds
                #上半場讓分
                if gameType == '1st half':
                    if homeO in (''):
                        # 讓分空不理
                        pass
                    elif homeO in ('0', '0.0'):
                        # 讓分要給0
                        bs.twZF.homeZF.line = "0"
                        bs.twZF.awayZF.line = "0"
                        bs.twZF.homeZF.odds = "0"
                        bs.twZF.awayZF.odds = "0"
                    else:
                        zfBShalf = testBSzf.calBSzf(source, gameClass, gameType, homeL, awayL, homeO, awayO, homeDe, awayDe)
                        bs.twZF.homeZF.line = zfBShalf[0]
                        bs.twZF.awayZF.line = zfBShalf[1]
                        if zfBShalf[0] == '0+0':
                            # 讓分算不出關盤
                            bs.twZF.homeZF.odds = "false"
                            bs.twZF.awayZF.odds = "0"
                        else:
                            # 讓分正確給0.95
                            bs.twZF.homeZF.odds = "0.95"
                            bs.twZF.awayZF.odds = "0.95"
                #全場讓分
                else:
                    # 讓分兩盤口
                    if ',' in homeL:
                        zfBStwo = newBSzf.calBSzf(source, gameClass, gameType, homeL, awayL, homeO, awayO)
                        bs.twZF.homeZF.line = zfBStwo[0]
                        bs.twZF.awayZF.line = zfBStwo[1]
                        if zfBStwo[0] == '0+0':
                            # 讓分算不出關盤
                            bs.usZF.homeZF.line = homeL.split(',')[0]
                            bs.usZF.awayZF.line = awayL.split(',')[0]
                            bs.usZF.homeZF.odds = homeO.split(',')[0]
                            bs.usZF.awayZF.odds = awayO.split(',')[0]
                            bs.twZF.homeZF.odds = "false"
                            bs.twZF.awayZF.odds = "0"
                        else:
                            # 讓分正確給0.95
                            bs.twZF.homeZF.odds = "0.95"
                            bs.twZF.awayZF.odds = "0.95"
                            bs.de.home = str(round((float(homeDe)-1), 2))
                            bs.de.away = str(round((float(awayDe)-1), 2))
                            bs.usZF.homeZF.line = homeL.split(',')[0]
                            bs.usZF.awayZF.line = awayL.split(',')[0]
                            bs.usZF.homeZF.odds = str(round((float(zfBStwo[2])+1), 2))
                            bs.usZF.awayZF.odds = str(round((float(zfBStwo[3])+1), 2))
                        ## 一輸二贏 (美盤讓分盤口減一)
                        bs.esre.let = 1 if "-" in homeL else 2
                        bs.esre.home = zfBStwo[2]
                        bs.esre.away = zfBStwo[3]
                    # 讓分單一盤口
                    else:
                        if homeDe in ('', '0', '0.0'):
                            if homeO in (''):
                                pass
                            elif homeO in ('0', '0.0'):
                                bs.twZF.homeZF.line = '0+0'
                                bs.twZF.awayZF.line = '0+0'
                                bs.twZF.homeZF.odds = "0"
                                bs.twZF.awayZF.odds = "0"
                            else:
                                pass
                        else:
                            if homeO in ('', '0', '0.0'):
                                # 有獨贏沒讓分 用 獨贏 算讓分的算法
                                zfBSde = testBSde.calBSde(source, gameClass, gameType, homeDe, awayDe)
                                bs.twZF.homeZF.line = zfBSde[0]
                                bs.twZF.awayZF.line = zfBSde[1]
                                if zfBSde[0] == '0+0':
                                    # 讓分算不出關盤
                                    bs.twZF.homeZF.line = '0+0'
                                    bs.twZF.awayZF.line = '0+0'
                                    bs.twZF.homeZF.odds = "false"
                                    bs.twZF.awayZF.odds = "0"
                                    bs.de.home = zfBSde[2]
                                    bs.de.away = zfBSde[3]

                                else:
                                    # 讓分正確給0.95
                                    bs.twZF.homeZF.odds = "0.95"
                                    bs.twZF.awayZF.odds = "0.95"
                                    bs.de.home = zfBSde[2]
                                    bs.de.away = zfBSde[3]
                            else:
                                # 有獨贏有讓分 用 獨贏+讓分 算讓分的算法
                                zfBS = testBSzf.calBSzf(source, gameClass, gameType, homeL, awayL, homeO, awayO, homeDe, awayDe)
                                bs.de.home = zfBS[2]
                                bs.de.away = zfBS[3]
                                bs.twZF.homeZF.line = zfBS[0]
                                bs.twZF.awayZF.line = zfBS[1]
                                if zfBS[0] == '0+0': ## 讓分算不出
                                    bs.twZF.homeZF.odds = "false"
                                    bs.twZF.awayZF.odds = "0"
                                else:
                                    bs.twZF.homeZF.odds = "0.95"
                                    bs.twZF.awayZF.odds = "0.95"

                                ## 一輸二贏 (美盤讓分盤口減一)
                                bs.esre.let = 1 if "-" in homeL else 2
                                bs.esre.home = zfBS[4]
                                bs.esre.away = zfBS[5]

                # 大小
                line = bs.usDS.line
                over = bs.usDS.over
                under = bs.usDS.under
                if over in (''):
                    pass
                elif over in ('0', '0.0'):
                    bs.twDS.line = '0'
                    bs.twDS.over = '0'
                    bs.twDS.under = '0'
                # 大小兩盤口
                elif ',' in line:
                    dsBS = newBSds.calBSds(source, gameClass, line, over, under)
                    bs.twDS.line = dsBS[0]
                    bs.usDS.line = dsBS[1]
                    bs.usDS.over = str(round((float(dsBS[2])+1), 2))
                    bs.usDS.under = str(round((float(dsBS[3])+1), 2))
                    if dsBS == '0+0': ## 大小算不出
                        bs.usDS.line = line.split(',')[0]
                        bs.usDS.over = over.split(',')[0]
                        bs.usDS.under = under.split(',')[0]
                        bs.twDS.over = "false"
                        bs.twDS.under = "0"
                    else:
                        bs.twDS.over = "0.94"
                        bs.twDS.under = "0.94"
                # 大小單一盤口
                else :
                    dsBS = testBSds.calBSds(source, gameClass, gameType, line, over, under)
                    bs.twDS.line = dsBS
                    if dsBS == '0+0': ## 大小算不出
                        bs.twDS.over = "false"
                        bs.twDS.under = "0"
                    else:
                        bs.twDS.over = "0.94"
                        bs.twDS.under = "0.94"
        except Exception as e:
            traceback.print_exc()
    return Data


if __name__ == '__main__':
    f = open('baseball.bin', 'rb')
    testData = f.read()
    enData = APHDC_noDB_pb2.ApHdcArr()
    enData.ParseFromString(testData)
    Data = enData.event
    print(Data)
    # baseballMix(Data) 

