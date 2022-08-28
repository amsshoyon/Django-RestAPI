from django.urls import path
from product.views import ProductCreate, ProductList, ProductDetail

urlpatterns = [
    path('', ProductCreate.as_view()),
    path('list/', ProductList.as_view()),
    path('<int:pk>', ProductDetail.as_view())
]
