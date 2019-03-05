from flask_cors import CORS
from flask import Flask, make_response
from flask import jsonify
from flask import request
import json
import requests
import sendMQ
import hcFunctionP
import bskFunctionP
import cutOneP
import beforeSeason
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
    for en in Data :
        game = en.game_class
    if 'basketball' in game :
        out = bskFunctionP.basketball(Data)
    elif 'football' in game :
        out = cutOneP.justCutOne_fun(Data)        
    elif 'hockey'  in game :
        out = hcFunctionP.hockey(Data)
    elif 'mlb' or 'npb' or 'cpbl' or  'kbo' in game :
        out = beforeSeason.seasonMLB(Data)

    
    outData = APHDC_pb2.ApHdcArr()
    outData.ParseFromString(out)
    Data = outData.aphdc
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
            
   
    # sendMQ.send_MQ(out,que)
    sendMQ.send_MQ(out,'Apple')
    return que


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5004, debug=True ,threaded=True)
    # app.run(host='0.0.0.0', port=5004, debug=True ,threaded=True)


   
