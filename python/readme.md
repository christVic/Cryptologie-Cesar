# Cryptologie-César-python
Cryptographie ( chiffrement et dechiffrement ) et cryptanalyse du chiffrement de Cesar en Python.

## Lancement du programme
python3 main.py

* Le fichier "texteAChiffrer.txt" contient un texte en clair
* Le fichier "texteChiffre.txt" contient un texte chiffré par la méthode de César

## Chiffrer et dechiffrer ( chiffrement.py )
* L'utilisateur peut definir son propre alphabet ou laisser l'alphabet par defaut.
* Les lettres de l'alphabet doivent être en minuscule. ex:alphabet="abcdef0123!?"
* L'utilisateur doit definir un clé d chiffrement/dechiffrement.
* Le texte à traiter peut contenir des lettres majuscules. ex:Il était une Fois
* Les caracteres/lettres du texte qui ne sont pas dans l'alphabet ne sont pas modifiées lors du chiffrement/dechiffrement.
* Pour chiffrer(dechiffrer) un texte, le booleen "chiffrer" doit etre à True(False).


## Attaque forceBrute
* L'utilisateur peut definir son propre alphabet  ou laisser l'alphabet par defaut.
* Les lettres de l'alphabet doivent être en minuscule. ex:alphabet="abcdef0123!?"
* Le texte à traiter peut contenir des lettres majuscules. ex:"Il était une Fois"
* Les caracteres/lettres du texte qui ne sont pas dans l'alphabet ne sont pas modifiées lors du chiffrement/dechiffrement.
* Pour attaquer un texte, le booleen "casser" doit etre à True.
* Pour voir tous les chiffrements possible d'un texte, le booleen "casser" doit etre à False.


## Attaque analyse fréquentielle
* Le texte à attaquer doit être assez long(minimum 3-4 mots differents) pour avoir un resultat correct
* L'alphabet utilisé est a...z
* Le fichier frequences.txt contient les fréquences d'apparition des lettres a...z en differentes langues
