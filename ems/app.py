from flask import (
    Flask, flash, g, redirect, render_template, request, session, url_for, make_response, send_file
)
from model.employee import Employee
from model.division import Division
from model.prefecture import Prefecture
from model.photo import Photo
from werkzeug import secure_filename
from io import StringIO
import csv

app = Flask(__name__)

@app.route("/")
@app.route("/employees")
def index():
    employees = Employee.find_all()
    return render_template('employee_list.html', employees=employees)

@app.route("/employee/new", methods=["GET"])
def new_employee():
    divisions = Division.find_all()
    prefectures = Prefecture.find_all()
    return render_template('new_employee.html', divisions=divisions, prefectures=prefectures)
    
@app.route("/employee/create", methods=["POST"])
def create_employee():
    errors = []
    if not request.form['name']:
        errors.append('名前は必須です。')

    cmd_type = request.form['cmd-type']
    if cmd_type == 'cancel':
        return render_template('new_division.html')

    success = ''
    age = 0
    pref_cd = 0
    photo_img = None
    mimetype = ''
    div_id = None
    hired_date = None
    retired_date = None
    if not errors:
        name = request.form['name']
        if len(request.form['age']) > 0 :
            age = request.form['age']
        gender = request.form['gender']
        zip_cd = request.form['zip-cd']
        if len(request.form['pref-cd']) > 0 :
            pref_cd = request.form['pref-cd']
        address = request.form['address']
        if len(request.form['div-id']) > 0 :
            div_id = request.form['div-id']
        if len(request.form['hired-date']) > 0 :
            hired_date = request.form['hired-date']
        if len(request.form['retired-date']) > 0 :
            retired_date = request.form['retired-date']
        if request.files['image-file']:
            f = request.files['image-file']
            photo_img = f.read()
            mimetype = f.mimetype
        Employee.insert(name, age, gender, zip_cd, pref_cd, address, div_id, hired_date, retired_date, photo_img, mimetype)
        success="社員の登録に成功しました。"
    
    return render_template('result.html', success=success, errors=errors)

@app.route("/division/<int:id>/edit", methods=["GET"])
def edit_employee(id):
    employee = Employee.find_by_id(id)
    divisions = Division.find_all()
    prefectures = Prefecture.find_all()
    return render_template('edit_employee.html', employee=employee, divisions=divisions, prefectures=prefectures)

@app.route("/employee/<int:id>/update", methods=["POST"])
def update_employee(id):
    errors = []
    if not request.form['name']:
        errors.append('名前は必須です。')

    cmd_type = request.form['cmd-type']
    if cmd_type == 'cancel':
        return render_template('new_division.html')

    age = 0
    pref_cd = 0
    photo_img = None
    mimetype = ''
    div_id = None
    hired_date = None
    retired_date = None
    if not errors:
        name = request.form['name']
        if len(request.form['age']) > 0 :
            age = request.form['age']
        gender = request.form['gender']
        zip_cd = request.form['zip-cd']
        if len(request.form['pref-cd']) > 0 :
            pref_cd = request.form['pref-cd']
        address = request.form['address']
        if len(request.form['div-id']) > 0 :
            div_id = request.form['div-id']
        if len(request.form['hired-date']) > 0 :
            hired_date = request.form['hired-date']
        if len(request.form['retired-date']) > 0 :
            retired_date = request.form['retired-date']
        if request.files['image-file'] :
            f = request.files['image-file']
            photo_img = f.read()
            mimetype = f.mimetype
        Employee.update(id, name, age, gender, zip_cd, pref_cd, address, div_id, hired_date, retired_date, photo_img, mimetype)
        success="社員情報の更新に成功しました。"

    return render_template('result.html', success=success, errors=errors)

@app.route("/employee/<int:id>/delete", methods=["POST"])
def delete_employee(id):
    errors = []

    employee = Employee.find_by_id(id)
    Employee.delete(id)
    success="データベースから社員(" +employee.name + ")を削除しました。"
    
    return render_template('result.html', success=success, errors=errors)

