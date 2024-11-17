from rest_framework import serializers
from .models import InventoryItem, Supplier

class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = '__all__'

class InventoryItemSerializer(serializers.ModelSerializer):
    supplier_info = SupplierSerializer()

    class Meta:
        model = InventoryItem
        fields = '__all__'

    def create(self, validated_data):
        # Extrair dados do fornecedor
        supplier_data = validated_data.pop('supplier_info', None)

        # Criar o fornecedor, se os dados existirem
        if supplier_data:
            supplier = Supplier.objects.create(**supplier_data)
            validated_data['supplier'] = supplier

        # Criar o item de inventário
        return InventoryItem.objects.create(**validated_data)
