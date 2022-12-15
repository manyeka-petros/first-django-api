from django.db import models

# Create your models here. 


class Teachers(models.Model):
    Teac_name = models.CharField( max_length=50)
    email = models.CharField( max_length=50)
    password = models.CharField( max_length=50)
    age = models.IntegerField()
    salary = models.FloatField()
    phone_numb = models.CharField( max_length=50)
