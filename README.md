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
[bskFunctionP.py]|籃球（已未使用）
[BKDS.py]|籃球大小Func(已未使用)
[BKZF.py]|籃球讓分Func(已未使用)
[couOneP.py]|美盤減一（已未使用）
[bsFunctionP.py]|冰球執行檔（線上使用）
[testBeforeSeason.py]|專用賽季前美棒執行檔（線上使用）
[testBSde.py]|專用棒球用獨贏算讓分Func（線上使用）
[testBskFunctionP.py]|籃球執行檔（線上使用）
[testBKds.py]|籃球大小Func（線上使用）
[testBKzf.py]|籃球讓分Func（線上使用）
[testCouOneP.py]|美盤減一（線上使用）
[testBsFunctionP.py]|美棒讓分（待測試）
[testBSzf.py]|專用美棒全場讓分Func（待測試）
[hcFunctionP.py]|冰球（待測試）
[testHCzf.py]|冰球讓分func（待測試）
[testBSds.py]|棒球冰球大小Func（待測試）
[gun.conf]| gevent 設定檔
[mapping.py]|mapping
[sendMQ.py]|sendMQfunction
[toTWhandiApi.py]|Main Api


- - - - - -