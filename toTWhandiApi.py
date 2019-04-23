from sendMQ import telegramBot
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
import testCutOneP
import testBsMixFunction


app = Flask(__name__)
CORS(app)

@app.route('/')
def hello():
    return 'Start to Trans ! '


@app.route('/transWithProtobuf', methods=['GET', 'POST'])
def trans():
    try : 
        data = request.get_data()
        enData = APHDC_pb2.ApHdcArr()
        enData.ParseFromString(data)
        Data = enData.aphdc
        try :
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
            elif 'mlb' or 'npb'  or  'kbo' in game :
                out = testBsMixFunction.baseballMix(Data)
        except :
            telegramBot(str(data))

        
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
                elif 'soccer' == ouc :
                    que = 'test_'+ous+'_SC'                   
                elif 'mlb' or 'npb'  or  'kbo'in ouc:
                    que = 'test_'+ous+'_BS'
            else:
                if 'hockey' == ouc:
                    que = ous+'_HC'
                elif 'football' == ouc :
                    que = ous+'_FB'
                elif 'basketball' in ouc :
                    que = ous+'_BK'
                elif 'soccer' == ouc :
                    que = ous+'_SC'                
                elif 'mlb'  or 'npb'  or  'kbo' in ouc:
                    que = ous+'_BS'



        # sendMQ.hkMQ(out,'test_PS38_BS','rmq.nba1688.net','GTR', '565p','5673')
        sendMQ.send_MQ(out,que,'10.0.1.198','GTR', '565p')
        return out        
        
            
    except Exception as e :
        telegramBot(str(e))


    
if __name__ == '__main__':
    # app.run(host='127.0.0.1', port=5004, debug=True ,threaded=True)
    app.run(host='0.0.0.0', port=5004, debug=True ,threaded=True)

