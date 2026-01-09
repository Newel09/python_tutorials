from django.db import models

class Product(models.Model):
    id = models.IntegerField(primary_key=True)

    # Basic data types
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True, null=True)
    stock = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)

    #dates
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    #choices
    CATEGORY_CHOICES = [
        ('ELEC', 'Electronics'),
        ('CLO', 'Clothing'),
        ('FD', 'Food'),
        ('OT', 'Other'),
    ]
    category = models.CharField(max_length=4, choices=CATEGORY_CHOICES, default='OT')


    def __str__(self):
        return f"{self.name} - {self.price}"
    
    class Meta:
        ordering = ['-created']
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
# Create your models here.
