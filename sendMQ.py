import configparser
import pika
import telegram

# 分成一次送50筆
def split_list(data):

    limit = 50
    return [data[i:i + limit] for i in range(0, len(data), limit)]


# telegram 機器人
def telegramBot(message):

    conf = configparser.ConfigParser()
    conf.read("config.ini")
    token = conf["telegram"]['token']
    id = conf['telegram']['chat_id']
    bot = telegram.Bot(token=token)
    bot.send_message(chat_id=id, text=message)

# 傳送資料到ＭＱ的交換機
def send_MQ(DATA, que, host, user, pw, port):     #資料送rabbitMQ

    cred = pika.PlainCredentials(user, pw)
    params = pika.ConnectionParameters(
        host=host,
        virtual_host='/',
        credentials=cred,
        socket_timeout=3,
        port=port
    )
    connection = pika.BlockingConnection(params)
    channel = connection.channel()
    channel.basic_publish(exchange=que,
                          routing_key='',
                          body=DATA
                          )
    connection.close()

