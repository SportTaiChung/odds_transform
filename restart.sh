#!/bin/bash
pkill -9 -f 'toTWhandiApi'
pipenv run gunicorn -c gun.py toTWhandiApi:app