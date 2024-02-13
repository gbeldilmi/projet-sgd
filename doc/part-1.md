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

### Modélisation UML

![Modélisation UML](./uml.png)

## Conception de la base de données

### Données primaires

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

### Collections secondaires

Afin de faciliter la recherche de films ou de cinémas par rapport à des critères spécifiques (par exemple, tous les films d'un réalisateur donné, tous les films d'un genre donné, tous les cinémas d'une ville donnée, etc.), nous utiliseront des collections secondaires pour stocker l'ensemble des valeurs possibles pour ces critères (par exemple, tous les genres de films, etc.). Ces collections secondaires seront mises à jour à chaque ajout, modification ou suppression d'un film ou d'un cinéma.

- Collections secondaires liées à la collection de `films`:
  - Collections de `realisateurs`
  - Collections d'`acteurs`
  - Collections de `genres`
- Collection secondaire liée à la collection de `cinemas` :
  - Collections de `villes`

