import mongo2, re

c, db = mongo2.connect_mongo2(); # Connexion à la base de données

def retrait(e_type, e_raison, e_element):
  print("Retrait de ", e_type, " pour : ", e_raison, " : ", e_element);
  db.erreurs.insert_one({"type": e_type, "raison": e_raison, "element": e_element});
  db[e_type].delete_one({"_id": e_element["_id"]});
  return 1;

# On essaye de détecter des erreurs dans les données
# Pour cela, on vérifie les champs de chaque collection (contenu, type et reférences)

t_genres_films = db.genres_films.find();
for t in t_genres_films:
  # Types
  if not isinstance(t["genre"], str):
    retrait("genres", "genre: type incorrect", t);
    continue;
  # Contenu
  if not t["genre"]:
    retrait("genres", "genre: vide", t);
    continue;
  # Références

t_personnes = db.personnes.find();
for t in t_personnes:
  # Types
  if not isinstance(t["nom"], str):
    retrait("personnes", "nom: type incorrect", t);
    continue;
  if not isinstance(t["prenom"], str):
    retrait("personnes", "prenom: type incorrect", t);
    continue;
  # Contenu
  if not t["nom"]:
    retrait("personnes", "nom: vide", t);
    continue;
  if not t["prenom"]:
    retrait("personnes", "prenom: vide", t);
    continue;
  # Références

t_films = db.films.find();
for t in t_films:
  ret = 0;
  # Types
  if not isinstance(t["titre"], str):
    retrait("films", "titre: type incorrect", t);
    continue;
  if not isinstance(t["duree"], int):
    retrait("films", "duree: type incorrect", t);
    continue;
  if not isinstance(t["date_sortie"], str):
    retrait("films", "date_sortie: type incorrect", t);
    continue;
  if not isinstance(t["synopsis"], str):
    retrait("films", "synopsis: type incorrect", t);
    continue;
  if not isinstance(t["realisateurs"], list):
    retrait("films", "realisateurs: type incorrect", t);
    continue;
  if not isinstance(t["acteurs"], list):
    retrait("films", "acteurs: type incorrect", t);
    continue;
  if not isinstance(t["genres"], list):
    retrait("films", "genres: type incorrect", t);
    continue;
  # Contenu
  if not t["titre"]:
    retrait("films", "titre: vide", t);
    continue;
  if t["duree"] <= 0:
    retrait("films", "duree: valeur négative ou nulle", t);
    continue;
  if not t["date_sortie"]:
    retrait("films", "date_sortie: vide", t);
    continue;
  if not re.match(r"^\d{4}-\d{2}-\d{2} \d{2}:\d{2}$", t["date_sortie"]):
    retrait("films", "date_sortie: format incorrect", t);
    continue;
  if not t["synopsis"]:
    retrait("films", "synopsis: vide", t);
    continue;
  if not t["realisateurs"]:
    retrait("films", "realisateurs: vide", t);
    continue;
  # Références
  for r in t["realisateurs"]:
    if not db.personnes.find_one({"_id": r}):
      ret = retrait("films", "realisateurs: référence réalisateurs " + r + " inexistante", t);
      break;
  if re:
    continue;
  for a in t["acteurs"]:
    if not db.personnes.find_one({"_id": a}):
      ret = retrait("films", "acteurs: référence acteurs " + a + " inexistante", t);
      break;
  if re:
    continue;
  for g in t["genres"]:
    if not db.genres_films.find_one({"_id": g}):
      retrait("films", "genres: référence genres " + g + " inexistante", t);
      break;

