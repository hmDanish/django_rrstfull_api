from django.db import models

# Create your models here.

class Books(models.Model):
    title = models.CharField(max_length=100)
    auther = models.CharField(max_length=50)


    def __str__(self):
        return self.title