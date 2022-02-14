#!/usr/bin/python3
from chiffrement import chiffrer_texte
from bruteForce import cryptanalyse_force_brute
from analyseFrequentielle import cryptanalyse_frequentielle

import string

alphabet=string.ascii_lowercase#+"0123456789"
print("************************************\nBienvenue dans le projet César\n************************************")
while True:
    print("************************************************************************")
    print("[1] Chiffrer un texte\n[2] Déchiffrer un texte\n[3] Cryptanalyser un texte par brute force\n[4] Cryptanalyser un texte par analyse des fréquences\n[5] Voir tous les chiffrements possibles d'un texte\n[6] Quitter")
    action=int(input("Que voulez-vous faire?(Saisissez le numero correspondant à l'action)\n>"))

    if action==1:
        chiffrer_texte(alphabet,True)
    elif action==2:
        chiffrer_texte(alphabet,False)
    elif action==3:
        cryptanalyse_force_brute(alphabet,True)
    elif action==4:
        cryptanalyse_frequentielle()
    elif action==5:
        cryptanalyse_force_brute(alphabet,False)
    else:
        exit()
