# Cryptologie-César-python
Cryptographie ( chiffrement et dechiffrement ) et cryptanalyse du chiffrement de Cesar en Python.

## Lancement du programme principal
python3 main.py

* * L'utilisateur peut definir son propre alphabet ou laisser l'alphabet par defaut (si c'est demandé).
* Le fichier "texteAChiffrer.txt" contient un texte en clair
* Le fichier "texteChiffre.txt" contient un texte chiffré par la méthode de César

## Chiffrer et dechiffrer ( chiffrement.py )
* L'utilisateur peut definir son propre alphabet.
* Les lettres de l'alphabet doivent être en minuscule. ex:alphabet="abcdef0123!?"
* L'utilisateur doit definir un clé d chiffrement/dechiffrement.
* Le texte à traiter peut contenir des lettres majuscules. ex:Il était une Fois
* Les caracteres/lettres du texte qui ne sont pas dans l'alphabet ne sont pas modifiées lors du chiffrement/dechiffrement.
* Pour chiffrer(dechiffrer) un texte, le booleen "chiffrer" doit etre à True(False).

EX :
''from chiffrement import chiffrement
alphabet="abcdefghijklmnopqrstuvwxyz"
texte="test"
chiffrer=True
cle=3
resultat=chiffrement(alphabet,texte,cle,chiffrer)
print(resultat)''

## Attaque forceBrute
* Les lettres de l'alphabet doivent être en minuscule. ex:alphabet="abcdef0123!?"
* Le texte à traiter peut contenir des lettres majuscules. ex:"Il était une Fois"
* Les caracteres/lettres du texte qui ne sont pas dans l'alphabet ne sont pas modifiées lors du chiffrement/dechiffrement.
* Pour attaquer un texte, le booleen "casser" doit etre à True.
* Pour voir tous les chiffrements possible d'un texte, le booleen "casser" doit etre à False.

EX:
''from bruteForce import forceBrute
alphabet="abcdefghijklmnopqrstuvwxyz"
texte="test"
casser=True
resultat=forceBrute(alphabet,texte,casser)
print(resultat)''

## Attaque analyse fréquentielle
* Le texte à attaquer doit être assez long(minimum 3-4 mots differents) pour avoir un resultat correct
* L'alphabet utilisé est a...z
* Le fichier frequences.txt contient les fréquences d'apparition des lettres a...z en differentes langues
* Les fréquences d'apparition des lettres sont tirées de [wikipedia](https://fr.wikipedia.org/wiki/Fr%C3%A9quence_d%27apparition_des_lettres_en_fran%C3%A7ais)
''from analyseFrequentielle import *
texte="Ru ojdc exhjpna, élarejrc Vxwcjrpwn. Lnuj anwm vxmnbcn, jsxdcjrc Oujdknac. Xw exhjpn yxda lqjwpna, wxw mn urnd, vjrb m’rménb, anwlqéarbbjrc Cjrwn. Nc br l’écjrc cxdc un lxwcajran. Mjwb dw pdrmn mn exhjpn bda u’Rwmxlqrwn mn 1923, jyaèb dwn yjpn mn ydkurlrcé yxda uj vjrbxw Armnc & Lrn, javdarna jd lnwcan mn Qjwxr, oxdawrbbjwc javnb nc vdwrcrxwb mn lqjbbn nc mn pdnaan, cxdb jllnbbxranb yxda lqjbbndab nc cxdarbcnb, yrbcxuncb jdcxvjcrzdnb xd ljajkrwnb, jejwc vêvn zdn wn bxrc éexzdén uj ... "
langue="Français"
cle,resultat=analyseFrequentielle(langue,texte)
print(resultat)''
