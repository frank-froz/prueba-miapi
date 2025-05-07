import django_filters
from rest_framework import viewsets
from .models import Producto
from .serializers import ProductoSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

class ProductoFilter(django_filters.FilterSet):
    nombre = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Producto
        fields = ['nombre']

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = ProductoFilter
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated] 
    
    
@api_view(['POST'])
def create_multiple_productos(request):
    """
    Crear múltiples productos en una sola solicitud.
    """
    if isinstance(request.data, list):  # Verifica que los datos sean una lista
        serializer = ProductoSerializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response({"error": "Se esperaba una lista de productos"}, status=status.HTTP_400_BAD_REQUEST)


