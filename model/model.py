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
        listSale = self._sales_dao.getVendDAO(anno, brand, retailer_code)
        listSale.sort(reverse = True)
        return listSale[0:5]

    def getAnalisi(self, anno, brand, retailer_code):
        listSale = self._sales_dao.getVendDAO(anno, brand, retailer_code)
        if len(listSale) == 0:
            return 0, 0, 0, 0
        else:
            ricavi = 0
            numR = set()
            numP = set()
            for sale in listSale:
                ricavi += sale.ricavo
                numR.add(sale.retailer_code)
                numP.add(sale.product_number)
            numV = len(listSale)
            return ricavi, numV, len(numR), len(numP)