from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Player(models.Model):
    user = models.OneToOneField(User)
    friends = models.ManyToManyField("self")

class Plant_Type(models.Model):
    name = models.CharField(max_length=100)
    image = models.OneToOneField(Plant_Image_Zip_File)

class Plant_Image_Zip_File(models.Model):
    image_base = models.CharField(max_length=100)
    file = models.FileField(storage=fs)

    #def save(self, *args, **kwargs):
        #if not self.id:
        #super(File, self).save(*args, **kwargs)
