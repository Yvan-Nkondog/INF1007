# -*- coding: utf-8 -*-

from pickle import FALSE, TRUE
# FONCTIONS POUR LES NOTES
def sacalaire_positif(a):
    if type(a)==int and a >= 0:
        return TRUE
    else:
        print(f'"{a}" N\'EST PAS UN SCALAIRE POSITIF')
        return FALSE

def vecteur_positif(vec):
    for value in vec:
        if type(value)!=int or value<0:
            print(f'"{vec}" N\'EST PAS UN VECTEUR POSITIF')
            return TRUE
    return FALSE

def vecteur_valide(vec):
    for value in vec:
        valide = True
        if type(value) != int or value < -1:
            print(f'CE VECTEUR N\'EST PAS VALIDE')
            valide = False
    return valide

def matrice_valide(matrice):
        for i in range(len(matrice)):
            if len(matrice) != len(matrice[i]):
                print ('MATRICE NON CARRÉE')
                return FALSE

        if not vecteur_valide(matrice[i]):
            return FALSE

        return TRUE


def indiceMinimum(vec):
    #To do: Trouve l’indice et la valeur minimum dans un vecteur              
    #NOTE
    if not vecteur_valide(vec):
        raise TypeError("Les entrées du vecteur ne sont pas du type désiré ou au moins " \
        "l'une des valeurs est inférieure à -1.")
    
    # Retourner (-1, -1) si toutes les valeurs dans le vecteur sont égales à -1.
    if sum(vec) == -1 * len(vec):
        return -1, -1

    indice_min = 0
    valeur_min = float('inf')
    
    for i in range(len(vec)):
        if (vec[i] != -1) and (vec[i] < valeur_min):
            valeur_min = vec[i]
            indice_min = i

    return indice_min, valeur_min
    
def noeudMinimalNonVisitesDeNoeud(matrice, noeud, noeuds_vis):
    #NOTE
    if not matrice_valide(matrice):
        raise TypeError("La matrice n'est pas carrée.") 
   
    for i in range(len(matrice)):
        if not vecteur_valide(matrice[i]):
            raise TypeError("Les entrées du vecteur ne sont pas du type désiré ou au moins " \
            "l'une des valeurs est inférieure à -1.")
        
    if not sacalaire_positif(noeud):
        raise TypeError("La valeur noeud doit être un entier positif.") 
    
    if not vecteur_positif(noeuds_vis):
        raise ValueError("Les entrées du vecteur ne sont pas du type désiré ou au moins " \
            "l'une des valeurs est inférieure à 0.")
    
    if noeud not in noeuds_vis:
       raise IndexError("Le noeud n'existe pas dans la matrice.")
    # 1) extraire la ligne du neoud de la matrice
    ligne_visite = matrice[noeud][:]
               
    # 2) affecter -1 pour chaque noeud des noeuds_vis de la ligne
    for nd in noeuds_vis:
        ligne_visite[nd] = -1

    # 3) Trouve l’indice et la valeur minimum de la ligne
    return indiceMinimum(ligne_visite)


def noeudMinimalNonVisites(matrice,noeuds_vis):
    #NOTE
    matrice_valide(matrice)
    vecteur_positif(noeuds_vis)
    #To do: Cherche le poids minimum entre un des nœuds visités et un de ses nœuds voisins
    #To do: utiliser la fonction noeudMinimalNonVisitesDeNoeud(matrice, noeud, noeuds_vis)
    if not matrice_valide(matrice):
        raise TypeError("La matrice n'est pas carrée.") 
   
    for i in range(len(matrice)):
        if not vecteur_valide(matrice[i]):
            raise TypeError("Les entrées du vecteur ne sont pas du type désiré ou au moins " \
            "l'une des valeurs est inférieure à -1.")
        
    if not vecteur_positif(noeuds_vis):
        raise ValueError("Les entrées du vecteur ne sont pas du type désiré ou au moins " \
            "l'une des valeurs est inférieure à 0.")

    # Initialiser la variable "resultat" avec des paramètres correspondant à la première ligne.
    noeud_depart = noeuds_vis[0]
    noeud_arrive, poids = noeudMinimalNonVisitesDeNoeud(matrice, noeud_depart, noeuds_vis)
    resultat = noeud_depart, noeud_arrive, poids

    # Itérer afin de mettre à jour la variable résultat, selon le poids minimum.
    for noeud in noeuds_vis:
        indice_noeud, poids = noeudMinimalNonVisitesDeNoeud(matrice, noeud, noeuds_vis)
        if poids < resultat[2]:
            resultat = noeud, indice_noeud, poids

    # Extraire le noued de départ et le noeud d'arrivée ayant le poids minimum de la variable
    # résultat et retourner ces valeurs.
    return resultat[0:2]
    

