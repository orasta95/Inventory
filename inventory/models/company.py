from django.db import models


class Company(models.Model):
    name = models.CharField("Company name", max_length=50)
    
    
    class Meta:
        verbose_name = "Company"
        verbose_name_plural = "Companies"
        ordering = ['name']
        
    def __str__(self) -> str:
        return self.name