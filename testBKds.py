from sendMQ import telegramBot

def calBKds(line,over,under):
    
    if over == "0" or over =="0.0":
        line = '0.0'
        over = float('0')
        under = float('0')
    else :
        line = str(float(line))     
        over = round((float(over)-1),2)
        under = round((float(under)-1),2)
    
    # print(line,over,under)
    water = abs((over + under)/2-over)*(100/7.6*100)
    move = int(water)
    # print(water)
    # print(move)

    testmap = {
        '0':{'key':line.split('.')[0],'value':+0},
        '5':{'key':line.split('.')[0],'value':-100}
        }
    key = testmap[line.split('.')[1]]['key']
    value = testmap[line.split('.')[1]]['value']
    # print(key,value)


    if move == 0 :
        percent = 0
    else :
        if  move%25 <13 :
            percent = 25 * int(move/25)
        else :
            percent = 25 * int(move/25) +25
    # print(percent)

    # print(value,percent)
    if over < under :
        ans = value-percent 
    else :
        ans = value+percent
    # print(ans)


    if value == 0:
        if 500 <= ans < 675 :
            newKey = str(abs(int(key) - 3))
            newValue = ans -600
        elif 300 <= ans <= 475:
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
    else :
        if 375 < ans <= 575 :
            newKey = str(abs(int(key) - 2))
            newValue = ans -500
        elif 200 <= ans <= 375 :
            newKey = str(abs(int(key) - 1))
            newValue = ans -300
        elif 0 < ans < 200 :
            newKey = key
            newValue = ans -100
        elif -100 <= ans <= 0 :
            newKey = key
            newValue = ans 
        elif -300 <= ans < -100 :
            newKey = str(int(key) + 1)
            newValue = 200 +ans
        elif -500 <= ans < -300 :
            newKey = str(int(key)+2)
            newValue = 400 +ans 
        elif -700 <= ans < -500 :
            newKey = str(int(key)+3)
            newValue = 600 +ans
        elif -800 <= ans < -700 :
            newKey = str(int(key)+4)
            newValue = 800 +ans     
    try :        
        if '-' in str(newValue) :
            newValue = str(newValue)
        else :
            newValue = '+' +  str(newValue)
        L = newKey+newValue
    except :
        telegramBot("BKds Mapping錯誤"+","+str(line)+","+str(over)+","+str(under))
        L = '0+0'

    # print(newKey+newValue)
    # print(hL + newKey+newValue)
    # print(aL + newKey+newValue)
    # print(L)
    return str(L) 

# if __name__ == '__main__':

#     line= "226.5"
#     over= "3.02"
#     under= "1.9"
#     calBKds(line,over,under)
