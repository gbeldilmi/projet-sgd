import mongo2

c, db = mongo2.connect_mongo2(); # Connexion à la base de données

# Suppression des collections existantes
db.erreurs.drop();
db.cinemas.drop();
db.villes.drop();
db.avis.drop();
db.films.drop();
db.genres_films.drop();
db.personnes.drop();

db.genres_films.insert_many([
  {
    "genre": "Drama"
  }, {
    "genre": "Crime"
  }, {
    "genre": "Action"
  }, {
    "genre": "Adventure"
  }, {
    "genre": "Fantasy"
  }, {
    "genre": "Thriller"
  }, {
    "genre": "Comedy"
  }, {
    "genre": "Family"
  }, {
    "genre": "Sci-Fi"
  }, {
    "genre": "Mystery"
  }, {
    "genre": "Biography"
  }, {
    "genre": "History"
  }, {
    "genre": "War"
  }, {
    "genre": "Romance"
  }, {
    "genre": "Music"
  }, {
    "genre": "Animation"
  }, {
    "genre": "Horror"
  }, {
    "genre": "Western"
  }, {
    "genre": "Sport"
  }
]);
gf = db.genres_films.find(); # Mise en cache

db.personnes.insert_many([
  {
    "prenom": "Frank",
    "nom": "Darabont"
  }, {
    "prenom": "Tim",
    "nom": "Robbins"
  }, {
    "prenom": "Morgan",
    "nom": "Freeman"
  }, {
    "prenom": "Bob",
    "nom": "Gunton"
  }, {
    "prenom": "William",
    "nom": "Sadler"
  }, {
    "prenom": "Clancy",
    "nom": "Brown"
  }, {
    "prenom": "Gil",
    "nom": "Bellows"
  }, {
    "prenom": "Mark",
    "nom": "Rolston"
  }, {
    "prenom": "James",
    "nom": "Whitmore"
  }, {
    "prenom": "Jeffrey",
    "nom": "DeMunn"
  }, {
    "prenom": "Larry",
    "nom": "Brandenburg"
  }, {
    "prenom": "Neil",
    "nom": "Giuntoli"
  }, {
    "prenom": "Brian",
    "nom": "Libby"
  }, {
    "prenom": "David",
    "nom": "Proval"
  }, {
    "prenom": "Joseph",
    "nom": "Ragno"
  }, {
    "prenom": "Jude",
    "nom": "Ciccolella"
  }, {
    "prenom": "Paul",
    "nom": "McCrane"
  }, {
    "prenom": "Renee",
    "nom": "Blaine"
  }, {
    "prenom": "Scott",
    "nom": "Mann"
  }, {
    "prenom": "John",
    "nom": "Dunne"
  }, {
    "prenom": "Brian",
    "nom": "Delate"
  }, {
    "prenom": "Don",
    "nom": "McManus"
  }, {
    "prenom": "Dorothy",
    "nom": "Silver"
  }, {
    "prenom": "Frank",
    "nom": "Medrano"
  }, {
    "prenom": "Alan",
    "nom": "Rosenberg"
  }, {
    "prenom": "Macka",
    "nom": "Brown"
  }, {
    "prenom": "Neil",
    "nom": "Rynolds"
  }, {
    "prenom": "John",
    "nom": "E. Summers"
  }, {
    "prenom": "Fred",
    "nom": "Henderson"
  }, {
    "prenom": "John",
    "nom": "R. Woodward"
  }, {
    "prenom": "Alfonso",
    "nom": "Freeman"
  }, {
    "prenom": "V.J.",
    "nom": "Foster"
  }, {
    "prenom": "Sergio",
    "nom": "K. Taylor"
  }, {
    "prenom": "John",
    "nom": "D. Craig"
  }, {
    "prenom": "Dion",
    "nom": "Anderson"
  }, {
    "prenom": "Claire",
    "nom": "S. Lanier"
  }, {
    "prenom": "Rita",
    "nom": "Hayworth"
  }, {
    "prenom": "Greta",
    "nom": "S. Blackburn"
  }, {
    "prenom": "Dana",
    "nom": "S. Snyder"
  }, {
    "prenom": "Diane",
    "nom": "S. Baker"
  }, {
    "prenom": "Renee",
    "nom": "S. Blaine"
  }, {
    "prenom": "Scott",
    "nom": "S. Mann"
  }, {
    "prenom": "John",
    "nom": "S. Dunne"
  }, {
    "prenom": "Brian",
    "nom": "S. Delate"
  }, {
    "prenom": "Don",
    "nom": "S. McManus"
  }, {
    "prenom": "Dorothy",
    "nom": "S. Silver"
  }, {
    "prenom": "Frank",
    "nom": "S. Medrano"
  }, {
    "prenom": "Alan",
    "nom": "S. Rosenberg"
  }, {
    "prenom": "Macka",
    "nom": "S. Brown"
  }, {
    "prenom": "Neil",
    "nom": "S. Rynolds"
  }, {
    "prenom": "John",
    "nom": "S. E. Summers"
  }, {
    "prenom": "Fred",
    "nom": "S. Henderson"
  }, {
    "prenom": "John",
    "nom": "S. R. Woodward"
  }, {
    "prenom": "Alfonso",
    "nom": "S. Freeman"
  }, {
    "prenom": "V.J.",
    "nom": "S. Foster"
  }, {
    "prenom": "Sergio",
    "nom": "S. K. Taylor"
  }, {
    "prenom": "John",
    "nom": "S. D. Craig"
  }, {
    "prenom": "Dion",
    "nom": "S. Anderson"
  }, {
    "prenom": "Claire",
    "nom": "S. Lanier"
  }, {
    "prenom": "Rita",
    "nom": "S. Hayworth"
  }, {
    "prenom": "Greta",
    "nom": "S. Blackburn"
  }, {
    "prenom": "Dana",
    "nom": "S. Snyder"
  }, {
    "prenom": "Diane",
    "nom": "S. Baker"
  }, {
    "prenom": "Renee",
    "nom": "S. Blaine"
  }, {
    "prenom": "Scott",
    "nom": "S. Mann"
  }, {
    "prenom": "John",
    "nom": "S. Dunne"
  }, {
    "prenom": "Brian",
    "nom": "S. Delate"
  }, {
    "prenom": "Don",
    "nom": "S. McManus"
  }, {
    "prenom": "Dorothy",
    "nom": "S. Silver"
  }, {
    "prenom": "Frank",
    "nom": "S. Medrano"
  }, {
    "prenom": "Alan",
    "nom": "S. Rosenberg"
  }, {
    "prenom": "Macka",
    "nom": "S. Brown"
  }, {
    "prenom": "Neil",
    "nom": "S. Rynolds"
  }, {
    "prenom": "John",
    "nom": "S. E. Summers"
  }, {
    "prenom": "Fred",
    "nom": "S. Henderson"
  }, {
    "prenom": "John",
    "nom": "S. R. Woodward"
  }, {
    "prenom": "Alfonso",
    "nom": "S. Freeman"
  }, {
    "prenom": "V.J.",
    "nom": "S. Foster"
  }, {
    "prenom": "Sergio",
    "nom": "S. K. Taylor"
  }, {
    "prenom": "John",
    "nom": "S. D. Craig"
  }, {
    "prenom": "Dion",
    "nom": "S. Anderson"
  }, {
    "prenom": "Claire",
    "nom": "S. Lanier"
  }, {
    "prenom": "Rita",
    "nom": "S. Hayworth"
  }, {
    "prenom": "Greta",
    "nom": "S. Blackburn"
  }, {
    "prenom": "Dana",
    "nom": "S. Snyder"
  }, {
    "prenom": "Diane",
    "nom": "S. Baker"
  }, {
    "prenom": "Renee",
    "nom": "S. Blaine"
  }, {
    "prenom": "Scott",
    "nom": "S. Mann"
  }, {
    "prenom": "John",
    "nom": "S. Dunne"
  }, {
    "prenom": "Brian",
    "nom": "S. Delate"
  }, {
    "prenom": "Don",
    "nom": "S. McManus"
  }, {
    "prenom": "Dorothy",
    "nom": "S. Silver"
  }, {
    "prenom": "Frank",
    "nom": "S. Medrano"
  }, {
    "prenom": "Alan",
    "nom": "S. Rosenberg"
  }, {
    "prenom": "Macka",
    "nom": "S. Brown"
  }, {
    "prenom": "Neil",
    "nom": "S. Rynolds"
  }, {
    "prenom": "John",
    "nom": "S. E. Summers"
  }, {
    "prenom": "Fred",
    "nom": "S. Henderson"
  }, {
    "prenom": "John",
    "nom": "S. R. Woodward"
  }, {
    "prenom": "Alfonso",
    "nom": "S. Freeman"
  }, {
    "prenom": "V.J.",
    "nom": "S. Foster"
  }, {
    "prenom": "Sergio",
    "nom": "S. K. Taylor"
  }, {
    "prenom": "John",
    "nom": "S. D. Craig"
  }, {
    "prenom": "Dion",
    "nom": "S. Anderson"
  }, {
    "prenom": "Claire",
    "nom": "S. Lanier"
  }, {
    "prenom": "Rita",
    "nom": "S. Hayworth"
  }, {
    "prenom": "Greta",
    "nom": "S. Blackburn"
  }, {
    "prenom": "Dana",
    "nom": "S. Snyder"
  }, {
    "prenom": "Diane",
    "nom": "S. Baker"
  }, {
    "prenom": "Renee",
    "nom": "S. Blaine"
  }, {
    "prenom": "Scott",
    "nom": "S. Mann"
  }, {
    "prenom": "John",
    "nom": "S. Dunne"
  }, {
    "prenom": "Brian",
    "nom": "S. Delate"
  }, {
    "prenom": "Don",
    "nom": "S. McManus"
  }, {
    "prenom": "Dorothy",
    "nom": "S. Silver"
  }, {
    "prenom": "Frank",
    "nom": "S. Medrano"
  }, {
    "prenom": "Alan",
    "nom": "S. Rosenberg"
  }, {
    "prenom": "Macka",
    "nom": "S. Brown"
  }, {
    "prenom": "Neil",
    "nom": "S. Rynolds"
  }, {
    "prenom": "John",
    "nom": "S. E. Summers"
  }, {
    "prenom": "Fred",
    "nom": "S. Henderson"
  }, {
    "prenom": "John",
    "nom": "S. R. Woodward"
  }, {
    "prenom": "Alfonso",
    "nom": "S. Freeman"
  }, {
    "prenom": "V.J.",
    "nom": "S. Foster"
  }, {
    "prenom": "Sergio",
    "nom": "S. K. Taylor"
  }, {
    "prenom": "John",
    "nom": "S. D. Craig"
  }, {
    "prenom": "Dion",
    "nom": "S. Anderson"
  }, {
    "prenom": "Claire",
    "nom": "S. Lanier"
  }, {
    "prenom": "Rita",
    "nom": "S. Hayworth"
  }, {
    "prenom": "Greta",
    "nom": "S. Blackburn"
  }, {
    "prenom": "Dana",
    "nom": "S. Snyder"
  }, {
    "prenom": "Diane",
    "nom": "S. Baker"
  }, {
    "prenom": "Renee",
    "nom": "S. Blaine"
  }, {
    "prenom": "Scott",
    "nom": "S. Mann"
  }, {
    "prenom": "John",
    "nom": "S. Dunne"
  }, {
    "prenom": "Brian",
    "nom": "S. Delate"
  }, {
    "prenom": "Don",
    "nom": "S. McManus"
  }, {
    "prenom": "Dorothy",
    "nom": "S. Silver"
  }, {
    "prenom": "Frank",
    "nom": "S. Medrano"
  }, {
    "prenom": "Alan",
    "nom": "S. Rosenberg"
  }, {
    "prenom": "Macka",
    "nom": "S. Brown"
  }, {
    "prenom": "Neil",
    "nom": "S. Rynolds"
  }, {
    "prenom": "John",
    "nom": "S. E. Summers"
  }, {
    "prenom": "Fred",
    "nom": "S. Henderson"
  }, {
    "prenom": "John",
    "nom": "S. R. Woodward"
  }, {
    "prenom": "Christopher",
    "nom": "Nolan"
  }, {
    "prenom": "Christian",
    "nom": "Bale"
  }, {
    "prenom": "Heath",
    "nom": "Ledger"
  }, {
    "prenom": "Aaron",
    "nom": "Eckhart"
  }, {
    "prenom": "Michael",
    "nom": "Caine"
  }, {
    "prenom": "Maggie",
    "nom": "Gyllenhaal"
  }, {
    "prenom": "Gary",
    "nom": "Oldman"
  }, {
    "prenom": "Morgan",
    "nom": "Freeman"
  }, {
    "prenom": "Monique",
    "nom": "Curnen"
  }, {
    "prenom": "Ron",
    "nom": "Dean"
  }, {
    "prenom": "Chin",
    "nom": "Han"
  }, {
    "prenom": "Nestor",
    "nom": "Carbonell"
  }, {
    "prenom": "Eric",
    "nom": "Roberts"
  }, {
    "prenom": "Ritchie",
    "nom": "Coster"
  }, {
    "prenom": "Anthony",
    "nom": "Michael"
  }, {
    "prenom": "Hall",
    "nom": "Michael"
  }, {
    "prenom": "Jai",
    "nom": "Courtney"
  }, {
    "prenom": "Leonard",
    "nom": "Robinson"
  }, {
    "prenom": "Cillian",
    "nom": "Murphy"
  }, {
    "prenom": "Chin",
    "nom": "Han"
  }, {
    "prenom": "Nestor",
    "nom": "Carbonell"
  }, {
    "prenom": "Eric",
    "nom": "Roberts"
  }, {
    "prenom": "Ritchie",
    "nom": "Coster"
  }, {
    "prenom": "Anthony",
    "nom": "Michael"
  }, {
    "prenom": "Hall",
    "nom": "Michael"
  }, {
    "prenom": "Jai",
    "nom": "Courtney"
  }, {
    "prenom": "Leonard",
    "nom": "Robinson"
  }, {
    "prenom": "Cillian",
    "nom": "Murphy"
  }, {
    "prenom": "Elliot",
    "nom": "Page"
  }, {
    "prenom": "Joseph",
    "nom": "Gordon-Levitt"
  },
]);
p = db.personnes.find();

