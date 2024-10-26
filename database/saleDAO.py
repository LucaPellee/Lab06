from database.DB_connect import DBConnect
from model.sale import Sale

class SaleDAO:

    def getAnniDAO(self):
        cnxPool = DBConnect.get_connection()
        if cnxPool is not None:
            cursor = cnxPool.cursor()
            query = """SELECT DISTINCT YEAR(Date)
                            FROM go_daily_sales"""
            cursor.execute(query)
            result = []
            for row in cursor:
                result.append(row)
            cursor.close()
            cnxPool.close()
            return result
        else:
            print("Errore nella connessione")
            return None