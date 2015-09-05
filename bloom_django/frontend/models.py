from django.db import models

# Create your models here.
class User_Plant(models.Model):
    name = models.CharField(max_length=100)
    last_press = models.DateField(auto_now=False, auto_now_add=True)
    created_date = models.DateField(auto_now=False, auto_now_add=True)
    type = models.ForeignKey(Plant_Type)
    owner = models.ForeignKey(Player)