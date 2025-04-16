from django.db import models

class Profile(models.Model):
    user = models.OneToOneField('User', on_delete=models.CASCADE)  # Один к одному
    bio = models.TextField()

class User(models.Model):
    name = models.CharField(max_length=100)
    friends = models.ManyToManyField('self', blank=True)  # Многие ко многим

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    seller = models.ForeignKey(User, on_delete=models.CASCADE)  # Один ко многим (многие к одному)
