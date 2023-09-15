from django.db import models
from django.conf import settings


class UserProduct(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="products")
    product = models.ForeignKey("inventory.product", on_delete=models.CASCADE, related_name="users")
    start_date = models.DateField("Start date", auto_now=False)
    end_date = models.DateField("End date", auto_now=False)  

    class Meta:
        verbose_name = "User product"
        verbose_name_plural = "User products"
        ordering = ["user"]
    
    def __str__(self) -> str:
        return f"{self.user} - {self.product} ({self.start_date})"    
    