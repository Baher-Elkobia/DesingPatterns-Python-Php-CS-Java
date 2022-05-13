from logger import Logger
from views import ProductListView
from models import Product

logger1 = Logger()
logger2 = Logger()

print(logger1 == logger2)
print(logger1)
print(logger2)

ProductListView.list_products('t-shirt')
Product.buy(quantity=2)
