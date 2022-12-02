from django.shortcuts import render
from .models import Product, Customer, Order

def product_list(request):
    products = Product.objects.all()
    return render(request, 'ecommerce/product_list.html',{'products': products})

def customer_orders(request, customer_id):
    customer = Customer.objects.get(id=customer_id)
    orders = Order.objects.filter(customer=customer)
    return render(request, 'ecommerce/customer_orders.html', {'customer': customer, 'orders': orders})
    

