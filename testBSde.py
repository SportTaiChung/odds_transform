import mapping
from sendMQ import telegramBot
def calBSde(source,gameClass,gameType,homeDe,awayDe):

    
    if homeDe != '0' :
        homeDe = round((float(homeDe)-1),2)
        awayDe = round((float(awayDe)-1),2)
    else :
        homeDe = float('0')
        awayDe = float('0')
   
        
    # 較小的獨贏 為smallDe
    if homeDe < awayDe :
        smallDe = homeDe 
    else :
        smallDe = awayDe
    
    # 如果 較小的獨贏 小於等於 0.7 中間值使用0.92
    # 如果 較小的獨贏 大於 0.7 中間值使用  （主隊獨贏＋客隊獨贏）/2
    # 棒球用 30 100%  25 100%
    if gameClass == 'hockey' :
        w = 25
    else :
        w = 30

    if homeDe != 0.0 :
        if smallDe <= 0.7 :
            middleDe = 0.92
        else : 
            middleDe = (homeDe + awayDe)/2
        water = abs(middleDe-smallDe)*(100/w*100)
        move = int(water)
    else :
        move = 0

    # 美棒級距是 5  Ex : 1+5 1+10
    if move == 0 :
        percent = 0
    else :
        if  move%5 <3 :
            percent = 5 * int(move/5)
        else :
            percent = 5 * int(move/5) +5
    # print(percent/100)
    try :
        try :
            # 對照表
            L = mapping.bsDeMap(percent/100)

            # 獨贏小的那邊為讓邊
            if homeDe < awayDe :
                hL = '-'
                aL = '+'
            else :
                hL = '+'
                aL = '-'
            
            h = hL + L
            a = aL + L
        except :
            h = '0+0'
            a = '0+0'
    except :
        telegramBot(source+","+"BSdeMapping錯誤"+","+str(gameType)+","+str(homeDe)+","+str(awayDe))

    # print(h,a,str(homeDe),str(awayDe))
    return str(h), str(a), str(homeDe), str(awayDe)


# if __name__ == '__main__':
#     source = 'PS38'
#     gameClass = 'mlb'
#     gameType ='full'
#     homeDe = '1.95'
#     awayDe = '1.95'
#     calBSde(source,gameClass,gameType,homeDe,awayDe)