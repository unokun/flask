from flask import (
    Flask, flash, g, redirect, render_template, request, session, url_for
)
from model.drink import Drink
from werkzeug import secure_filename

app = Flask(__name__)

@app.route("/")
def index():
    drinks = Drink.findAll()
    return render_template('drink_list.html', drinks=drinks)

@app.route("/drinks/new")
def new_drink():
    return render_template('new_drink.html')

@app.route("/drinks/add", methods=['POST'])
def add_drink():
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

@app.route('/hello')
def hello():
    return 'Hello, World!'