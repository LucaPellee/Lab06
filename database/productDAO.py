from database.DB_connect import DBConnect
from model.product import Product

class ProductDAO:

    def getBrandDAO(self):
        cnx= DBConnect.get_connection()
        cursor= cnx.cursor()
        query = """SELECT DISTINCT product_brand FROM go_products"""
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()
        cnx.close()
        return result