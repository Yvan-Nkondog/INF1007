# -*- coding: utf-8 -*-
from Algo import sacalaire_positif, vecteur_positif, vecteur_valide
import random

def saisirMatrice():
    #To do: Saisit une matrice d’adjacence au clavier
    nombre_noeuds = int(input('Donner le nombre de noeuds dans la martice: '))
    nombre_poids = int(input('Donner le nombre de poids dans la martice: '))
    matrice = [[-1 for i in range(nombre_noeuds)] for j in range(nombre_noeuds)]
    for j in range(nombre_poids):
        print('Saisir le poids '+ str(j))
        start = int(input('Donner le noeud d\'extremité 1: '))
        end = int(input('Donner le noeud d\'extremité 2: '))
        poids = int(input('Saisir le poids: '))
        matrice[start][end] = matrice[end][start] = poids
    return matrice


def genereMatriceAleatoire(nb_noeuds):
    #NOTE
    sacalaire_positif(nb_noeuds)
    #To do: Génère une matrice d’adjacence de manière aléatoire
    if not(type(nb_noeuds) == int and nb_noeuds >= 0):
        print ('Le nombre de noeuds doit être un entier positif')
        return None
    matrice = []
    for i in range(nb_noeuds):
        vector = []
        for j in range(nb_noeuds):
            vector.append(-1)
        matrice.append(vector)
    for i in range(nb_noeuds):
        for j in range(nb_noeuds):
            if matrice[i][j] == (-1) and i < j and random.randint(0, 1) == 0:
                matrice[i][j] = matrice[j][i] = random.randint(1, 99)
    return matrice


def afficheChemin(predecesseurs, depart, arrive):
    #NOTE
    if predecesseurs == [0 for i in range(len(predecesseurs))]:
        print('LISTE DE PREDECESSEURS NULLE')
    vecteur_valide(predecesseurs)
    sacalaire_positif(depart)
    sacalaire_positif(arrive)
    #To do: Affiche le chemin entre un nœud de départ et d’arrivé à partir du tableau de prédécesseurs
    noeud_arrivant = arrive
    noeud = str(noeud_arrivant)+': FIN \n'
    while noeud_arrivant != depart:
        noeud= str(predecesseurs[noeud_arrivant]) + '  ==> '+ noeud
        noeud_arrivant = predecesseurs[noeud_arrivant]
    noeud = 'Le chemin à parcourir est:\n\t'+ 'DEBUT : ' + noeud
    return noeud



if __name__ == '__main__':
    saisirMatrice()
    
    nb_noeuds = 5
    matAlea = genereMatriceAleatoire(nb_noeuds)
    txt = "la matrice aleatoire est: \n\t"
    for i in matAlea:
        for j in i:
            txt += "{}\t".format(j)
        txt += "\n\t"
    print(txt)
    
    predecesseurs = [-1, 0, 0, 2, 5, 2]
    depart = 0
    arrive = 4
    afficheChemin(predecesseurs, depart, arrive)
