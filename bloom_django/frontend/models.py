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
    image = models.OneToOneField(PlantImageZipFile)

    def __unicode__(self):
        return self.name

class PressDate(models.Model):
    press_date = models.DateField()

    def __unicode__(self):
        return self.press_date

class Timeline(models.Model):
    plant_name = models.CharField(max_length=100, null=True)
    press_date = models.ManyToManyField(PressDate)

    def __unicode__(self):
        return self.plant_name or ''


class UserPlant(models.Model):
    name = models.CharField(max_length=100)
    last_press = models.DateField(auto_now=False, auto_now_add=True)
    created_date = models.DateField(auto_now=False, auto_now_add=True)
    type = models.ForeignKey(PlantType)
    owner = models.ForeignKey(Player)
    timeline = models.OneToOneField(Timeline, null=True)

    def save(self, *args, **kwargs):
        cur_date = datetime.datetime.today()
        if not self.id:
            self.timeline.save()
        self.last_press = cur_date
        cur_press = PressDate()
        cur_press.press_date = cur_date
        cur_press.save()
        self.timeline.press_date.add(cur_press)
        super(UserPlant, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name