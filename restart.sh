pkill -9 -f 'gunicorn -w 9 -b 0.0.0.0:5004 toTWhandiApi:app'
pipenv run gunicorn -w 9 -b 0.0.0.0:5004 toTWhandiApi:app & > /dev/null
