from database.DB_connect import DBConnect
from model.retailer import Retailer

class RetailerDAO:

    def getRetailerDAO(self):
        cnx = DBConnect.get_connection()
        if cnx is not None:
            result = []
            cursor = cnx.cursor(dictionary=True)
            query = """SELECT DISTINCT * FROM go_retailers"""
            cursor.execute(query)
            for row in cursor:
                result.append(Retailer(row["Retailer_code"], row["Retailer_name"], row["Type"], row["Country"]))
            cursor.close()
            cnx.close()
            return result
        else:
            print("Connessione non riuscita")
            return None

