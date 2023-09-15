from django.db import models


class Amortization(models.Model):   
    
    product = models.ForeignKey('inventory.product', on_delete=models.CASCADE, related_name='amortization')
    expire_year = models.DateField("Expire year", auto_now=False)
    
    class Meta:
        verbose_name = "Amortization"
        verbose_name_plural = "Amortizations"
        ordering = ['product']
        
    def __str__(self) -> str:
        return self.product