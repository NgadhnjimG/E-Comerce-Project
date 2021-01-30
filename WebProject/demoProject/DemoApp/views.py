from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, Category
# Create your views here.


def cart(request):
    context={}
    return render(request, 'Cart.html', context)



def index(request):
    return render(request,'index.html')

def category_List(request):
    getCategory = {
        "Category": Category.objects.all()
    }
    return render(request,'index.html',getCategory)


def product_List(request):
    getProducts = {
        "Products": Product.objects.all()
    }
    return render(request,'index.html',getProducts)

def List_All(request):
    getAll = {
                      "Products": Product.objects.all(),
                      "Category": Category.objects.all()
                  }

    return render(request, 'index.html', getAll)