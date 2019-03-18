from product.models import Product
from dpatterns.repository import RepositoryMixin

class ProductRepository(RepositoryMixin):
    class Meta:
        model = Product
    
    @classmethod
    def buy_product(cls,pk):
        """
        buy one product
        pk: Int
        return: String
        """
        product = cls.get(pk=pk)
        #have in stock
        if product.amount > 0:
            product.amount -= 1
            product.save()
            return 'Sold :)'
        else:
            raise Exception('Out of stock :(')
    
    @classmethod
    def add_stock(cls,pk):
        """
        add one product in the sotck
        pk: Int
        return:
        """
        # add more one
        product = cls.get(pk=pk)
        product.amount += 1
        product.save()