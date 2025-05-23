from django.shortcuts import render
from .models import Producto
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Producto
from .serializers import ProductoSerializer

# Create your views here.

def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, 'productos.html', {'productos': productos})

class ProductoAPIView(APIView):
    def get(self, request):
        productos = Producto.objects.all()
        serializer = ProductoSerializer(productos, many=True)
        return Response(serializer.data)