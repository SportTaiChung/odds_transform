from flask_cors import CORS
from flask import Flask
from flask import request
from sendMQ import telegramBot
import sendMQ
import APHDC_noDB_pb2
import testHcFunctionP
import testBskFunctionP
import testCutOneP
import newBSMixFunction

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello():
    return 'Start to Trans ! '


@app.route('/transWithProtobuf', methods=['GET', 'POST'])
def trans():
    try:
        data = request.get_data()
        enData = APHDC_noDB_pb2.ApHdcArr()
        enData.ParseFromString(data)
        Data = enData.aphdc
        try:
            ## 球賽對應function
            for en in Data:
                game = en.game_class

            if 'basketball' in game:
                out = testBskFunctionP.basketball(Data)
            elif 'football' in game:
                out = testCutOneP.justCutOne_fun(Data)
            elif 'soccer' in game:
                out = testCutOneP.justCutOne_fun(Data)
            elif 'hockey'  in game:
                out = testHcFunctionP.hockey(Data)
            elif 'mlb' or 'npb'  or  'kbo' in game:
                # out = testBsMixFunction.baseballMix(Data)
                out = newBSMixFunction.baseballMix(Data)
        except:
            telegramBot(str(data))

        outData = APHDC_noDB_pb2.ApHdcArr()
        outData.ParseFromString(out)
        Data = outData.aphdc
        ## 來源對應que
        for ou in Data:
            ous = ou.source
            ouc = ou.game_class
            if 'test' in ous:
                que = 'test_CMD'
            else:
                if ouc == 'hockey':
                    que = ous+'_HC'
                elif ouc == 'football':
                    que = ous+'_FB'
                elif 'basketball' in ouc:
                    que = ous+'_BK'
                elif ouc == 'soccer':
                    que = ous+'_SC'
                elif 'mlb'  or 'npb'  or  'kbo' in ouc:
                    que = ous+'_BS'


        sendMQ.send_MQ(out, 'test_CMD', '10.0.1.197', 'AE86', '200p')
        # sendMQ.hkMQ(out, 'test_PS38_BS', 'rmq.nba1688.net', 'GTR', '565p', '5673')
        # sendMQ.send_MQ(out, que, '10.0.1.198', 'GTR', '565p')
        return out

    except Exception as e:
        telegramBot(str(e))


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5004, debug=True, threaded=True)
    # app.run(host='0.0.0.0', port=5004, debug=True, threaded=True)
