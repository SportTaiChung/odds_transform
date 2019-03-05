

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
        elif 0 < ans < 200 :
            newKey = key
            newValue = ans -100
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
    # print(hL + newKey+newValue)
    # print(aL + newKey+newValue)
    L = newKey+newValue
    return L 

# if __name__ == '__main__':

#     line= "230.5"
#     over= "2.11"
#     under= "1.78"
#     print(calBKds(line,over,under))
