from database.saleDAO import SaleDAO
from database.productDAO import ProductDAO
from database.retailerDAO import RetailerDAO
class Model:
    def __init__(self):
        self._sales_dao = SaleDAO()
        self._products_dao = ProductDAO()
        self._retailers_dao = RetailerDAO()

    def getAnni(self):
        return self._sales_dao.getAnniDAO()

    def getBrands(self):
        return self._products_dao.getBrandDAO()

    def getRetailers(self):
        return self._retailers_dao.getRetailerDAO()

    def getTopVendite(self, anno, brand, retailer_code):
        return self._sales_dao.getVendDAO(anno, brand, retailer_code)