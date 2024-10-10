from sqlite3 import *

connexion = connect("database/sqlite.db")
request = connexion.cursor()



def album_from_artist(artiste):
    """
    Description: Permet d'obtenir une liste de tuple sous la forme (Artiste, Album) pour un artiste donné en paramètre
    """
    request.execute(f"SELECT nomArtiste, nomAlbum from Artiste NATURAL JOIN Album WHERE nomArtiste == '{artiste}'")
    listeAlbums = []
    for album in request:
        if album not in listeAlbums:
            listeAlbums.append(album)
    return listeAlbums


def album_style():
    """
    Description: Permet d'obtenir la liste de tuples sous la forme (nomAlbum, style) de facon ordonnée
    """
    return [album for album in request.execute("SELECT nomAlbum, style from Album ORDER BY nomAlbum")]


def album_from_style(style):
    """
    Description: Permet d'obtenir une liste de tuples sous la forme (Artiste, Album) pour un style donné en paramètre
    """
    return [album for album in
            request.execute(f"SELECT nomArtiste, nomAlbum from Artiste NATURAL JOIN Album WHERE style = '{style}'")]


def album_from_song(song):
    """
    Description: Permet d'obtenir un Album pour un morceau donné en paramètre
    
    """
    return (album for album in
            request.execute(f"SELECT nomAlbum from Album INNER JOIN Morceau ON Album.nomMorceau = Morceau.nomMorceau WHERE nomMorceau = '{song}'"))


def update_artists(listeArtiste):
    """
    Permet de mettre a jour une liste d'albums donnée en paramètres par rapport a la base de donnée
    """
    request.execute('SELECT * from Artiste')
    for artiste in request:
        if artiste not in listeArtiste:
            listeArtiste[artiste[0]] = artiste[1:]
    return listeArtiste


def update_albums(listeAlbum):
    """
    Description: Permet de mettre a jour une liste d'albums en paramètres par rapport a la base de donnée
    
    """
    request.execute('SELECT * from Album')
    for album in request:
        if album not in listeAlbum:
            listeAlbum[album[0]] = album[1:]
    return listeAlbum


def update_songs(listeMorceau):
    """
    Description: Permet de mettre a jour une liste de Morceaux passée en paramètre par rapport a la base de donnée
    Exemple: update_songs(SongsList)
    """
    request.execute('SELECT * from Morceau')
    for morceau in request:
        if morceau not in listeMorceau:
            listeMorceau[morceau[0]] = morceau[1:]
    return listeMorceau

def add_album():
    """
    Descripton: Permet d'ajouter un album a la base de donnée avec les inputs réalisés par la fonction
    """
    nomAlbum = str(input("Nom de l'album: "))
    date_sortie = str(input("Date de sortie: "))
    nb_morceau = input("Nombre de morceaux: ")
    certif = str(input("Certification: "))
    style = str(input("Style: "))
    nomArtiste= str(input("Nom artiste: "))
    langue = str(input("Langue: "))
    request.execute(f"INSERT INTO Album(nomAlbum, date_sortie, nb_morceau, certif, style, nomArtiste, langue) VALUES('{nomAlbum}','{date_sortie}', {nb_morceau}, '{certif}', '{style}', '{nomArtiste}', '{langue}');")
    request.execute(f"SELECT nomAlbum, date_sortie, nb_morceau, certif, style, nomArtiste, langue FROM Album WHERE nomAlbum = '{nomAlbum}';")
    for album in request:
        print(album)
    print('Album ajouté !')

def delete_album():
    """
    Description: Permet de supprimer une album de la base de donnée par rapport a un ID donnée par un input
    """
    albumID = int(input("ID de l'album a supprimer: "))
    request.execute(f'DELETE FROM Album WHERE idAlbum = {albumID};')
    print('Album supprimé !')


def artiste_from_song(artiste1):
    nomMorcrau = str(input('Nom du morceau: '))
    request.execute(f"SELECT nomArtiste FROM Artiste NATURAL JOIN COMPOSE NATURAL JOIN Morceau WHERE nomMorceau = '{nomMorcrau};'")
    for artiste in request:
        print(artiste)
    print(artiste1)
    
Albums = {}
Albums = update_albums(Albums)

Artistes = {}
Artistes = update_artists(Artistes)

Morceaux = {}
Morceaux = update_songs(Morceaux)

print(Albums)
print(Artistes)
print(Morceaux)