db.films.insert_many([
  {
    "titre": "The Shawshank Redemption",
    "duree": 142,
    "date_sortie": "1995-03-01 00:00",
    "synopsis": "En 1947, Andy Dufresne, un jeune banquier, est condamné à la prison à vie pour le meurtre de sa femme et de son amant. Ayant beau clamer son innocence, il est emprisonné à `Shawshank', le pénitencier le plus sévère de l'Etat du Maine. Il y fait la rencontre de Red, un homme désabusé, détenu depuis 20 ans. Commence alors une grande histoire d'amitié entre les deux hommes.",
    "realisateurs": [
      p[0]["_id"],
      p[1]["_id"]
    ],
    "acteurs": [
      p[1]["_id"],
      p[2]["_id"],
      p[3]["_id"],
      p[4]["_id"]
    ],
    "genres": [
      gf[0]["_id"],
      gf[1]["_id"]
    ]
  }, {
    "titre": "The Godfather",
    "duree": 175,
    "date_sortie": "1972-03-24 00:00",
    "synopsis": "En 1945, à New York, les Corleone sont une des cinq familles de la mafia. Don Vito Corleone, `parrain' de cette famille, marie sa fille à un bookmaker. Sollozzo, `parrain' de la famille Tattaglia, propose à Don Vito une association dans le trafic de drogue, mais celui-ci refuse. Sonny, un de ses fils, y est quant à lui favorable. Afin de traiter avec Sonny, Sollozzo tente de faire tuer Don Vito, mais celui-ci en réchappe. Michael, le frère cadet de Sonny, recherche alors les commanditaires de l'attentat et tue Sollozzo et le chef de la police, en représailles. Il part alors en Sicile, où il épouse Apollonia, mais celle-ci est assassinée à sa place. De retour à New York, Michael épouse Kay Adams et se prépare à devenir le successeur de son père...",
    "realisateurs": [
      p[5]["_id"]
    ],
    "acteurs": [
      p[6]["_id"],
      p[7]["_id"],
      p[8]["_id"],
      p[9]["_id"]
    ],
    "genres": [
      gf[0]["_id"],
      gf[4]["_id"]
    ]
  }, {
    "titre": "The Dark Knight",
    "duree": 152,
    "date_sortie": "2008-07-18 00:00",
    "synopsis": "Batman aborde une phase décisive de sa guerre au crime. Avec l'aide du lieutenant de police Jim Gordon et du procureur Harvey Dent, Batman entreprend de démanteler les dernières organisations criminelles qui infestent les rues de sa ville. L'association s'avère efficace, mais le trio se heurte bientôt à un nouveau génie du crime qui répand la terreur et le chaos dans Gotham : le Joker...",
    "realisateurs": [
      p[10]["_id"]
    ],
    "acteurs": [
      p[11]["_id"],
      p[12]["_id"],
      p[13]["_id"],
      p[14]["_id"]
    ],
    "genres": [
      gf[2]["_id"],
      gf[5]["_id"],
      gf[8]["_id"]
    ]
  }, {
    "titre": "Inception",
    "duree": 148,
    "date_sortie": "2010-07-16 00:00",
    "synopsis": "Dom Cobb est un voleur expérimenté – le meilleur qui soit dans l'art périlleux de l'extraction : sa spécialité consiste à s'approprier les secrets les plus précieux d'un individu, enfouis au plus profond de son subconscient, pendant qu'il rêve et que son esprit est particulièrement vulnérable. Très recherché pour ses talents dans l'univers trouble de l'espionnage industriel, Cobb est également devenu un fugitif traqué dans le monde entier qui a perdu tout ce qui lui est cher. Mais une ultime mission pourrait lui permettre de retrouver sa vie d'avant – à condition qu'il puisse accomplir l'impossible : l'inception. Au lieu de subtiliser un rêve, Cobb et son équipe doivent faire l\'inverse : implanter une idée dans l\'esprit d\'un individu. S\'ils y parviennent, cela pourrait être le crime parfait.",
    "realisateurs": [
      p[15]["_id"]
    ],
    "acteurs": [
      p[16]["_id"],
      p[17]["_id"],
      p[18]["_id"],
      p[19]["_id"],
      p[20]["_id"]
    ],
    "genres": [
      gf[2]["_id"],
      gf[5]["_id"],
      gf[8]["_id"]
    ]
  }, {
    "titre": "The Lord of the Rings: The Return of the King",
    "duree": 201,
    "date_sortie": "2003-12-17 00:00",
    "synopsis": "Les armées de Sauron ont attaqué Minas Tirith, la capitale de Gondor. Jamais ce royaume autrefois puissant n'a eu autant besoin de son roi. Mais Aragorn trouvera-t-il en lui la volonté d'accomplir sa destinée ? Tandis que Gandalf s'efforce de soutenir les forces brisées de Gondor, Théoden exhorte les guerriers de Rohan à se joindre au combat. Mais malgré leur courage et leur loyauté, les forces des Hommes ne sont pas de taille à lutter contre les innombrables légions d'ennemis qui s'abattent sur le royaume... Chaque victoire se paye d'immenses sacrifices. Malgré ses pertes, la Communauté se jette dans la bataille pour la vie, ses membres faisant tout pour détourner l'attention de Sauron afin de donner à Frodon une chance d'accomplir sa quête. Voyageant à travers les terres ennemies, ce dernier doit se reposer sur Sam et Gollum, pendant que l'Anneau continue de le tenter...",
    "realisateurs": [
      p[21]["_id"]
    ],
    "acteurs": [
      p[22]["_id"],
      p[23]["_id"],
      p[24]["_id"],
      p[25]["_id"],
      p[26]["_id"]
    ],
    "genres": [
      gf[3]["_id"],
      gf[4]["_id"]
    ]
  }, {
    "titre": "Interstellar",
    "duree": 169,
    "date_sortie": "2014-11-05 00:00",
    "synopsis": "Le film raconte les aventures d'un groupe d'explorateurs qui utilisent une faille récemment découverte dans l'espace-temps afin de repousser les limites humaines et partir à la conquête des distances astronomiques dans un voyage interstellaire.",
    "realisateurs": [
      p[27]["_id"]
    ],
    "acteurs": [
      p[28]["_id"],
      p[19]["_id"],
      p[30]["_id"],
      p[31]["_id"],
      p[32]["_id"]
    ],
    "genres": [
      gf[3]["_id"],
      gf[8]["_id"]
    ]
  }, {
    "titre": "The Matrix",
    "duree": 136,
    "date_sortie": "1999-03-31 00:00",
    "synopsis": "Programmeur anonyme dans un service administratif le jour, Thomas Anderson devient Neo la nuit venue. Sous ce pseudonyme, il est l'un des pirates les plus recherchés du cyber-espace. À cheval entre deux mondes, Neo est assailli par d'étranges songes et des messages cryptés provenant d'un certain Morpheus. Celui-ci l'exhorte à aller au-delà des apparences et à trouver la réponse à la question qui hante constamment ses pensées : qu'est-ce que la Matrice ? Nul ne le sait, et aucun homme n'est encore parvenu à en percer les defenses. Mais Morpheus est persuadé que Neo est l'Elu, le libérateur mythique de l'humanité annoncé selon la prophétie. Ensemble, ils se lancent dans une lutte sans retour contre la Matrice et ses terribles agents...",
    "realisateurs": [
      p[3]["_id"],
      p[25]["_id"]
    ],
    "acteurs": [
      p[23]["_id"],
      p[18]["_id"],
      p[14]["_id"],
      p[8]["_id"],
    ],
    "genres": [
      gf[2]["_id"],
      gf[5]["_id"],
      gf[8]["_id"]
    ]
  }, {
    "titre": "The Green Mile",
    "duree": 189,
    "date_sortie": "1999-12-10 00:00",
    "synopsis": "Paul Edgecomb, pensionnaire centenaire d'une maison de retraite, est hanté par ses souvenirs. Gardien-chef du pénitencier de Cold Mountain en 1935, il était chargé de veiller au bon déroulement des exécutions capitales en s'efforçant d'adoucir les derniers moments des condamnés. Parmi eux se trouvait un colosse du nom de John Coffey, accusé du viol et du meurtre de deux fillettes. Intrigué par cet homme candide et timide, Edgecomb va tisser avec lui des liens très forts.",
    "realisateurs": [
      p[0]["_id"],
      p[1]["_id"]
    ],
    "acteurs": [
      p[1]["_id"],
      p[2]["_id"],
      p[3]["_id"],
      p[4]["_id"]
    ],
    "genres": [
      gf[0]["_id"],
      gf[1]["_id"]
    ]
  }, {
    "titre": "The 100",
    "duree": 43,
    "date_sortie": "2014-03-19 00:00",
    "synopsis": "Après une apocalypse nucléaire causée par l'Homme lors d'une troisième Guerre Mondiale, les 318 survivants recensés se réfugient dans des stations spatiales et parviennent à y vivre et à se reproduire, atteignant le nombre de 4000. Mais 97 ans plus tard, le vaisseau mère, The Ark, est en piteux état. Une centaine de jeunes délinquants emprisonnés au fil des années pour des crimes ou des trahisons sont choisis comme cobayes par les autorités pour redescendre sur Terre et tester les chances de survie. Dès leur arrivée, ils découvrent un nouveau monde dangereux mais fascinant...",
    "realisateurs": [
      p[33]["_id"]
    ],
    "acteurs": [
      p[14]["_id"],
      p[25]["_id"],
      p[19]["_id"],
      p[28]["_id"]
    ],
    "genres": [
      gf[2]["_id"],
      gf[5]["_id"],
      gf[8]["_id"]
    ]
  }, {
    "titre": "Taken",
    "duree": 41,
    "date_sortie": "2008-02-27 00:00",
    "synopsis": "Ancien agent secret, Bryan Mills est désormais garde du corps. Il rend visite à Kim, sa fille, qui vit avec sa mère Lenore et son beau-père Stuart. Il apprend que cette dernière a accepté un voyage à Paris avec son amie Amanda. Peu après leur arrivée, elles se font enlever par des Albanais. Bryan va devoir tout mettre en oeuvre pour les retrouver et les sauver...",
    "realisateurs": [
      p[34]["_id"]
    ],
    "acteurs": [
      p[35]["_id"],
      p[36]["_id"],
      p[37]["_id"],
      p[38]["_id"]
    ],
    "genres": [
      gf[2]["_id"],
      gf[5]["_id"]
    ]
  }, {
    "titre": "The Revenant",
    "duree": 156,
    "date_sortie": "2016-02-24 00:00",
    "synopsis": "Dans une Amérique profondément sauvage, Hugh Glass, un trappeur, est attaqué par un ours et laissé pour mort par ses équipiers. Il refuse de mourir. Seul, armé de sa volonté et porté par l'amour qu'il voue à sa femme et à leur fils, Glass entreprend un voyage de plus de 300 km dans un environnement hostile, sur la piste de l'homme qui l'a trahi. Sa soif de vengeance va se transformer en une lutte héroïque pour braver tous les obstacles, revenir chez lui et trouver la rédemption.",
    "realisateurs": [
      p[39]["_id"]
    ],
    "acteurs": [
      p[40]["_id"],
      p[41]["_id"],
      p[42]["_id"],
      p[43]["_id"]
    ],
    "genres": [
      gf[0]["_id"],
      gf[1]["_id"]
    ]
  }, {
    "titre": "Pulp Fiction",
    "duree": 154,
    "date_sortie": "1994-10-14 00:00",
    "synopsis": "L'odyssée sanglante et burlesque de petits malfrats dans la jungle de Hollywood à travers trois histoires qui s'entremêlent.",
    "realisateurs": [
      p[44]["_id"]
    ],
    "acteurs": [
      p[45]["_id"],
      p[46]["_id"],
      p[47]["_id"],
      p[48]["_id"]
    ],
    "genres": [
      gf[2]["_id"],
      gf[5]["_id"],
      gf[8]["_id"]
    ]
  },
  {
    "titre": "Fight Club",
    "duree": 139,
    "date_sortie": "1999-10-15 00:00",
    "synopsis": "Le narrateur, sans identité précise, vit seul, travaille seul, dort seul, mange seul ses plateaux-repas pour une personne comme beaucoup d'autres personnes seules qui connaissent la misère humaine, morale et sexuelle. C'est pourquoi il va devenir membre du Fight club, un lieu clandestin ou il va pouvoir retrouver sa virilité, l'échange et la communication. Ce club est dirigé par Tyler Durden, une sorte d'anarchiste entre gourou et philosophe qui prêche l'amour de son prochain.",
    "realisateurs": [
      p[49]["_id"]
    ],
    "acteurs": [
      p[50]["_id"],
      p[51]["_id"],
      p[52]["_id"],
      p[53]["_id"]
    ],
    "genres": [
      gf[2]["_id"],
      gf[5]["_id"],
      gf[8]["_id"]
    ]
  }
]);
f = db.films.find();

