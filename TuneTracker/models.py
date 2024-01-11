from django.db import models



# Define Artist model with name field
class Artist(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# Define song model with title field and ManytoOne relationship with artist.
class Song(models.Model):
    title = models.CharField(max_length=100)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, null=True, related_name='songs', db_column='artist_id')

    def __str__(self):
        return f"{self.title} by {self.artist.name}"
