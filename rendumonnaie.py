'''
[1,4,6]
V=8

8/1 = 8


'''
#> 
#<
sys_mon=[]
Valeur = int()

def gen_liste_pieces(tab,prix):
    '''
    Input --> tab:list, prix:int
    Output --> liste_peces:list, liste_prix:list

    Prend un systeme monétaire, le prix 
    Sort une liste avec le bon nombre de pièces permettant de faire l'algo mais aussi leurs sizes qui est de -1

    '''
    listes_pieces=[]
    liste_prix=[]
    for i in range(len(tab)):
        for j in range(prix//tab[i]):
            listes_pieces.append(tab[i])
    for i in range(len(listes_pieces)):
        liste_prix.append(-1)
    return listes_pieces, liste_prix

def pieces_necessaires(tab,prix):
    '''
    Input --> tab:list, prix:int
    Output --> list_pieces_necessaires:list

    Prends une liste avec le bon nombre de pieces, le prix qu'on va chercher
    Sors la liste ou il y a moins le moins depieces possible ou la somme est égal au prix
    '''
