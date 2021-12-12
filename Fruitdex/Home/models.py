from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.


class Country(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    flag = models.ImageField(default = 'default.jpg', upload_to='flag_image')
    
    def __str__(self):
        return self.name
        

class Fruit(models.Model):
    fruit_name = models.CharField(max_length=100)
    image = models.ImageField(default = 'default.jpg', upload_to='fruit_image')
    country = models.ManyToManyField(Country)
    content = models.TextField()
    date_posted = models.DateTimeField(default= timezone.now) 
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.fruit_name

    def get_absolute_url(self):
        return reverse('fruit-detail', kwargs= {'pk': self.pk})

