# 兩個盤口算法
def calBSds(source, gameClass, line, over, under):

    if over != '0':
        firstL = str(float(line.split(',')[0]))
        firstO = round((float(over.split(',')[0])-1), 3)
        firstU = round((float(under.split(',')[0])-1), 3)
        secondL = str(float(line.split(',')[1]))
        secondO = round((float(over.split(',')[1])-1), 3)
        secondU = round((float(under.split(',')[1])-1), 3)
    else:
        firstL = str(float('0'))
        firstO = float('0')
        firstU = float('0')
        secondL = str(float('0'))
        secondO = float('0')
        secondU = float('0')

    fsmallO = firstO if firstO < firstU else firstU
    smallL = firstL if float(firstL) < float(secondL) else secondL
    smallO = firstO if firstO < secondO else secondO
    smallU = firstU if firstU < secondU else secondU
    bigL = firstL if float(firstL) > float(secondL) else secondL
    bigO = firstO if firstO > secondO else secondO
    bigU = firstU if firstU > secondU else secondU
 
    #以小數點後面數字來判斷 Ex: 0.5 >> 0-100 [.5 == -100]
    testmap = {
        '0':{'key':firstL.split('.')[0], 'value':+0},
        '5':{'key':firstL.split('.')[0], 'value':-100}
        }
    key = testmap[firstL.split('.')[1]]['key']
    value = testmap[firstL.split('.')[1]]['value']
    # print(key,value)
    try:
        try:
            a = (0.95-fsmallO)/(bigO-smallO)
            if firstO < secondO:
                water = 0-a
            else :
                water = a
            percent = int((round((water)*2,1)/2)*100)

            if value == 0:
                if 100 <= percent <= 295:
                    newKey = str(int(key)-1)
                    newValue = -200 + percent
                elif -100 <= percent <=95:
                    newKey = str(int(key))
                    newValue = percent
                elif -300 <= percent <= -105:
                    newKey = str(int(key) + 1)
                    newValue = 200 + percent 
            else:
                if 200 <= percent <= 300:
                    newKey = str(int(key)-1)
                    newValue = -200 + percent
                elif 0 <= percent <= 195:
                    newKey = str(int(key))
                    newValue = -100 + percent
                elif -200 <= percent <= -5:
                    newKey = str(int(key) + 1)
                    newValue = 100 + percent
                elif -300 <= percent <= -205:
                    newKey = str(int(key) + 2)
                    newValue = 300 + percent

            if '-' in str(newValue):
                newValue = str(newValue)
            else:
                newValue = '+' + str(newValue)
            L = newKey+newValue
        except Exception as e:
            # print(str(e))
            L = '0+0'
    except Exception as e:
        print(str(e))
    # print(L, firstL, firstO, firstU)
    return str(L), str(firstL), str(firstO), str(firstU)
# if __name__ == '__main__':
    # source = 'PS38'
    # gameClass ='mlb'
    # line = '9.0,8.5'
    # over = '2.04,1.833'
    # under = '1.877,2.09'
    # calBSds(source, gameClass, line, over, under)
    # source = 'PS38'
    # gameClass ='mlb'
    # line = '10.0,10.5'
    # over = '1.909,2.07'
    # under = '1.961,1.84'
    # calBSds(source, gameClass, line, over, under)

# 奧克蘭運動家		
# 9.0,8.0 2.040,1.680 1.869,2.330		
# 紐約洋基		
# 9.0,10.0 1.943,2.390 1.961,1.649		
# 聖路易紅雀		
# 8.5,7.5 2.010,1.719 1.892,2.260		
# 休士頓太空人		
# 9.0,8.0 2.030,1.671 1.884,2.340		
# 亞利桑那響尾蛇		
# 8.5,7.5 1.980,1.694 1.925,2.300		
# 洛杉磯道奇		
# 7.0,8.0 1.826,2.320 2.100,1.684		
		