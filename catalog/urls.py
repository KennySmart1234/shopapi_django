from django.urls import path, include
from rest_framework_nested import routers

from .views import ProductViewSet, get_product_by_category, CartViewSet, ReviewViewSet

router = routers.DefaultRouter()
router.register('products', ProductViewSet, basename='products')
router.register('carts', CartViewSet, basename='carts')


product_router = routers.NestedDefaultRouter(router, 'products', lookup='product')
product_router.register('reviews', ReviewViewSet, basename='Product-reviews')



urlpatterns = [

    path('', include(router.urls)),
    path('', include(product_router.urls)),
    path('categories/<slug:slug>/', get_product_by_category, name='product_list_by_category'),

]

# urlpatterns += router.urls