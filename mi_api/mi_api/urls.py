from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('productos.urls')),  # Asegúrate de que 'productos' esté bien escrito
]
