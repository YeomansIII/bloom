from django.contrib import admin
from frontend.models import Player, PlantType, UserPlant, PlantImageZipFile

class UserPlantInline(admin.TabularInline):
    model = UserPlant

class PlayerAdmin(admin.ModelAdmin):
    inlines = [
        UserPlantInline,
    ]


# Register your models here.
admin.site.register(Player, PlayerAdmin)
admin.site.register(UserPlant)
admin.site.register(PlantType)
admin.site.register(PlantImageZipFile)
