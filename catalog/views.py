from django.shortcuts import render
from .models import Product, Contacts


def contacts(request):
    contacts_fill = Contacts.objects.all()
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(name, phone, message)
    return render(request, 'catalog/contacts.html', {'contacts': contacts_fill})


def home(request):
    latest_products = Product.objects.order_by('-created_at')[:2]  # выборка последних двух товаров (у меня их мало просто)
    for product in latest_products:
        print(product)
    return render(request, 'catalog/home.html')
