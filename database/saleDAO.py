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

    def getVendDAO(self, anno, brand, retailer_code):
        cnx = DBConnect.get_connection()
        if cnx is not None:
            result = []
            cursor = cnx.cursor(dictionary= True)
            query = """SELECT gds.*, gds.Unit_sale_price*gds.Quantity AS Ricavo
                FROM go_daily_sales gds, go_retailers gr, go_products gp 
                WHERE gds.Retailer_code  = gr.Retailer_code  
                AND gds.Product_number = gp.Product_number 
                AND (YEAR(gds.Date)=COALESCE(%s,YEAR(gds.Date)))
                AND (gp.Product_brand =COALESCE(%s,gp.Product_brand))
                AND (gr.Retailer_code =COALESCE(%s,gr.Retailer_code))"""
            cursor.execute(query, (anno, brand, retailer_code,))
            for row in cursor:
                result.append(Sale(row["Retailer_code"],
                                   row["Product_number"],
                                   row["Order_method_code"],
                                   row["Date"],
                                   row["Quantity"],
                                   row["Unit_price"],
                                   row["Unit_sale_price"]))
            cursor.close()
            cnx.close()
            return result
        else:
            print("Errore nella connessione")
            return None

    def getStatVend(self):
        pass