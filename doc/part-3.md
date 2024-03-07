# Partie 3: Python et pyMongo

## Requêtes simples

Les requêtes simples sont en grande partie les mêmes que celles de la partie 2, mais cette fois-ci en Python avec pyMongo.

[cf. `queries.py`](../src/queries.py)

## Ajouts à la base de données

Les ajouts à la base de données sont effectués selon les mêmes principes que dans la partie 2, mais cette fois-ci en Python avec pyMongo et sa méthode `insert_many` (remplaçant la méthode `insertMany` de MongoDB).

Le contenu remplissant la base de donnée a été généré dans un but de démonstration, et ne contient pas de données pertinentes.

[cf. `fill.py`](../src/fill.py)

## Traitements des erreurs

### Détection des erreurs

Pour la détection des erreurs, nous avons utilisé un script Python avec pyMongo. Ce script parcourt chaque collection de la base de données et leur arborescence et vérifie, dans l'ordre, que:

- le type de donnée de chaque champ est correct.
- les valeurs de chaque champ sont correctes, non nulles et non vides selon les critères définis dans le shéma de la base de données, cohérentes entre elles et cohérentes avec les autres données de la collection, et que les dates sont au bon format.
- les références entre les collections sont correctes et correspondent à des documents existants.

Si une erreur est détectée, le document est ajouté à la collection `errors` avec, comme décrit en partie 2, les champs suivants:

- 'type' étant le nom de la collection d'origine du document.
- 'raison' étant une description de l'erreur.
- 'element' étant le document erroné.

Pour chaque collection, le script `detect_errors.py` récupère l'ensemble des documents de la collection, les parcourt et les vérifie un par un. Si une erreur est détectée, le document est ajouté à la collection `errors` et le script passe au document suivant. Une fois toutes les collections parcourues, le script notitifie de sa fin, si aucun autre affichage ne s'est produit précédemment, cela signifie que le script s'est terminé sans erreur.

[cf. `detect_errors.py`](../src/detect_errors.py)

### Correction des erreurs et réintégration des données

Comme décrit dans la partie 2, les erreurs sont contenues dans la collection `errors` et doivent être corrigées manuellement par l'utilisation de la méthode `updateOne` de l'interface de MongoDB.

Une fois les erreurs corrigées, les données peuvent être réintégrées dans leur collection d'origine et supprimées de la collection `errors`.

Notre script `insert_errors.py` permet de réintégrer les données dans leur collection d'origine. Cependant, ce script ne gère pas la détéction des erreurs et intègrera toules les données de la collection `errors` dans leur collection d'origine sans distinction. Il est donc conseillé d'utiliser le script `detect_errors.py` à la suite de `insert_errors.py` pour vérifier que d'autres erreurs ne subsistent pas.

[cf. `insert_errors.py`](../src/insert_errors.py)