db.avis.insert_many([
  {
    "film": f[0]["_id"],
    "note": 5,
    "commentaire": "Très bon film, à voir absolument.",
    "source": "Allociné",
    "auteur": "John Doe"
  }, {
    "film": f[0]["_id"],
    "note": 4,
    "commentaire": "Un classique du cinéma, à voir et à revoir.",
    "source": "IMDb",
    "auteur": "Jane Doe"
  }, {
    "film": f[1]["_id"],
    "note": 5,
    "commentaire": "Un chef d'oeuvre.",
    "source": "Allociné",
    "auteur": "John Doe"
  }, {
    "film": f[1]["_id"],
    "note": 5,
    "commentaire": "Un film à voir absolument.",
    "source": "IMDb",
    "auteur": "Jane Doe"
  }, {
    "film": f[2]["_id"],
    "note": 5,
    "commentaire": "Un film exceptionnel.",
    "source": "Allociné",
    "auteur": "John Doe"
  }, {
    "film": f[2]["_id"],
    "note": 5,
    "commentaire": "Un film à voir absolument.",
    "source": "IMDb",
    "auteur": "Jane Doe"
  }, {
    "film": f[3]["_id"],
    "note": 5,
    "commentaire": "Un film exceptionnel.",
    "source": "Allociné",
    "auteur": "John Doe"
  }, {
    "film": f[3]["_id"],
    "note": 5,
    "commentaire": "Un film à voir absolument.",
    "source": "IMDb",
    "auteur": "Jane Doe"
  }, {
    "film": f[4]["_id"],
    "note": 5,
    "commentaire": "Un film exceptionnel.",
    "source": "Allociné",
    "auteur": "John Doe"
  }, {
    "film": f[4]["_id"],
    "note": 5,
    "commentaire": "Un film à voir absolument.",
    "source": "IMDb",
    "auteur": "Jane Doe"
  }, {
    "film": f[5]["_id"],
    "note": 5,
    "commentaire": "Un film exceptionnel.",
    "source": "Allociné",
    "auteur": "John Doe"
  }, {
    "film": f[5]["_id"],
    "note": 5,
    "commentaire": "Un film à voir absolument.",
    "source": "IMDb",
    "auteur": "Jane Doe"
  }, {
    "film": f[6]["_id"],
    "note": 2,
    "commentaire": "Pas terrible.",
    "source": "Allociné",
    "auteur": "John Doe"
  }, {
    "film": f[6]["_id"],
    "note": 4,
    "commentaire": "Pas mal.",
    "source": "IMDb",
    "auteur": "Paul Smith"
  }, {
    "film": f[7]["_id"],
    "note": 5,
    "commentaire": "Un film qui m'a marqué.",
    "source": "Allociné",
    "auteur": "John Doe"
  }, {
    "film": f[7]["_id"],
    "note": 1,
    "commentaire": "Un film à oublier.",
    "source": "IMDb",
    "auteur": "Sir Headache"
  }, {
    "film": f[8]["_id"],
    "note": 5,
    "commentaire": "Un film exceptionnel.",
    "source": "Allociné",
    "auteur": "John Doe"
  }, {
    "film": f[8]["_id"],
    "note": 5,
    "commentaire": "Un film à voir absolument.",
    "source": "IMDb",
    "auteur": "Jane Doe"
  }, {
    "film": f[9]["_id"],
    "note": 5,
    "commentaire": "Un film exceptionnel.",
    "source": "Allociné",
    "auteur": "John Doe"
  }, {
    "film": f[9]["_id"],
    "note": 5,
    "commentaire": "Un film à voir absolument.",
    "source": "IMDb",
    "auteur": "Jane Doe"
  }, {
    "film": f[10]["_id"],
    "note": 5,
    "commentaire": "Un film exceptionnel.",
    "source": "Allociné",
    "auteur": "John Doe"
  }, {
    "film": f[10]["_id"],
    "note": 5,
    "commentaire": "Un film à voir absolument.",
    "source": "IMDb",
    "auteur": "Jane Doe"
  }, {
    "film": f[11]["_id"],
    "note": 4,
    "commentaire": "Un film intéressant.",
    "source": "Allociné",
    "auteur": "John Doe"
  }, {
    "film": f[11]["_id"],
    "note": 3,
    "commentaire": "Pas mal, mais peut mieux faire.",
    "source": "IMDb",
    "auteur": "Jane Doe"
  }, {
    "film": f[12]["_id"],
    "note": 5,
    "commentaire": "Un chef-d'œuvre du cinéma.",
    "source": "Allociné",
    "auteur": "John Doe"
  }, {
    "film": f[12]["_id"],
    "note": 4,
    "commentaire": "Un film captivant.",
    "source": "IMDb",
    "auteur": "Jane Doe"
  }, {
    "film": f[0]["_id"],
    "note": 5,
    "commentaire": "Un film inoubliable.",
    "source": "Allociné",
    "auteur": "John Doe"
  }, {
    "film": f[1]["_id"],
    "note": 5,
    "commentaire": "Un film à voir absolument.",
    "source": "IMDb",
    "auteur": "Jane Doe"
  }, {
    "film": f[2]["_id"],
    "note": 4,
    "commentaire": "Un film intéressant.",
    "source": "Allociné",
    "auteur": "John Doe"
  }, {
    "film": f[3]["_id"],
    "note": 3,
    "commentaire": "Pas mal, mais peut mieux faire.",
    "source": "IMDb",
    "auteur": "Jane Doe"
  }, {
    "film": f[4]["_id"],
    "note": 5,
    "commentaire": "Un film exceptionnel.",
    "source": "Allociné",
    "auteur": "John Doe"
  }, {
    "film": f[5]["_id"],
    "note": 5,
    "commentaire": "Un film à voir absolument.",
    "source": "IMDb",
    "auteur": "Jane Doe"
  }, {
    "film": f[6]["_id"],
    "note": 4,
    "commentaire": "Un film intéressant.",
    "source": "Allociné",
    "auteur": "John Doe"
  }, {
    "film": f[7]["_id"],
    "note": 3,
    "commentaire": "Pas mal, mais peut mieux faire.",
    "source": "IMDb",
    "auteur": "Jane Doe"
  }
]);
a = db.avis.find();