def noeudsVoisins(matrice, noeud):
    matrice_valide(matrice)
    sacalaire_positif(noeud)
    noeuds_voisin = []
    poids = []
    #To do: Cherche les nœuds voisins et leur poids par rapport à un nœud initial.
    


def dijkstra(matrice, depart, arrive):
    #NOTE
    matrice_valide(matrice)
    sacalaire_positif(depart)
    sacalaire_positif(arrive)
    # To do: Calcule le plus court chemin entre un nœud de départ et un nœud d’arrivée.
    
        
    #Trouver le noeud voisin de distance minimun par rapport au noeud courant
        
    return None, None


if __name__ == '__main__':
    vec     = [-1, 4, 6, -1, -1, 3, 5]
    indice, minimum = indiceMinimum(vec)
    txt = "la valeur minimale du vecteur est {} à la position {}"
    print(txt.format(minimum, indice))
    
    matrice = [[-1, 20, 56, -1], [20, -1, 12, 17], [56, 12, -1, -1], [-1, 17, -1, -1]]
    noeud   = 1
    noeuds_vis = [1]
    indice, minimum = noeudMinimalNonVisitesDeNoeud(matrice, noeud, noeuds_vis)
    txt = "le poids minimum du noeud non visités est {} à la position {}"
    print(txt.format(minimum, indice))
    
    matrice = [[-1, 20, 56, -1], [20, -1, 12, 17], [56, 12, -1, -1], [-1, 17, -1, -1]]
    noeud   = 1
    noeuds_vis = [1, 2, 3]
    indice, minimum = noeudMinimalNonVisitesDeNoeud(matrice, noeud, noeuds_vis)
    txt = "le poids minimum du noeud non visités est {} à la position {}"
    print(txt.format(minimum, indice))
    
    matrice = [[-1, 20, 56, -1], [20, -1, 12, 17], [56, 12, -1, -1], [-1, 17, -1, -1]]
    noeud = 1
    noeudsVoisins(matrice, noeud)
    noeuds, poids = noeudsVoisins(matrice, noeud)
    txt = "les noeuds voisin sont {} et leur poids {} rapport à un noeud {}"
    print(txt.format(noeuds, poids, noeud))
    
    
    matrice = [[-1, 20, 56, -1], [20, -1, 12, 17], [56, 12, -1, -1], [-1, 17, -1, -1]]
    noeud = 3
    noeuds, poids = noeudsVoisins(matrice, noeud)
    txt = "les noeuds voisin sont {} et leur poids {} rapport à un noeud {}"
    print(txt.format(noeuds, poids, noeud))
    
    matrice = [[-1, 20, 56, -1], [20, -1, 12, 17], [56, 12, -1, -1], [-1, 17, -1, -1]]
    depart  = 0
    arrive  = 3
    indice, prédécesseurs = dijkstra(matrice, depart, arrive)
    txt = "la distance la plus cours entre un noeud de départ {} et un noeud d’arrivée {} est {} avec les prédécesseurs {}"
    print(txt.format(depart, arrive, indice, prédécesseurs))
        