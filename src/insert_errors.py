import mongo2

c, db = mongo2.connect_mongo2(); # Connexion à la base de données

# On essaye de réinsérer des données corrompues après les avoir corrigées manuellement

e_genres_films = db.erreurs.find({"type": "genres_films"});
for e in e_genres_films:
  db.genres_films.insert_one(e["element"]);
  db.erreurs.delete_one({"_id": e["_id"]});

e_personnes = db.erreurs.find({"type": "personnes"});
for e in e_personnes:
  db.personnes.insert_one(e["element"]);
  db.erreurs.delete_one({"_id": e["_id"]});

e_films = db.erreurs.find({"type": "films"});
for e in e_films:
  db.films.insert_one(e["element"]);
  db.erreurs.delete_one({"_id": e["_id"]});

e_avis = db.erreurs.find({"type": "avis"});
for e in e_avis:
  db.avis.insert_one(e["element"]);
  db.erreurs.delete_one({"_id": e["_id"]});

e_villes = db.erreurs.find({"type": "villes"});
for e in e_villes:
  db.villes.insert_one(e["element"]);
  db.erreurs.delete_one({"_id": e["_id"]});

e_cinemas = db.erreurs.find({"type": "cinemas"});
for e in e_cinemas:
  db.cinemas.insert_one(e["element"]);
  db.erreurs.delete_one({"_id": e["_id"]});
