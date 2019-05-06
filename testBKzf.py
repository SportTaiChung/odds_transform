from sendMQ import telegramBot

def calBKzf(source, gameType, homeL, awayL, homeO, awayO, homeDe, awayDe):
    try:
        if homeO == '0':
            homeL = '0.0'
            awayL = '0.0'
            homeO = float('0.0')
            awayO = float('0.0')
        else:
            homeO = round((float(homeO)-1), 2)
            awayO = round((float(awayO)-1), 2)

        try:
            if  homeDe == '0' or homeDe == '':
                homeDe = float('0.0')
                awayDe = float('0.0')
            else:
                homeDe = round((float(homeDe)-1), 2)
                awayDe = round((float(awayDe)-1), 2)
        except:
            homeDe = float('0.0')
            awayDe = float('0.0')
    except Exception as e:
        telegramBot(source+","+"BKzf錯誤"+","+str(gameType)+","+str(homeDe)+","+str(awayDe)+","+str(homeO)+","+str(awayO)+","+str(e))
    # print(homeDe)

    water = abs((homeO + awayO)/2-homeO)*(100/8*100)
    move = int(water)
    # print((homeO + awayO)/2-homeO)
    # print(water)
    # print(move)

    #以小數點後面數字來判斷 Ex: 0.5 >> 0-100 [.5 == -100]
    testmap = {
        '0':{'key':homeL.split('.')[0], 'value':+0},
        '5':{'key':homeL.split('.')[0], 'value':-100}
        }
    key = testmap[homeL.split('.')[1]]['key'][1:]
    value = testmap[homeL.split('.')[1]]['value']
    # print(key,value)

    #籃球級距為25 Ex: 1+25 1+50
    if move == 0:
        percent = 0
    else:
        if  move%25 < 13:
            percent = 25 * int(move/25)
        else:
            percent = 25 * int(move/25) +25
    # print(percent)

    ## 主讓
    if '-' in homeL:
        if homeO < awayO:
            percent = value-percent
        else:
            percent = value+percent
    ## 客讓
    else:
        if homeO > awayO:
            percent = value-percent
        else:
            percent = value+percent
    # print(percent)


    if value == 0:
        if 500 <= percent < 675:
            newKey = str(abs(int(key) - 3))
            newValue = percent -600
        elif 300 <= percent <= 475:
            newKey = str(abs(int(key) - 2))
            newValue = percent -400
        elif 100 <= percent < 300:
            newKey = str(abs(int(key) - 1))
            newValue = percent -200
        elif -100 <= percent < 100:
            newKey = key
            newValue = percent
        elif -300 <= percent < -100:
            newKey = str(int(key) + 1)
            newValue = 200 +percent
        elif -500 <= percent < -300:
            newKey = str(int(key)+2)
            newValue = 400 + percent
    else:
        if 375 < percent <= 575:
            newKey = str(abs(int(key) - 2))
            newValue = percent -500
        elif 200 <= percent <= 375:
            newKey = str(abs(int(key) - 1))
            newValue = percent -300
        elif 0 < percent < 200:
            newKey = key
            newValue = percent -100
        elif -100 <= percent <= 0:
            newKey = key
            newValue = percent
        elif -300 <= percent < -100:
            newKey = str(int(key) + 1)
            newValue = 200 +percent
        elif -500 <= percent < -300:
            newKey = str(int(key)+2)
            newValue = 400 +percent
        elif -700 <= percent < -500:
            newKey = str(int(key)+3)
            newValue = 600 +percent
        elif -800 <= percent < -700:
            newKey = str(int(key)+4)
            newValue = 800 +percent

    try:
        try:
            if '-' in str(newValue):
                newValue = str(newValue)
            else:
                newValue = '+' +  str(newValue)

            # print(newValue)

            if homeDe != 0.0:
                if homeDe < awayDe:
                    hL = '-'
                    aL = '+'
                elif homeDe > awayDe:
                    hL = '+'
                    aL = '-'
                else:
                    hL = homeL[0]
                    aL = awayL[0]
            else:
                if homeO != 0.0:
                    hL = homeL[0]
                    aL = awayL[0]

            # print(newKey+newValue)
            # print(hL + newKey+newValue)
            # print(aL + newKey+newValue)


            ## 沒有 0+
            if '+' in newValue and newKey == '0':
                if newKey+newValue != '0+0':
                    newValue = newValue.replace('+', '-')


            # print(hL + newKey+newValue)
            # print(aL + newKey+newValue)

            ## 全場沒有 0-
            if 'full' in gameType:
                if '-' in newValue and newKey == '0':
                    newKey = '1'
                    newValue = '+' + str(int(newValue) + 100)


            # print(newKey+newValue)
            # print(hL + newKey+newValue)
            # print(aL + newKey+newValue)
            # L = newKey+newValue

            try:
                h = hL + newKey+newValue
                a = aL + newKey+newValue
            except:
                h = '0+0'
                a = '0+0'
            if (newKey+newValue) == '+0':
                h = '0+0'
                a = '0+0'
        except:
            h = '0+0'
            a = '0+0'
    except:
        telegramBot(source+","+"BKzf Mapping錯誤"+","+str(gameType)+","+str(homeDe)+","+str(awayDe)+","+str(homeL)+","+str(awayL)+","+str(homeO)+","+str(awayO))

    # print(h,a)
    # print(h , a ,str(homeDe) ,str(awayDe))
    return  str(h), str(a), str(homeDe), str(awayDe)

# if __name__ == '__main__':
#     source = 'PS38'
#     gameType ='full'
#     homeL = '-0.0'
#     awayL = '+0.0'
#     homeO = '2.66'
#     awayO = '1.46'
#     homeDe = '0'
#     awayDe = '0'
#     calBKzf(source,gameType,homeL,awayL,homeO,awayO,homeDe,awayDe)