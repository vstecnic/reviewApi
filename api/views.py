from rest_framework import viewsets
from .models import Entrada
from .serializer import EntradaSerializer

# Create your views here.
class EntradaViewSet(viewsets.ModelViewSet):
    queryset = Entrada.objects.all()
    serializer_class = EntradaSerializer
