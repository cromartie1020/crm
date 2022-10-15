from django.shortcuts import render, redirect

from accounts.models import *
from .forms import OrderForm
from .forms import CreateForm


def home(request):
    orders = Order.objects.all()
    products = Product.objects.all()
    customers=Customer.objects.all()
    
    firstCustomer=Customer.objects.get(name= 'Haynes Cromartie')  
    
    order_total = 0

    for customer in customers:
        name=Customer.objects.get(name=customer)
        order=name.order_set.all().count()
        order_total = order_total + order
        if not customer:
            return order_total
    

    out_for_delivery=Order.objects.filter(status="Out for delivery").count()
    
    
    order_delivered=Order.objects.filter(status="Delivered").count()
    
    order1 =Order.objects.filter(status="Pending").count()
       
    
   
    context={
        "orders":orders[:5],
        "customers":customers,
        "products":products,
        "order_total": order_total,
        "order":order,
        "order_delivered":order_delivered,
        "order1":order1
    
    }
    return render(request, 'accounts/dashboard.html',context)


def customers(request):
    orders = Order.objects.all()
    order=Order.objects.all().count()
    products = Product.objects.all()
    #customer=Customer.objects.get(name=request.user)
    customers=Customer.objects.all()
    
    print(order)
    for customer in customers:
        print (customer.name)
        total = Customer.objects.filter(name=customer.name).count()
        print(total) 
        
    context={
        "orders":orders,
        "products":products,
        "customer":customer 

    }
    return render(request, 'accounts/customers.html',context)

def customer(request, customer_id):
    
    
    products = Product.objects.all()
    customer=Customer.objects.get(id=customer_id)
    orders = Order.objects.filter(customer=customer)
    total_orders=customer.order_set.all().count()  
    for order in orders:
        print(order)  
    
        
    context={
        "orders":orders,
        "products":products,
        "customer":customer,
        "total_orders":total_orders 

    }
    return render(request, 'accounts/customers.html',context)

def products(request):
    products=Product.objects.all()
    context={
        'products':products,
        'stat':stat,
       

    }
    return render(request, 'accounts/products.html',context)

            
def order_update(request, order_id):
    order=Order.objects.get(id=order_id)
    form = OrderForm(request.POST or None, instance=order )
    
    if form.is_valid():
        order=form.save(commit=False)
        order.save()
        return redirect('home')



    context = {
        'form':form,
        'order':order


    }
    return render(request,'accounts/order_update.html',context)


def order_delete(request, order_id):
    order = Order.objects.get(id=order_id)
    if request.method == "POST":
         
        order.delete()
        return redirect('home')
    context = {
        "order":order   
    }   

    return render(request,'accounts/order_delete.html',context)
    

def create_order(request):

    form=OrderForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')

    context = {
        "form":form
    }  
    return render(request, 'accounts/create_order.html', context)  


    