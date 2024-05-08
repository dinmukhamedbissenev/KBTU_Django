from django.shortcuts import render
from .models import *
# Create your views here.
def get_product(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'objects':products})

def get_categories(request):
    categories = Category.objects.all()
    return render(request, 'index.html', {'objects':categories})

def get_cart(request):
    cart = Cart_Item.objects.all()
    return render(request,'index.html', {'objects':cart})

def get_customers(request):
    customers = Customer.objects.all()
    return render(request, 'index.html', {'objects':customers})