e_avis = db.avis.find();
for e in e_avis:
  # Types
  if not isinstance(e["note"], int):
    retrait("avis", "note: type incorrect", e);
    continue;
  if not isinstance(e["commentaire"], str):
    retrait("avis", "commentaire: type incorrect", e);
    continue;
  if not isinstance(e["source"], str):
    retrait("avis", "source: type incorrect", e);
    continue;
  if not isinstance(e["auteur"], str):
    retrait("avis", "auteur: type incorrect", e);
    continue;
  # Contenu
  if e["note"] == -1 and not e["commentaire"]:
    retrait("avis", "note ou commentaire: vide", e);
    continue;
  if e["note"] < -1 or e["note"] > 5:
    retrait("avis", "note: valeur incorrecte", e);
    continue;
  if not e["source"]:
    retrait("avis", "source: vide", e);
    continue;
  if not e["auteur"]:
    retrait("avis", "auteur: vide", e);
    continue;
  # Références
  if not db.films.find_one({"_id": e["film"]}):
    retrait("avis", "film: référence film inexistante", e);
    continue;

t_villes = db.villes.find();
for t in t_villes:
  # Types
  if not isinstance(t["nom_ville"], str):
    retrait("villes", "nom_ville: type incorrect", t);
    continue;
  # Contenu
  if not t["nom_ville"]:
    retrait("villes", "nom_ville: vide", t);
    continue;
  # Références

t_cinemas = db.cinemas.find();
for t in t_cinemas:
  ret = 0;
  # Types
  if not isinstance(t["nom"], str):
    retrait("cinemas", "nom: type incorrect", t);
    continue;
  if not isinstance(t["adresse"], str):
    retrait("cinemas", "adresse: type incorrect", t);
    continue;
  if not isinstance(t["salles"], list):
    retrait("cinemas", "salles: type incorrect", t);
    continue;
  # Contenu
  if not t["nom"]:
    retrait("cinemas", "nom: vide", t);
    continue;
  if not t["adresse"]:
    retrait("cinemas", "adresse: vide", t);
    continue;
  # Références
  if not db.villes.find_one({"_id": t["ville"]}):
    retrait("cinemas", "ville: référence ville inexistante", t);
    continue;
  # Sous-éléments
  for s in t["salles"]:
    # Types
    if not isinstance(s["nom"], str):
      ret = retrait("cinemas", "salles.nom: type incorrect", t);
      break;
    if not isinstance(s["nombre_places"], int):
      ret = retrait("cinemas", "salles.nombre_places: type incorrect", t);
      break;
    if not isinstance(s["films_diffuses"], list):
      ret = retrait("cinemas", "salles.films_diffuses: type incorrect", t);
      break;
    # Contenu
    if not s["nom"]:
      ret = retrait("cinemas", "salles.nom: vide", t);
      break;
    if s["nombre_places"] < 0:
      ret = retrait("cinemas", "salles.nombre_places: valeur négative", t);
      break;
    # Références
    # Sous-éléments
    for f in s["films_diffuses"]:
      # Types
      if not isinstance(f["date_diffusion"], str):
        ret = retrait("cinemas", "salles.films_diffuses.date_diffusion: type incorrect", t);
        break;
      if not isinstance(f["nombre_entrees"], int):
        ret = retrait("cinemas", "salles.films_diffuses.nombre_entrees: type incorrect", t);
        break;
      # Contenu
      if not f["date_diffusion"]:
        ret = retrait("cinemas", "salles.films_diffuses.date_diffusion: vide", t);
        break;
      if not re.match(r"^\d{4}-\d{2}-\d{2} \d{2}:\d{2}$", f["date_diffusion"]):
        ret = retrait("cinemas", "salles.films_diffuses.date_diffusion: format incorrect", t);
        break;
      if f["nombre_entrees"] < 0:
        ret = retrait("cinemas", "salles.films_diffuses.nombre_entrees: valeur négative", t);
        break;
      if f["nombre_entrees"] > s["nombre_places"]:
        ret = retrait("cinemas", "salles.films_diffuses.nombre_entrees: valeur supérieure au nombre de places", t);
        break;
      # Références
      if not db.films.find_one({"_id": f["film"]}):
        ret = retrait("cinemas", "salles.films_diffuses.film: référence film inexistante", t);
        break;
    if re:
      break;
  if re:
    continue;

print("Détection des erreurs terminée");
