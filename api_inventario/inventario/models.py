from django.db import models
class Supplier(models.Model):
    
    supplier_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    contact = models.CharField(max_length=255)
    def __str__(self):
        return self.name
class InventoryItem(models.Model):
    product_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity_in_stock = models.IntegerField()
    reorder_threshold = models.IntegerField()
    last_restock_date = models.DateField()
    supplier_info = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

