import multiprocessing

bind = '127.0.0.1:5004'
workers = multiprocessing.cpu_count() * 2 + 1
backlog = 128
worker_class = "gevent"
daemon = True
timeout = 60
keepalive = 5
proc_name = 'gunicorn.proc'
pidfile = '/tmp/gunicorn.pid'
logfile = '/home/pyuser/log/odds_transform_api.log'
debug = True
loglevel = 'debug'
