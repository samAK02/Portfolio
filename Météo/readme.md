# Météo


## Dans la partie HTML (fichier HTML) :

. Le programme crée une page web avec une balise <head> qui contient le titre "Météo" et un lien vers une feuille de style externe ("styles.css").
Dans la balise <body>, et crée une structure pour afficher les données météorologiques.
. Il y a un champ de recherche où l'utilisateur peut entrer le nom d'une ville, un bouton de recherche, une icône météo, des éléments pour afficher le nom de la ville, la température, l'humidité et la vitesse du vent.
. Il inclut également un script JavaScript en bas du corps de la page qui gère la récupération des données météorologiques et leur affichage.



## Le fichier CSS ("styles.css") :

Ici est définit le style visuel de la page, y compris le fond, la mise en page, les couleurs, la taille du texte, etc.



## Le script JavaScript :

. Utilise une clé d'API météo (apiKey) pour récupérer des données météorologiques à partir d'une URL fournie (apiUrl) via une requête HTTP asynchrone.
 
. Identifie des éléments HTML pour la recherche, l'icône météo, et d'autres informations.
 
. Définit une fonction checkWeather qui envoie une requête pour obtenir les données météorologiques de la ville entrée par l'utilisateur.

. Les données météorologiques sont extraites de la réponse et affichées dans les éléments HTML correspondants.

 
. En fonction des conditions météorologiques (telles que "Clouds", "Clear", "Rain", "Drizzle", "Mist"), l'icône météo est modifiée.




Résultat du code: 

![New York](https://github.com/samAK02/Portfolio/assets/131418700/917b562c-99aa-4e4c-88ac-0f3ca5a2e19b)


![Alger](https://github.com/samAK02/Portfolio/assets/131418700/c8937b26-95d8-4220-ba43-79170fa53ef9)