db.villes.insert_many([
  {
    "nom_ville": "Paris"
  }, {
    "nom_ville": "Lyon"
  }, {
    "nom_ville": "Marseille"
  }, {
    "nom_ville": "Toulouse"
  }, {
    "nom_ville": "Nice"
  }, {
    "nom_ville": "Nantes"
  }, {
    "nom_ville": "Strasbourg"
  }, {
    "nom_ville": "Montpellier"
  }, {
    "nom_ville": "Bordeaux"
  }, {
    "nom_ville": "Lille"
  }, {
    "nom_ville": "Rennes"
  }, {
    "nom_ville": "Reims"
  }, {
    "nom_ville": "Le Havre"
  }, {
    "nom_ville": "Cergy"
  }, {
    "nom_ville": "Toulon"
  }, {
    "nom_ville": "Grenoble"
  }, {
    "nom_ville": "Dijon"
  }, {
    "nom_ville": "Angers"
  }, {
    "nom_ville": "Nîmes"
  }, {
    "nom_ville": "Villeurbanne"
  }, {
    "nom_ville": "Saint-Denis"
  }, {
    "nom_ville": "Le Mans"
  }, {
    "nom_ville": "Aix-en-Provence"
  }, {
    "nom_ville": "Clermont-Ferrand"
  }, {
    "nom_ville": "Brest"
  }, {
    "nom_ville": "Tours"
  }, {
    "nom_ville": "Limoges"
  }, {
    "nom_ville": "Amiens"
  }, {
    "nom_ville": "Annecy"
  }, {
    "nom_ville": "Perpignan"
  }, {
    "nom_ville": "Boulogne-Billancourt"
  }, {
    "nom_ville": "Metz"
  }, {
    "nom_ville": "Besançon"
  }, {
    "nom_ville": "Orléans"
  }, {
    "nom_ville": "Saint-Denis"
  }, {
    "nom_ville": "Argenteuil"
  }, {
    "nom_ville": "Rouen"
  }, {
    "nom_ville": "Montreuil"
  }, {
    "nom_ville": "Mulhouse"
  }, {
    "nom_ville": "Caen"
  }, {
    "nom_ville": "Saint-Paul"
  }, {
    "nom_ville": "Nancy"
  }, {
    "nom_ville": "Nouméa"
  }, {
    "nom_ville": "Tourcoing"
  }, {
    "nom_ville": "Roubaix"
  }, {
    "nom_ville": "Nanterre"
  }, {
    "nom_ville": "Vitry-sur-Seine"
  }, {
    "nom_ville": "Avignon"
  }, {
    "nom_ville": "Créteil"
  }, {
    "nom_ville": "Poitiers"
  }, {
    "nom_ville": "Dunkerque"
  }, {
    "nom_ville": "Aubervilliers"
  }, {
    "nom_ville": "Versailles"
  }, {
    "nom_ville": "Asnières-sur-Seine"
  }, {
    "nom_ville": "Courbevoie"
  }, {
    "nom_ville": "Colombes"
  }, {
    "nom_ville": "Aulnay-sous-Bois"
  }
]);
v = db.villes.find();

