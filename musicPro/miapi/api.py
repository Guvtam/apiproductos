from rest_framework import viewsets
from .models import Producto
from .serializers import ProductoSerializer
#from .permissions import IsAdminOrReadOnly

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    #permission_classes = [IsAdminOrReadOnly]




    