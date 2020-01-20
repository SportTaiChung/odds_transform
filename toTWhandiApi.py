from flask_cors import CORS
from flask import Flask
from flask import request
from sendMQ import telegramBot
import datetime
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
                gameId = en.game_id

            if 'basketball' in game:
                out = testBskFunctionP.basketball(Data)
            elif 'hockey'  in game:
                out = testHcFunctionP.hockey(Data)
            elif game in ('football', 'soccer', 'tennis'):
                out = testCutOneP.justCutOne_fun(Data)
            elif game in ('mlb', 'npb', 'kbo'):
                out = newBSMixFunction.baseballMix(Data)


            # sportMap ={
            #     'mlb':'_BS',
            #     'npb':'_BS',
            #     'kbo':'_BS',
            #     'hockey':'_HC',
            #     'football':'_FB',
            #     'basketball':'_BK',
            #     'otherbasketball':'_OBK',
            #     'soccer':'_SC',
            #     'tennis':'_TN'
            # }
            # outData = APHDC_noDB_pb2.ApHdcArr()
            # outData.ParseFromString(out)
            # Data = outData.aphdc
            # ## 來源對應que
            # for ou in Data:
            #     ous = ou.source
            #     ouc = ou.game_class
            #     que = ous + sportMap.get(ouc)
        
            # sendMQ.send_MQ(out, 'test_CMD', 'rabbit.avia520.com', 'AE86', '200p', 5672)
            sendMQ.send_MQ(out, 'test_PS38', 'rtmcq.nba1688.net', 'GTR', '565p', 5672)
            return 'Success !!'
        except Exception as e:
            errorfile = open('error.log', 'a')
            errorfile.write(str(data)+'\n'+str(e)+'\n'+datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')+'\n')
            errorfile.close()
            return 'Error !!' +'\n'+ 'gameId: ' + gameId

    except Exception as e:
        print(str(e))
        

if __name__ == '__main__':
    # app.run(host='127.0.0.1', port=5004, debug=True, threaded=True)
    app.run(host='0.0.0.0', port=5004, debug=True, threaded=True)
