from rest_framework import serializers
from .models import Product, Category, Supplier, Customer, Order, OrderItem, Employee, Inventory, Invoice

# Product Serializer
class ProductSerializer(serializers.ModelSerializer):
    # Allow the category and supplier fields to accept IDs
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
    supplier = serializers.PrimaryKeyRelatedField(queryset=Supplier.objects.all())

    class Meta:
        model = Product
        fields = '__all__'

    # Custom create method to handle nested category and supplier
    def create(self, validated_data):
        category = validated_data.pop('category')
        supplier = validated_data.pop('supplier')
        product = Product.objects.create(category=category, supplier=supplier, **validated_data)
        return product

# Category Serializer
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

# Supplier Serializer
class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = '__all__'

# Customer Serializer
class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'
    def create(self, validated_data):
        # Assuming 'customer' is a ForeignKey in Order, and you pass a customer ID.
        customer = validated_data.pop('customer')
        order = Order.objects.create(customer=customer, **validated_data)
        return order

# Order Serializer
class OrderSerializer(serializers.ModelSerializer):
    customer= serializers.PrimaryKeyRelatedField(queryset=Customer.objects.all())

    class Meta:
        model = Order
        fields = '__all__'

    # Custom create method for orders
    def create(self, validated_data):
        customer = validated_data.pop('customer')
        order = Order.objects.create(customer=customer, **validated_data)
        return order

# OrderItem Serializer
class OrderItemSerializer(serializers.ModelSerializer):
    order = serializers.PrimaryKeyRelatedField(queryset=Order.objects.all())
    product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())

    class Meta:
        model = OrderItem
        fields = '__all__' 

# Employee Serializer
class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

# Inventory Serializer
class InventorySerializer(serializers.ModelSerializer):
    product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())

    class Meta:
        model = Inventory
        fields = '__all__'
    def create(self, validated_data):
        product = validated_data.get('product')
        inventory_item, created = Inventory.objects.update_or_create(
            product=product,
            defaults=validated_data
        )

        return inventory_item
# Invoice Serializer
class InvoiceSerializer(serializers.ModelSerializer):
    order = serializers.PrimaryKeyRelatedField(queryset=Order.objects.all())

    class Meta:
        model = Invoice
        fields = '__all__'
