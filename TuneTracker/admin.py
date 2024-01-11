from django.contrib import admin
from .models import Artist, Song


# Registering Artist and Song models to admin

admin.site.register(Artist)
admin.site.register(Song)
