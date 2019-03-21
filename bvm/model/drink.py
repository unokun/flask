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

    def find_all():
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

    def find_by_id(drink_id):
        """
        drinkテーブルから飲み物情報を取得する
        Returns
        -------
        drinkクラス
        """
        cnx = model.db.get_connection()
        cur = cnx.cursor()
        query = ("SELECT T1.id, T1.name, T1.price, T2.count, T1.image, T1.status, T1.created_at, T1.updated_at FROM drinks AS T1"
                 " INNER JOIN stocks AS T2"
                 " ON "
                 " T2.id = T1.id"
                 " WHERE T1.id = %s")
        val = (drink_id,)
        cur.execute(query, val)

        (id, name, price, count, image, status, created_at, updated_at) = cur.fetchone()
        drink = Drink(id, name, price, count, image, status, created_at, updated_at)
        cnx.close()

        return drink

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

    def buy_drink(drink_id):
        """
        飲み物購入
        """
        cnx = model.db.get_connection()
        cur = cnx.cursor()
    
        # 在庫管理の数を一つ減らす
        query = "UPDATE stocks SET count = count - 1, updated_at = now() WHERE id = %s"
        val = (drink_id,)
        cur.execute(query, val)

        # 購入履歴に登録
        query = ("INSERT INTO  buy_histories (id, buy_at) VALUES (%s, now())")
        val = (drink_id,)
        cur.execute(query, val)

        cnx.commit()
        cnx.close()
    
        return

    def update_count(drink_id, count):
        """
        個数更新
        """
        cnx = model.db.get_connection()
        cur = cnx.cursor()
    
        # 在庫管理の数を一つ減らす
        query = "UPDATE stocks SET count = %s, updated_at = now() WHERE id = %s"
        val = (count, drink_id,)
        cur.execute(query, val)

        cnx.commit()
        cnx.close()
    
        return

    def update_status(drink_id, status):
        """
        飲み物ステータス更新
        """
        cnx = model.db.get_connection()
        cur = cnx.cursor()
    
        # 在庫管理の数を一つ減らす
        query = "UPDATE drinks SET status = %s, updated_at = now() WHERE id = %s"
        val = (status, drink_id,)
        cur.execute(query, val)

        cnx.commit()
        cnx.close()
    
        return
