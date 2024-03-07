import mongo2

c, db = mongo2.connect_mongo2();

# Compter le nombre d'éléments dans chaque collection
print("Compter le nombre d'éléments dans chaque collection");
gfc = db.genres_films.count();
pc = db.personnes.count();
fc = db.films.count();
ac = db.avis.count();
vc = db.villes.count();
cc = db.cinemas.count();
print("genres_films: ", gfc);
print("personnes: ", pc);
print("films: ", fc);
print("avis: ", ac);
print("villes: ", vc);
print("cinemas: ", cc);

print("####################################################################################################");
print("####################################################################################################");

# Tous les avis d'un film
print("Tous les avis d'un film (Interstellar)");
f_interstellar = db.films.find_one({"titre": "Interstellar"});
liste_avis_interstellar = db.avis.find({"film": f_interstellar["_id"]});
for avis in liste_avis_interstellar:
    print(avis);

print("####################################################################################################");
print("####################################################################################################");

# Tous les films d'un genre
print("Tous les films d'un genre (Science-fiction)");
g_sf = db.genres_films.find_one({"genre": "Sci-Fi"});
liste_films_sf = db.films.find({"genres": g_sf["_id"]});
for film in liste_films_sf:
    print(film);

print("####################################################################################################");
print("####################################################################################################");

# Note d'appréciation générale d'un film avec MapReduce
print("Note d'appréciation générale d'un film avec MapReduce");
map = "function() { emit(this.film, this.note); }";
reduce = "function(key, values) { return Array.avg(values); }";
note_g = db.avis.map_reduce(map, reduce, "note_g");
note_g_films = db.note_g.aggregate([
  { "$lookup": { "from": "films", "localField": "_id", "foreignField": "_id", "as": "film" } },
  { "$unwind": "$film" },
  { "$project": { "_id": 0, "film": "$film.titre", "value": "$value" } }
]);
for film in note_g_films:
    print(film);

print("####################################################################################################");
print("####################################################################################################");

# Les 10 films les plus diffusés
print("Les 10 films les plus diffusés");
mdf = db.cinemas.aggregate([
  { "$unwind": "$salles" },
  { "$unwind": "$salles.films_diffuses" },
  { "$group": { "_id": "$salles.films_diffuses.film", "count": { "$sum": 1 } } },
  { "$sort": { "count": -1 } },
  { "$limit": 10 },
  { "$lookup": { "from": "films", "localField": "_id", "foreignField": "_id", "as": "film" } },
  { "$unwind": "$film" },
  { "$project": { "_id": 0, "film": "$film.titre", "count": "$count" } }
]);
for film in mdf:
    print(film);

print("####################################################################################################");
print("####################################################################################################");

# Les noms des 10 cinémas diffusant le plus de films les mieux notés
print("Les noms des 10 cinémas diffusant le plus de films les mieux notés");
mpfc = db.cinemas.aggregate([
  { "$unwind": "$salles" },
  { "$unwind": "$salles.films_diffuses" },
  { "$lookup": { "from": "films", "localField": "salles.films_diffuses.film", "foreignField": "_id", "as": "film" } },
  { "$unwind": "$film" },
  { "$lookup": { "from": "note_g", "localField": "film._id", "foreignField": "_id", "as": "note" } },
  { "$unwind": "$note" },
  { "$match": { "note.value": { "$gte": 4 } } },
  { "$group": { "_id": "$_id", "count": { "$sum": 1 } } },
  { "$sort": { "count": -1 } },
  { "$limit": 10 },
  { "$lookup": { "from": "cinemas", "localField": "_id", "foreignField": "_id", "as": "cinema" } },
  { "$unwind": "$cinema" },
  { "$project": { "_id": 0, "cinema": "$cinema.nom", "count": "$count" } }
]);
for cinema in mpfc:
    print(cinema);
