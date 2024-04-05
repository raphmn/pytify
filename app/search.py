from sqlite3 import *

connexion = connect("database/SpotifyDB.db")
requete = connexion.cursor()


def search_from_nationality(nationality):
    return requete.execute(f'SELECT nomArtiste FROM Artiste WHERE nationalite = {nationality}')

def search_from_style(style):
    return requete.execute(f'SELECT (nomArtiste, nomAlbum) from Artiste NATURAL JOIN Album WHERE style = {style}')

search_from_style('RAP')