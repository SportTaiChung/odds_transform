# -*- coding:utf-8 -*-
import traceback
from google.protobuf import text_format
from app import APHDC_noDB_pb2
from app import mapping

def cutOne(home, away):
    if home != '0':
        hO = str(round((float(home) -1), 2))
        aO = str(round((float(away) -1), 2))
    else:
        hO = str(home)
        aO = str(away)
    return str(hO), str(aO)


def justCutOne_fun(Data, single=None):
    for cut in Data.aphdc:
        if single:
            cut = single
        try:
            homeline = cut.usZF.homeZF.line
            awayline = cut.usZF.awayZF.line
            homeodds = cut.usZF.homeZF.odds
            awayodds = cut.usZF.awayZF.odds
            if homeodds in (''):
                pass
            elif homeodds in ('0', '0.0'):
                cut.twZF.homeZF.line = '0'
                cut.twZF.awayZF.line = '0'
                cut.twZF.homeZF.odds = '0'
                cut.twZF.awayZF.odds = '0'
            else:
                if cut.game_class in ('UCL', 'soccer', 'hockey'):
                    try:
                        cut.twZF.homeZF.line = homeline[0]+mapping.scMap(homeline[1:])
                        cut.twZF.awayZF.line = awayline[0]+mapping.scMap(awayline[1:])
                    except:
                        cut.twZF.homeZF.line = homeline
                        cut.twZF.awayZF.line = awayline
                else:
                    cut.twZF.homeZF.line = homeline
                    cut.twZF.awayZF.line = awayline
                zf = cutOne(homeodds, awayodds)
                cut.twZF.homeZF.odds = zf[0]
                cut.twZF.awayZF.odds = zf[1]

            dsline = cut.usDS.line
            over = cut.usDS.over
            under = cut.usDS.under
            if over in (''):
                pass
            elif over in ('0', '0.0'):
                cut.twDS.line = '0'
                cut.twDS.over = '0'
                cut.twDS.under = '0'
            else:
                if cut.game_class in ('UCL', 'soccer', 'hockey'):
                    try:
                        cut.twDS.line = mapping.scMap(dsline)
                    except:
                        cut.twDS.line = dsline
                else:
                    cut.twDS.line = dsline
                ds = cutOne(over, under)
                cut.twDS.over = ds[0]
                cut.twDS.under = ds[1]


            dehome = cut.de.home
            deaway = cut.de.away
            if dehome in ('', '0', '0.0'):
                pass
            else:
                de = cutOne(dehome, deaway)
                cut.de.home = de[0]
                cut.de.away = de[1]

            draw = cut.draw
            if draw in ('', '0', '0.0'):
                pass
            else:
                cut.draw = str(round((float(draw) -1), 2))

            sdhome = cut.sd.home
            sdaway = cut.sd.away
            if sdhome in ('', '0', '0.0'):
                pass
            else:
                sd = cutOne(sdhome, sdaway)
                cut.sd.home = sd[0]
                cut.sd.away = sd[1]
            if single:
                break
        except Exception as e:
            traceback.print_exc()
            if single:
                break
    return Data


if __name__ == '__main__':
    with open('ps38_soccer_today.bin', 'rb') as data:
        enData = APHDC_noDB_pb2.ApHdcArr()
        enData.ParseFromString(data.read())
        out = justCutOne_fun(enData)
        text = text_format.MessageToString(out, as_utf8=True)
