## 環境構築

無料で始めるならVisual Studio Codeがお勧めです。候補補完機能とLintを追加すると捗ります。

- [VS CodeとFlaskによるWebアプリ開発「最初の一歩」 \(1/3\)：Visual Studio Codeで始めるPythonプログラミング \- ＠IT](https://www.atmarkit.co.jp/ait/articles/1807/24/news024.html)

また、チュートリアルにも環境構築例がありますが、venv(virtual env)は使った方が良いです。

モジュール追加時のバージョン問題などを回避することができます。



## チュートリアル

チュートリアルを行ってからクイックスタートを写経するが良いと思います。

- [Tutorial — Flask 1\.0\.2 documentation](http://flask.pocoo.org/docs/1.0/tutorial/)
- [Quickstart — Flask 1\.0\.2 documentation](http://flask.pocoo.org/docs/1.0/quickstart/#quickstart)
- [クイックスタート — Flask v0\.5\.1 documentation](https://a2c.bitbucket.io/flask/quickstart.html)

補足)

Tutorialのソースは[GitHub](https://github.com/pallets/flask/tree/master/examples/tutorial)にあるのでここも参考にした方が良いと思います。コメントが充実しています。



Visual Studio Codeのチュートリアルも良いです。

[Python and Flask Tutorial in Visual Studio Code](https://code.visualstudio.com/docs/python/tutorial-flask)



### テスト

古いチュートリアルではunittestを使っていましたが、pytestに変わっています。

注意) pytestする前に対象モジュール(flaskr)をインストールする必要がある。

pytestに失敗する場合、pythonでモジュール指定で実行する。

```bash
(venv) $ python -m pytest  
============================================== test session starts ==============================================
platform darwin -- Python 3.6.5, pytest-4.3.1, py-1.8.0, pluggy-0.9.0
rootdir: flaskr-tutorial, inifile: setup.cfg
collected 2 items                                                                                               

tests/test_factory.py ..  

(venv) $ pytest 
...
ModuleNotFoundError: No module named 'flaskr'
ERROR: could not load flaskr-tutorial/tests/conftest.py
```



- [Testing Flask Applications — Flask 1\.0\.2 documentation](http://flask.pocoo.org/docs/1.0/testing/)

- [Flaskアプリケーションのテスト — Flask v0\.5\.1 documentation](https://a2c.bitbucket.io/flask/testing.html)

  



### お役立ちコマンド

#### Flask Command Line Interface

[Command Line Interface — Flask 1\.0\.2 documentation](http://flask.pocoo.org/docs/1.0/cli/)



#### Route一覧取得

[python \- Get list of all routes defined in the Flask app \- Stack Overflow](https://stackoverflow.com/questions/13317536/get-list-of-all-routes-defined-in-the-flask-app)

```bash
$ env FLASK_APP=flaskr flask routes
Endpoint       Methods    Rule
-------------  ---------  -----------------------
auth.login     GET, POST  /auth/login
auth.logout    GET        /auth/logout
auth.register  GET, POST  /auth/register
hello          GET        /hello
index          GET        /
static         GET        /static/<path:filename>
```



#### インストール済みモジュール一覧

```bash
(venv) $ pip list
Package        Version Location                                        
-------------- ------- ------------------------------------------------
atomicwrites   1.3.0   
attrs          19.1.0  
Click          7.0     
coverage       4.5.3   
Flask          1.0.2   
flaskr         1.0.0   /Users/unokun/work/working/flask/flaskr-tutorial
itsdangerous   1.1.0   
Jinja2         2.10    
MarkupSafe     1.1.1   
more-itertools 6.0.0   
pip            19.0.3  
pluggy         0.9.0   
py             1.8.0   
pytest         4.3.1   
setuptools     39.0.1  
six            1.12.0  
Werkzeug       0.14.1  
```



#### Shell

アプリのデータを確認できる。``` $ rails console ```みたいなものかな？

```bash
(venv) $ flask shell 
Python 3.6.5 |Anaconda, Inc.| (default, Apr 26 2018, 08:42:37) 
[GCC 4.2.1 Compatible Clang 4.0.1 (tags/RELEASE_401/final)] on darwin
App: flaskr [development]
Instance: flaskr-tutorial/instance
>>> 
```



### リンク

- [Packaging Python Projects — Python Packaging User Guide](https://packaging.python.org/tutorials/packaging-projects/)
- [Template Designer Documentation — Jinja2 Documentation \(2\.10\)](http://jinja.pocoo.org/docs/2.10/templates/#for)
- [Extensions Registry \| Flask \(A Python Microframework\)](http://flask.pocoo.org/extensions/)
- [ウェブアプリケーションフレームワーク Flask を使ってみる \- Qiita](https://qiita.com/ynakayama/items/2cc0b1d3cf1a2da612e4)
- [The Python Tutorial — Python 3\.7\.3rc1 documentation](https://docs.python.org/3/tutorial/)
- [Flask Tutorial](https://weblog.metacircular-evaluator.org/blog/2018/07/16/flask/)


