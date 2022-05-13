from decimal import Decimal as D
from logger import Logger

logger = Logger()


class Product:
    id = 10
    name = 'Adidas'
    price = D('34.6')
    quantity = 30

    @classmethod
    def buy(cls, quantity: int):
        cls.quantity = - quantity
        """
        Rest of the method code
        """
        logger.info(f'Purchase of {quantity} items of {cls.id} - {cls.name}')
        logger.info(f'Reimagining products of {cls.id} - {cls.name} is {cls.quantity}')

