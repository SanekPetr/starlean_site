from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest, HttpResponsePermanentRedirect
from .models import Product
from django.views.generic import View

def index(request):
    return render(request, 'index.html')
def show_all_products(request):
    all_products = Product.objects.all()
    return render(request, "shop/index.html", context={'products':all_products})

def delete_concrete_products(request:HttpRequest, id:int)->HttpResponse:
    Product.objects.get(id=id).delete()
    return HttpResponsePermanentRedirect("/products")

def show_products(request):
    all_products = Product.objects.all()
    return render(request, "shop/products.html", context={'products':all_products})


def Home_Page(View):
    def post(self, *args, **kwargs):
        return redirect("/products")

def All_Products(View):
    def post(self, *args, **kwargs):
        return redirect("/products/all/")


