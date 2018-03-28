import os, random
from collections import namedtuple
# from vlc import MediaPlayer

class Song(object):
    
    def __init__(self, title=None, artist=None, album=None, file=None):
        self.title = title
        self.artist = artist
        self.album = album
        self.file = file

    def __repr__(self):
        return str({'track':self.title, 'artist':self.artist, 'album':self.album, 'file':self.file})

    def play(self):
        # if self.file != None:
        #   player = MediaPlayer(self.file)
        #   player.play()
        # else:
        #   print(self.__str__() + ' file not found')
        print('play doesn\'t work')


class SongLibrary(object):

    def __init__(self):
        self.tracks = []
        self.artists = set()
        self.albums = set()

    def __len__(self):
        return len(self.tracks)     

    def __getitem__(self, position):
        return self.tracks[position]

    def __repr__(self):
        return str(self.tracks)

    def add(self, song):
        self.tracks.append(song)
        self.artists.add(song.artist)
        self.albums.add(song.album)

    def play(self, track):
        for song in self.tracks:
            if song.track == track:
                song.play()

    def shuffle(self):
        random.shuffle(self.tracks)


if __name__ == '__main__':
    music_dir = os.path.join(os.getcwd(), 'songs')
    my_library = SongLibrary()
    # for file in os.listdir(music_dir):
    #   if file.endswith('.mp3'):
    #       song = Song(file=os.path.join(music_dir, file))
    #       print(song)
    #       song.play()
    my_library.add(Song("Don't stop believing", 'Journey', 'Dads love this'))
    my_library.add(Song("Drop it like it's hot", 'Snoop Dogg', 'Dogs love this'))
    my_library.add(Song("Thunder", 'Imagine Dragons', 'Dads love this'))
    my_library.add(Song("Text", 'Text', 'Text'))
    my_library.add(Song("Let me love you", 'JBieb', 'Dads hate this'))
    print(my_library)
    my_library.shuffle()
    print(my_library)
    print(len(my_library))
    my_library.shuffle()
    print(my_library[-1])
    print(my_library.albums)