db.cinemas.insert_many([
  {
    "nom": "UGC Ciné Cité Les Halles",
    "adresse": "7 Place de la Rotonde",
    "ville": v[0]["_id"],
    "salles": [
      {
        "nom": "Salle 1",
        "nombre_places": 400,
        "films_diffuses": [
          {
            "film": f[0]["_id"],
            "date_diffusion": "2021-08-01 14:00",
            "nombre_entrees": 150
          }, {
            "film": f[1]["_id"],
            "date_diffusion": "2021-08-01 17:00",
            "nombre_entrees": 200
          }, {
            "film": f[2]["_id"],
            "date_diffusion": "2021-08-01 20:00",
            "nombre_entrees": 80
          }, {
            "film": f[3]["_id"],
            "date_diffusion": "2021-08-01 23:00",
            "nombre_entrees": 150
          }, {
            "film": f[4]["_id"],
            "date_diffusion": "2021-08-02 14:00",
            "nombre_entrees": 150
          }, {
            "film": f[5]["_id"],
            "date_diffusion": "2021-08-02 17:00",
            "nombre_entrees": 50
          }, {
            "film": f[6]["_id"],
            "date_diffusion": "2021-08-02 20:00",
            "nombre_entrees": 130
          }, {
            "film": f[7]["_id"],
            "date_diffusion": "2021-08-02 23:00",
            "nombre_entrees": 150
          }, {
            "film": f[8]["_id"],
            "date_diffusion": "2021-08-03 14:00",
            "nombre_entrees": 150
          }, {
            "film": f[9]["_id"],
            "date_diffusion": "2021-08-03 17:00",
            "nombre_entrees": 150
          }, {
            "film": f[10]["_id"],
            "date_diffusion": "2021-08-03 20:00",
            "nombre_entrees": 150
          }
        ]
      }, {
        "nom": "Salle 2",
        "nombre_places": 300,
        "films_diffuses": [
          {
            "film": f[0]["_id"],
            "date_diffusion": "2021-08-01 14:00",
            "nombre_entrees": 150
          }, {
            "film": f[1]["_id"],
            "date_diffusion": "2021-08-01 17:00",
            "nombre_entrees": 200
          }, {
            "film": f[2]["_id"],
            "date_diffusion": "2021-08-01 20:00",
            "nombre_entrees": 80
          }, {
            "film": f[3]["_id"],
            "date_diffusion": "2021-08-01 23:00",
            "nombre_entrees": 150
          }, {
            "film": f[4]["_id"],
            "date_diffusion": "2021-08-02 14:00",
            "nombre_entrees": 150
          }, {
            "film": f[5]["_id"],
            "date_diffusion": "2021-08-02 17:00",
            "nombre_entrees": 50
          }, {
            "film": f[6]["_id"],
            "date_diffusion": "2021-08-02 20:00",
            "nombre_entrees": 130
          }, {
            "film": f[7]["_id"],
            "date_diffusion": "2021-08-02 23:00",
            "nombre_entrees": 150
          }, {
            "film": f[8]["_id"],
            "date_diffusion": "2021-08-03 14:00",
            "nombre_entrees": 150
          }, {
            "film": f[9]["_id"],
            "date_diffusion": "2021-08-03 17:00",
            "nombre_entrees": 150
          }, {
            "film": f[10]["_id"],
            "date_diffusion": "2021-08-03 20:00",
            "nombre_entrees": 150
          }
        ]
      }
    ]
  }, {
      "nom": "Cinéma 2",
      "adresse": "123 Rue du Cinéma",
      "ville": v[1]["_id"],
      "salles": [
        {
          "nom": "Salle 1",
          "nombre_places": 500,
          "films_diffuses": [
            {
              "film": f[11]["_id"],
              "date_diffusion": "2021-08-04 14:00",
              "nombre_entrees": 120
            },
            {
              "film": f[12]["_id"],
              "date_diffusion": "2021-08-04 17:00",
              "nombre_entrees": 150
            },
            {
              "film": f[0]["_id"],
              "date_diffusion": "2021-08-04 20:00",
              "nombre_entrees": 100
            },
            {
              "film": f[1]["_id"],
              "date_diffusion": "2021-08-04 23:00",
              "nombre_entrees": 130
            },
            {
              "film": f[2]["_id"],
              "date_diffusion": "2021-08-05 14:00",
              "nombre_entrees": 140
            },
            {
              "film": f[3]["_id"],
              "date_diffusion": "2021-08-05 17:00",
              "nombre_entrees": 160
            },
            {
              "film": f[4]["_id"],
              "date_diffusion": "2021-08-05 20:00",
              "nombre_entrees": 180
            },
            {
              "film": f[5]["_id"],
              "date_diffusion": "2021-08-05 23:00",
              "nombre_entrees": 200
            },
            {
              "film": f[6]["_id"],
              "date_diffusion": "2021-08-06 14:00",
              "nombre_entrees": 150
            },
            {
              "film": f[7]["_id"],
              "date_diffusion": "2021-08-06 17:00",
              "nombre_entrees": 170
            },
            {
              "film": f[8]["_id"],
              "date_diffusion": "2021-08-06 20:00",
              "nombre_entrees": 190
            },
            {
              "film": f[9]["_id"],
              "date_diffusion": "2021-08-06 23:00",
              "nombre_entrees": 210
            },
            {
              "film": f[10]["_id"],
              "date_diffusion": "2021-08-07 14:00",
              "nombre_entrees": 160
            },
            {
              "film": f[11]["_id"],
              "date_diffusion": "2021-08-07 17:00",
              "nombre_entrees": 180
            },
            {
              "film": f[12]["_id"],
              "date_diffusion": "2021-08-07 20:00",
              "nombre_entrees": 200
            }
          ]
        },
        {
          "nom": "Salle 2",
          "nombre_places": 250,
          "films_diffuses": [
            {
              "film": f[11]["_id"],
              "date_diffusion": "2021-08-04 14:00",
              "nombre_entrees": 120
            },
            {
              "film": f[12]["_id"],
              "date_diffusion": "2021-08-04 17:00",
              "nombre_entrees": 150
            },
            {
              "film": f[3]["_id"],
              "date_diffusion": "2021-08-04 20:00",
              "nombre_entrees": 100
            },
            {
              "film": f[4]["_id"],
              "date_diffusion": "2021-08-04 23:00",
              "nombre_entrees": 130
            },
            {
              "film": f[5]["_id"],
              "date_diffusion": "2021-08-05 14:00",
              "nombre_entrees": 140
            },
            {
              "film": f[6]["_id"],
              "date_diffusion": "2021-08-05 17:00",
              "nombre_entrees": 160
            },
            {
              "film": f[7]["_id"],
              "date_diffusion": "2021-08-05 20:00",
              "nombre_entrees": 180
            },
            {
              "film": f[8]["_id"],
              "date_diffusion": "2021-08-05 23:00",
              "nombre_entrees": 200
            },
            {
              "film": f[9]["_id"],
              "date_diffusion": "2021-08-06 14:00",
              "nombre_entrees": 150
            },
            {
              "film": f[0]["_id"],
              "date_diffusion": "2021-08-06 17:00",
              "nombre_entrees": 170
            },
            {
              "film": f[1]["_id"],
              "date_diffusion": "2021-08-06 20:00",
              "nombre_entrees": 190
            },
            {
              "film": f[2]["_id"],
              "date_diffusion": "2021-08-06 23:00",
              "nombre_entrees": 210
            },
            {
              "film": f[3]["_id"],
              "date_diffusion": "2021-08-07 14:00",
              "nombre_entrees": 160
            },
            {
              "film": f[4]["_id"],
              "date_diffusion": "2021-08-07 17:00",
              "nombre_entrees": 180
            },
            {
              "film": f[5]["_id"],
              "date_diffusion": "2021-08-07 20:00",
              "nombre_entrees": 200
            }
          ]
        }
      ]
    }, {
      "nom": "Cinéma 3",
      "adresse": "456 Avenue du Cinéma",
      "ville": v[2]["_id"],
      "salles": [
        {
          "nom": "Salle 1",
          "nombre_places": 220,
          "films_diffuses": [
            {
              "film": f[8]["_id"],
              "date_diffusion": "2021-08-08 14:00",
              "nombre_entrees": 160
            },
            {
              "film": f[7]["_id"],
              "date_diffusion": "2021-08-08 17:00",
              "nombre_entrees": 180
            },
            {
              "film": f[6]["_id"],
              "date_diffusion": "2021-08-08 20:00",
              "nombre_entrees": 200
            },
            {
              "film": f[5]["_id"],
              "date_diffusion": "2021-08-08 23:00",
              "nombre_entrees": 220
            },
            {
              "film": f[3]["_id"],
              "date_diffusion": "2021-08-09 14:00",
              "nombre_entrees": 150
            },
            {
              "film": f[4]["_id"],
              "date_diffusion": "2021-08-09 17:00",
              "nombre_entrees": 170
            },
            {
              "film": f[5]["_id"],
              "date_diffusion": "2021-08-09 20:00",
              "nombre_entrees": 190
            },
            {
              "film": f[3]["_id"],
              "date_diffusion": "2021-08-09 23:00",
              "nombre_entrees": 210
            },
            {
              "film": f[9]["_id"],
              "date_diffusion": "2021-08-10 14:00",
              "nombre_entrees": 160
            },
            {
              "film": f[5]["_id"],
              "date_diffusion": "2021-08-10 17:00",
              "nombre_entrees": 180
            },
            {
              "film": f[6]["_id"],
              "date_diffusion": "2021-08-10 20:00",
              "nombre_entrees": 200
            },
            {
              "film": f[7]["_id"],
              "date_diffusion": "2021-08-10 23:00",
              "nombre_entrees": 220
            },
            {
              "film": f[8]["_id"],
              "date_diffusion": "2021-08-11 14:00",
              "nombre_entrees": 160
            },
            {
              "film": f[9]["_id"],
              "date_diffusion": "2021-08-11 17:00",
              "nombre_entrees": 180
            },
            {
              "film": f[10]["_id"],
              "date_diffusion": "2021-08-11 20:00",
              "nombre_entrees": 200
            }
          ]
        },
        {
          "nom": "Salle 2",
          "nombre_places": 300,
          "films_diffuses": [
            {
              "film": f[11]["_id"],
              "date_diffusion": "2021-08-08 14:00",
              "nombre_entrees": 160
            },
            {
              "film": f[12]["_id"],
              "date_diffusion": "2021-08-08 17:00",
              "nombre_entrees": 180
            },
            {
              "film": f[1]["_id"],
              "date_diffusion": "2021-08-08 20:00",
              "nombre_entrees": 200
            },
            {
              "film": f[4]["_id"],
              "date_diffusion": "2021-08-08 23:00",
              "nombre_entrees": 220
            },
            {
              "film": f[5]["_id"],
              "date_diffusion": "2021-08-09 14:00",
              "nombre_entrees": 150
            },
            {
              "film": f[6]["_id"],
              "date_diffusion": "2021-08-09 17:00",
              "nombre_entrees": 170
            },
            {
              "film": f[7]["_id"],
              "date_diffusion": "2021-08-09 20:00",
              "nombre_entrees": 190
            },
            {
              "film": f[8]["_id"],
              "date_diffusion": "2021-08-09 23:00",
              "nombre_entrees": 210
            },
            {
              "film": f[4]["_id"],
              "date_diffusion": "2021-08-10 14:00",
              "nombre_entrees": 160
            },
            {
              "film": f[3]["_id"],
              "date_diffusion": "2021-08-10 17:00",
              "nombre_entrees": 180
            },
            {
              "film": f[2]["_id"],
              "date_diffusion": "2021-08-10 20:00",
              "nombre_entrees": 200
            },
            {
              "film": f[1]["_id"],
              "date_diffusion": "2021-08-10 23:00",
              "nombre_entrees": 220
            },
            {
              "film": f[0]["_id"],
              "date_diffusion": "2021-08-11 14:00",
              "nombre_entrees": 160
            },
            {
              "film": f[0]["_id"],
              "date_diffusion": "2021-08-11 17:00",
              "nombre_entrees": 180
            },
            {
              "film": f[0]["_id"],
              "date_diffusion": "2021-08-11 20:00",
              "nombre_entrees": 200
            }
          ]
        }
      ]
    },
    {
      "nom": "Cinéma 4",
      "adresse": "789 Boulevard du Cinéma",
      "ville": v[3]["_id"],
      "salles": [
        {
          "nom": "Salle 1",
          "nombre_places": 400,
          "films_diffuses": [
            {
              "film": f[1]["_id"],
              "date_diffusion": "2021-08-12 14:00",
              "nombre_entrees": 140
            },
            {
              "film": f[2]["_id"],
              "date_diffusion": "2021-08-12 17:00",
              "nombre_entrees": 160
            },
            {
              "film": f[3]["_id"],
              "date_diffusion": "2021-08-12 20:00",
              "nombre_entrees": 180
            },
            {
              "film": f[4]["_id"],
              "date_diffusion": "2021-08-12 23:00",
              "nombre_entrees": 200
            },
            {
              "film": f[5]["_id"],
              "date_diffusion": "2021-08-13 14:00",
              "nombre_entrees": 150
            },
            {
              "film": f[6]["_id"],
              "date_diffusion": "2021-08-13 17:00",
              "nombre_entrees": 170
            },
            {
              "film": f[7]["_id"],
              "date_diffusion": "2021-08-13 20:00",
              "nombre_entrees": 190
            },
            {
              "film": f[8]["_id"],
              "date_diffusion": "2021-08-13 23:00",
              "nombre_entrees": 210
            },
            {
              "film": f[9]["_id"],
              "date_diffusion": "2021-08-14 14:00",
              "nombre_entrees": 160
            },
            {
              "film": f[10]["_id"],
              "date_diffusion": "2021-08-14 17:00",
              "nombre_entrees": 180
            },
            {
              "film": f[11]["_id"],
              "date_diffusion": "2021-08-14 20:00",
              "nombre_entrees": 200
            },
            {
              "film": f[12]["_id"],
              "date_diffusion": "2021-08-14 23:00",
              "nombre_entrees": 220
            },
            {
              "film": f[0]["_id"],
              "date_diffusion": "2021-08-15 14:00",
              "nombre_entrees": 160
            },
            {
              "film": f[1]["_id"],
              "date_diffusion": "2021-08-15 17:00",
              "nombre_entrees": 180
            },
            {
              "film": f[2]["_id"],
              "date_diffusion": "2021-08-15 20:00",
              "nombre_entrees": 200
            }
          ]
        },
        {
          "nom": "Salle 2",
          "nombre_places": 250,
          "films_diffuses": [
            {
              "film": f[1]["_id"],
              "date_diffusion": "2021-08-12 14:00",
              "nombre_entrees": 140
            },
            {
              "film": f[2]["_id"],
              "date_diffusion": "2021-08-12 17:00",
              "nombre_entrees": 160
            },
            {
              "film": f[3]["_id"],
              "date_diffusion": "2021-08-12 20:00",
              "nombre_entrees": 180
            },
            {
              "film": f[4]["_id"],
              "date_diffusion": "2021-08-12 23:00",
              "nombre_entrees": 200
            },
            {
              "film": f[5]["_id"],
              "date_diffusion": "2021-08-13 14:00",
              "nombre_entrees": 150
            },
            {
              "film": f[6]["_id"],
              "date_diffusion": "2021-08-13 17:00",
              "nombre_entrees": 170
            },
            {
              "film": f[7]["_id"],
              "date_diffusion": "2021-08-13 20:00",
              "nombre_entrees": 190
            },
            {
              "film": f[8]["_id"],
              "date_diffusion": "2021-08-13 23:00",
              "nombre_entrees": 210
            },
            {
              "film": f[9]["_id"],
              "date_diffusion": "2021-08-14 14:00",
              "nombre_entrees": 160
            },
            {
              "film": f[0]["_id"],
              "date_diffusion": "2021-08-14 17:00",
              "nombre_entrees": 180
            },
            {
              "film": f[1]["_id"],
              "date_diffusion": "2021-08-14 20:00",
              "nombre_entrees": 200
            },
            {
              "film": f[2]["_id"],
              "date_diffusion": "2021-08-14 23:00",
              "nombre_entrees": 220
            },
            {
              "film": f[3]["_id"],
              "date_diffusion": "2021-08-15 14:00",
              "nombre_entrees": 160
            },
            {
              "film": f[4]["_id"],
              "date_diffusion": "2021-08-15 17:00",
              "nombre_entrees": 180
            },
            {
              "film": f[5]["_id"],
              "date_diffusion": "2021-08-15 20:00",
              "nombre_entrees": 200
            }
          ]
        }
      ]
    }
]);
c = db.cinemas.find();

