from django.urls import path, include
from .views import ProductoViewSet
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'productos', ProductoViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api/productos/multiple/', views.create_multiple_productos, name='create-multiple-productos'),
]
