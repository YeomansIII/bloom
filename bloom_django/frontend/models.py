from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Player(models.Model):
    user = models.OneToOneField(User)
    friends = models.ManyToManyField("self", null=True, blank=True)

    def __unicode__(self):
        return self.user.username

class PlantImageZipFile(models.Model):
    image_base = models.CharField(max_length=100)
    file = models.FileField(upload_to="plant_zips/")

class PlantType(models.Model):
    name = models.CharField(max_length=100)
    image = models.OneToOneField(PlantImageZipFile)

class UserPlant(models.Model):
    name = models.CharField(max_length=100)
    last_press = models.DateField(auto_now=False, auto_now_add=True)
    created_date = models.DateField(auto_now=False, auto_now_add=True)
    type = models.ForeignKey(PlantType)
    owner = models.ForeignKey(Player)

    #def save(self, *args, **kwargs):
        #if not self.id:
        #super(File, self).save(*args, **kwargs)
