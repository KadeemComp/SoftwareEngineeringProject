from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.


class Country(models.Model):
    name = models.CharField(max_length=64)
    flag = models.ImageField(default = 'default_flag_image.jpg', upload_to='flag_image')

    def __str__(self):
        return self.name



class Fruit(models.Model):
    fruit_name = models.CharField(max_length=64)
    image = models.ImageField(default = 'default.jpg', upload_to='fruit_image')
    #country = models.ForeignKey(Country,blank=True, on_delete=models.CASCADE, related_name= "country")
    content = models.TextField()
    date_posted = models.DateTimeField(default= timezone.now) 
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.fruit_name

    def get_absolute_url(self):
        return reverse('fruit-detail', kwargs= {'pk': self.pk})


class LocalName(models.Model):
    fruit = models.ForeignKey(Fruit, related_name= 'local_name',on_delete=models.CASCADE)
    country_name = models.CharField(max_length=64)
    country_origin = models.ForeignKey(Country,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.localname