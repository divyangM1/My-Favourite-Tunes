from django.shortcuts import render
from .models import *
import math
from django.db.models import Count

# for page number at the end of the page and limited data according to page.
from django.core.paginator import Paginator
from django.db.models import Q




# View to display details of specific song when clicked.
def song_details(request, song_id):
    song = Song.objects.get(id=song_id)
    print(1234)
    return render(request, "song_details.html", {'song':song})



# View to display list of all songs
def list_of_songs(request):

    if request.GET.get('optionFilter'):
        optionFilter = request.GET.get('optionFilter')

    queryset = Song.objects.all()
    search = ''

    # Search feature logic
    if request.GET.get('search'):
        search = request.GET.get('search')
        lookup = {f"{optionFilter}__startswith": search}
        query = Q(**lookup)
        queryset = queryset.filter(query)  



    paginator = Paginator(queryset, 12)  # Show 15 songs per page.
    a = math.ceil(len(queryset)/12)
    page_number = request.GET.get("page",1)
    page_obj = paginator.get_page(page_number)  


    return render(request, "song_list.html", {'queryset' : page_obj, "range": range(a), "search" : search})



# View to take input from webpage to add songs to the catalogue
def add_songs(request):

    if request.method == "POST":
        data = request.POST
        title = data.get('title')
        artist_name = data.get('artist')

        # Check if the artist already exists
        artist, artist_created = Artist.objects.get_or_create(name=artist_name)

        # Check if the song with the given title and artist already exists
        song, song_created = Song.objects.get_or_create(title=title, artist=artist)

        if artist_created or song_created:
            
            message = "Song added Successfully!"
        else:
            # Both artist and song already exist
            message = "Song already exist."
        
        return render(request, "add_songs.html",{"message" : message})

    return render(request, "add_songs.html")



# View to display Artists and their corresponding no. of songs.
def artist_song_count(request):
    artist_counts = Artist.objects.annotate(song_count=Count('songs'))

    search = ''

    # Search feature logic
    if request.GET.get('search'):
        search = request.GET.get('search')
        lookup = {"name__startswith": search}
        query = Q(**lookup)
        artist_counts = artist_counts.filter(query)  





    paginator = Paginator(artist_counts, 12)  # Show 12 artists per page.
    a = math.ceil(len(artist_counts)/12)
    page_number = request.GET.get("page",1)
    page_obj = paginator.get_page(page_number)  

    return render(request,'artist-song-count.html',{"queryset":page_obj, "range": range(a)})