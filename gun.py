import multiprocessing

bind = '0.0.0.0:5004'
workers = multiprocessing.cpu_count() * 2 + 1
backlog = 128
worker_class = "gevent"
daemon = True
timeout = 60
keepalive = 5
logfile = '/home/pyuser/log/odds_transform_api.log'
debug = True
loglevel = 'debug'