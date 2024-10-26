from database.saleDAO import SaleDAO
class Model:
    def __init__(self):
        self._sales_dao = SaleDAO()

    def getAnni(self):
        return self._sales_dao.getAnniDAO()