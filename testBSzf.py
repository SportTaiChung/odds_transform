import mapping


def calBSzf(gameType,homeL,awayL,homeO,awayO,homeDe,awayDe):
    if homeO != '0' :
        homeO = round((float(homeO)-1),2)
        awayO = round((float(awayO)-1),2)
    else :
        homeO = float('0')
        awayO = float('0')
    if homeDe != '0' :
        homeDe = round((float(homeDe)-1),2)
        awayDe = round((float(awayDe)-1),2)
    else :
        homeDe = float('0')
        awayDe = float('0')
    
    if homeO == 0.0 or homeDe == 0.0 :
        h = '0+0'
        a = '0+0'
        # print(h)
        # print(a)
    else :
        limit1 = (awayDe*(100 -((100-(100*awayDe))/(awayO-awayDe))))-(100-(100*awayDe))/(awayO-awayDe)
        limit2 = ((homeO*(100-(100*homeDe))/(homeO-homeDe))-(100 -((100-(100*homeDe))/(homeO-homeDe))))*-1
        water = (limit1+limit2)/2 
        # print(limit1)
        # print(limit2)
        # print(water)
        if water == 0 :
            percent = 0
        elif water > 0 :
            if  water%5 < 3 :
                percent = 5 * int(water/5)
            else :
                percent = 5 * int(water/5) +5
        else :
            residue = (water/5) - int(water/5) 
            if residue < -0.5 :
                percent = 5 *int(water/5) -5
            else :
                percent = 5 *int(water/5) 
        # print(percent)
        
        if homeDe < awayDe :
            hL = '-'
            aL = '+'
        else :
            hL = '+'
            aL = '-'
        L = mapping.bsMap(percent/100)
        # print(L)
        h = hL + L
        a = aL + L
        return h ,a , homeO ,awayO ,homeDe ,awayDe
        # print(h ,a , homeO ,awayO ,homeDe ,awayDe)
if __name__ == '__main__':
    gameType ='full'
    homeL = '-1.5'
    awayL = '+1.5'
    homeO = '2.14'
    awayO = '1.793'
    homeDe = '1.427'
    awayDe = '3.09'
    calBSzf(gameType,homeL,awayL,homeO,awayO,homeDe,awayDe)
 
