from django.db import models

# Create your models here.
class Info(models.Model):
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)

    def __str__(self):
        return self.email