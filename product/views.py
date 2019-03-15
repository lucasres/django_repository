from django.views import generic
from django.http import HttpResponse
from product.repository import ProductRepository

# Create your views here.
class SellProduct(generic.View):

    def get(self,request,pk):
        try:
            rs = ProductRepository.buy_product(pk)
            return HttpResponse(rs)
        except Exception as e:
            return HttpResponse(str(e))


class AddStock(generic.View):

    def get(self,request,pk):
        try:
            ProductRepository.add_stock(pk)
            return HttpResponse('Add successful')
        except Exception as e:
            return HttpResponse(str(e))