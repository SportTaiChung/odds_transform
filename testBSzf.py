import mapping
from sendMQ import telegramBot

## 冰球棒球都是用亞洲賠率(不加本金)計算 
def calBSzf(gameClass,gameType,homeL,awayL,homeO,awayO,homeDe,awayDe):
    # if gameClass == 'mlb' :
    #     homeO = float(homeO)
    #     awayO = float(awayO)
    #     homeDe = float(homeDe)
    #     awayDe = float(awayDe)
    # elif gameClass == 'hockey':
    if homeO != '0' :
        homeO = round((float(homeO)-1),2)
        awayO = round((float(awayO)-1),2)
    else :
        homeO = "0"
        awayO = "0"
    if homeDe != '0' :
        homeDe = round((float(homeDe)-1),2)
        awayDe = round((float(awayDe)-1),2)
    else :
        homeDe = "0"
        awayDe = "0"

    limit1=(awayDe*(100-((100-(100*awayDe))/(awayO-awayDe))))-((100-(100*awayDe))/(awayO-awayDe))
    limit2=((homeO*((100-(100*homeDe))/(homeO-homeDe)))-(100-((100-(100*homeDe))/(homeO-homeDe))))*-1
    water = (limit1+limit2)/2

    # print(limit1)
    # print(limit2)
    # print(water)

    if water == 0 :
        percent = 0
    elif water > 0 :
        if  water%5 < 3 :
            percent = 5 * int(water/5)
        else :
            percent = 5 * int(water/5) +5
    else :
        residue = (water/5) - int(water/5) 
        if residue < -0.5 :
            percent = 5 *int(water/5) -5
        else :
            percent = 5 *int(water/5) 
    # print(percent)
    
    if homeDe < awayDe :
        hL = '-'
        aL = '+'
    else :
        hL = '+'
        aL = '-'
    ## 如果沒有mapping到就關盤
    try :
        L = mapping.bsMap(percent/100)
        # print(L)
        h = hL + L
        a = aL + L

        # if gameClass == 'mlb' :
        #     if homeO != '0' :
        #         homeO = round((float(homeO)-1),2)
        #         awayO = round((float(awayO)-1),2)
        #     else :
        #         homeO = "0"
        #         awayO = "0"
        #     if homeDe != '0' :
        #         homeDe = round((float(homeDe)-1),2)
        #         awayDe = round((float(awayDe)-1),2)
        #     else :
        #         homeDe = "0"
        #         awayDe = "0"
        # elif gameClass == 'hockey' :
        #     homeO = homeO
        #     awayO = awayO
        #     homeDe = homeDe
        #     awayDe = awayDe
    except :
        telegramBot("BSzfMapping錯誤"+","+str(gameType)+","+str(homeDe)+","+str(awayDe)+","+str(homeO)+","+str(awayO))
        h = '0+0'
        a = '0+0'
        homeO = 0
        awayO = 0

    # print(h ,a , homeO ,awayO ,homeDe ,awayDe)
    return h ,a ,str(homeDe),str(awayDe), str(homeO),str(awayO)
        
# if __name__ == '__main__':
#     gameClass ='mlb'
#     gameType ='full'
#     homeL = '+1.5'
#     awayL = '-1.5'
#     homeO = '3.1'
#     awayO = '1.425'
#     homeDe = '2.13'
#     awayDe = '1.819'
#     calBSzf(gameClass,gameType,homeL,awayL,homeO,awayO,homeDe,awayDe)
 
