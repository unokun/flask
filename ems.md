# 【課題】社員情報管理



#### mysql-connecor-pythonでblobデータ読み込みに失敗する

connector作成時に「use_pure=True」を追加する。

* [Properly getting blobs from mysql database with mysql connector in python \- Stack Overflow](https://stackoverflow.com/questions/52759667/properly-getting-blobs-from-mysql-database-with-mysql-connector-in-python/52992413)
* [MySQL :: MySQL Connector/Python Developer Guide :: 7\.1 Connector/Python Connection Arguments](https://dev.mysql.com/doc/connector-python/en/connector-python-connectargs.html)



画像データをインライン表示する

```python
def getImage(id):
  respose = make_response()
  response.data = 画像データ(バイナリ)
  response.content_type=mimetype(例：img/png)
  return response
```

