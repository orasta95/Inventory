from django.db import models


class Category(models.Model):
    name = models.CharField("Name", max_length=50)
    parent = models.ForeignKey("inventory.category", related_name='child', verbose_name="parent", on_delete=models.CASCADE, null= True, blank=True)
    
    
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        ordering = ['name']
        
    def __str__(self) -> str:
        return self.name