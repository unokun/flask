from flask import (
    Flask, flash, g, redirect, render_template, request, session, url_for
)
from model.drink import Drink
from werkzeug import secure_filename

app = Flask(__name__)

@app.route("/")
def index():
    drinks = Drink.find_all()
    return render_template('drink_list.html', drinks=drinks)

@app.route("/drinks/new")
def new_drink():
    """ 新規商品(飲み物)追加 """
    return render_template('new_drink.html')

@app.route("/drinks/add", methods=['POST'])
def add_drink():
    """ 新規商品(飲み物)DB登録 """
    name = request.form['name']
    price = int(request.form['price'])
    count = int(request.form['count'])
    filename = ''
    #image_file = request.form['image_file']
    f = request.files['image_file']
    if f != None:
        filename = '/static/images/' + secure_filename(f.filename)
        f.save('.' + filename)
    
    status = request.form['status']
    Drink.insert(name, price, count, filename, status)
    return redirect('/')

@app.route("/drinks/buy", methods=['POST'])
def buy_drink():
    """ 購入 """
    errors = []
    # 入力チェック
    # drink_idはradio buttonのvalueにセットしているため
    # 未選択の場合にはkeyが存在しない
    try:
        v = request.form['drink_id']
    except KeyError:
        errors.append('飲み物を選んでください。')

    if not request.form['charge']:
        errors.append('金額は必須です。')

    # 金額形式チェック
    if not errors:
        try:
            charge = int(request.form['charge'])
            if charge < 0:
                errors.append('金額は正の数値を入力してください')
        except:
            errors.append('金額は数値を入力してください')

    # 飲み物情報取得
    drink_id = int(request.form['drink_id'])
    drink = Drink.find_by_id(drink_id)

    # 金額チェック
    if not errors:
        if (charge < drink.price):
            errors.append('金額が足りません。')
    
    # 在庫チェック
    if not errors:
        if (drink.count < 1):
            errors.append('商品の在庫がありません。')

    if not errors:
        # 在庫更新、購入履歴登録
        Drink.buy_drink(drink_id)
        return render_template('buy_drink.html', drink=drink, charge=charge)
    
    # エラーあり
    return render_template('buy_drink.html', errors=errors)

@app.route("/drinks/edit", methods=['GET'])
def edit_drinks():
    """ 商品編集画面 """

    drinks = Drink.find_all()
    return render_template('edit_drinks.html', drinks=drinks)

@app.route("/drink/<int:id>/update", methods=['POST'])
def update_drink(id):
    """ 商品更新 """

    errors = []

    try:
        v = request.form['update_count']
        update_count = int(v)
        if update_count > 0:
            Drink.update_count(id, update_count);
    except KeyError:
        pass

    # 個数入力チェック
    # errors.append('個数が不正な値です。')

    if not errors:
        try:
            change_status= request.form['change_status']
            Drink.update_status(id, change_status);
        except KeyError:
            pass

    return redirect('/drinks/edit');

@app.route('/hello')
def hello():
    return 'Hello, World!'