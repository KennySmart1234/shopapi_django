from rest_framework import serializers
from .models import Product, Category, Cart, CartItem, Review


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['title', 'price', 'description', 'sku']


class CategorySerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True)

    class Meta:
        model = Category
        fields = ['id', 'name', 'products']


class CartItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    total_price = serializers.SerializerMethodField()

    class Meta:
        model = CartItem
        fields = ['product', 'quantity', 'total_price']

    def get_total_price(self, item: CartItem):
        total_price = item.product.price * item.quantity
        return total_price


class CartSerializer(serializers.ModelSerializer):
    cart_id = serializers.UUIDField(read_only=True)
    item = CartItemSerializer(many=True, read_only=True)

    class Meta:
        model = Cart
        fields = ['cart_id', 'item']

    def get_total_price(self, cart: Cart):
        return sum(item.product.price * item.quantity for item in cart.items.all())



class ProductReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        read_only_fields = ['user', 'product']
        fields = ['rating', 'comment']