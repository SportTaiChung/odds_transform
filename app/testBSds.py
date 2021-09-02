from app.sendMQ import telegramBot

def calBSds(source, gameClass, gameType, line, over, under):
    if over in ('', '0', '0.0'):
        line = str(float('0'))
        over = float('0')
        under = float('0')
    else:
        line = str(float(line))
        over = round((float(over)-1), 2)
        under = round((float(under)-1), 2)

    #冰球水位 25 100%
    #美棒水位 16 100%
    #其他的棒球水位 30 100%
    if gameClass == 'hockey':
        w = 25
    elif gameClass == 'mlb':
        if gameType == 'full':
            w = 16
        elif gameType == '1st half':
            w = 30
    else:
        w = 30
    water = abs((over + under)/2-over)*(100/w*100)
    move = int(water)

    #以小數點後面數字來判斷 Ex: 0.5 >> 0-100 [.5 == -100]
    testmap = {
        '0':{'key':line.split('.')[0], 'value':+0},
        '25':{'key':line.split('.')[0], 'value':-50},
        '5':{'key':line.split('.')[0], 'value':-100},
        '75':{'key':line.split('.')[0], 'value':+50}
        }
    key = testmap[line.split('.')[1]]['key']
    value = testmap[line.split('.')[1]]['value']

    #棒球級距為5 Ex : 1+5 1+10
    if move == 0:
        percent = 0
    else:
        if  move%5 < 3:
            percent = 5 * int(move/5)
        else:
            percent = 5 * int(move/5) +5

    if over < under:
        ans = value-percent
    else:
        ans = value+percent

    if value == 0:
        if 300 <= ans <= 475:
            newKey = str(abs(int(key) - 2))
            newValue = ans - 400
        elif 100 <= ans < 300:
            newKey = str(abs(int(key) - 1))
            newValue = ans - 200
        elif -100 <= ans < 100:
            newKey = key
            newValue = ans
        elif -300 <= ans < -100:
            newKey = str(int(key) + 1)
            newValue = 200 + ans
        elif -500 <= ans < -300:
            newKey = str(int(key) + 2)
            newValue = 400 + ans
    elif value == -50:
        if 300 <= ans <= 475:
            newKey = str(abs(int(key) - 2))
            newValue = ans -400
        elif 100 <= ans <= 275:
            newKey = str(abs(int(key) - 1))
            newValue = ans - 200
        elif -100 <= ans <= 75:
            newKey = key
            newValue = ans
        elif -300 <= ans <= -125:
            newKey = str(int(key) + 1)
            newValue = 200 + ans
        elif -500 <= ans <= -325:
            newKey = str(int(key) + 2)
            newValue = 400 + ans
    elif value == -100:
        if 375 < ans <= 575:
            newKey = str(abs(int(key) - 2))
            newValue = ans -500
        elif 200 <= ans <= 375:
            newKey = str(abs(int(key) - 1))
            newValue = ans -300
        elif 0 < ans < 200:
            newKey = key
            newValue = ans - 100
        elif -100 <= ans <= 0:
            newKey = key
            newValue = ans
        elif -300 <= ans < -100:
            newKey = str(int(key) + 1)
            newValue = 200 + ans
        elif -500 <= ans < -300:
            newKey = str(int(key) + 2)
            newValue = 400 + ans
    elif value == 50:
        if 300 <= ans <= 475:
            newKey = str(abs(int(key) - 2))
            newValue = ans - 400
        elif 100 <= ans <= 275:
            newKey = str(abs(int(key) - 1))
            newValue = ans - 200
        elif -100 <= ans <= 75:
            newKey = key
            newValue = ans
        elif -300 <= ans <= -125:
            newKey = str(int(key) + 1)
            newValue = 200 + ans
        elif -500 <= ans <= -500:
            newKey = str(int(key)+2)
            newValue = 400 + ans
    try:
        try:
            if '-' in str(newValue):
                newValue = str(newValue)
            else:
                newValue = '+' + str(newValue)
            L = newKey+newValue
        except:
            L = '0+0'
    except:
        telegramBot(source+","+"BSds Mapping錯誤"+","+str(line)+","+str(over)+","+str(under))


    return str(L)

# if __name__ == '__main__':
#     source = 'PS38'
#     gameClass = 'mlb'
#     gameType = '1st half'
#     line= "10.5"
#     over= "6.02"
#     under= "1.05"
#     calBSds(source,gameClass,line,over,under)