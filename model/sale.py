import datetime
from dataclasses import dataclass

@dataclass
class Sale:
    retailer_code: int
    product_number: int
    order_method_code: int
    date: datetime.date
    quantity: int
    unit_price: float
    unit_sale_price: float

    def __eq__(self, other):
        return (self.retailer_code == other.retailer_code and self.product_number == other.product_number and self.order_method_code == other.order_method_code)

    def __hash__(self):
        return hash((self.retailer_code, self.product_number, self.order_method_code))