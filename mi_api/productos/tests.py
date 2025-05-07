from rest_framework.test import APITestCase
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from .models import Producto

class ProductoAPITestCase(APITestCase):
    def setUp(self):
        # Crear un usuario de prueba
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        # Crear un token para el usuario
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)  # Autenticación

    def test_create_producto(self):
        url = '/api/productos/'
        data = {
            'nombre': 'Producto Test',
            'descripcion': 'Descripción de prueba',
            'precio': 100.0,
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_productos(self):
        url = '/api/productos/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_producto(self):
        producto = Producto.objects.create(nombre='Producto A', descripcion='Descripción', precio=50.0)
        url = f'/api/productos/{producto.id}/'
        data = {'nombre': 'Producto A Actualizado', 'descripcion': 'Nueva descripción', 'precio': 60.0}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_producto(self):
        producto = Producto.objects.create(nombre='Producto A', descripcion='Descripción', precio=50.0)
        url = f'/api/productos/{producto.id}/'
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
