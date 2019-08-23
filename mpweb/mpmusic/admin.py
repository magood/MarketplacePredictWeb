from django.contrib import admin

from .models import Music, Target, Prediction

admin.site.register(Music)
admin.site.register(Target)
admin.site.register(Prediction)