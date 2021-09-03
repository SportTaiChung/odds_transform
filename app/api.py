import datetime
import traceback
from flask import current_app, jsonify, request, Blueprint
from app import APHDC_noDB_pb2
from google.protobuf import text_format
from app import testHcFunctionP
from app import testBskFunctionP
from app import testCutOneP
from app import newBSMixFunction
from app.sendMQ import send_MQ


sport_queue_postfix_map ={
    'mlb':'_BS',
    'npb':'_BS',
    'kbo':'_BS',
    'hockey':'_HC',
    'football':'_FB',
    'basketball':'_BK',
    'otherbasketball':'_BK',
    'soccer':'_SC',
    'UCL':'_SC',
    'tennis':'_TN',
    'eSport':'_ES'
}


api = Blueprint('api', __name__)


@api.route('/transWithProtobuf', methods=['GET', 'POST'])
def trans():
    try:
        raw_data = request.get_data()
        data = APHDC_noDB_pb2.ApHdcArr()
        data.ParseFromString(raw_data)
        if not data.aphdc:
            return jsonify({'success': True, 'empty': True})
        try:
            source = data.aphdc[-1].source
            sport = data.aphdc[-1].game_class
            if 'basketball' in sport:
                out = testBskFunctionP.basketball(data)
            elif 'hockey' in sport:
                out = testHcFunctionP.hockey(data)
            elif sport in ('UCL', 'football', 'soccer', 'tennis', 'eSport'):
                out = testCutOneP.justCutOne_fun(data)
            elif sport in ('mlb', 'npb', 'kbo'):
                out = newBSMixFunction.baseballMix(data)
            que = source + sport_queue_postfix_map.get(sport)
            send_MQ(out, current_app.config['MQ_EXCHANGE'], que, current_app.config['MQ_URL'])
            return jsonify({'success': True})
        except Exception as e:
            with open('Log/error.log', 'a') as error_log:
                error_log.write(
                    f'{datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\n'
                    f'{traceback.format_exc()}\n'
                    f'{text_format.MessageToString(data, as_utf8=True)}\n'
                )
            return jsonify({'success': False, 'error': traceback.format_exc()}), 400
    except Exception as e:
        return jsonify({'error': traceback.format_exc()}), 400
