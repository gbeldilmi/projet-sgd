# Partie 2: Requêtage de la base de données MongoDB

## Requêtes simples

Les requêtes suivantes sont des exemples de requêtes que nous pourrions effectuer sur la base de données MongoDB.

### Compter le nombre d'éléments dans chaque collection

Après avoir importé les données dans la base de données, nous pourrons effectuer les requêtes suivantes pour compter le nombre d'éléments dans chaque collection:

```javascript
db.genres_films.count();
db.personnes.count();
db.films.count();
db.avis.count();
db.villes.count();
db.cinemas.count();
```

### Tous les avis d'un film

Pour obtenir tous les avis d'un film (dont une partie serait vue depuis la page de présentation du film en question), nous pourrions effectuer la requête suivante:

```javascript
f = db.films.findOne({titre: "Interstellar"});
liste_avis = db.avis.find({film: f["_id"]});
```

### Note d'appréciation générale d'un film avec MapReduce

Pour obtenir la note d'appréciation générale d'un film, nous pourrions utiliser la méthode `mapReduce` de MongoDB pour effectuer un calcul de moyenne des notes d'appréciation d'un film. Voici un exemple de requête pour obtenir la note d'appréciation générale de tous les films:

```javascript
db.note_g.drop();
var my_map = function() {
  emit(this.film, this.note);
}
var my_reduce = function(film_id, notes) {
  return Array.avg(notes);
}
db.avis.mapReduce(my_map, my_reduce, {out: "note_g"});
note_g_films = db.note_g.aggregate([
  { $lookup: { from: "films", localField: "_id", foreignField: "_id", as: "film" } },
  { $unwind: "$film" },
  { $project: { _id: 0, film: "$film.titre", value: "$value" } }
]);
```

### Les 10 films les plus diffusés

```javascript
db.cinemas.aggregate([
  { $unwind: "$salles" },
  { $unwind: "$salles.films_diffuses" },
  { $group: { _id: "$salles.films_diffuses.film", count: { $sum: 1 } } },
  { $sort: { count: -1 } },
  { $limit: 10 },
  { $lookup: { from: "films", localField: "_id", foreignField: "_id", as: "film" } },
  { $unwind: "$film" },
  { $project: { _id: 0, film: "$film.titre", count: "$count" } }
]);
```

### Les noms des 10 cinémas diffusant le plus de films les mieux notés

```javascript
db.cinemas.aggregate([
  { $unwind: "$salles" },
  { $unwind: "$salles.films_diffuses" },
  { $lookup: { from: "films", localField: "salles.films_diffuses.film", foreignField: "_id", as: "film" } },
  { $unwind: "$film" },
  { $lookup: { from: "note_g", localField: "film._id", foreignField: "_id", as: "note" } },
  { $unwind: "$note" },
  { $match: { "note.value": { $gte: 4 } } },
  { $group: { _id: "$_id", count: { $sum: 1 } } },
  { $sort: { count: -1 } },
  { $limit: 10 },
  { $lookup: { from: "cinemas", localField: "_id", foreignField: "_id", as: "cinema" } },
  { $unwind: "$cinema" },
  { $project: { _id: 0, cinema: "$cinema.nom", count: "$count" } }
]);
```

## Ajouts à la base de données

Les ajouts à la base de données se feront de manière manuelle, en utilisant les méthodes `insert` et `insertMany` de MongoDB. Les données à ajouter devront être formatées correctement et cohérentes avec les données déjà présentes dans la base de données.

Si plusieurs collections sont concernées par l'ajout, il faudra veiller à mettre à jour les collections dans le bon ordre, en commençant par les collections primaires et en finissant par les collections qui font référence à ces collections primaires afin de garantir le bon référencement des éléments ajoutés.

```javascript
// toujours dans cet ordre...
db.genres_films.insertMany([ ... ]);
db.personnes.insertMany([ ... ]);
db.films.insertMany([ ... ]);
db.avis.insertMany([ ... ]);
db.villes.insertMany([ ... ]);
db.cinemas.insertMany([ ... ]);
```

## Traitements des erreurs

### Détection des erreurs

Pour la détection des erreurs, nous procéderons comme suit:

- Tout d'abord, nous allons créer une collection `erreurs` dans laquelle nous stockerons les éléments erronés que nous rencontrerons. Cette collection contiendra les champs suivants:
  - `type`: la collection d'origine de l'élément erroné (films, genres_films, personnes, cinemas, villes, avis)
  - `raison`: la raison pour laquelle l'élément est erroné
  - `element`: l'élément erroné
- Ensuite, nous vérifierons que les données sont bien formatées et cohérentes progressivement dans chaque collections (des collections primaires aux collections faisant référence à ces collections primaires).
- Si une erreur est détectée, nous retirerons l'élément de la collection d'origine et nous l'ajouterons à la collection `erreurs`.

N.B: Si l'élément vérifié contient une référence erronée, il sera retiré de la collection d'origine. Ainsi, un élément erroné dans une collection primaire entraînera la détection de tous les éléments qui y font référence comme des erreurs.

```javascript
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
```

### Correction des erreurs et réintégration des données

La correction des erreurs devra se faire manuellement collection par collection, des éléments issus des collections primaires aux éléments. Une fois le traitement de toutes les erreurs d'une collection terminé, nous pourrons essayer de réintégrer les éléments corrigés dans la collection d'origine, ainsi que de tester si le reste des éléments présents dans la collection `erreurs` peuvent être réintégrés sans erreur (ex: correction d'un élément référencé par un autre élément).

///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


Requêtes complexes mixtes et diverses (à détailler)
Plus value et intérêt de ces requêtes
Sous requêtes et agrégations pertinentes


///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

