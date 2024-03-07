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

Cette requête fait partie des requêtes les plus simples que nous pourrions effectuer sur la base de données. Elle consiste à rechercher l'identifiant du film dans la collection `films` puis à rechercher tous les avis qui font référence à cet identifiant dans la collection `avis`. Le résultat de cette requête serait une liste d'avis pour le film "Interstellar".

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

La fonction `my_map` permet de créer une liste de couples (clé, valeur) où la clé est l'identifiant du film et la valeur est la note d'appréciation. La fonction `reduce` permet de calculer la moyenne des notes pour chaque film. L'appel à la méthode `mapReduce` permet d'effectuer ces opérations et de stocker le résultat dans la collection `note_g`.

Le résultat de cette requête est peu exploitable en l'état, car il ne contient que les identifiants des films et les notes d'appréciation moyennes, restant peu lisibles dans l'état. Pour obtenir les titres des films et les notes d'appréciation moyennes, nous effectuons une jointure avec la collection `films` à l'aide de la méthode `aggregate` de MongoDB et des directives `$lookup`, `$unwind` et `$project`. 

### Les 10 films les plus diffusés

Cette requête peut permettre d'analyser la fréquence de diffusion des films dans les cinémas.

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

Pour effectuer cette requête, nous utilisons la méthode `aggregate` de MongoDB afin d'effectuer des opérations suivantes à partir des données de la collection `cinemas`:

- Tout d'abord, nous déroulons les tableaux `salles` et `films_diffuses` pour pouvoir accéder aux films diffusés dans chaque salle avec la méthode `$unwind`.
- Ensuite, nous regroupons les films par leur identifiant avec la méthode `$group` en comptant le nombre de fois qu'ils ont été diffusés dans les salles. Puis nous trions les films par le nombre de fois qu'ils ont été diffusés avec `$sort` et nous limitons le résultat à 10 films avec `$limit`.
- Jusqu'ici, nous avons obtenu les identifiants des 10 films les plus diffusés. Pour obtenir les titres de ces films, nous faisons une jointure avec la collection `films` avec la méthode `$lookup`. La méthode `$unwind` nous permet de dérouler les tableaux résultants de la jointure, puis nous projetons les titres des films et le nombre de fois qu'ils ont été diffusés avec `$project`. Nous donnant ainsi les titres des 10 films les plus diffusés triés par ordre décroissant du nombre de fois qu'ils ont été diffusés.

### Les noms des 10 cinémas diffusant le plus de films les mieux notés

Cette requête peut permettre d'analyser l'attractivité des cinémas en fonction de l'appréciation des films qu'ils diffusent.

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

Cette requête est plus complexe que les précédentes, car elle nécessite de faire des jointures entre plusieurs collections et de faire des calculs sur les données. Pour cela nous utilisons la méthode `aggregate` de MongoDB afin d'effectuer des opérations suivantes à partir des données de la collection `cinemas`:

- Tout d'abord, nous déroulons les tableaux `salles` et `films_diffuses` pour pouvoir accéder aux films diffusés dans chaque salle avec la méthode `$unwind`.
- Ensuite, nous faisons une jointure avec la collection `films` pour obtenir les informations des films diffusés dans chaque salle avec la méthode `$lookup`.
- Puis, nous faisons une jointure avec la collection `note_g` pour obtenir les notes d'appréciation des films diffusés dans chaque salle, encore une fois, avec la méthode `$lookup`.
- Ensuite, nous filtrons les films qui ont une note d'appréciation supérieure ou égale à 4 avec la méthode `$match`.
- Enfin, nous regroupons les cinémas par leur identifiant avec la méthode `$group`, nous comptons le nombre de films diffusés dans chaque cinéma puis nous trions les cinémas par le nombre de films diffusés avec `$sort` et nous limitons le résultat à 10 cinémas avec `$limit`.
- Jusqu'ici, nous avons obtenu les identifiants des 10 cinémas diffusant le plus de films les mieux notés. Pour obtenir les noms de ces cinémas, nous faisons une jointure avec la collection `cinemas` avec la méthode `$lookup`. La méthode `$unwind` nous permet de dérouler les tableaux résultants de la jointure, puis nous projetons les noms des cinémas et le nombre de films diffusés avec `$project`. Nous donnant ainsi le nom des 10 cinémas diffusant le plus de films les mieux notés triés par ordre décroissant du nombre de films diffusés.

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

Nous détaillerons les détails de l'implémentation de la détection des erreurs dans la troisième partie.

### Correction des erreurs et réintégration des données

La correction des erreurs devra se faire manuellement collection par collection, des éléments issus des collections primaires aux éléments. Une fois le traitement de toutes les erreurs d'une collection terminé, nous pourrons essayer de réintégrer les éléments corrigés dans la collection d'origine, ainsi que de tester si le reste des éléments présents dans la collection `erreurs` peuvent être réintégrés sans erreur (ex: correction d'un élément référencé par un autre élément).

Une fois les erreurs corrigées, nous pourrons réintégrer les éléments corrigés dans leur collection d'origine de la façon suivante:

```javascript
// dans le même ordre que pour les ajouts...
e_genres_films = db.errors.find({type: "genres_films"});
e_genres_films.forEach(function(e) {
  db.genres_films.insert(e.element);
  db.errors.remove(e);
});
e_personnes = db.errors.find({type: "personnes"});
e_personnes.forEach(function(e) {
  db.personnes.insert(e.element);
  db.errors.remove(e);
});
e_films = db.errors.find({type: "films"});
e_films.forEach(function(e) {
  db.films.insert(e.element);
  db.errors.remove(e);
});
e_avis = db.errors.find({type: "avis"});
e_avis.forEach(function(e) {
  db.avis.insert(e.element);
  db.errors.remove(e);
});
e_villes = db.errors.find({type: "villes"});
e_villes.forEach(function(e) {
  db.villes.insert(e.element);
  db.errors.remove(e);
});
e_cinemas = db.errors.find({type: "cinemas"});
e_cinemas.forEach(function(e) {
  db.cinemas.insert(e.element);
  db.errors.remove(e);
});
```

Une fois les erreurs corrigées et les éléments réintégrés dans leur collection d'origine, nous pourrons répéter le processus de détection des erreurs pour vérifier que les éléments réintégrés ne sont plus erronés et ont été corrigés correctement.
