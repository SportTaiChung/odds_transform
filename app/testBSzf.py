from app import mapping
from app import testBSde
from app.sendMQ import telegramBot

## 冰球棒球都是用亞洲賠率(不加本金)計算
def calBSzf(source, gameClass, gameType, homeL, awayL, homeO, awayO, homeDe, awayDe):

    if homeO in ('', '0', '0.0'):
        homeO = 0
        awayO = 0
    else:
        homeO = round((float(homeO)-1), 2)
        awayO = round((float(awayO)-1), 2)


    if homeDe in ('', '0', '0.0'):
        homeDe = 0
        awayDe = 0
    else:
        homeDe = round((float(homeDe)-1), 2)
        awayDe = round((float(awayDe)-1), 2)



    #上半場公式
   
    #如果讓分隊是低水,用低水-0.94
    #如果讓分隊是高水,用0.94-低水
    if gameType == '1st half':
        # 當球頭0.0的時候 判斷低水邊為讓分隊
        if '0.0' == homeL[1:]:
            if homeO < awayO:
                homeL = '-' + homeL[1:]
                awayL = '+' + awayL[1:]
            else:
                homeL = '+' + homeL[1:]
                awayL = '-' + awayL[1:]
        # 主讓
        if '-' in homeL: 
            # 主隊為低水邊                                   # 客隊為低水邊 
            water = (homeO-0.94)*30 if homeO < awayO else (0.94-awayO)*30
        # 客讓
        else:
            # 主隊為低水邊                                   # 客隊為低水邊
            water = (0.94-homeO)*30 if homeO < awayO else (awayO-0.94)*30

        # print(water)
        #棒球級距為5 Ex: 1+5 1+10
        percent = round(water*2)/2
        # print(percent)
    else:
        #公式
        limit1 = (awayDe*(100-((100-(100*awayDe))/(awayO-awayDe))))-((100-(100*awayDe))/(awayO-awayDe))
        limit2 = ((homeO*((100-(100*homeDe))/(homeO-homeDe)))-(100-((100-(100*homeDe))/(homeO-homeDe))))*-1
        water = (limit1+limit2)/2
    
        #棒球級距為5 Ex: 1+5 1+10
        if water == 0:
            percent = 0
        elif water > 0:
            if  water%5 < 3:
                percent = 5 * int(water/5)
            else:
                percent = 5 * int(water/5) +5
        else:
            residue = water%5
            if residue < -0.5:
                percent = 5 *int(water/5) -5
            else:
                percent = 5 *int(water/5)

    #獨贏低水邊為讓邊
    if homeDe != 0:
        if homeDe < awayDe:
            hL = '-'
            aL = '+'
        else:
            hL = '+'
            aL = '-'
    else:
        hL = homeL[0]
        aL = awayL[0]

    #如果沒有mapping到就關盤 
    
    try:
        try:
            if gameType == '1st half':
                if '0.0' == homeL[1:]:
                    L = mapping.bshalf0(percent)
                elif '0.5' == homeL[1:]:
                    L = mapping.bshalf05(percent)
                elif '1.0' == homeL[1:]:
                    L = mapping.bshalf1(percent)
                h = hL + L
                a = aL + L
            else:
                try:
                    L = mapping.bsMap(percent/100)
                    h = hL + L
                    a = aL + L
                except:
                    deCalzf = testBSde.calBSde(source, gameClass, gameType, homeDe+1, awayDe+1)
                    h = deCalzf[0]
                    a = deCalzf[1]
        except:
            h = '0+0'
            a = '0+0'
    except:
        telegramBot(source+","+"BSzfMapping錯誤"+","+str(gameType)+","+str(homeL)+","+str(awayL)+","+str(homeO)+","+str(awayO)+","+str(homeDe)+","+str(awayDe))

    # print(h ,a , homeO ,awayO ,homeDe ,awayDe)
    return str(h), str(a), str(homeDe), str(awayDe), str(homeO), str(awayO)

# if __name__ == '__main__':
#     source = 'PS38'
#     gameClass ='mlb'
#     gameType ='1st half'
#     homeL = '+1.0'
#     awayL = '-1.0'
#     homeO = '1.909'
#     awayO = '1.98'
#     homeDe = '0.0'
#     awayDe = '0.0'
#     calBSzf(source,gameClass,gameType,homeL,awayL,homeO,awayO,homeDe,awayDe)
