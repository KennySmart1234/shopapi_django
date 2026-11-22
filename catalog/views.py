from rest_framework import status, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response

import products
from .serializers import ProductSerializer, CategorySerializer
from .models import Product, Category
from rest_framework.mixins import ListModelMixin

# Create your views here.

# @api_view(['GET'])
# def product_list(request):

    # products = Product.objects.all().all().filter(is_active=True)
    # serializer = ProductSerializer(products, many=True)
    # return Response(serializer.data, status=status.HTTP_200_OK)


class ProductListView(ListAPIView):
    queryset = Product.objects.filter(is_active=True)
    serializer_class = ProductSerializer
    permission_classes = [AllowAny]


# class CategoryListView(ListAPIView):
#     serializer_class = ProductSerializer
#
#     def get_queryset(self, slug):
#         return Category.objects.get(slug=slug)

@api_view(['GET'])
@permission_classes([AllowAny])
def get_product_by_category(request, slug):
    try:
        category = Category.objects.get(slug=slug)
        serializer = CategorySerializer(category)
        return Response(serializer.data, status=status.HTTP_200_OK)

    except Category.DoesNotExist:
        return Response({"Error": "category not found"}, status=status.HTTP_404_NOT_FOUND)

