#!/usr/bin/python3
import string
from chiffrement import chiffrement

def force_brute(alphabet,texte,casser):
    """
        réalise une attaque par force brute sur le texte

        Args:
            - alphabet (string ou liste de caractere): l'alphabet
            - texte (string) : le texte à chiffrer/dechiffrer
            - casser (booleen) : indique si l'on veut effectuer un chiffrement (True) ou un dechiffrement (False).
        Returns:
            - resultat (dictionaire) : les textes obtenus après le chiffrement/dechiffrement selon les differentes clés possibles
    """
    resultats={}

    chiffrer=True
    if casser:
        chiffrer=False

    for k in range(len(alphabet)):
        resultats[k]=chiffrement(alphabet,texte,k,chiffrer)
    return resultats

def cryptanalyse_force_brute(alphabet,casser):
    """
        réalise une attaque force brute sur un un texte  saisi par l'utilisateur par la méthode de Cesar

        Args:
            - alphabet (string ou liste de caractere): l'alphabet
            - casser (booleen) : indique si l'on veut trouver tous les dechiffrements (True) ou tous les chiffrements possibles (False).
    """

    if casser:
        print("Cryptanalyser un texte par brute force\n***************************")
        texte_input="\tSaisissez le texte à attaquer\n\t>"
        texte_resultat="\tResultats"
    else:
        print("Chiffrements possible d'un texte\n*****************************")
        texte_input="\tSaisissez le texte à chiffrer\n\t>"
        texte_resultat="\tResultats"

    print("\tPour utiliser l'alphabet par defaut(",alphabet,"), laisser vide et appuyer sur Entrer ")
    alphabet_input=input("\tQuel alphabet souhaitez-vous utiliser?(les lettres en miniscules!Pas de majuscule)\n\t>")
    if alphabet_input:
        alphabet=alphabet_input

    print("\tLe texte est formé à partir des mots de l'alphabet choisi et peut contenir des lettres majuscules.")
    texte=input("\tSaisissez le texte à attaquer\n\t>")
    while not texte:
        print("le texte ne peut pas etre vide")
        texte=input("\tSaisissez le texte à attaquer\n\t>")

    resultats=force_brute(alphabet,texte,casser)

    for cle,resultat in resultats.items():
        print("clé=",cle,"=>",resultat)
        print("************************************************************************")
