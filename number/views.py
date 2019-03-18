from django.shortcuts import render, HttpResponse
from django.views import generic
from number.repository import NumberRepository

# Create your views here.
class Number20(generic.View):

    def get(self,request,*args, **kwargs):
        rs = NumberRepository.handle_great_20(int(kwargs.get('number',None)))
        return HttpResponse(rs)