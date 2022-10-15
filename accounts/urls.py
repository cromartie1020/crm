from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('create/',views.create_order, name='create'),
    path('products/',views.products, name='products'),
    path('customers/',views.customers, name='customers'),
    path("<int:order_id>",views.order_update,name='update'),
    path('delete/<int:order_id>/',views.order_delete,name='delete'),
    path('customer/<int:customer_id>/',views.customer,name="customer")
]