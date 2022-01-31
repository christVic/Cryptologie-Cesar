#!/usr/bin/python3
import string

def chiffrement(alphabet,texte,cle,chiffrer):
    resultat=""
    if not chiffrer:
        cle=cle*(-1)
    for caractere in texte:
        if caractere in alphabet:
            indexNewCar=(alphabet.index(caractere)+cle)%len(alphabet)
            resultat+=alphabet[indexNewCar]
        #si un caractere n'est pas dans l'alphabet
        else:
            if caractere.isupper():
                car=caractere.lower()
                indexNewCar=(alphabet.index(car)+cle)%len(alphabet)
                resultat+=alphabet[indexNewCar].upper()
            else:
                resultat+=caractere
    return resultat

def chiffrerTexte(alphabet,chiffrer):
    if chiffrer:
        print("Chiffrer un texte\n*********************")
        texteInput="\tSaisissez le texte à chiffrer\n\t>"
        texteResultat="\tTexte chiffré"
        ftexte="texteAChiffrer.txt"
    else:
        print("Déchiffrer un texte\n**********************")
        texteInput="\tSaisissez le texte à déchiffrer\n\t>"
        texteResultat="\tTexte déchiffré"
        ftexte="texteChiffre.txt"

    print("\tPour utiliser l'alphabet par defaut(",alphabet,"), laisser vide et appuyer sur Entrer ")
    alphabetInput=input("\tQuel alphabet souhaitez-vous utiliser?(les lettres en miniscules!Pas de majuscule)\n\t>")
    if alphabetInput:
        alphabet=alphabetInput

    cle=int(input("\tQuelle clé(un entier) souhaitez-vous utiliser?(ex:3)\n\t>"))

    print("\tLe texte est formé à partir des mots de l'alphabet choisi et peut contenir des lettres majuscules.")
    print("\t[0]Lire le fichier \"",ftexte,"\"\n\t[1]Saisir le texte\n\t")
    choix=int(input("\tQue choisissez-vous?\n\t>"))
    if choix==0:
        f=open(ftexte,"r")
        texte=f.read().strip()
        f.close()
    else:
        texte=input(texteInput)

    resultat=chiffrement(alphabet,texte,cle,chiffrer)
    print(texteResultat,"\n\t>",resultat)
