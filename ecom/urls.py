from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', include('book_api.urls')),
    path('product/', include('product.urls'))
]
