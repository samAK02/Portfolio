# Encryption 

Ce programme ouvre un fichier d'entrée ("data.txt"), 
effectue une simple opération de chiffrement sur chaque caractère alphabétique en le décalant et le multipliant, 
puis écrit le résultat dans un fichier de sortie ("Output.txt").

## Ouverture des fichiers :

- Le programme ouvre un fichier en mode lecture ("data.txt") et vérifie s'il a été ouvert correctement. S'il y a une erreur, le programme affiche un message d'erreur et se termine.
- Un autre fichier est ouvert en mode écriture ("Output.txt").

## Traitement du fichier d'entrée :

- Le programme lit chaque caractère du fichier d'entrée un par un à l'aide de la boucle while jusqu'à atteindre la fin du fichier (EOF).
- Pour chaque lettre lue, le programme effectue une opération d'encryption.
- La lettre transformée est ensuite écrite dans le fichier de sortie.

## Fermeture des fichiers:

- Une fois le traitement terminé, les fichiers d'entrée et de sortie sont fermés.

## Affichage d'un message de fin :

- Le programme affiche un message indiquant que l'encryption est terminée et que le fichier de sortie ("Output.txt") a été créé.
