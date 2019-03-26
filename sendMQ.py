import pika
import telegram
import configparser
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
    message = message
    bot.send_message(chat_id=id, text=message) 

# 傳送資料到ＭＱ
def send_MQ(DATA,que,host,user,ps):     #資料送rabbitMQ

    # cred = pika.PlainCredentials('AE86', '200p')
    # cred = pika.PlainCredentials('GTR', '565p')  #正式
    cred = pika.PlainCredentials(user,ps)
    params = pika.ConnectionParameters(
        # host='10.0.1.198',
        # host='rmq.nba1688.net',
        # host='rabbit.avia520.com',
        host = host,
        virtual_host='/',
        credentials=cred,
        socket_timeout=3
    )
    connection = pika.BlockingConnection(params)
    channel = connection.channel()
    channel.basic_publish(exchange=que,
                          routing_key='',
                          body=DATA
                          )
    # print("sent")

    connection.close()


