#!/usr/bin/python3
from chiffrement import chiffrerTexte
from bruteForce import cryptanalyseForceBrute
from analyseFrequentielle import cryptanalyseFrequentielle

import string

alphabet=string.ascii_lowercase#+"0123456789"
print("************************************\nBienvenue dans le projet César\n************************************")
while True:
    print("************************************************************************")
    print("[1] Chiffrer un texte\n[2] Déchiffrer un texte\n[3] Cryptanalyser un texte par brute force\n[4] Cryptanalyser un texte par analyse des fréquences\n[5] Voir tous les chiffrements possibles d'un texte\n[6] Quitter")
    action=int(input("Que voulez-vous faire?(Saisissez le numero correspondant à l'action)\n>"))

    if action==1:
        chiffrerTexte(alphabet,True)
    elif action==2:
        chiffrerTexte(alphabet,False)
    elif action==3:
        cryptanalyseForceBrute(alphabet,True)
    elif action==4:
        cryptanalyseFrequentielle()
    elif action==5:
        cryptanalyseForceBrute(alphabet,False)
    else:
        exit()
