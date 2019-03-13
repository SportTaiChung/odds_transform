import mapping


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
    water = abs((over + under)/2-over)/(100/7.6)*1000
    move = int(water)
    # print(water)
    # print(move)

    testmap = {
        '0':{'key':line.split('.')[0],'value':+0},
        '5':{'key':line.split('.')[0],'value':-100}
        }
    key = testmap[line.split('.')[1]]['key']
    value = testmap[line.split('.')[1]]['value']
    

    if over < under :
        newMove = 0 - move
    else :
        newMove = 0 + move

    # print(newMove)
    if value == 0 :
        if 12 <= move <= 19 :
            newKey = str((int(key) -2))
            newValue = mapping.bkMap(newMove)
        elif 4 <= move <= 11 :
            newKey = str((int(key) -1))
            newValue = mapping.bkMap(newMove)
        elif -4 <= move <= 3 :
            newKey = str(key)
            newValue = mapping.bkMap(newMove)
        elif -12 <= move <= -5 :
            newKey = str((int(key) +1))
            newValue = mapping.bkMap(newMove)            
        elif -20 <= move <= -13 :
            newKey = str((int(key) +2))
            newValue = mapping.bkMap(newMove) 
    else :
        newMove = newMove -4
        # print(newMove)
        if 16 <= move <= 23 :
            newKey = str((int(key) -2))
            newValue = mapping.bkMap(newMove)  
        elif 8 <= move <= 15 :
            newKey = str((int(key) -1))
            newValue = mapping.bkMap(newMove)  
        elif 0 <=  move <= 7:
            newKey = str(key)
            newValue = mapping.bkMap(newMove)
        elif -8 <= move <= -1 :
            newKey = str((int(key) +1))
            newValue = mapping.bkMap(newMove)
        elif -16 <= move <= -9 :
            newKey = str((int(key) +2))
            newValue = mapping.bkMap(newMove)            
    # print(newKey + newValue)           


    L = newKey+newValue

    return L 


# if __name__ == '__main__':

#     line= "58"
#     over= "2.00"
#     under= "1.84"
#     calBKds(line,over,under)
