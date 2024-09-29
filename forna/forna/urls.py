from django.urls import path ,include
from django.contrib import admin
from .product.views import (
    ProductListCreateView, ProductRetrieveUpdateDestroyView,
    CategoryListCreateView, CategoryRetrieveUpdateDestroyView,
    SupplierListCreateView, SupplierRetrieveUpdateDestroyView,
    CustomerListCreateView, CustomerRetrieveUpdateDestroyView,
    OrderListCreateView, OrderRetrieveUpdateDestroyView,
    OrderItemListCreateView, OrderItemRetrieveUpdateDestroyView,
    EmployeeListCreateView, EmployeeRetrieveUpdateDestroyView,
    InventoryListCreateView, InventoryRetrieveUpdateDestroyView,
    InvoiceListCreateView, InvoiceRetrieveUpdateDestroyView ,
)

urlpatterns = [
     # Admin
    path('admin/', admin.site.urls),  
    
    # Products
    path('products/', ProductListCreateView.as_view(), name='product-list-create'),
    path('products/<int:pk>/', ProductRetrieveUpdateDestroyView.as_view(), name='product-detail'),
    
    # Categories
    path('categories/', CategoryListCreateView.as_view(), name='category-list-create'),
    path('categories/<int:pk>/', CategoryRetrieveUpdateDestroyView.as_view(), name='category-detail'),

    # Suppliers
    path('suppliers/', SupplierListCreateView.as_view(), name='supplier-list-create'),
    path('suppliers/<int:pk>/', SupplierRetrieveUpdateDestroyView.as_view(), name='supplier-detail'),

    # Customers
    path('customers/', CustomerListCreateView.as_view(), name='customer-list-create'),
    path('customers/<int:pk>/', CustomerRetrieveUpdateDestroyView.as_view(), name='customer-detail'),

    # Orders
    path('orders/', OrderListCreateView.as_view(), name='order-list-create'),
    path('orders/<int:pk>/', OrderRetrieveUpdateDestroyView.as_view(), name='order-detail'),

    # Order Items
    path('order-items/', OrderItemListCreateView.as_view(), name='orderitem-list-create'),
    path('order-items/<int:pk>/', OrderItemRetrieveUpdateDestroyView.as_view(), name='orderitem-detail'),

    # Employees
    path('employees/', EmployeeListCreateView.as_view(), name='employee-list-create'),
    path('employees/<int:pk>/', EmployeeRetrieveUpdateDestroyView.as_view(), name='employee-detail'),

    # Inventory
    path('inventory/', InventoryListCreateView.as_view(), name='inventory-list-create'),
    path('inventory/<int:pk>/', InventoryRetrieveUpdateDestroyView.as_view(), name='inventory-detail'),

    # Invoices
    path('invoices/', InvoiceListCreateView.as_view(), name='invoice-list-create'),
    path('invoices/<int:pk>/', InvoiceRetrieveUpdateDestroyView.as_view(), name='invoice-detail'),
    
]
