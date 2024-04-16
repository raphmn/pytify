from sqlite3 import *

connexion = connect("database/sqlite.db")
request = connexion.cursor()


def search_from_nationality(nationality):
    return [artiste for artiste in
            request.execute(f"SELECT nomArtiste from Artiste where nationalite = '{nationality}'")]


def album_from_artist(artiste):
    request.execute(f"SELECT nomArtiste, nomAlbum from Artiste NATURAL JOIN Album WHERE nomArtiste == '{artiste}'")
    listeAlbums = []
    for album in request:
        if album not in listeAlbums:
            listeAlbums.append(album)
    return listeAlbums


def album_style():
    return [album for album in request.execute("SELECT nomAlbum, style from Album")]


def album_from_style(style):
    return [album for album in
            request.execute(f"SELECT nomArtiste, nomAlbum from Artiste NATURAL JOIN Album WHERE style = '{style}'")]


def album_from_song(song):
    return (album for album in
            request.execute(f"SELECT nomAlbum from Album NATURAL JOIN Morceau WHERE nomMorceau = '{song}'"))


def update_artists(listeArtiste):
    request.execute('SELECT * from Artiste')
    for artiste in request:
        if artiste not in listeArtiste:
            listeArtiste[artiste[0]] = artiste[1:]
    return listeArtiste


def update_albums(listeAlbum):
    request.execute('SELECT * from Album')
    for album in request:
        if album not in listeAlbum:
            listeAlbum[album[0]] = album[1:]
    return listeAlbum


def update_songs(listeMorceau):
    request.execute('SELECT * from Morceau')
    for morceau in request:
        if morceau not in listeMorceau:
            listeMorceau[morceau[0]] = morceau[1:]
    return listeMorceau


Albums = {}
Albums = update_albums(Albums)

Artistes = {}
Artistes = update_artists(Artistes)

Morceaux = {}
Morceaux = update_songs(Morceaux)

print(Albums)
print(Artistes)
print(Morceaux)
