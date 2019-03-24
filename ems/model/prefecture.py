import model.db

class Prefecture(object):
    def __init__(self, id, name, name_kana):
        self.id = id
        self.name = name
        self.name_kana = name_kana
    
    def find_all():
        """ 都道府県一覧取得 """        
        cnx = model.db.get_connection()
        cur = cnx.cursor()
        query = ("SELECT id, name, name_kana FROM prefectures ORDER BY id")
        cur.execute(query)

        prefectures = []
        for (id, name, name_kana) in cur:
            prefecture = Prefecture(id, name, name_kana)
            prefectures.append(prefecture)
        cnx.close()

        return prefectures

    def find_by_id(id):
        """ 都道府県取得 """        
        cnx = model.db.get_connection()
        cur = cnx.cursor()
        query = ("SELECT id, name, name_kana FROM prefectures WHERE id=%s")
        val =(id,)
        cur.execute(query, val)

        (id, name, name_kana) = cur.fetchone()
        prefecture = prefecture(id, name, name_kana)
        cnx.close()

        return prefecture



