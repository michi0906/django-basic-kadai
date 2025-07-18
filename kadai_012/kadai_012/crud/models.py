from django.db import models
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    img = models.ImageField(blank=True, default='noImage.png')
    description = models.TextField(blank=True, null=True)



    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('list')

