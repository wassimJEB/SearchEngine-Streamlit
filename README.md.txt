Lors de la construction d'un moteur de recherche d'images, nous devons d'abord indexer notre ensemble de données. L'indexation d'un ensemble de données est le processus de quantification de notre ensemble de données en utilisant un descripteur d'image pour extraire les caractéristiques de chaque image. 

Le descripteur d'image régit la manière dont l'image est quantifiée. 

 Les caractéristiques, quant à elles, sont le résultat d'un descripteur d'image. Lorsque vous introduisez une image dans un descripteur d'image, vous obtenez des caractéristiques à l'autre extrémité. 

En termes simples, les caractéristiques (ou vecteurs de caractéristiques) sont simplement une liste de nombres utilisés pour représenter et quantifier les images de manière abstraite. 

# SOLUTION


Dans ce projet, pour la partie indexation, nous avons choisi Edge histogram descriptor 
, Color Structure Descriptor (CSD) et Scalable Color Descriptor (SCD) et MongoDB pour le stockage des données et la recherche.  

Pour la partie recherche, nous avons utilisé l'algorithme de classification non supervisée "Kmeans".et pour visualiser les résultats on a utilisé Streamlit le framework basé sur python 
## Architecture de la solution proposée 

### Edge histogram descriptor 

C'est l'une des méthodes les plus utilisées pour la détection des formes. Il représente essentiellement la fréquence relative d'occurrence de 5 types d'arêtes dans chaque zone locale appelée sous-image ou bloc d'image 

### Kmeans 

Étant donné des points et un nombre entier k, le problème consiste à diviser les points en k groupes, souvent appelés clusters, de façon à minimiser une certaine fonction.  

Cette fonction est la distance d'un point à la moyenne des points de son groupe. cluster. 


