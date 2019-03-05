
def calBSde(gameType,homeDe,awayDe):
    if homeDe != '0' :
        homeDe = round((float(homeDe)-1),2)
        awayDe = round((float(awayDe)-1),2)
    else :
        homeDe = float('0')
        awayDe = float('0')
   
    water = abs((homeDe + awayDe)/2-homeDe)*(100/30*100)
    move = int(water)
    # print(water)
    # print(move)
    key = '0'
    value = 0

    if move == 0 :
        percent = 0
    else :
        if  move%5 <3 :
            percent = 5 * int(move/5)
        else :
            percent = 5 * int(move/5) +5
    # print(percent)


    if homeDe < awayDe :
        ans = value-percent 
    else :
        ans = value+percent
    # print(ans)

    # if 'full' not in gameType :
    if 300 <= ans <= 475:
        newKey = str(abs(int(key) - 2))
        newValue = ans -400
    elif 100 <= ans <300:
        newKey = str(abs(int(key) - 1))
        newValue = ans -200
    elif -100 <= ans < 100 :
        newKey = key
        newValue = ans
    elif -300 <= ans < -100 :
        newKey = str(int(key) + 1)
        newValue = 200 +ans
    elif -500 <= ans < -300 :
        newKey = str(int(key)+2)
        newValue = 400 +ans 

    

    # else :
    #     if ans >= -100 :
    #         newKey = int(key) +1
    #         newValue = 100 + ans
    #     elif -200 <= ans < -100 :
    #         newKey = int(key) +1
    #         newValue = ans +100
    #     else :
    #         newKey = int(key) +2
    #         newValue = 100 + ans


    if '-' in str(newValue) :
        newValue = str(newValue)
    else :
        newValue = '+' +  str(newValue)

    # print(str(newKey) + str(newValue))

    if homeDe < awayDe :
        hL = '-'
        aL = '+'
    else :
        hL = '+'
        aL = '-'

    
    if 'full' in gameType :
        if '-' in newValue :
            newValue = newValue[0].replace('-','+') + str(100-int(newValue[1:]))
        else :
            newValue = newValue[0].replace('+','-') + str(100-int(newValue[1:]))
        if newKey == '0'  :
            newKey = '1'
        elif newKey == '1' :
            if 0 > int(newValue) >= -100 :
                newKey == '1'
            elif 0 <= int(newValue) <= 95 :
                newKey == '2'

    L = str(newKey) + str(newValue)
    h = hL + L
    a = aL + L

    return h, a, str(homeDe), str(awayDe)

if __name__ == '__main__':
    gameType ='full'
    homeDe = '2.35'
    awayDe = '1.63'
    # print(calBSde(gameType,homeDe,awayDe))