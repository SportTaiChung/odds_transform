pkill -2 -f 'gunicorn -w 2 -b 0.0.0.0:5005 toTWhandiApi:app'
pipenv run gunicorn -w 2 -b 0.0.0.0:5005 toTWhandiApi:app & > /dev/null
