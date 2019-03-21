# 準備

## 環境構築

無料で始めるならVisual Studio Codeがお勧めです。候補補完機能とLintを追加すると捗ります。

- [VS CodeとFlaskによるWebアプリ開発「最初の一歩」 \(1/3\)：Visual Studio Codeで始めるPythonプログラミング \- ＠IT](https://www.atmarkit.co.jp/ait/articles/1807/24/news024.html)

また、チュートリアルにも環境構築例がありますが、venv(virtual env)は使った方が良いです。

モジュール追加時のバージョン問題などを回避することができます。



## チュートリアル

チュートリアルを行ってからクイックスタートを写経するが良いと思う。

- [Tutorial — Flask 1\.0\.2 documentation](http://flask.pocoo.org/docs/1.0/tutorial/)
- [Quickstart — Flask 1\.0\.2 documentation](http://flask.pocoo.org/docs/1.0/quickstart/#quickstart)
- [クイックスタート — Flask v0\.5\.1 documentation](https://a2c.bitbucket.io/flask/quickstart.html)

補足)

Tutorialのソースは[GitHub](https://github.com/pallets/flask/tree/master/examples/tutorial)にあるのでここも参考にした方が良いと思います。コメントが充実しています。



#### テスト

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

  

### Flask Command Line Interface

[Command Line Interface — Flask 1\.0\.2 documentation](http://flask.pocoo.org/docs/1.0/cli/)



### お役立ちコマンド

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



#### モジュール一覧

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



# 課題

## ひとこと掲示板

### 要件

1. 利用者が名前とコメントを入力し、発言できる。
2. 利用者の過去の発言内容をテキストファイルで管理する。
3. 全ての利用者の過去の発言内容を一覧で表示する。一覧には「名前」「コメント」「発言日時」の3つを1行ずつ表示する。
4. 利用者の名前は最大20文字以内まで発言できる。もし20文字より多くの文字を入力して発言した場合はエラーメッセージを表示し、発言できないようにする。
5. 利用者のコメントは最大100文字以内まで発言できる。もし100文字より多くの文字を入力して発言した場合はエラーメッセージを表示し、発言できないようにする。
6. 利用者の名前とコメントは必ず文字が入力される。もし名前あるいはコメントが未入力で発言した場合はエラーメッセージを表示し、発言できないようにする。

### リンク

* [PythonでCSVファイルを読み込み・書き込み（入力・出力） \| note\.nkmk\.me](https://note.nkmk.me/python-csv-reader-writer/)

* [Bootstrap · The most popular HTML, CSS, and JS library in the world\.](https://getbootstrap.com/)



## 自動販売機

### はまりどころ

#### mysql-connecorのバージョン

```bash
pip install  mysql-connector-python
```

mysql-connectorはだめみたい...

[python \- How to install mysql\-connector via pip \- Stack Overflow](https://stackoverflow.com/questions/32754461/how-to-install-mysql-connector-via-pip)



#### Prepared Statement

データが一つの場合もカンマが必要。

```python
        query = ("INSERT INTO stocks (id, count, created_at, updated_at) VALUES (LAST_INSERT_ID(), %s, now(), now())")
        # カンマが必要
        val = (count,)
        cur.execute(query, val)
```





### 購入画面

#### URL

/bvm/

#### 要件

1. ステータスが「公開」のドリンク情報（「商品画像」「商品名」「値段」）を一覧で表示する。

2. 金額を投入するテキストボックスを作成する。

3. ドリンクを選択するラジオボタンを作成する。

4. ドリンクの在庫が0の場合、ドリンクを選択するラジオボタンは表示せず、「売り切れ」と表示する。

5. 購入ボタンを押すと購入結果ページへ遷移する。

   

### 購入完了画面

#### URL

/bvm/result

#### 要件

1. ドリンクの購入が正常に完了した場合、指定ドリンクの「画像」「商品名」「お釣りの情報」を表示する。
2. ドリンクの購入が正常に完了した場合、指定ドリンクの在庫を減らす（管理ページの在庫数が減っていること）。
3. 購入ページへ戻るリンクを作成する。
4. 購入するドリンクを指定していない場合、エラーメッセージを表示して、ドリンクを購入することはできない。
5. 投入金額と指定ドリンクを購入するときに必要な金額を比べ、もし投入金額が足りない場合はエラーメッセージを表示して、ドリンクを購入することはできない。
6. 投入金額は0以上の整数のみ可能である。0以上の整数以外の場合は、エラーメッセージを表示して、ドリンクを購入することはできない。
7. 指定ドリンクの在庫を確認し、もし在庫がなかった場合はエラーメッセージを表示して、ドリンクを購入することはできない（確認手順の例は以下になります）。
   1. 購入ページで、在庫がある商品を表示する。
   2. もう１つのブラウザで管理ページを表示させて、購入予定の在庫がある商品の在庫数を0に変更する（在庫なしにする）。
   3. 別のブラウザで開いていた購入ページで、在庫数を0に変更した商品を選択して、購入するボタンを押した場合、エラーメッセージが表示されること
8. 指定ドリンクのステータスを確認し、もしステータスが非公開の場合はエラーメッセージを表示して、ドリンクを購入することはできない（確認手順の例は以下になります）。
   1. 購入ページで、ステータスが公開の商品を表示する。
   2. もう１つのブラウザで管理ページを表示させて、購入予定のステータスが公開である商品について、ステータスを非公開に変更する（ステータスを非公開にする）。
   3. 別のブラウザで開いていた購入ページで、ステータスを非公開に変更した商品を選択して、購入するボタンを押した場合、エラーメッセージが表示されること。
9. ドリンクの購入が正常に完了した場合、指定ドリンクと購入日時の情報をデータベースに保存する（※この要件は必須ではなく任意です）。



### 商品一覧画面

#### URL

/bvm/drinks/

#### 要件

1. 追加した商品の一覧情報として、「商品画像」、「商品名」、「値段」、「在庫数」、「公開ステータス」のデータを一覧で表示する。



### 商品登録画面

#### URL

/vending/drinks/new

#### 要件

1. 「ドリンク名」「値段」「在庫数」「公開ステータス」を入力し、商品を追加できる。
2. 商品を追加する場合、「商品画像」を指定してアップロードできる。
3. 商品を追加する場合、「商品名」「値段」、「在庫数」、「公開ステータス」「商品画像」のいずれかを指定していない場合、エラーメッセージを表示して、商品を追加できない。
4. 商品を追加する場合、「値段」、「在庫数」は、0以上の整数のみ可能とする。0以上の整数以外はエラーメッセージを表示して、商品を追加できない。
5. 商品を追加する場合、公開ステータスは「公開」あるいは「非公開」のみ可能とする。「公開」あるいは「非公開」以外はエラーメッセージを表示して、商品を追加できない。
6. アップロードできる「商品画像」のファイル形式は「JPEG」、「PNG」のみ可能とする。「JPEG」、「PNG」以外はエラーメッセージを表示して、商品を追加できない。

### 

### 商品変更画面

#### URL

/vending/drinks/update/id

#### 要件

1. 商品一覧から指定ドリンクの在庫数を入力し、在庫数の変更ができる。
2. 商品一覧から指定ドリンクの公開ステータス「公開」あるいは「非公開」の変更ができる。
3. 商品の追加あるいは指定ドリンク情報（「在庫数」、「公開ステータス」）の変更が正常に完了した場合、完了のメッセージを表示する。
4. 商品一覧から指定ドリンクの在庫数を変更する場合、0以上の整数のみ可能とする。0以上の整数以外はエラーメッセージを表示して、変更できない。

社員情報管理