from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.
class Player(models.Model):
    user = models.OneToOneField(User)
    friends = models.ManyToManyField("self", blank=True)

    def __unicode__(self):
        return self.user.username

class PlantImageZipFile(models.Model):
    image_base = models.CharField(max_length=100)
    file = models.FileField(upload_to="plant_zips/")

    def __unicode__(self):
        return self.image_base

class PlantType(models.Model):
    name = models.CharField(max_length=100)
    sample_image = models.ImageField(upload_to="plant_type_samples/")
    piece_image = models.ImageField(upload_to="plant_type_pieces/")
    imagezip = models.OneToOneField(PlantImageZipFile)

    def __unicode__(self):
        return self.name

class PressDate(models.Model):
    press_date = models.DateField(auto_now=False, auto_now_add=True)

    def __unicode__(self):
        return self.press_date

class Timeline(models.Model):
    plant_name = models.CharField(max_length=100, null=True)
    press_date = models.ManyToManyField(PressDate)

    def __unicode__(self):
        return self.plant_name or ''

class Background(models.Model):
    background_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="backgrounds/")
    promo_image = models.ImageField(upload_to="promo_images/")

    def __unicode__(self):
        return self.background_name

class UserPlant(models.Model):
    name = models.CharField(max_length=100)
    last_press = models.DateField(auto_now=False, auto_now_add=True)
    created_date = models.DateField(auto_now=False, auto_now_add=True)
    type = models.ForeignKey(PlantType)
    owner = models.ForeignKey(Player)
    timeline = models.OneToOneField(Timeline)
    background = models.ForeignKey(Background)

    def save(self, *args, **kwargs):
        cur_date = datetime.datetime.today()
        if not self.id:
            pressdatenow = PressDate()
            pressdatenow.save()
            new_timeline = Timeline(plant_name=self.name)
            new_timeline.save()
            new_timeline.press_date.add(pressdatenow)
            new_timeline.save()
            self.timeline = new_timeline
        self.last_press = cur_date
        super(UserPlant, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name
