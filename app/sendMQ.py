import pika
from pika.exceptions import StreamLostError, AMQPError
from flask import current_app
import telegram


# 分成一次送50筆
def split_list(data):

    limit = 50
    return [data[i:i + limit] for i in range(0, len(data), limit)]


# telegram 機器人
def telegramBot(message):
    bot = telegram.Bot(token=current_app.config['TELEGRAM']['TOKEN'])
    bot.send_message(chat_id=current_app.config['TELEGRAM']['CHAT_ID'], text=message)


# 傳送資料到ＭＱ的交換機
def send_MQ(data, exchange, key, url):
    try:
        params = pika.URLParameters(url)
        with pika.BlockingConnection(params) as connection:
            with connection.channel() as channel:
                channel.basic_publish(
                    exchange=exchange,
                    routing_key=key,
                    body=data.SerializeToString()
                )
    except (StreamLostError, AMQPError) as ex:
        print(ex)
        return False
    return True
