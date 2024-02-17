# Partie 1: Conception et mise en œuvre de la base de données MongoDB

## Cahier des charges

### Demandes client

On s'intéresse, ici, aux données concernent les films qui ont été diffusés dans des salles de cinéma à des fins d’analyse.

Par exemple, pour un film, on peut vouloir connaître sa description, les salles où il a été diffusé, la durée de diffusion, le nombre d’entrées, etc.

L'objectif de ces informations sera d’avoir des statistiques générales pour l’ensemble des cinémas d’une ville, mais aussi de façon plus personnalisée sur un film, ou un cinéma, etc.

En complément de ces informations, doivent être stockés et mis en relation les commentaires faits sur les réseaux sociaux sur les films qui ont été diffusés. Il peut s’agir des commentaires textuels et/ou de notes d’appréciation pour le film.

Les informations sur les films sont les informations usuelles (titre, réalisateur, durée, etc.) ainsi que sa catégorie pour permettre des recherches par catégorie. Les informations issues des réseaux sociaux pourront venir enrichir l’analyse pour un film donné, ou une catégorie de film, etc.

### Premier jet de la base de données

De par ces demandes, on peut déjà identifier les nos objets métiers principaux:

- Les films et leurs caractéristiques
- Les cinémas et leurs salles
- Les avis sur les films

On peut donc déjà identifier les collections suivantes:

- Collection de films
- Collection de cinémas
- Collection d'avis

Un objet de la collection de films contiendrait les champs suivants:

- le titre du film
- sa durée
- sa date de sortie
- le synopsis du film
- la liste des réalisateurs ayant participé à la réalisation de ce film
- la liste des acteurs ayant joué dans ce film
- la liste des genres auxquels appartient ce film

Un objet de la collection de cinémas contiendrait les champs suivants:

- le nom du cinéma
- l'adresse du cinéma
- la ville où se trouve le cinéma
- la liste des salles de cinéma disponibles dans ce cinéma, avec, pour chaque salle:
  - le nom de la salle
  - le nombre de places disponibles dans la salle
  - la liste des films diffusés dans cette salle, avec, pour chaque film:
    - la référence au film concerné
    - la date de diffusion du film
    - le nombre d'entrées pour ce film

Un objet de la collection d'avis contiendrait les champs suivants:

- une référence au film concerné
- une note sur le film
- le commentaire textuel sur le film
- la date de publication de l'avis
- la source de l'avis
- l'auteur de l'avis

## Conception de la base de données

### Données primaires

On a donc les collections suivantes:

- Collections de `films`: cette collection répertorie les films disponibles dans la base de données. Chaque document de cette collection contient les champs suivants:
  - `titre`: titre du film
  - `duree`: durée du film
  - `date_sortie`: date de sortie du film
  - `synopsis`: synopsis du film
  - `realisateurs`: liste des réalisateurs ayant participé à la réalisation de ce film
  - `acteurs`: liste des acteurs ayant joué dans ce film
  - `genres`: liste des genres auxquels appartient ce film

- Collections de `cinemas`: cette collection répertorie les cinémas disponibles dans la base de données. Chaque document de cette collection contient les champs suivants:
  - `nom`: nom du cinéma
  - `adresse`: adresse du cinéma
  - `ville`: ville où se trouve le cinéma
  - `salles`: liste des salles de cinéma disponibles dans ce cinéma, pour chaque salle, on a les champs suivants:
    - `nom_salle`: nom de la salle
    - `nombre_places`: nombre de places disponibles dans la salle
    - `films_diffuses`: liste des films diffusés dans cette salle, pour chaque film, on a les champs suivants:
      - `film`: référence au film concerné
      - `date_diffusion`: date de diffusion du film
      - `nombre_entrees`: nombre d'entrées pour ce film

- Collections d'`avis`: cette collection répertorie les avis sur les films disponibles dans la base de données. Chaque document de cette collection contient les champs suivants:
  - `film`: référence au film concerné
  - `note`: note sur le film
  - `commentaire`: commentaire textuel sur le film
  - `date_publication`: date de publication de l'avis
  - `source`: source de l'avis
  - `auteur`: auteur de l'avis

### Mises en liens

Pour des raisons de simplicité, les références aux objets de la collection de `films` se feront sous la forme de l'identifiant de l'objet concerné (`ObjectId` généré automatiquement par MongoDB dans le champs `_id` de chaque objet), et non sous la forme d'un objet complet afin de limiter la redondance des données, faciliter la mise à jour des données et éviter les problèmes de cohérence des données.

En effet, si on stockait l'objet complet de la collection de `films` dans chaque document de la collection d'`avis`, cela nous obligerait à mettre à jour tous les documents de la collection d'`avis` à chaque modification d'un film, ce qui serait coûteux en termes de performances et de ressources et pourrait entraîner des problèmes de cohérence des données dans le cas où la valeur d'un champ d'un film serait erronée.

### Cas des realisateurs et des acteurs de films et mises en perspectives

Pour les champs `realisateurs` et `acteurs` de la collection de `films`, on pourrait stocker les noms des réalisateurs et des acteurs sous forme de chaînes de caractères. Cependant, cela pourrait entraîner des problèmes de cohérence des données dans le cas où un nom de réalisateur ou d'acteur serait mal orthographié, sans oublier que deux réalisateurs ou acteurs différents pourraient avoir le même nom.

Pour éviter ces problèmes, on pourrait stocker les réalisateurs et les acteurs sous forme de références à des documents de collections de `personnes`. Cette solution permettrait de stocker des informations supplémentaires sur les réalisateurs et les acteurs (par exemple, leur date de naissance, leur nationalité, etc.) et de faire des recherches sur ces derniers. De plus, cela permettrait aussi de gérer les cas où un réalisateur ait joué dans un film ou un acteur ait réalisé un film.

Ainsi, on pourrait avoir la collection de `personnes` suivante:

- `nom`: nom de la personne
- `prenom`: prénom de la personne
- `date_naissance`: date de naissance de la personne
- `nationalite`: nationalité de la personne

Chaque référence à un réalisateur ou à un acteur dans un document de la collection de `films` serait donc sous la forme de l'identifiant de l'objet concerné dans la collection de `personnes`.

Avec cette même logique, on pourrait aussi avoir des collections `genres_films` et `villes` pour stocker respectivement les genres de films et les villes où un cinéma est implanté. De cette manière, la collection de `genres_films` contiendrait des documents avec comme seuls champs `nom_genre` et `description`, et la collection de `villes` contiendrait uniquement le champ `nom_ville` (ainsi que le champ `_id` généré automatiquement par MongoDB).

De plus, les mises à jour des documents des collections de `personnes`, `genres_films` et `villes` seraient moins fréquentes que celles des documents de la collection de `films` et `cinemas`, donc leurs mises en cache serait pertinente.

### Modélisation UML

La modélisation UML de la base de données sera donc la suivante:

![Modélisation UML](./uml.png)
