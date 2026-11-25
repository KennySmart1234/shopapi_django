# from accounts import serializers
# from catalog.serializers import CartItemSerializer
# from orders.models import Order
#
#
# class OrderSerializer(serializers.ModelSerializer):
#     cart_items = CartItemSerializer(many=True)
#
#     class Meta:
#         model = Order
#         fields = ('id', 'name', 'email', 'phone', 'address', 'city', 'state',)