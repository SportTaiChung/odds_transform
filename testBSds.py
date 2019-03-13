


def calBSds(line,over,under):
    if over != '0' :
        over = round((float(over)-1),2)
        under = round((float(under)-1),2)
    else :
        over = float('0')
        under = float('0')

    oneWater = 1/abs(under-over)
    # print(oneWater)
    water = abs((over + under)/2-over)*(100/oneWater*100)
    move = int(water)
    # print(water)
    # print(move)

    # print(line.split('.')[1])
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
        if  move%5 <3 :
            percent = 5 * int(move/5)
        else :
            percent = 5 * int(move/5) +5
    # print(percent)


    if over < under :
        ans = value-percent 
    else :
        ans = value+percent
    # print(ans)

    
    if value == 0:
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
    else :
        if 200 <= ans <= 375 :
            newKey = str(abs(int(key) - 1))
            newValue = ans -300
        elif -100 <= ans < 200 :
            newKey = key
            newValue = ans
        elif -300 <= ans < -100 :
            newKey = str(int(key) + 1)
            newValue = 200 +ans
        elif -500 <= ans < -300 :
            newKey = str(int(key)+2)
            newValue = 400 +ans 
     
    if '-' in str(newValue) :
        newValue = str(newValue)
    else :
        newValue = '+' +  str(newValue)
    # print(newKey+newValue)
    L = newKey+newValue
    return L 

# if __name__ == '__main__':

#     line= "7.5"
#     over= "1.91"
#     under= "1.97"
#     print(calBSds(line,over,under))