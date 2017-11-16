from date import datetime


class Song:
  
  def __init__(self, name, artist, date_of_release, genre):
    self.name = name
    self.artist = artist
    self.date_of_release = date_of_release
    self.genre = genre
  

class Artist:

  def __init__(self, name):
    self.name = name
    self.albums = []

  def add_album(self, album):
    self.albums.append(album)


class Album:

  def __init__(self, name, date_of_release, owner):
    self.name = name
    self.songs = []
    self.date_of_release = date_of_release
    self.owner = owner
    self.featured_artists = []

  def add_song(self, song):
    self.songs.append(song)

  def add_featured_artist(self, artist):
    self.add_featured_artist.append(artist)


class Playlist:
  
  def __init__(self, name, various_artists):
    self.name = name
    self.songs = []
    self.various_artists = various_artists

  def add_song(self, song):
    self.songs.append(song)  

  def add_songs_from_album(self, album):
    for song in album.songs:
      self.add_song(song)  


if __name__ == '__main__':
  artist = Artist('Vlad')
  album = Album('Glory', datetime.date('2016', '08', '19'), artist)
  oshey = Song('oshey', artist, datetime.date('2016', '08', '19'), 'vibes')
  brighton = Song('brighton', artist, datetime.date('2016', '08', '19'), 'sealife')
  album.add_song(oshey)
  album.add_song(brighton)
  playlist = Playlist('Train vibes', artist)
  playlist.add_songs_from_album(album)



        
