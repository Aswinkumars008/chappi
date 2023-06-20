from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    content = models.TextField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name
    



class Product(models.Model):
    img = models.ImageField( upload_to='', height_field=None, width_field=None, blank=True)
    P_name = models.CharField(max_length=200,unique=True)
    price = models.IntegerField()
    CATEGORY_CHOICES = (
        ('snack', 'Snack'),
        ('hot_drink', 'Hot Drink'),
        ('cold_drink', 'Cold Drink'),
    )
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    def __str__(self):
        return self.P_name