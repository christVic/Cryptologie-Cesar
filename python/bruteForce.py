#!/usr/bin/python3
import string
from chiffrement import chiffrement

def forceBrute(alphabet,texte,casser):
    resultats={}

    chiffrer=True
    if casser:
        chiffrer=False

    for k in range(len(alphabet)):
        resultats[k]=chiffrement(alphabet,texte,k,chiffrer)
    return resultats

def cryptanalyseForceBrute(alphabet,casser):
    if casser:
        print("Cryptanalyser un texte par brute force\n***************************")
        texteInput="\tSaisissez le texte à attaquer\n\t>"
        texteResultat="\tResultats"
        ftexte="texteChiffre.txt"
    else:
        print("Chiffrements possible d'un texte\n*****************************")
        texteInput="\tSaisissez le texte à chiffrer\n\t>"
        texteResultat="\tResultats"
        ftexte="texteAChiffrer.txt"

    print("\tPour utiliser l'alphabet par defaut(",alphabet,"), laisser vide et appuyer sur Entrer ")
    alphabetInput=input("\tQuel alphabet souhaitez-vous utiliser?(les lettres en miniscules!Pas de majuscule)\n\t>")
    if alphabetInput:
        alphabet=alphabetInput

    print("\tLe texte est formé à partir des mots de l'alphabet choisi et peut contenir des lettres majuscules.")
    print("\t[0]Lire le fichier \"",ftexte,"\"\n\t[1]Saisir le texte\n\t")
    choix=int(input("\tQue choisissez-vous?\n\t>"))
    if choix==0:
        f=open(ftexte,"r")
        texte=f.read().strip()
    else:
        texte=input("\tSaisissez le texte à attaquer\n\t>")

    resultats=forceBrute(alphabet,texte,casser)

    for cle,resultat in resultats.items():
        print("clé=",cle,"=>",resultat)
        print("************************************************************************")
