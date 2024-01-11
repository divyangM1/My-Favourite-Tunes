from django.urls import path
from .views import *


# Link url paths to views

urlpatterns = [
    path('', list_of_songs, name="list_of_songs"),
    path('songs/<int:song_id>/', song_details, name='song_details'),
    path('add-songs/',add_songs , name="add_songs"),
    path('artist-songs/', artist_song_count, name="artist_song_count")
]
