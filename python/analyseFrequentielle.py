#!/usr/bin/python3
import string
from chiffrement import chiffrement
from bruteForce import forceBrute

def readFrequences():
    frequences={}
    f=open('frequences.txt',"r")
    fichier=f.read().strip()
    #ex : Francais=a/b/c/d/.../z;
    groupes=fichier.split(";")
    f.close()
    for groupe in groupes:
        langage=groupe.split("=")
        key=langage[0]
        value=langage[1].split("/")
        frequences[key]=value
    return frequences

def getLangues():
    return list(readFrequences().keys())

def getFrequences(alphabet,texte):
    longueurTexte=len(texte)
    frequences=[]*len(alphabet)
    for lettre in alphabet:
        nbApparition=texte.count(lettre)#ni
        frequence=nbApparition/longueurTexte*100#fi=ni/n
        frequences.append(frequence)
    return frequences

def analyseFrequentielle(langue,texte):
    alphabet=string.ascii_lowercase
    longueurAlphabet=len(alphabet)
    #frequences de la langue
    frequencesLangues=readFrequences()
    frequencesLangue=frequencesLangues[langue]
    #calcul de la frequence de chaque lettre de l'alphabet
    frequencesTexte=getFrequences(alphabet,texte)
    #on trouve tous les chiffrements possible du texte
    resultats=forceBrute(alphabet,texte,True)
    coincidence=[0]*longueurAlphabet
    for i in range(longueurAlphabet):
        #on trouve les frequences des lettres du texte
        freq=getFrequences(alphabet,resultats[i])
        k=0
        for j in range(longueurAlphabet):
            k+=freq[j]*float(frequencesLangue[j])#k+=f*fi
        coincidence[i]=k
    #la clé correspond au plus haut indice de coincidence
    cle=coincidence.index(max(coincidence))
    resultat=chiffrement(alphabet,texte,cle,False)
    return cle,resultat

def cryptanalyseFrequentielle():
    print("Cryptanalyser un texte par analyse fréquentielle\n***************************")

    langue="Français"
    langues=getLangues()

    texteLangue=""
    for i in range(len(langues)):
        texteLangue+="\t["+str(i)+"]"+langues[i]+"\n"
    print(texteLangue)
    langueInput=int(input("\tQuelle est la langue du texte d'origine?\n\t"))
    if langueInput==1:
        langue="Anglais"

    print("\tLe texte à attaquer ne doit contenir que des lettres de l'alphabet(",alphabet,") peut importe la casse")
    print("\t[0]Lire le fichier \"texteChiffre.txt\"\n\t[1]Saisir le texte\n\t")
    choix=int(input("\tQue choisissez-vous?\n\t>"))
    if choix==0:
        f=open("texteChiffre.txt","r")
        texte=f.read().strip()
        f.close()
    else:
        texte=input("\tSaisissez le texte à attaquer\n\t>")

    cle,resultat=analyseFrequentielle(langue,texte)

    print("\t>La clé est ",cle,"\n\t>",resultat)
