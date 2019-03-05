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
        limit1 = (((9650-((9850-(homeDe*9650))/(homeO-homeDe)))*homeDe)-((9850-(homeDe*9650))/(homeO-homeDe)))/9850
        limit2 = ((((9650-(((awayO*9650)-9850)/(awayO-awayDe)))*awayO)-((awayO*9650)-9850)/(awayO-awayDe))/9850)*-1
        water = round(((limit1+limit2)/2),3)*100

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
        # print(percent/100)


        L = mapping.bsMap(percent/100)

        ##判別home 或 away 讓
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
        else :
            if homeO != 0.0 :
                if homeO < awayO :
                    hL = '-'
                    aL = '+'
                elif homeO > awayO :
                    hL = '+'
                    aL = '-'
                else :
                    hL = homeL[0]
                    aL = awayL[0]

        ## 全場沒有 0-
        if 'full' in gameType :
            if L[0] == '0' and '0-' in L   :
                L = L.replace('0-','1+')
        h = hL + L
        a = aL + L
        # print(h)
        # print(a)
    return h,a ,str(homeDe),str(awayDe),str(homeO),str(awayO)
if __name__ == '__main__':
    # gameType ='full'
    # homeL = '-1.5'
    # awayL = '+1.5'
    # homeO = '3.06'
    # awayO = '1.337'
    # homeDe = '2.03'
    # awayDe = '1.87'
    # calBSzf(gameType,homeL,awayL,homeO,awayO,homeDe,awayDe)

    # gameType ='half'
    # homeL = '-1.5'
    # awayL = '+1.5'
    # homeO = '3.06'
    # awayO = '1.337'
    # homeDe = '2.03'
    # awayDe = '1.87'
    # calBSzf(gameType,homeL,awayL,homeO,awayO,homeDe,awayDe)

    gameType ='full'
    homeL = '-1.5'
    awayL = '+1.5'
    homeO = '2.65'
    awayO = '1.54'
    homeDe = '1.625'
    awayDe = '2.44'
    calBSzf(gameType,homeL,awayL,homeO,awayO,homeDe,awayDe)