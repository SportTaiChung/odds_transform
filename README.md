# NewAsia function
美盤轉台盤 API

* 籃球 : bskFunctionP.py
* 籃球 (多玩法) : cutOneP.py
* 棒球 : bsFunctionP.py
* 美足 : cutOneP.py
* 冰球 (含加時): hcFunctionP.py
* 冰球 : cutOneP.py

Mehtod: POST

* 一包資料
API URL: http://txpywapi.nice666.net:5004/transWithProtobuf

## 啟動服務
```
機器 223
cd toTwP
python toTWhandiApi.py & >/dev/null 2>&1
或是 (目前使用↓)
gunicorn -w 2 -k gevent -b 0.0.0.0:5004 toTWhandiApi:app & >/dev/null 2>&1

```
## 內容
```
經Post 傳送protobuf (byte)資料到Api
            ↓
Api (解析 .轉換 .轉成protobuf .傳到MQ)

```

## 程式說明
程式|功能
----|----
[APHDC.proto]|protobuf格式
[APHDC_pb2]|protoc --python_out=. APHDC.proto  產生
[beforeSeason.py]|專用賽季前棒球
[bsFunctionP.py]|棒球
[bskFunctionP.py]|籃球
[hcFunctionP.py]|冰球
[couOneP.py]|美盤減一
[testBKds.py]|籃球大小func
[testBKzf.py]|籃球讓分func
[testBSds.py]|棒球冰球大小func
[testBSde.py]|專用棒球用獨贏算讓分func
[testBSzf.py]|專用美棒全場讓分func
[testHCzf.py]|冰球讓分func
[BKDS.py]|改寫目前線上版本(誤差較小但不是盤室要的)
[BKZF.py]|改寫目前線上版本(誤差較小但不是盤室要的)
[mapping.py]|mapping
[sendMQ].py]|sendMQfunction
- - - - - -