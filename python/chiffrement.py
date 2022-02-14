#!/usr/bin/python3
import string

def chiffrement(alphabet,texte,cle,chiffrer):
    """
        Chiffre/Dechiffre un texte par la méthode de Cesar

        Args:
            - alphabet (string ou liste de caractere): l'alphabet
            - texte (string) : le texte à chiffrer/dechiffrer
            - cle (int) : la clé utilisée pour chiffrer/dechiffrer le texte
            - chiffrer (booleen) : indique si l'on veut effectuer un chiffrement (True) ou un dechiffrement (False).
        Returns:
            - resultat (string) : le texte obtenu après le chiffrement/dechiffrement
    """
    resultat=""
    if not chiffrer:
        cle=cle*(-1)
    for caractere in texte:
        caractere_lower = caractere.lower()
        if caractere_lower in alphabet:
            index_nouveau_caractere=(alphabet.index(caractere_lower)+cle)%len(alphabet)
            if caractere.isupper():
                resultat+=alphabet[index_nouveau_caractere].upper()
            else:
                resultat+=alphabet[index_nouveau_caractere]
        else:
            resultat+=caractere
    return resultat

def chiffrer_texte(alphabet,chiffrer):
    """
        Chiffre/Dechiffre un texte saisi par l'utilisateur par la méthode de Cesar

        Args:
            - alphabet (string ou liste de caractere): l'alphabet
            - chiffrer (booleen) : indique si l'on veut effectuer un chiffrement (True) ou un dechiffrement (False).
        Returns:
            - resultat (string) : le texte obtenu après le chiffrement/dechiffrement
    """
    if chiffrer:
        print("Chiffrer un texte\n*********************")
        texte_input="\tSaisissez le texte à chiffrer\n\t>"
        texte_resultat="\tTexte chiffré"
    else:
        print("Déchiffrer un texte\n**********************")
        texte_input="\tSaisissez le texte à déchiffrer\n\t>"
        texte_resultat="\tTexte déchiffré"

    print("\tPour utiliser l'alphabet par defaut(",alphabet,"), laisser vide et appuyer sur Entrer ")
    alphabet_input=input("\tQuel alphabet souhaitez-vous utiliser?(les lettres en miniscules!Pas de majuscule)\n\t>")
    if alphabet_input:
        alphabet=alphabet_input

    cle=int(input("\tQuelle clé(un entier) souhaitez-vous utiliser?(ex:3)\n\t>"))

    print("\tLe texte est formé à partir des mots de l'alphabet choisi et peut contenir des lettres majuscules.")
    texte=input(texte_input)
    while not texte:
        print("le texte ne peut pas etre vide")
        texte=input(texte_input)

    resultat=chiffrement(alphabet,texte,cle,chiffrer)
    print(texte_resultat,"\n\t>",resultat)
