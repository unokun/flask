import model.db

class Photo(object):
    def __init__(self, id, image, mimetype):
        self.id = id
        self.image = image
        self.mimetype = mimetype

    def find_by_id(id):
        """ 画像取得 """        
        cnx = model.db.get_connection()
        cur = cnx.cursor()
        query = ("SELECT id, image, mimetype FROM photos WHERE id=%s")
        val =(id,)
        cur.execute(query, val)

#        (id, image, mimetype) = cur.fetchone()
        for (id, image, mimetype) in cur:
            photo = Photo(id, image, mimetype)
        cnx.close()

        return photo