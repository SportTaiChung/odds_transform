
import mapping

def calBSde(gameType,homeDe,awayDe):
    if homeDe != '0' :
        homeDe = round((float(homeDe)-1),2)
        awayDe = round((float(awayDe)-1),2)
    else :
        homeDe = float('0')
        awayDe = float('0')
   
    water = abs((homeDe + awayDe)/2-homeDe)*(100/30*100)
    move = int(water)
    # print(water)
    # print(move)
    key = '0'
    value = 0

    if move == 0 :
        percent = 0
    else :
        if  move%5 <3 :
            percent = 5 * int(move/5)
        else :
            percent = 5 * int(move/5) +5
    print(percent/100)

    L = mapping.bsDeMap(percent/100)



    if homeDe < awayDe :
        hL = '-'
        aL = '+'
    else :
        hL = '+'
        aL = '-'

    
    h = hL + L
    a = aL + L

    
    return h, a, str(homeDe), str(awayDe)

# if __name__ == '__main__':
#     gameType ='full'
#     homeDe = '2.1'
#     awayDe = '1.77'
#     calBSde(gameType,homeDe,awayDe)