from django.db import models

# Create your models here.
class Employees(models.Model):
    username = models.CharField(max_length=200, null=True)
    name = models.CharField(max_length=200, null=True)
    category = models.CharField(max_length=200, default="Useful")
    url = models.CharField(max_length=200, null=True)
    description = models.CharField(max_length=200, null=True)


    def __str__(self):
        return self.name
