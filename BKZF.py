import mapping

def calBKzf(gameType,homeL,awayL,homeO,awayO,homeDe,awayDe):
        
    if homeO == '0.0' or homeO =='0' :
        homeL = '0.0'
        awayL = '0.0'
        homeO = float('0.0')
        awayO = float('0.0')
    else :
        homeO = round((float(homeO)-1),2)
        awayO = round((float(awayO)-1),2)


    if homeDe == '0.0' or homeDe == '0' :
        homeDe = float('0.0')
        awayDe = float('0.0')
    else :
        homeDe = round((float(homeDe)-1),2)
        awayDe = round((float(awayDe)-1),2)

    # print(homeDe)

    water = abs((homeO + awayO)/2-homeO)/(100/7.6)*1000
    move = int(water)
    # print(water)
    # print(move)

    testmap = {
        '0':{'key':homeL.split('.')[0],'value':+0},
        '5':{'key':homeL.split('.')[0],'value':-100}
        }
    key = testmap[homeL.split('.')[1]]['key'][1:]
    value = testmap[homeL.split('.')[1]]['value']
    # print(key,value)
    
    if '-' in homeL :
        if homeO < awayO :
            newMove = 0 - move
        else :
            newMove = 0 + move
    else :
        if homeO < awayO :
            newMove = 0 + move
        else :
            newMove = 0 - move
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
       
    

    ## 讓邊為獨贏小的那一邊 , 若沒獨贏就照原本的
    if homeDe != 0.0 :
        if homeDe < awayDe :
            hL = '-'
            aL = '+'
        elif homeDe > awayDe :
            hL = '+'
            aL = '-'
    else :
        hL = homeL[0]
        aL = awayL[0]
        
    ## 沒有 0+35
    if '+' in newValue :
        if newKey == '0' :
            if newKey+newValue != '0+0':
                newKey = '1'
                newValue = newValue.replace('+','-')
    ## 全場沒有 0-
    if 'full' in gameType :
        if '-' in newValue and newKey == '0' :
            newKey = '1'
            newValue = newValue.replace('+','-')

    try :
        h = hL + newKey+newValue
        a = aL + newKey+newValue
    except :
        h = '0+0'
        a = '0+0'        
    if (newKey+newValue) == '+0':
        h = '0+0'
        a = '0+0'
    # print(newKey + newValue)
    # print(h , a ,str(homeDe) ,str(awayDe))
    return  h , a ,str(homeDe) ,str(awayDe)
if __name__ == '__main__':

    gameType ='full'
    homeL = '-4.5'
    awayL = '+4.5'
    homeO = '1.98'
    awayO = '1.9'
    homeDe = '0'
    awayDe = '0'
    calBKzf(gameType,homeL,awayL,homeO,awayO,homeDe,awayDe)