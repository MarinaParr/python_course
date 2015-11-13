# -*- coding: utf-8 -*-
class Song:

    def __init__(self, name, artist, album, position, year, sec):
        self.name = name
        self.artist = artist
        self.album_name = album
        self.position_in_album = str(position)
        self.year = str(year)
        self.length_in_sec = str(sec)

    def __repr__(self):
        song = "%s\t%s\t%s\t%s\t%s\t%s\t" % (self.name, self.artist, self.album, self.position, self.year, self.sec)
        return song

    def __lt__(self, other):
        if self.artist < other.artist:
            return True
        if self.artist == other.artist and self.name < other.name:
            return True
        return False


def import_songs(file_name):
    with open("file_name", "r", encoding='utf-8') as f:
        songs = list()
        lines = f.read().split('\n')
        for line in lines:
            words = line.split('\t')
            songs.append(words)
        return(songs)


def export_songs(songs, file_names):
    with open("export", "w") as exp:
        for song in songs:
            answ = song.name + '\t' + song.artist + '\t' + song.album + '\t' + song.position + '\t' + song.year + '\t' + song.sec
            exp.write(answ)

