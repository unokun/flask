import model.db

class Employee(object):
    """
    従業員情報
    ----------
    id : ID
    name : 氏名
    age : 年齢
    gender : 性別
    address : 住所
    photo_image : 写真イメージ
    div_name : 部署名
    """
    def __init__(self, id, name, age=None, gender="", photo_id=None, zip_cd="", pref_cd=None, address = "", div_id = None, hired_date=None, retired_date=None, created_at=None, updated_at=None):
        self.id = id
        self.name = name
        self.age = age
        self.gender = gender
        self.photo_id = photo_id
        self.zip_cd = zip_cd
        self.pref_cd = pref_cd
        self.address = address
        self.div_id = div_id
        self.hired_date = hired_date
        self.retired_date = retired_date
        self.created_at = created_at
        self.updated_at = updated_at

    def find_all():
        cnx = model.db.get_connection()
        cur = cnx.cursor()
        query = ("SELECT id, name FROM employees")
        cur.execute(query)

        employees = []
        for (id, name) in cur:
            employee = Employee(id, name)
            employees.append(employee)
        cnx.close()

        return employees

    def find_all_in_details():
        cnx = model.db.get_connection()
        cur = cnx.cursor()
        query = ("SELECT T1.id, T1.name, T1.age, T1.gender, T1.zip_cd, T1.pref_cd, T3.name pref_name, T1.address, T1.div_id, T2.name div_name, T1.hired_date, T1.retired_date, T1.created_at, T1.updated_at FROM employees AS T1"
                 " INNER JOIN divisions AS T2"
                 " ON "
                 " T2.id = T1.div_id"
                 " INNER JOIN prefectures AS T3"
                 " ON "
                 " T3.id = T1.pref_cd"
                 )
        cur.execute(query)

        employees = []
        for (id, name, age, gender, zip_cd, pref_cd, pref_name, address, div_id, div_name, hired_date, retired_date, created_at, updated_at) in cur:
            employee = Employee(id, name, age, gender, 0, zip_cd, pref_cd, address, div_id, hired_date, retired_date, created_at, updated_at)
            employee.pref_name = pref_name
            employee.div_name = div_name
            employees.append(employee)
        cnx.close()

        return employees

    def find_by_id(id):
        """ 社員情報取得 """        
        cnx = model.db.get_connection()
        cur = cnx.cursor()
        query = ("SELECT id, name, age, gender, photo_id, zip_cd, pref_cd, address, div_id, hired_date, retired_date FROM employees WHERE id=%s")
        val =(id,)
        cur.execute(query, val)

        (id, name, age, gender, photo_id, zip_cd, pref_cd, address, div_id, hired_date, retired_date) = cur.fetchone()
        employee = Employee(id, name, age, gender, photo_id, zip_cd, pref_cd, address, div_id, hired_date, retired_date)
        cnx.close()

        return employee

    def find_by(div_id, id_from, id_to, kw):
        """ 社員情報絞り込み """        
        cnx = model.db.get_connection()
        cur = cnx.cursor()
        constraint = ""
        val = ()
        if div_id > 0:
            if len(constraint) > 0:
                constraint = constraint + " AND "
            constraint = constraint + "div_id = %s"
            val = val + (div_id,)

        if id_from > 0:
            if len(constraint) > 0:
                constraint = constraint + " AND "
            constraint = constraint + "id >= %s"
            val = val + (id_from,)

        if id_to > 0:
            if len(constraint) > 0:
                constraint = constraint + " AND "
            constraint = constraint + "id <= %s"
            val = val + (id_to,)

        if len(kw) > 0:
            if len(constraint) > 0:
                constraint = constraint + " AND "
            constraint = constraint + "name LIKE CONCAT('%', %s, '%')"
            val = val + (kw,)

        if len(constraint) == 0:
            query = ("SELECT id, name FROM employees")
            cur.execute(query)
        else:
            constraint = " WHERE " + constraint
            query = ("SELECT id, name FROM employees " + constraint)
            cur.execute(query, val)
             
        employees = []
        for (id, name) in cur:
            employee = Employee(id, name)
            employees.append(employee)
        cnx.close()

        return employees

    def insert(name, age, gender, zip_cd, pref_cd, address, div_id, hired_date, retired_date, photo_img, mimetype):
        """ 社員情報挿入 """
        cnx = model.db.get_connection()
        cur = cnx.cursor()

        if photo_img:
            # 画像登録
            query = ("INSERT INTO photos (image, mimetype) VALUES (%s, %s)")
            val = (photo_img, mimetype,)
            cur.execute(query, val)

            # 社員登録
            query = ("INSERT INTO employees (name, age, gender, photo_id, zip_cd, pref_cd, address, div_id, hired_date, retired_date, created_at, updated_at) VALUES (%s, %s, %s, LAST_INSERT_ID(), %s, %s, %s, %s, %s, %s, now(), now())")
            val = (name, age, gender, zip_cd, pref_cd, address, div_id, hired_date, retired_date,)
            cur.execute(query, val)
        else:
            # 社員登録
            query = ("INSERT INTO employees (name, age, gender, photo_id, zip_cd, pref_cd, address, div_id, hired_date, retired_date, created_at, updated_at) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, now(), now())")
            val = (name, age, gender, None, zip_cd, pref_cd, address, div_id, hired_date, retired_date,)
            cur.execute(query, val)

        cnx.commit()
        cnx.close()

        return

    def update(id, name, age, gender, zip_cd, pref_cd, address, div_id, hired_date, retired_date, photo_img, mimetype):
        """ 社員情報更新 """        
        cnx = model.db.get_connection()
        cur = cnx.cursor()

        # 画像登録
        query = ("INSERT INTO photos (photo_image, mimetype) VALUES (%s, %s)")
        val = (photo_img, mimetype,)
        cur.execute(query, val)

        # 社員情報更新
        query = ("UPDATE employees SET name=%s, age=%s, gender=%s, photo_id=LAST_INSERT_ID(), zip_cd=%s, pref_cd=%s, address=%s, div_id=%s, hired_date=%s, retired_date=%s, updated_at=now() WHERE id=%s")
        val = (name, age, gender, zip_cd, pref_cd, address, div_id, hired_date, retired_date, id,)
        cur.execute(query, val)
        cnx.commit()
        cnx.close()
        return

    def delete(id):
        """ 社員削除 """        
        cnx = model.db.get_connection()
        cur = cnx.cursor()
        query = ("DELETE FROM employees WHERE id = %s")
        val = (id,)
        cur.execute(query, val)
        cnx.commit()
        cnx.close()
        return