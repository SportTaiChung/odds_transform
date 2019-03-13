from flask_cors import CORS
from flask import Flask, make_response
from flask import jsonify
from flask import request
import json
import requests
import sendMQ
import testHcFunctionP
import testBskFunctionP
import testBsFunctionP
import testCutOneP
import testBeforeSeason
 
import bsFunctionP
import bskFunctionP
import cutOneP
import APHDC_pb2



app = Flask(__name__)
CORS(app)

@app.route('/')
def hello():

    return 'Start to Trans ! '


@app.route('/transWithProtobuf', methods=['GET', 'POST'])
def func3():

    data = request.get_data()
    enData = APHDC_pb2.ApHdcArr()
    enData.ParseFromString(data)
    Data = enData.aphdc
    ## 球賽對應function
    for en in Data :
        game = en.game_class
    ## 測試用    
    if 'testPs' == en.source  or 'CMD' == en.source:
        if 'basketball' in game :
            out = testBskFunctionP.basketball(Data)
        elif 'football' in game :
            out = testCutOneP.justCutOne_fun(Data)   
        elif 'soccer' in game :
            out = testCutOneP.justCutOne_fun(Data)   
        elif 'hockey'  in game :
            out = testHcFunctionP.hockey(Data)
        elif 'mlb' in game :
            out = testBsFunctionP.baseball(Data)
            
    ## 正式用     
    else :
        if 'basketball' in game :
            out = testBskFunctionP.basketball(Data)
            # out = bskFunctionP.basketball_fun(Data)
        elif 'football' in game :
            out = testCutOneP.justCutOne_fun(Data) 
        elif 'hockey'  in game :
            out = testHcFunctionP.hockey(Data)
            # out = bsFunctionP.baseball_fun(Data)
        elif 'mlb'  in game :
            out = testBeforeSeason.seasonMLB(Data) 
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
        if ous == 'PS38':
            if 'hockey' == ouc:
                que = 'PS38_HC'
            elif 'football' == ouc :
                que = 'PS38_FB'
            elif 'basketball' in ouc :
                if 'full' in outype :
                    que = 'PS38_BK'
                else :
                    que = 'PS38_OBK'
            elif 'mlb' or 'npb' or 'cpbl' or  'kbo' in ouc:
                que = 'PS38_BS'
        elif ous == 'CMD':
            if 'basketball' in ouc:
                que = 'CMD_BK'
            elif 'hockey' == ouc:
                que = 'CMD_HC'
            elif 'soccer' == ouc :
                que = 'CMD_SC'
        elif 'test' in ous :
            que = 'Apple'
        
    # sendMQ.send_MQ(out,'Apple','rabbit.avia520.com','AE86', '200p')
    sendMQ.send_MQ(out,que,'10.0.1.198','GTR', '565p')
    return out


if __name__ == '__main__':
    # app.run(host='127.0.0.1', port=5004, debug=True ,threaded=True)
    app.run(host='0.0.0.0', port=5004, debug=True ,threaded=True)


   
