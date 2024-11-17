from rest_framework import viewsets
from .models import InventoryItem, Supplier
from .serializers import InventoryItemSerializer, SupplierSerializer
from rest_framework.response import Response
from rest_framework import status
class InventoryItemViewSet(viewsets.ModelViewSet):
    queryset = InventoryItem.objects.all()
    serializer_class = InventoryItemSerializer
class SupplierViewSet(viewsets.ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
