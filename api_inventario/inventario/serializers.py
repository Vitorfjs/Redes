from rest_framework import serializers
from .models import InventoryItem, Supplier

class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = '__all__'

class InventoryItemSerializer(serializers.ModelSerializer):
    # Representação do fornecedor
    supplier_info = SupplierSerializer(read_only=True)
    # Criação/atualização do fornecedor por ID
    supplier = serializers.PrimaryKeyRelatedField(
        queryset=Supplier.objects.all(), write_only=True, source='supplier_info'
    )

    class Meta:
        model = InventoryItem
        fields = '__all__'
