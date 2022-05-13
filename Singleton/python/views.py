from logger import Logger

logger = Logger()


class ProductListView:
    @staticmethod
    def list_products(category: str):
        logger.info(f'View of all products from {category} - category')
        """
        Code to list all products
        """
