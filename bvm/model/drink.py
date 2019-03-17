#from model.db import db
import model.db
import datetime

class Drink(object):
    """
    飲み物情報
    Attributes
    ----------
    id : ID
    name : 飲み物名前
    price : 価格
    count : 個数
    image : 画像のファイルパス
    status : ステータス
    creaed_at : 作成日
    updated_at : 更新日
    """
    def __init__(self, id, name, price, count, image, status, created_at = "", updated_at = ""):
        self.id = id
        self.name = name
        self.price = price
        self.count = count
        self.image = image
        self.status = status
        self.created_at = created_at
        self.updated_at = updated_at

    def findAll():
        """
        drinkテーブルから飲み物一覧を取得する
        Returns
        -------
        drinkクラスのリスト
        """
        cnx = model.db.get_connection()
        cur = cnx.cursor()
        query = ("SELECT T1.id, T1.name, T1.price, T2.count, T1.image, T1.status, T1.created_at, T1.updated_at FROM drinks AS T1"
                 " INNER JOIN stocks AS T2"
                 " ON "
                 " T2.id = T1.id")
        cur.execute(query)

        drinks = []
        for (id, name, price, count, image, status, created_at, updated_at) in cur:
            drink = Drink(id, name, price, count, image, status, created_at, updated_at)
            drinks.append(drink)
        cnx.close()

        return drinks

    def insert(name, price, count, filename, status):
        """
        drinkテーブルに登録する
        """
        cnx = model.db.get_connection()
        cur = cnx.cursor()
        now = datetime.datetime.now
        query = ("INSERT INTO drinks (name, price, image, status, created_at, updated_at) VALUES (%s, %s, %s, %s, now(), now())")
        val = (name, price, filename, status)
        cur.execute(query, val)


        query = ("INSERT INTO stocks (id, count, created_at, updated_at) VALUES (LAST_INSERT_ID(), %s, now(), now())")
        # カンマが必要
        val = (count,)
        cur.execute(query, val)

        cnx.commit()
        cnx.close()

        return