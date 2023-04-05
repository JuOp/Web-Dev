from django.urls import path
from shop_api.views import products_list, get_product_by_id, categories_list, get_category_by_id 

urlpatterns = [
    path('products/', products_list),
    path('products/<int:product_id>/', get_product_by_id),
    path('categories/', categories_list),
    path('categories/<int:category_id>/', get_category_by_id),
]