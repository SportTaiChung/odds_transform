import mapping
import testBSde
from sendMQ import telegramBot

## 冰球棒球都是用亞洲賠率(不加本金)計算
def calBSzf(source, gameClass, gameType, homeL, awayL, homeO, awayO, homeDe, awayDe):

    if homeO != '0':
        homeO = round((float(homeO)-1), 2)
        awayO = round((float(awayO)-1), 2)
    else:
        homeO = 0
        awayO = 0
    if homeDe != '0':
        homeDe = round((float(homeDe)-1), 2)
        awayDe = round((float(awayDe)-1), 2)
    else:
        homeDe = 0
        awayDe = 0

    #上半場公式   
    if gameType == '1st half' :
        water = (homeO-0.94)*30 if homeO < awayO else (awayO-0.94)*30
        #棒球級距為5 Ex : 1+5 1+10
        percent = round(water*2)/2
        # print(percent)
    else :
        #公式
        limit1 = (awayDe*(100-((100-(100*awayDe))/(awayO-awayDe))))-((100-(100*awayDe))/(awayO-awayDe))
        limit2 = ((homeO*((100-(100*homeDe))/(homeO-homeDe)))-(100-((100-(100*homeDe))/(homeO-homeDe))))*-1
        water = (limit1+limit2)/2
    
        #棒球級距為5 Ex : 1+5 1+10
        if water == 0:
            percent = 0
        elif water > 0:
            if  water%5 < 3:
                percent = 5 * int(water/5)
            else:
                percent = 5 * int(water/5) +5
        else:
            residue = (water/5) - int(water/5)
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
            if gameType == '1st half' :
                if '0.0' == homeL[1:]:
                    L = mapping.bshalf0(percent)
                    # print(L)
                elif '0.5' == homeL[1:]:
                    L = mapping.bshalf05(percent)       
                h = hL + L
                a = aL + L
            else :
                try :
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
#     gameType ='full'
#     homeL = '-1.5'
#     awayL = '+1.5'
#     homeO = '2.92'
#     awayO = '1.465'
#     homeDe = '2.0'
#     awayDe = '1.9'
#     calBSzf(source,gameClass,gameType,homeL,awayL,homeO,awayO,homeDe,awayDe)
