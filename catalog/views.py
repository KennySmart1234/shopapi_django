from rest_framework import status, permissions
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin
from rest_framework.permissions import IsAdminUser
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, GenericViewSet

from .serializers import ProductSerializer, CategorySerializer, CartSerializer, ProductReviewSerializer
from .models import Product, Category, Cart, Review


# Create your views here.

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all().filter(is_active=True)
    serializer_class = ProductSerializer

    def get_permissions(self):
        if self.request.method in permissions.SAFE_METHODS:
            return [AllowAny()]
        return [IsAdminUser()]



@api_view(['GET'])
@permission_classes([AllowAny])
def get_product_by_category(request, slug):
    try:
        category = Category.objects.get(slug=slug)
        serializer = CategorySerializer(category)
        return Response(serializer.data, status=status.HTTP_200_OK)

    except Category.DoesNotExist:
        return Response({"Error": "category not found"}, status=status.HTTP_404_NOT_FOUND)



class CartViewSet(CreateModelMixin, RetrieveModelMixin, GenericViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [AllowAny]


class ReviewViewSet(ModelViewSet):
    serializer_class = ProductReviewSerializer
    queryset = Review.objects.all()

