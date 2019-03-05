import pika


def split_list(data):   # 分成一次送50筆

    limit = 50

    return [data[i:i + limit] for i in range(0, len(data), limit)]



def send_MQ(DATA,que):     #資料送rabbitMQ

    cred = pika.PlainCredentials('AE86', '200p')
    # cred = pika.PlainCredentials('GTR', '565p')  #正式
    params = pika.ConnectionParameters(
        # host='10.0.1.198',
        host='rabbit.avia520.com',
        virtual_host='/',
        credentials=cred,
        socket_timeout=3
    )
    connection = pika.BlockingConnection(params)
    channel = connection.channel()
    channel.basic_publish(exchange='',
                          routing_key=que,
                          body=DATA
                          )
    # print("sent")

    connection.close()


