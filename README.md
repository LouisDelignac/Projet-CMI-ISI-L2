<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>
    # Projet-CMI-ISI-L2

Voici notre projet qui a pour but de déchiffrer les données fournies par des scientifiques travaillant sur certaines forêts des pyrénées.

On propose plusieurs visualisations, comme des sun-burst, pie-chart, ou même des graphes. 
<img src="image1.PNG" width="400">

Ceci fait office à la fois de sommaire et de "bouton" pour afficher les visualisations. 

Penchons nous d'abord sur la "Dispersion" qui,  quand on click dessus, nous amène à un graphe nous présentant le nombre de Ntot (nombre de glands) par année et par station.
Ce diagramme est clair car on aperçoie très rapidemment quelle station domine sur les autres selon l'année.
<img src="image2.PNG" width="400">

Ensuite, nous avons un diagramme en rayon de soleil et un pie_chart qui se ressemblent mais ne proposent pas tout à fait les mêmes visualisations.
Si on regarde le diagramme en rayon de soleil, on peut voir facilement grâce au découpage du graphe l'ensemble des Ntots d'une station dans une vallée à l'année souhaitée.
Pour accéder à cette valeur, il suffit de glisser la souris sur la partie 


La base de données est créé par le fichier "db.py" à partir d'un fichier csv.

Le fichier "db.py" va tout d'abord importer les bibliotèques et framework dont il a besoin.
Il va ensuite se connecter à la base de données "database.db".
Grâce à la fonction "execute" qui permet d'exécuter du code SQLite, on va créer 4 tables : "Valley", "Station", "Tree" et "Harvest".

La fonction "addData" va quant à elle permettre d'ajouter les données.
Cette fonction va remplir la table passée en paramètre à partir des données d'un fichier csv.
L'argument "dataList" indique les colonnes à sélectionner dans le fichier csv.
L'argument "ForeinKey" est facultatif.
Dans un premier temps elle vérifie si l'élément n'est pas déjà inséré, auquel cas elle ne fait rien.
Dans un second temps, elle récupère les données du csv ligne par ligne et les insère dans la table passée en argument.

</body>
</html>
