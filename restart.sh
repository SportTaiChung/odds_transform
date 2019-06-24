pkill -9 -f 'gunicorn -w 5 -b 0.0.0.0:5004 toTWhandiApi:app'
gunicorn -w 5 -b 0.0.0.0:5004 toTWhandiApi:app & > /dev/null