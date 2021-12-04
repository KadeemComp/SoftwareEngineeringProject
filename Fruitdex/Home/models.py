from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Fruits(models.Model):
    fruit_name = models.CharField(max_length=100)
    #image = models.ImageField(default = 'default.jpg', upload_to='fruit_image')
    content = models.TextField()
    date_posted = models.DateTimeField(default= timezone.now) 
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.fruit_name