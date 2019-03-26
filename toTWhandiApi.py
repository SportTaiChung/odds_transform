from flask_cors import CORS
from flask import Flask, make_response
from flask import jsonify
from flask import request
import json
import requests
import sendMQ
import APHDC_pb2
import testHcFunctionP
import testBskFunctionP
import testBsFunctionP
import testCutOneP
import testBeforeSeason
import testBsMixFunction


app = Flask(__name__)
CORS(app)

@app.route('/')
def hello():
    return 'Start to Trans ! '


@app.route('/transWithProtobuf', methods=['GET', 'POST'])
def trans():

    data = request.get_data()
    enData = APHDC_pb2.ApHdcArr()
    enData.ParseFromString(data)
    Data = enData.aphdc
    ## 球賽對應function
    for en in Data :
        game = en.game_class

    if 'basketball' in game :
        out = testBskFunctionP.basketball(Data)
    elif 'football' in game :
        out = testCutOneP.justCutOne_fun(Data) 
    elif 'soccer' in game :
        out = testCutOneP.justCutOne_fun(Data)
    elif 'hockey'  in game : 
        out = testHcFunctionP.hockey(Data)
    elif 'mlb'  in game :
        out = testBsMixFunction.baseballMix(Data)
    # elif 'mlb' or 'npb' or 'cpbl' or  'kbo' or 'hockey' in game :
    #     out = bsFunctionP.baseball_fun(Data)

    
    outData = APHDC_pb2.ApHdcArr()
    outData.ParseFromString(out)
    Data = outData.aphdc
    ## 來源對應que
    for ou in Data :
        ous = ou.source
        ouc = ou.game_class
        outype = ou.game_type
        twzf = ou.twZF.homeZF.line
        if 'test' in ous :
            ous=ous.replace('test','')
            if 'hockey' == ouc:
                que = 'test_'+ous+'_HC'
            elif 'football' == ouc :
                que = 'test_'+ous+'_FB'
            elif 'basketball' in ouc :
                que = 'test_'+ous+'_BK'
            elif 'mlb' in ouc:
                que = 'test_'+ous+'_BS'
            elif 'soccer' == ouc :
                que = 'test_'+ous+'_SC'            
        else:
            if 'hockey' == ouc:
                que = ous+'_HC'
            elif 'football' == ouc :
                que = ous+'_FB'
            elif 'basketball' in ouc :
                que = ous+'_BK'
            elif 'mlb' in ouc:
                que = ous+'_BS'
            elif 'soccer' == ouc :
                que = ous+'_SC'


    # sendMQ.send_MQ(out,'Apple','rabbit.avia520.com','AE86', '200p')
    sendMQ.send_MQ(out,que,'10.0.1.198','GTR', '565p')
    return out


if __name__ == '__main__':
    # app.run(host='127.0.0.1', port=5004, debug=True ,threaded=True)
    app.run(host='0.0.0.0', port=5004, debug=True ,threaded=True)

