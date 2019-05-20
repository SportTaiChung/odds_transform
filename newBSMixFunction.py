import copy
import APHDC_pb2
import testBSzf
import testBSds
import testBSde
import testCutOneP
import newBSds
import newBSzf
from sendMQ import telegramBot
import datetime as dt

def baseballMix(Data):
    try:
        sendData = []
        noCalList = []
        for bs in Data:
            source = bs.source
            league = bs.information.league
            gameType = bs.game_type
            gameClass = bs.game_class
            homeDe = bs.de.home
            awayDe = bs.de.away
            if homeDe == '0.0' or homeDe == '':
                homeDe = '0'
                awayDe = '0'
            homeL = bs.usZF.homeZF.line
            awayL = bs.usZF.awayZF.line
            homeO = bs.usZF.homeZF.odds
            awayO = bs.usZF.awayZF.odds
            line = bs.usDS.line
            over = bs.usDS.over
            under = bs.usDS.under
            if '_' in league:
                noCalList.append(bs)
                noCal = testCutOneP.justCutOne_fun(noCalList)
                enData = APHDC_pb2.ApHdcArr()
                enData.ParseFromString(noCal)
                noCalData = enData.aphdc
                for no in noCalData:
                    no
            elif "總得分" in league:
                dsBS = testBSds.calBSds(source, gameClass, gameType, line, over, under)
                bs.twDS.line = dsBS
                if over == '0' or over == "0.0" or dsBS == '0+0':
                    bs.twDS.over = "0"
                    bs.twDS.under = "0"
                else:
                    bs.twDS.over = "0.94"
                    bs.twDS.under = "0.94"
                bs.twZF.homeZF.line = '0+0'
                bs.twZF.homeZF.odds = '0'
                bs.twZF.awayZF.line = '0+0'
                bs.twZF.awayZF.odds = '0'

            else:
                #上半場
                if gameType == '1st half':
                    zfBShalf = testBSzf.calBSzf(source, gameClass, gameType, homeL, awayL, homeO, awayO, homeDe, awayDe)
                    bs.de.home = zfBShalf[2]
                    bs.de.away = zfBShalf[3]
                    bs.twZF.homeZF.line = zfBShalf[0]
                    bs.twZF.awayZF.line = zfBShalf[1]
                    if homeO == '0' or zfBShalf[0] == '0+0':
                        bs.twZF.homeZF.odds = "0"
                        bs.twZF.awayZF.odds = "0"
                    else:
                        bs.twZF.homeZF.odds = "0.95"
                        bs.twZF.awayZF.odds = "0.95"

                    dsBS = testBSds.calBSds(source, gameClass, gameType, line, over, under)
                    bs.twDS.line = dsBS
                    if over == '0' or over == "0.0" or dsBS == '0+0':
                        bs.twDS.over = "0"
                        bs.twDS.under = "0"
                    else:
                        bs.twDS.over = "0.94"
                        bs.twDS.under = "0.94"
                #全場
                else:
                    # print(homeL)
                    if ',' in homeL :
                        zfBS = newBSzf.calBSzf(source,gameClass,gameType,homeL,awayL,homeO,awayO)
                        bs.twZF.homeZF.line = zfBS[0]
                        bs.twZF.awayZF.line = zfBS[1]
                        if zfBS[0] == '0+0':
                            bs.twZF.homeZF.odds = "0"
                            bs.twZF.awayZF.odds = "0"
                        else:
                            bs.twZF.homeZF.odds = "0.95"
                            bs.twZF.awayZF.odds = "0.95"
                            bs.de.home = str(round((float(homeDe)-1),2))
                            bs.de.away = str(round((float(awayDe)-1),2))
                            bs.usZF.homeZF.line = homeL.split(',')[0]
                            bs.usZF.awayZF.line = awayL.split(',')[0]
                            bs.usZF.homeZF.odds = str(round((float(zfBS[2])+1),2))
                            bs.usZF.awayZF.odds = str(round((float(zfBS[3])+1),2))
                        ## 一輸二贏 (美盤讓分盤口減一)
                        bs.esre.let = 1 if "-" in homeL else 2
                        bs.esre.home = zfBS[2]
                        bs.esre.away = zfBS[3]
                        # print(bs)
                    else:
                        # 若 沒讓分 有獨贏 用獨贏算讓分的算法
                        if homeDe != '0':
                            if homeO in ('0', '', '0.0'): #沒讓分有獨贏
                                zfBS1 = testBSde.calBSde(source, gameClass, gameType, homeDe, awayDe)
                                bs.twZF.homeZF.line = zfBS1[0]
                                bs.twZF.awayZF.line = zfBS1[1]
                                if homeDe == '0' or zfBS1[0] == '0+0':
                                    bs.twZF.homeZF.odds = "0"
                                    bs.twZF.awayZF.odds = "0"
                                    bs.de.home = '0'
                                    bs.de.away = '0'
                                else:
                                    bs.twZF.homeZF.odds = "0.95"
                                    bs.twZF.awayZF.odds = "0.95"
                                    bs.de.home = zfBS1[2]
                                    bs.de.away = zfBS1[3]
                            # 若 有讓分 有獨贏 用讓分＋獨贏的算法
                            else:  #有獨贏有讓分
                                zfBS2 = testBSzf.calBSzf(source, gameClass, gameType, homeL, awayL, homeO, awayO, homeDe, awayDe)
                                bs.de.home = zfBS2[2]
                                bs.de.away = zfBS2[3]
                                bs.twZF.homeZF.line = zfBS2[0]
                                bs.twZF.awayZF.line = zfBS2[1]
                                if homeO == '0' or '0+0' == zfBS2[0]:
                                    bs.twZF.homeZF.odds = "0"
                                    bs.twZF.awayZF.odds = "0"
                                else:
                                    bs.twZF.homeZF.odds = "0.95"
                                    bs.twZF.awayZF.odds = "0.95"

                                ## 一輸二贏 (美盤讓分盤口減一)
                                bs.esre.let = 1 if "-" in homeL else 2
                                bs.esre.home = zfBS2[4]
                                bs.esre.away = zfBS2[5]
                if league == '美國職棒大聯盟 (MLB)' and gameType == 'full':
                    dsBS = newBSds.calBSds(source, gameClass, line, over, under)
                    bs.twDS.line = dsBS[0]
                    bs.usDS.line = dsBS[1]
                    bs.usDS.over = str(round((float(dsBS[2])+1),2))
                    bs.usDS.under = str(round((float(dsBS[3])+1),2))
                    if over == '0' or over == "0.0" or dsBS == '0+0':
                        bs.twDS.over = "0"
                        bs.twDS.under = "0"
                    else:
                        bs.twDS.over = "0.94"
                        bs.twDS.under = "0.94"
                else :
                    dsBS = testBSds.calBSds(source, gameClass, gameType, line, over, under)
                    bs.twDS.line = dsBS
                    if over == '0' or over == "0.0" or dsBS == '0+0':
                        bs.twDS.over = "0"
                        bs.twDS.under = "0"
                    else:
                        bs.twDS.over = "0.94"
                        bs.twDS.under = "0.94"

            sendData.append(copy.deepcopy(bs))
        # print(sendData)
        datas = APHDC_pb2.ApHdcArr()
        datas.aphdc.extend(sendData)
        data = datas.SerializeToString()  #變成byte
        return data
    except Exception as e:
        pass
        telegramBot("BS錯誤")
        datas = APHDC_pb2.ApHdcArr()
        datas.aphdc.extend(Data)
        data = datas.SerializeToString()
        BSfile = open('bs.log','a')
        BSfile.write(str(data)+'\n'+str(e)+'\n'+dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')+'\n')




# f = b'\n\xc5\x02\n\x04PS38\x12\x03mlb\x1a\x081st half"\n9873772501*\x0c149.28.23.642\x010:\x132019-05-18 07:05:00B\x132019-05-17 14:17:19J\x05falseRg\n\x1b\xe7\xbe\x8e\xe5\x9c\x8b\xe8\x81\xb7\xe6\xa3\x92\xe5\xa4\xa7\xe8\x81\xaf\xe7\x9b\x9f (MLB)\x12\x0c0_9873772501\x1a\x1b\n\x0f\xe8\xb2\xbb\xe5\x9f\x8e\xe8\xb2\xbb\xe5\x9f\x8e\xe4\xba\xba\x12\x08C. Irvin"\x1d\n\x12\xe7\xa7\x91\xe7\xbe\x85\xe6\x8b\x89\xe5\xa4\x9a\xe8\x90\xbd\xe7\xa3\xaf\x12\x07J. GrayZ\x06\n\x010\x12\x010b\x1e\n\r\n\x04+0.0\x12\x051.847\x12\r\n\x04-0.0\x12\x052.050j\x13\n\x035.0\x12\x051.943\x1a\x051.925r\x1e\n\r\n\x05-0-25\x12\x040.95\x12\r\n\x05+0-25\x12\x040.95z\x11\n\x035+0\x12\x040.94\x1a\x040.94\x82\x01\x06\n\x010\x12\x010\n\x94\x02\n\x04PS38\x12\x03mlb\x1a\x081st half"\n9873772611*\x0c149.28.23.642\x010:\x132019-05-18 07:05:00B\x132019-05-17 14:17:19J\x05falseRi\n\x1b\xe7\xbe\x8e\xe5\x9c\x8b\xe8\x81\xb7\xe6\xa3\x92\xe5\xa4\xa7\xe8\x81\xaf\xe7\x9b\x9f (MLB)\x12\x0c0_9873772611\x1a\x1e\n\x0f\xe8\x8f\xaf\xe7\x9b\x9b\xe9\xa0\x93\xe5\x9c\x8b\xe6\xb0\x91\x12\x0bM. Scherzer"\x1c\n\x0f\xe8\x8a\x9d\xe5\x8a\xa0\xe5\x93\xa5\xe5\xb0\x8f\xe7\x86\x8a\x12\tC. HamelsZ\x06\n\x010\x12\x010b\x1e\n\r\n\x04-0.5\x12\x051.980\x12\r\n\x04+0.5\x12\x051.892j\x13\n\x034.0\x12\x051.840\x1a\x052.040\x82\x01\x06\n\x010\x12\x010\n\x95\x02\n\x04PS38\x12\x03mlb\x1a\x081st half"\n9873772511*\x0c149.28.23.642\x010:\x132019-05-18 07:10:00B\x132019-05-17 14:17:19J\x05falseRj\n\x1b\xe7\xbe\x8e\xe5\x9c\x8b\xe8\x81\xb7\xe6\xa3\x92\xe5\xa4\xa7\xe8\x81\xaf\xe7\x9b\x9f (MLB)\x12\x0c0_9873772511\x1a\x1e\n\x0f\xe6\xb3\xa2\xe5\xa3\xab\xe9\xa0\x93\xe7\xb4\x85\xe8\xa5\xaa\x12\x0bR. Porcello"\x1d\n\x12\xe4\xbc\x91\xe5\xa3\xab\xe9\xa0\x93\xe5\xa4\xaa\xe7\xa9\xba\xe4\xba\xba\x12\x07G. ColeZ\x06\n\x010\x12\x010b\x1e\n\r\n\x04+0.5\x12\x051.900\x12\r\n\x04-0.5\x12\x051.970j\x13\n\x035.5\x12\x052.030\x1a\x051.847\x82\x01\x06\n\x010\x12\x010\n\x97\x02\n\x04PS38\x12\x03mlb\x1a\x081st half"\n9873772531*\x0c149.28.23.642\x010:\x132019-05-18 07:10:00B\x132019-05-17 14:17:19J\x05falseRl\n\x1b\xe7\xbe\x8e\xe5\x9c\x8b\xe8\x81\xb7\xe6\xa3\x92\xe5\xa4\xa7\xe8\x81\xaf\xe7\x9b\x9f (MLB)\x12\x0c0_9873772531\x1a#\n\x12\xe8\xbe\x9b\xe8\xbe\x9b\xe9\x82\xa3\xe6\x8f\x90\xe7\xb4\x85\xe4\xba\xba\x12\rA. Desclafani"\x1a\n\x0f\xe6\xb4\x9b\xe6\x9d\x89\xe7\xa3\xaf\xe9\x81\x93\xe5\xa5\x87\x12\x07R. HillZ\x06\n\x010\x12\x010b\x1e\n\r\n\x04+0.5\x12\x051.854\x12\r\n\x04-0.5\x12\x052.020j\x13\n\x035.0\x12\x051.862\x1a\x052.020\x82\x01\x06\n\x010\x12\x010\n\xa0\x02\n\x04PS38\x12\x03mlb\x1a\x081st half"\n9873772571*\x0c149.28.23.642\x010:\x132019-05-18 07:10:00B\x132019-05-17 14:17:19J\x05falseRu\n\x1b\xe7\xbe\x8e\xe5\x9c\x8b\xe8\x81\xb7\xe6\xa3\x92\xe5\xa4\xa7\xe8\x81\xaf\xe7\x9b\x9f (MLB)\x12\x0c0_9873772571\x1a(\n\x18\xe5\x85\x8b\xe9\x87\x8c\xe5\xa4\xab\xe8\x98\xad\xe5\x8d\xb0\xe5\x9c\xb0\xe5\xae\x89\xe4\xba\xba\x12\x0cJ. Rodriguez"\x1e\n\x12\xe5\xb7\xb4\xe7\x88\xbe\xe7\x9a\x84\xe6\x91\xa9\xe9\x87\x91\xe9\xb6\xaf\x12\x08D. BundyZ\x06\n\x010\x12\x010b\x1e\n\r\n\x04-0.5\x12\x051.840\x12\r\n\x04+0.5\x12\x052.040j\x13\n\x035.0\x12\x051.952\x1a\x051.917\x82\x01\x06\n\x010\x12\x010\n\x95\x02\n\x04PS38\x12\x03mlb\x1a\x081st half"\n9873772581*\x0c149.28.23.642\x010:\x132019-05-18 07:10:00B\x132019-05-17 14:17:19J\x05falseRj\n\x1b\xe7\xbe\x8e\xe5\x9c\x8b\xe8\x81\xb7\xe6\xa3\x92\xe5\xa4\xa7\xe8\x81\xaf\xe7\x9b\x9f (MLB)\x12\x0c0_9873772581\x1a\x1c\n\x0f\xe5\xba\x95\xe7\x89\xb9\xe5\xbe\x8b\xe8\x80\x81\xe8\x99\x8e\x12\tD. Norris"\x1f\n\x12\xe5\xa5\xa7\xe5\x85\x8b\xe8\x98\xad\xe9\x81\x8b\xe5\x8b\x95\xe5\xae\xb6\x12\tF. MontasZ\x06\n\x010\x12\x010b\x1e\n\r\n\x04+0.5\x12\x051.990\x12\r\n\x04-0.5\x12\x051.884j\x13\n\x034.5\x12\x051.840\x1a\x052.040\x82\x01\x06\n\x010\x12\x010\n\x97\x02\n\x04PS38\x12\x03mlb\x1a\x081st half"\n9873772541*\x0c149.28.23.642\x010:\x132019-05-18 07:10:00B\x132019-05-17 14:17:19J\x05falseRl\n\x1b\xe7\xbe\x8e\xe5\x9c\x8b\xe8\x81\xb7\xe6\xa3\x92\xe5\xa4\xa7\xe8\x81\xaf\xe7\x9b\x9f (MLB)\x12\x0c0_9873772541\x1a!\n\x12\xe9\x82\x81\xe9\x98\xbf\xe5\xaf\x86\xe9\xa6\xac\xe6\x9e\x97\xe9\xad\x9a\x12\x0bT. Richards"\x1c\n\x0f\xe7\xb4\x90\xe7\xb4\x84\xe5\xa4\xa7\xe9\x83\xbd\xe6\x9c\x83\x12\tJ. DeGromZ\x06\n\x010\x12\x010b\x1e\n\r\n\x04+0.5\x12\x052.070\x12\r\n\x04-0.5\x12\x051.819j\x13\n\x033.5\x12\x052.070\x1a\x051.813\x82\x01\x06\n\x010\x12\x010\n\x9a\x02\n\x04PS38\x12\x03mlb\x1a\x081st half"\n9873784641*\x0c149.28.23.642\x010:\x132019-05-18 07:20:00B\x132019-05-17 14:17:19J\x05falseRo\n\x1b\xe7\xbe\x8e\xe5\x9c\x8b\xe8\x81\xb7\xe6\xa3\x92\xe5\xa4\xa7\xe8\x81\xaf\xe7\x9b\x9f (MLB)\x12\x0c0_9873784641\x1a\x1e\n\x12\xe4\xba\x9e\xe7\x89\xb9\xe8\x98\xad\xe5\xa4\xa7\xe5\x8b\x87\xe5\xa3\xab\x12\x08M. Fried""\n\x15\xe5\xaf\x86\xe7\x88\xbe\xe7\x93\xa6\xe5\x9f\xba\xe9\x87\x80\xe9\x85\x92\xe4\xba\xba\x12\tJ. ChacinZ\x06\n\x010\x12\x010b\x1e\n\r\n\x04-0.5\x12\x052.000\x12\r\n\x04+0.5\x12\x051.877j\x13\n\x035.0\x12\x051.833\x1a\x052.040\x82\x01\x06\n\x010\x12\x010\n\x91\x02\n\x04PS38\x12\x03mlb\x1a\x081st half"\n9873840401*\x0c149.28.23.642\x010:\x132019-05-18 08:10:00B\x132019-05-17 14:17:19J\x05falseRf\n\x1b\xe7\xbe\x8e\xe5\x9c\x8b\xe8\x81\xb7\xe6\xa3\x92\xe5\xa4\xa7\xe8\x81\xaf\xe7\x9b\x9f (MLB)\x12\x0c0_9873840401\x1a\x1a\n\x0f\xe8\x8a\x9d\xe5\x8a\xa0\xe5\x93\xa5\xe7\x99\xbd\xe8\xa5\xaa\x12\x07I. Nova"\x1d\n\x0f\xe5\xa4\x9a\xe5\x80\xab\xe5\xa4\x9a\xe8\x97\x8d\xe9\xb3\xa5\x12\nA. SanchezZ\x06\n\x010\x12\x010b\x1e\n\r\n\x04+0.0\x12\x051.869\x12\r\n\x04-0.0\x12\x052.020j\x13\n\x035.0\x12\x051.980\x1a\x051.892\x82\x01\x06\n\x010\x12\x010\n\x9b\x02\n\x04PS38\x12\x03mlb\x1a\x081st half"\n9873925371*\x0c149.28.23.642\x010:\x132019-05-18 09:40:00B\x132019-05-17 14:17:19J\x05falseRp\n\x1b\xe7\xbe\x8e\xe5\x9c\x8b\xe8\x81\xb7\xe6\xa3\x92\xe5\xa4\xa7\xe8\x81\xaf\xe7\x9b\x9f (MLB)\x12\x0c0_9873925371\x1a!\n\x15\xe4\xba\x9e\xe5\x88\xa9\xe6\xa1\x91\xe9\x82\xa3\xe9\x9f\xbf\xe5\xb0\xbe\xe8\x9b\x87\x12\x08M. Kelly" \n\x0f\xe8\x88\x8a\xe9\x87\x91\xe5\xb1\xb1\xe5\xb7\xa8\xe4\xba\xba\x12\rJ. SamardzijaZ\x06\n\x010\x12\x010b\x1e\n\r\n\x04-0.5\x12\x052.020\x12\r\n\x04+0.5\x12\x051.854j\x13\n\x035.0\x12\x051.961\x1a\x051.909\x82\x01\x06\n\x010\x12\x010\n\x95\x02\n\x04PS38\x12\x03mlb\x1a\x081st half"\n9874007911*\x0c149.28.23.642\x010:\x132019-05-18 10:07:00B\x132019-05-17 14:17:19J\x05falseRj\n\x1b\xe7\xbe\x8e\xe5\x9c\x8b\xe8\x81\xb7\xe6\xa3\x92\xe5\xa4\xa7\xe8\x81\xaf\xe7\x9b\x9f (MLB)\x12\x0c0_9874007911\x1a\x1c\n\x0f\xe6\xb4\x9b\xe6\x9d\x89\xe7\xa3\xaf\xe5\xa4\xa9\xe4\xbd\xbf\x12\tM. Harvey"\x1f\n\x12\xe5\xa0\xaa\xe8\x96\xa9\xe6\x96\xaf\xe5\xb8\x82\xe7\x9a\x87\xe5\xae\xb6\x12\tB. KellerZ\x06\n\x010\x12\x010b\x1e\n\r\n\x04-0.5\x12\x051.877\x12\r\n\x04+0.5\x12\x051.990j\x13\n\x035.5\x12\x051.925\x1a\x051.943\x82\x01\x06\n\x010\x12\x010\n\x96\x02\n\x04PS38\x12\x03mlb\x1a\x081st half"\n9874007881*\x0c149.28.23.642\x010:\x132019-05-18 10:10:00B\x132019-05-17 14:17:19J\x05falseRk\n\x1b\xe7\xbe\x8e\xe5\x9c\x8b\xe8\x81\xb7\xe6\xa3\x92\xe5\xa4\xa7\xe8\x81\xaf\xe7\x9b\x9f (MLB)\x12\x0c0_9874007881\x1a!\n\x12\xe8\x81\x96\xe5\x9c\xb0\xe7\x89\x99\xe5\x93\xa5\xe6\x95\x99\xe5\xa3\xab\x12\x0bJ. Lucchesi"\x1b\n\x0f\xe5\x8c\xb9\xe8\x8c\xb2\xe5\xa0\xa1\xe6\xb5\xb7\xe7\x9b\x9c\x12\x08J. LylesZ\x06\n\x010\x12\x010b\x1e\n\r\n\x04-0.5\x12\x051.990\x12\r\n\x04+0.5\x12\x051.884j\x13\n\x034.0\x12\x051.943\x1a\x051.917\x82\x01\x06\n\x010\x12\x010\n\x96\x02\n\x04PS38\x12\x03mlb\x1a\x081st half"\n9874007901*\x0c149.28.23.642\x010:\x132019-05-18 10:10:00B\x132019-05-17 14:17:19J\x05falseRk\n\x1b\xe7\xbe\x8e\xe5\x9c\x8b\xe8\x81\xb7\xe6\xa3\x92\xe5\xa4\xa7\xe8\x81\xaf\xe7\x9b\x9f (MLB)\x12\x0c0_9874007901\x1a\x1e\n\x0f\xe8\xa5\xbf\xe9\x9b\x85\xe5\x9c\x96\xe6\xb0\xb4\xe6\x89\x8b\x12\x0bM. Gonzales"\x1e\n\x12\xe6\x98\x8e\xe5\xb0\xbc\xe8\x98\x87\xe9\x81\x94\xe9\x9b\x99\xe5\x9f\x8e\x12\x08M. PerezZ\x06\n\x010\x12\x010b\x1e\n\r\n\x04+0.0\x12\x052.060\x12\r\n\x04-0.0\x12\x051.840j\x13\n\x034.5\x12\x051.854\x1a\x052.020\x82\x01\x06\n\x010\x12\x010'

# enData = APHDC_pb2.ApHdcArr()
# enData.ParseFromString(f)
# Data = enData.aphdc
# baseballMix(Data)