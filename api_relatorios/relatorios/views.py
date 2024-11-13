from rest_framework import generics
from .models import Relatorio
from .serializers import RelatorioSerializer

class RelatorioListCreate(generics.ListCreateAPIView):
    queryset = Relatorio.objects.all()
    serializer_class = RelatorioSerializer

