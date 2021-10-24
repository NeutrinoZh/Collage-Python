# 8 (0,5)

class Playlist:

    class Track:
        def __init__(self, title, artist, album, duration):
            self.title = title
            self.artist = artist
            self.album = album
            self.duration = duration

    tracks = {}

    def add(self, track):
        self.tracks[track.title] = track
        return self
    
    def remove(self, title):
        del self.tracks[title]
        return self

    def size(self):
        return len(self.tracks)
    
    def clear(self):
        self.clear()

    def duration(self):
        result = 0
        for track in self.tracks.values():
            result += int(track.duration)
        return result
    
    def __str__(self):
        result = f'Playlist({self.duration()}s):\n'
        for track in self.tracks.values():
            result += f'"{track.title}" ({track.artist}) {track.duration}s\n'
        return result

playlist = Playlist()

playlist.add(Playlist.Track('Fly Away', 'TheFatRat, Anjulie', 'Single', '248'))
playlist.add(Playlist.Track('Chroline', 'Twenty One Pilots', 'Trench', '324'))
playlist.add(Playlist.Track('Rise Up', 'TheFatRat', 'Single', '209'))

print(playlist)
playlist.remove('Chroline')
print(playlist)