
import APHDC_pb2 
import copy
import testBSde

def seasonMLB(Data):
    sendData = []   
    for mlb in Data:
        gameType = mlb.game_type
        homeDe = mlb.de.home
        awayDe = mlb.de.away
        zfMLB = testBSde.calBSde(gameClass,gameType,homeDe,awayDe)
        mlb.twZF.homeZF.line=zfMLB[0]
        mlb.twZF.awayZF.line=zfMLB[1]
        if homeDe == '0' : 
            mlb.twZF.homeZF.odds="0"
            mlb.twZF.awayZF.odds="0" 
            mlb.de.home='0'
            mlb.de.away='0'
        else :
            mlb.twZF.homeZF.odds="0.95"
            mlb.twZF.awayZF.odds="0.95"  
            mlb.de.home=zfMLB[2]
            mlb.de.away=zfMLB[3]

        sendData.append(copy.deepcopy(mlb))                

    # print(sendData)
    datas = APHDC_pb2.ApHdcArr()
    datas.aphdc.extend(sendData)
    data = datas.SerializeToString()  #變成byte
    return data


# f = b'\n\xdb\x01\n\x04PS38\x12\x03mlb\x1a\x04full"\t9568153942\x010:\x132019-02-27 02:05:00B\x132019-02-26 11:33:53J\x05falseRS\n\x15\xe7\xbe\x8e\xe5\x9c\x8b\xe8\x81\xb7\xe6\xa3\x92\xe5\xa4\xa7\xe8\x81\xaf\xe7\x9b\x9f\x12\x0b0_956815394\x1a\x17\n\x12\xe5\xb7\xb4\xe7\x88\xbe\xe7\x9a\x84\xe6\x91\xa9\xe9\x87\x91\xe9\xb6\xaf\x12\x010"\x14\n\x0f\xe5\x9d\xa6\xe5\xb8\x95\xe7\x81\xa3\xe5\x85\x89\xe8\x8a\x92\x12\x010Z\x06\n\x010\x12\x010b\x10\n\x06\n\x010\x12\x010\x12\x06\n\x010\x12\x010j\t\n\x010\x12\x010\x1a\x010\x82\x01\x0e\n\x052.100\x12\x051.775\n\xde\x01\n\x04PS38\x12\x03mlb\x1a\x04full"\t9568153952\x010:\x132019-02-27 02:05:00B\x132019-02-26 11:33:53J\x05falseRV\n\x15\xe7\xbe\x8e\xe5\x9c\x8b\xe8\x81\xb7\xe6\xa3\x92\xe5\xa4\xa7\xe8\x81\xaf\xe7\x9b\x9f\x12\x0b0_956815395\x1a\x17\n\x12\xe9\x82\x81\xe9\x98\xbf\xe5\xaf\x86\xe9\xa6\xac\xe6\x9e\x97\xe9\xad\x9a\x12\x010"\x17\n\x12\xe4\xbc\x91\xe5\xa3\xab\xe9\xa0\x93\xe5\xa4\xaa\xe7\xa9\xba\xe4\xba\xba\x12\x010Z\x06\n\x010\x12\x010b\x10\n\x06\n\x010\x12\x010\x12\x06\n\x010\x12\x010j\t\n\x010\x12\x010\x1a\x010\x82\x01\x0e\n\x052.450\x12\x051.584\n\xdb\x01\n\x04PS38\x12\x03mlb\x1a\x04full"\t9568153912\x010:\x132019-02-27 02:05:00B\x132019-02-26 11:33:53J\x05falseRS\n\x15\xe7\xbe\x8e\xe5\x9c\x8b\xe8\x81\xb7\xe6\xa3\x92\xe5\xa4\xa7\xe8\x81\xaf\xe7\x9b\x9f\x12\x0b0_956815391\x1a\x17\n\x12\xe6\x98\x8e\xe5\xb0\xbc\xe8\x98\x87\xe9\x81\x94\xe9\x9b\x99\xe5\x9f\x8e\x12\x010"\x14\n\x0f\xe5\x8c\xb9\xe8\x8c\xb2\xe5\xa0\xa1\xe6\xb5\xb7\xe7\x9b\x9c\x12\x010Z\x06\n\x010\x12\x010b\x10\n\x06\n\x010\x12\x010\x12\x06\n\x010\x12\x010j\t\n\x010\x12\x010\x1a\x010\x82\x01\x0e\n\x051.746\x12\x052.150\n\xd5\x01\n\x04PS38\x12\x03mlb\x1a\x04full"\t9568153932\x010:\x132019-02-27 02:05:00B\x132019-02-26 11:33:53J\x05falseRM\n\x15\xe7\xbe\x8e\xe5\x9c\x8b\xe8\x81\xb7\xe6\xa3\x92\xe5\xa4\xa7\xe8\x81\xaf\xe7\x9b\x9f\x12\x0b0_956815393\x1a\x11\n\x0c\xe7\xb4\x90\xe7\xb4\x84\xe6\xb4\x8b\xe5\x9f\xba\x12\x010"\x14\n\x0f\xe8\xb2\xbb\xe5\x9f\x8e\xe8\xb2\xbb\xe5\x9f\x8e\xe4\xba\xba\x12\x010Z\x06\n\x010\x12\x010b\x10\n\x06\n\x010\x12\x010\x12\x06\n\x010\x12\x010j\t\n\x010\x12\x010\x1a\x010\x82\x01\x0e\n\x051.632\x12\x052.350\n\xd8\x01\n\x04PS38\x12\x03mlb\x1a\x04full"\t9568153962\x010:\x132019-02-27 02:05:00B\x132019-02-26 11:33:53J\x05falseRP\n\x15\xe7\xbe\x8e\xe5\x9c\x8b\xe8\x81\xb7\xe6\xa3\x92\xe5\xa4\xa7\xe8\x81\xaf\xe7\x9b\x9f\x12\x0b0_956815396\x1a\x14\n\x0f\xe8\x8f\xaf\xe7\x9b\x9b\xe9\xa0\x93\xe5\x9c\x8b\xe6\xb0\x91\x12\x010"\x14\n\x0f\xe8\x81\x96\xe8\xb7\xaf\xe6\x98\x93\xe7\xb4\x85\xe9\x9b\x80\x12\x010Z\x06\n\x010\x12\x010b\x10\n\x06\n\x010\x12\x010\x12\x06\n\x010\x12\x010j\t\n\x010\x12\x010\x1a\x010\x82\x01\x0e\n\x051.746\x12\x052.150\n\xd8\x01\n\x04PS38\x12\x03mlb\x1a\x04full"\t9568153972\x010:\x132019-02-27 02:07:00B\x132019-02-26 11:33:53J\x05falseRP\n\x15\xe7\xbe\x8e\xe5\x9c\x8b\xe8\x81\xb7\xe6\xa3\x92\xe5\xa4\xa7\xe8\x81\xaf\xe7\x9b\x9f\x12\x0b0_956815397\x1a\x14\n\x0f\xe5\xa4\x9a\xe5\x80\xab\xe5\xa4\x9a\xe8\x97\x8d\xe9\xb3\xa5\x12\x010"\x14\n\x0f\xe6\xb3\xa2\xe5\xa3\xab\xe9\xa0\x93\xe7\xb4\x85\xe8\xa5\xaa\x12\x010Z\x06\n\x010\x12\x010b\x10\n\x06\n\x010\x12\x010\x12\x06\n\x010\x12\x010j\t\n\x010\x12\x010\x1a\x010\x82\x01\x0e\n\x052.150\x12\x051.746\n\xde\x01\n\x04PS38\x12\x03mlb\x1a\x04full"\t9568153922\x010:\x132019-02-27 04:05:00B\x132019-02-26 11:33:53J\x05falseRV\n\x15\xe7\xbe\x8e\xe5\x9c\x8b\xe8\x81\xb7\xe6\xa3\x92\xe5\xa4\xa7\xe8\x81\xaf\xe7\x9b\x9f\x12\x0b0_956815392\x1a\x14\n\x0f\xe8\x8a\x9d\xe5\x8a\xa0\xe5\x93\xa5\xe5\xb0\x8f\xe7\x86\x8a\x12\x010"\x1a\n\x15\xe4\xba\x9e\xe5\x88\xa9\xe6\xa1\x91\xe9\x82\xa3\xe9\x9f\xbf\xe5\xb0\xbe\xe8\x9b\x87\x12\x010Z\x06\n\x010\x12\x010b\x10\n\x06\n\x010\x12\x010\x12\x06\n\x010\x12\x010j\t\n\x010\x12\x010\x1a\x010\x82\x01\x0e\n\x051.632\x12\x052.350\n\xdb\x01\n\x04PS38\x12\x03mlb\x1a\x04full"\t9568183342\x010:\x132019-02-27 04:05:00B\x132019-02-26 11:33:53J\x05falseRS\n\x15\xe7\xbe\x8e\xe5\x9c\x8b\xe8\x81\xb7\xe6\xa3\x92\xe5\xa4\xa7\xe8\x81\xaf\xe7\x9b\x9f\x12\x0b0_956818334\x1a\x17\n\x12\xe8\xbe\x9b\xe8\xbe\x9b\xe9\x82\xa3\xe6\x8f\x90\xe7\xb4\x85\xe4\xba\xba\x12\x010"\x14\n\x0f\xe8\x88\x8a\xe9\x87\x91\xe5\xb1\xb1\xe5\xb7\xa8\xe4\xba\xba\x12\x010Z\x06\n\x010\x12\x010b\x10\n\x06\n\x010\x12\x010\x12\x06\n\x010\x12\x010j\t\n\x010\x12\x010\x1a\x010\x82\x01\x0e\n\x051.775\x12\x052.100\n\xe1\x01\n\x04PS38\x12\x03mlb\x1a\x04full"\t9568183372\x010:\x132019-02-27 04:05:00B\x132019-02-26 11:33:53J\x05falseRY\n\x15\xe7\xbe\x8e\xe5\x9c\x8b\xe8\x81\xb7\xe6\xa3\x92\xe5\xa4\xa7\xe8\x81\xaf\xe7\x9b\x9f\x12\x0b0_956818337\x1a\x1a\n\x15\xe5\xaf\x86\xe7\x88\xbe\xe7\x93\xa6\xe5\x9f\xba\xe9\x87\x80\xe9\x85\x92\xe4\xba\xba\x12\x010"\x17\n\x12\xe8\x81\x96\xe5\x9c\xb0\xe7\x89\x99\xe5\x93\xa5\xe6\x95\x99\xe5\xa3\xab\x12\x010Z\x06\n\x010\x12\x010b\x10\n\x06\n\x010\x12\x010\x12\x06\n\x010\x12\x010j\t\n\x010\x12\x010\x1a\x010\x82\x01\x0e\n\x051.714\x12\x052.200\n\xdb\x01\n\x04PS38\x12\x03mlb\x1a\x04full"\t9568153982\x010:\x132019-02-27 04:05:00B\x132019-02-26 11:33:53J\x05falseRS\n\x15\xe7\xbe\x8e\xe5\x9c\x8b\xe8\x81\xb7\xe6\xa3\x92\xe5\xa4\xa7\xe8\x81\xaf\xe7\x9b\x9f\x12\x0b0_956815398\x1a\x17\n\x12\xe5\xa5\xa7\xe5\x85\x8b\xe8\x98\xad\xe9\x81\x8b\xe5\x8b\x95\xe5\xae\xb6\x12\x010"\x14\n\x0f\xe6\xb4\x9b\xe6\x9d\x89\xe7\xa3\xaf\xe5\xa4\xa9\xe4\xbd\xbf\x12\x010Z\x06\n\x010\x12\x010b\x10\n\x06\n\x010\x12\x010\x12\x06\n\x010\x12\x010j\t\n\x010\x12\x010\x1a\x010\x82\x01\x0e\n\x051.775\x12\x052.100\n\xe4\x01\n\x04PS38\x12\x03mlb\x1a\x04full"\t9568183292\x010:\x132019-02-27 04:10:00B\x132019-02-26 11:33:53J\x05falseR\\\n\x15\xe7\xbe\x8e\xe5\x9c\x8b\xe8\x81\xb7\xe6\xa3\x92\xe5\xa4\xa7\xe8\x81\xaf\xe7\x9b\x9f\x12\x0b0_956818329\x1a\x17\n\x12\xe7\xa7\x91\xe7\xbe\x85\xe6\x8b\x89\xe5\xa4\x9a\xe8\x90\xbd\xe7\xa3\xaf\x12\x010"\x1d\n\x18\xe5\x85\x8b\xe9\x87\x8c\xe5\xa4\xab\xe8\x98\xad\xe5\x8d\xb0\xe5\x9c\xb0\xe5\xae\x89\xe4\xba\xba\x12\x010Z\x06\n\x010\x12\x010b\x10\n\x06\n\x010\x12\x010\x12\x06\n\x010\x12\x010j\t\n\x010\x12\x010\x1a\x010\x82\x01\x0e\n\x051.900\x12\x051.952\n\xd8\x01\n\x04PS38\x12\x03mlb\x1a\x04full"\t9568183272\x010:\x132019-02-27 04:10:00B\x132019-02-26 11:33:53J\x05falseRP\n\x15\xe7\xbe\x8e\xe5\x9c\x8b\xe8\x81\xb7\xe6\xa3\x92\xe5\xa4\xa7\xe8\x81\xaf\xe7\x9b\x9f\x12\x0b0_956818327\x1a\x14\n\x0f\xe8\xa5\xbf\xe9\x9b\x85\xe5\x9c\x96\xe6\xb0\xb4\xe6\x89\x8b\x12\x010"\x14\n\x0f\xe5\xbe\xb7\xe5\xb7\x9e\xe9\x81\x8a\xe9\xa8\x8e\xe5\x85\xb5\x12\x010Z\x06\n\x010\x12\x010b\x10\n\x06\n\x010\x12\x010\x12\x06\n\x010\x12\x010j\t\n\x010\x12\x010\x1a\x010\x82\x01\x0e\n\x051.775\x12\x052.100'

# enData = APHDC_pb2.ApHdcArr()
# enData.ParseFromString(f)
# Data = enData.aphdc
# seasonMLB(Data)