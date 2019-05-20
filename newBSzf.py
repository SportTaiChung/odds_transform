import mapping
import testBSde
from sendMQ import telegramBot

## 冰球棒球都是用亞洲賠率(不加本金)計算
def calBSzf(source, gameClass, gameType, homeL, awayL, homeO, awayO):

    if homeO != '0':

        firstHL = str(float(homeL.split(',')[0]))
        firstHO = round((float(homeO.split(',')[0])-1), 3)
        firstAL = str(float(awayL.split(',')[0]))
        firstAO = round((float(awayO.split(',')[0])-1), 3)
        secondHL = str(float(homeL.split(',')[1]))
        secondHO = round((float(homeO.split(',')[1])-1), 3)
        secondAL = str(float(awayL.split(',')[1]))
        secondAO = round((float(awayO.split(',')[1])-1), 3)
    else:
        firstHL = str(float('0'))
        firstHO = float('0')
        firstAL = str(float('0'))
        firstAO = float('0')
        secondHL = str(float('0'))
        secondHO = float('0')
        secondAL = str(float('0'))
        secondAO = float('0')

    #公式
    limit1 = (firstAO*(100-((100-(100*firstAO))/(secondAO-firstAO))))-((100-(100*firstAO))/(secondAO-firstAO))
    limit2 = ((secondHO*((100-(100*firstHO))/(secondHO-firstHO)))-(100-((100-(100*firstHO))/(secondHO-firstHO))))*-1
    water = (limit1+limit2)/2

    #棒球級距為5 Ex: 1+5 1+10
    if water == 0:
        percent = 0
    elif water > 0:
        if  water%5 < 3:
            percent = 5 * int(water/5)
        else:
            percent = 5 * int(water/5) +5
    else:
        residue = (water/5) - int(water/5)
        if residue < -0.5:
            percent = 5 *int(water/5) -5
        else:
            percent = 5 *int(water/5)

    hL = homeL[0]
    aL = awayL[0]

    #如果沒有mapping到就關盤 
    try:
        try:
            L = mapping.twoHandiBsZf(percent/100)
            h = hL + L
            a = aL + L
        except:
            h = '0+0'
            a = '0+0'
    except:
        telegramBot(source+","+"BSzfMapping錯誤"+","+str(gameType)+","+str(homeL)+","+str(awayL)+","+str(homeO)+","+str(awayO))

    # print(str(h), str(a), str(firstHO), str(firstAO))
    return str(h), str(a), str(firstHO), str(firstAO)

# if __name__ == '__main__':
#     source = 'PS38'
#     gameClass ='mlb'
#     gameType ='full'
#     homeL = '-1.5,-2.5'
#     awayL = '+1.5,+2.5'
#     homeO = '1.714,2.100'
#     awayO = '2.260,1.793'
#     calBSzf(source,gameClass,gameType,homeL,awayL,homeO,awayO)


# -1.5,-2.5 1.714,2.100 +1.5,+2.5 2.260,1.793