#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Exercice 2 - code de Caesar - ROT13

# fonction d'encodage
def encode(texte):
    # definir le dictionnaire d'encodage
    rot13 = {'a':'n', 'b':'o', 'c':'p', 'd':'q', 'e':'r', 'f':'s', 'g':'t', 'h':'u', 'i':'v', 'j':'w', 'k':'x', 'l':'y', 'm':'z', 'n':'a','o':'b','p':'c','q':'d','r':'e','s':'f','t':'g','u':'h','v':'i','w':'j','x':'k','y':'l', 'z':'m', ' ':' '}
    # coder les lettres
    texte_encode=''
    for i in range(len(texte)):
        texte_encode=texte_encode+rot13[texte[i]]
    return(texte_encode)


# programme principal
def main():
    txt= input("Entrez le texte à encoder: ")
    print("texte encode : " + encode(txt))

if __name__ == '__main__':
	main()
