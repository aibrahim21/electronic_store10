from django.urls import path
from .views import (
    ProductListView, 
    ProductCreateView, 
    ProductUpdateView, 
    ProductDeleteView,
    product_detail
)

app_name = 'store'

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('<slug:category_slug>/', ProductListView.as_view(), name='product_list_by_category'),
    path('create/', ProductCreateView.as_view(), name='product_create'),
    path('<int:pk>/update/', ProductUpdateView.as_view(), name='product_update'),
    path('<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),
    path('<int:id>/<slug:slug>/', product_detail, name='product_detail'),
]