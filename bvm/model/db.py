import mysql.connector

DB_USER_NAME = "vending"
DB_PASSWORD = "vending"
DB_HOST = "localhost"
DB_PORT = "3306"
DB_NAME = "vendingdb"

def get_connection():
    """ DBコンテキスト取得　"""
    conn = mysql.connector.connect(
                    user=DB_USER_NAME,
                    password=DB_PASSWORD,
                    host=DB_HOST,
                    port=DB_PORT,
                    database=DB_NAME)
    return conn