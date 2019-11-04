

* API
223API URL: http://txpywapi.nice666.net:5004/transWithProtobuf
237API URL: http://ptcy.nba1688.net:5004/transWithProtobuf
## 啟動服務
```
機器 237
cd newToTWApi
python toTWhandiApi.py & >/dev/null 2>&1
或是 (目前使用↓)
gunicorn -w 5 -k gevent -b 0.0.0.0:5004 toTWhandiApi:app & >/dev/null 2>&1

```
## 重啟
```
sh restart.sh
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
[APHDC_noDB.proto]|protobuf格式
[APHDC_noDB_pb2]|protoc --python_out=. APHDC_noDB.proto  產生
[testBskFunctionP.py]|籃球執行檔
[testBKds.py]|籃球大小Func
[testBKzf.py]|籃球讓分Func
[testCouOneP.py]|美盤減一
[testHcFunctionP.py]|冰球執行檔
[testBSzf.py]|美棒冰球讓分Func
[testBSds.py]|美棒大小Func
[testBSde.py]|專用棒球用獨贏算讓分Func
[newBSzf]|兩盤口計算讓分
[newBSds]|兩盤口計算大小
[newBSMixFunctionP.py]|美棒執行檔
[gun.conf]| gevent 設定檔
[mapping.py]|mapping
[sendMQ.py]|sendMQ func
[toTWhandiApi.py]|Main Api

- - - - - -