@app.route("/employees/search", methods=["GET"])
def search_employees():
    divisions = Division.find_all()
    divisions.insert(0, Division(0, '未指定'))
    return render_template('search_employee.html', divisions=divisions)

@app.route("/employee/search", methods=["POST"])
def find_employees():
    div_id = 0
    id_from = 0
    id_to = 0
    if len(request.form['div-id']) > 0 :
        div_id = int(request.form['div-id'])
    if len(request.form['id-from']) > 0 :
        id_from = int(request.form['id-from'])
    if len(request.form['id-to']) > 0 :
        id_to = int(request.form['id-to'])
    kw = request.form['kw']

    # TODO: 社員ID範囲チェック
    employees = Employee.find_by(div_id, id_from, id_to, kw)
    return render_template('employee_list.html', employees=employees)

@app.route("/download/employee", methods=["GET"])
def download_employee():
    f = StringIO()
    writer = csv.writer(f, quotechar='"', quoting=csv.QUOTE_ALL, lineterminator="\n")

    writer.writerow(['id','名前', '年齢', '性別', '郵便番号', '都道府県', '住所', '部署名', '入社日', '退社日', '作成日時', '更新日時'])
    employees = Employee.find_all_in_details()
    for emp in employees:
        writer.writerow([emp.id, emp.name, emp.age, emp.gender, emp.zip_cd, emp.pref_name, emp.address, emp.div_name, emp.hired_date, emp.retired_date, emp.created_at, emp.updated_at])

    res = make_response()
    res.data = f.getvalue()
    res.headers['Content-Type'] = 'text/csv'
    res.headers['Content-Disposition'] = 'attachment; filename=employee_list.csv'
    return res

@app.route("/divisions")
def divisions():
    divisions = Division.find_all()
    return render_template('division_list.html', divisions=divisions)

@app.route("/division/new", methods=["GET"])
def new_division():
    return render_template('new_division.html')
    
@app.route("/division/create", methods=["POST"])
def create_division():
    errors = []
    if not request.form['name']:
        errors.append('部署名は必須です。')

    cmd_type = request.form['cmd-type']
    if cmd_type == 'cancel':
        return render_template('new_division.html')

    if not errors:   
        name = request.form['name']
        Division.insert(name)
        success="部署の登録に成功しました。"
    
    return render_template('result.html', success=success, errors=errors)

@app.route("/division/<int:id>/edit", methods=["GET"])
def edit_division(id):
    division = Division.find_by_id(id)
    return render_template('edit_division.html', division=division)

@app.route("/division/<int:id>/update", methods=["POST"])
def update_division(id):
    errors = []
    if not request.form['name']:
        errors.append('部署名は必須です。')

    cmd_type = request.form['cmd-type']
    if cmd_type == 'cancel':
        division = Division.find_by_id(id)
        return render_template('edit_division.html', division=division)

    if not errors:   
        name = request.form['name']
        division = Division.update(id, name)
        success="データベースへの登録に成功しました。"
    
    return render_template('result.html', success=success, errors=errors)

@app.route("/division/<int:id>/delete", methods=["POST"])
def delete_division(id):
    errors = []

    division = Division.find_by_id(id)
    Division.delete(id)
    success="データベースから部署(" +division.name + ")を削除しました。"
    
    return render_template('result.html', success=success, errors=errors)

@app.route('/photo/<int:id>', methods=["GET"])
def get_photo_image(id):
    try:
        photo = Photo.find_by_id(id)
        response = make_response()
        response.data = photo.image
        response.headers["Content-type"] = photo.mimetype
        return response
    except:
        pass

    success = ''
    errors = []
    errors.append('画像の取得に失敗しました。')
    return render_template('result.html', success=success, errors=errors)

@app.route('/hello')
def hello():
    return 'Hello, World!'