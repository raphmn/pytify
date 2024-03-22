create table IF NOT EXISTS Artiste ( idArtiste int AUTOINCREMENT PRIMARY KEY, nomArstiste char, nom char, annee_naissance date, age int, nationalite char);
CREATE table if not EXISTS Album ( idAlbum int AUTOINCREMENT PRIMARY KEY, date_sortie date, nb_morceau int, certif bool, style char, nomArtiste char, FOREIGN KEY (nomArtiste) REFERENCES Artiste(nomArtiste));
CREATE TABLE if NOT EXISTS Compose ( idArtiste int, nomMorceau char, date_sortie_morceau date, FOREIGN KEY (idArtiste) REFERENCES Artiste(idArtiste), PRIMARY KEY (idArtiste,nomMorceau));
CREATE TABLE if NOT EXISTS Morceau ( idMorceau int AUTOINCREMENT PRIMARY KEY, nomMorceau char, idAlbum int, FOREIGN KEY (nomMorceau) REFERENCES Compose(nomMorceau), FOREIGN KEY (idAlbum) REFERENCES Album(idAlbum));