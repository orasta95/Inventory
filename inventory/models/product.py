from django.db import models


class Product(models.Model):

    class ProductStatus(models.TextChoices):
        WAREHOUSE = 'warehouse'
        WORKER = 'worker'
        SOLD = 'sold'
        THROWN = 'thrown'

    name = models.CharField("Name", max_length=50)
    date = models.DateField("Buy date", auto_now=False)
    photo = models.ImageField("Photo", upload_to=None, height_field=None, width_field=None, max_length=None)
    cost = models.FloatField("Cost")
    store = models.CharField("Store", max_length=50)
    made_company = models.CharField("Made company", max_length=50)
    inventory_number = models.CharField("Inventory number", max_length=50)
    status = models.CharField(
        max_length=15, choices=ProductStatus.choices, default=ProductStatus.WAREHOUSE)

    category = models.ForeignKey(
        'inventory.category', on_delete=models.CASCADE, related_name="products")
    company = models.ForeignKey(
        'inventory.company', on_delete=models.CASCADE, related_name="products")

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"
        ordering = ['name', 'inventory_number']

    def __str__(self) -> str:
        return self.name
