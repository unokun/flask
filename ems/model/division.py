import model.db

class Division(object):
    def __init__(self, id, name):
        self.id = id
        self.name = name
    
    def find_all():
        """ 部署一覧取得 """        
        cnx = model.db.get_connection()
        cur = cnx.cursor()
        query = ("SELECT id, name FROM divisions ORDER BY id")
        cur.execute(query)

        divisions = []
        for (id, name) in cur:
            division = Division(id, name)
            divisions.append(division)
        cnx.close()

        return divisions

    def find_by_id(id):
        """ 部署取得 """        
        cnx = model.db.get_connection()
        cur = cnx.cursor()
        query = ("SELECT id, name FROM divisions WHERE id=%s")
        val =(id,)
        cur.execute(query, val)

        (id, name) = cur.fetchone()
        division = Division(id, name)
        cnx.close()

        return division

    def insert(name):
        """ 部署挿入 """        
        cnx = model.db.get_connection()
        cur = cnx.cursor()
        query = ("INSERT INTO divisions (name, created_at, updated_at) VALUES (%s, now(), now())")
        val = (name,)
        cur.execute(query, val)
        cnx.commit()
        cnx.close()
        return
    
    def update(id, name):
        """ 部署情報更新 """        
        cnx = model.db.get_connection()
        cur = cnx.cursor()
        query = ("UPDATE divisions SET name=%s, updated_at=now() WHERE id=%s")
        val = (name, id,)
        cur.execute(query, val)
        cnx.commit()
        cnx.close()
        return

    def delete(id):
        """ 部署削除 """        
        cnx = model.db.get_connection()
        cur = cnx.cursor()
        query = ("DELETE FROM divisions WHERE id = %s")
        val = (id,)
        cur.execute(query, val)
        cnx.commit()
        cnx.close()
        return
    


