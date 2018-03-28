import os
from collections import namedtuple
# from vlc import MediaPlayer

class Song(object):
	
	def __init__(self, title=None, artist=None, album=None, file=None):
		self.title = title
		self.artist = artist
		self.album = album
		self.file = file

	def __repr__(self):
		return {'track':self.title, 'artist':self.artist, 'album':self.album, 'file':self.file}

	def __str__(self):
		return str(self.__repr__())

	def play(self):
		# if self.file != None:
		# 	# player = MediaPlayer(self.file)
		# 	# player.play()
		# else:
			print(self.__str__() + ' file not found')


class SongLibrary(object):

	def __init__(self):
		self.tracks = []
		self.artists = set()
		self.albums = set()

	def add(self, song):
		self.tracks.append(song)
		self.artists.add(song['artist'])
		self.albums.add(song['album'])

	def play(self, track):
		for i in range(len(self.tracks)):
			if self.library[i]['track'] == track:
				self.library[i].play()


if __name__ == '__main__':
	music_dir = os.path.join(os.getcwd(), 'songs')
	my_library = SongLibrary()
	for file in os.listdir(music_dir):
		if file.endswith('.mp3'):
			song = Song(file=os.path.join(music_dir, file))
			song.play()
