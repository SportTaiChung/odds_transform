from sendMQ import telegramBot

def calBKds(source, line, over, under):


    line = str(float(line))
    over = round((float(over)-1), 2)
    under = round((float(under)-1), 2)

    water = abs((over + under)/2-over)*(100/7.6*100)
    move = int(water)

    #以小數點後面數字來判斷 Ex: 0.5 >> 0-100 [.5 == -100]
    testmap = {
        '0':{'key':line.split('.')[0], 'value':+0},
        '5':{'key':line.split('.')[0], 'value':-100}
        }
    key = testmap[line.split('.')[1]]['key']
    value = testmap[line.split('.')[1]]['value']

    #籃球級距為25 Ex: 1+25 1+50
    if move == 0:
        percent = 0
    else:
        if  move%25 < 13:
            percent = 25 * int(move/25)
        else:
            percent = 25 * int(move/25) +25
    # print(percent)

    if over < under:
        ans = value-percent
    else:
        ans = value+percent
    # print(ans)

    if value == 0:
        if 500 <= ans < 675:
            newKey = str(abs(int(key) - 3))
            newValue = ans -600
        elif 300 <= ans <= 475:
            newKey = str(abs(int(key) - 2))
            newValue = ans -400
        elif 100 <= ans < 300:
            newKey = str(abs(int(key) - 1))
            newValue = ans -200
        elif -100 <= ans < 100:
            newKey = key
            newValue = ans
        elif -300 <= ans < -100:
            newKey = str(int(key) + 1)
            newValue = 200 +ans
        elif -500 <= ans < -300:
            newKey = str(int(key)+2)
            newValue = 400 +ans
    else:
        if 375 < ans <= 575:
            newKey = str(abs(int(key) - 2))
            newValue = ans -500
        elif 200 <= ans <= 375:
            newKey = str(abs(int(key) - 1))
            newValue = ans -300
        elif 0 < ans < 200:
            newKey = key
            newValue = ans -100
        elif -100 <= ans <= 0:
            newKey = key
            newValue = ans
        elif -300 <= ans < -100:
            newKey = str(int(key) + 1)
            newValue = 200 +ans
        elif -500 <= ans < -300:
            newKey = str(int(key)+2)
            newValue = 400 +ans
        elif -700 <= ans < -500:
            newKey = str(int(key)+3)
            newValue = 600 +ans
        elif -800 <= ans < -700:
            newKey = str(int(key)+4)
            newValue = 800 +ans
    try:
        try:
            if '-' in str(newValue):
                newValue = str(newValue)
            else:
                newValue = '+' + str(newValue)
            L = newKey+newValue
        except:
            L = '0+0'
    except Exception as e:
        e
    # print(newKey+newValue)
    # print(hL + newKey+newValue)
    # print(aL + newKey+newValue)
    # print(L)
    return str(L)

# if __name__ == '__main__':
#     source = 'PS38'
#     line= "226.5"
#     over= "3.02"
#     under= "1.9"
#     calBKds(source, line, over, under)
