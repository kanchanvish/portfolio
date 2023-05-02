from django.db import models



class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=20)
    message = models.TextField(blank=True, null=True)

# Create your models here.

class portfolio(models.Model):
    title = models.CharField(max_length=100)
    image_path1 = models.CharField(max_length=300)
    des = models.TextField(max_length=1000)
