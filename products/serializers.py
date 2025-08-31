from rest_framework import serializers
from .models import Product, Category, Order
from django.contrib.auth.models import User

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'category', 'stock_quantity', 'image_url', 'created_date']

    def validate(self, data):
        # Custom validation for required fields
        if not data.get('name'):
            raise serializers.ValidationError({"name": "This field is required."})
        if 'price' not in data or data['price'] <= 0:
            raise serializers.ValidationError({"price": "Price must be greater than 0."})
        if 'stock_quantity' not in data or data['stock_quantity'] < 0:
            raise serializers.ValidationError({"stock_quantity": "Stock quantity cannot be negative."})
        return data
    
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'description']

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'user', 'product', 'quantity', 'created_at', 'total_price']
        read_only_fields = ['user', 'created_at', 'total_price']  # Auto-set user and timestamps

    def create(self, validated_data):
        # Set user to the authenticated user
        validated_data['user'] = self.context['request'].user
        
        # Check and reduce stock
        product = validated_data['product']
        if product.stock_quantity < validated_data['quantity']:
            raise serializers.ValidationError({"stock_quantity": "Insufficient stock."})
        
        # Reduce stock
        product.stock_quantity -= validated_data['quantity']
        product.save()
        
        # Create order
        return super().create(validated_data)