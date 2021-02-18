#Groupe : Enzo , Florian , Justin , Célyan , Issam
import pprint

############################################################################################### Fonctions

def remplir_tab(tab,nb,itempoid,itemvaleur):
    '''
    Entree: tab (list), nb (int), itempoid (list), itemvaleur (list)
    Sortie: tab(list)

    -> Prend en entrée le tab initial, rempli de '-1' désignant des cases vides, et procède au remplissage du tableau via la méthode vue en classe
    '''

    print('NB',nb)

    #Cas dans lequel on a entièrement remonté le tableau, et ainsi rempli toutes les colonnes. La fonction prend fin.
    if nb==-1:
        return(tab)
    
    #Sinon, la fonction tourne.
    else:
        #Cas dans lequel nous nous situons dans la dernière colonne du tableau. Comme nous n'avons pas de colonne antérieure sur laquelle nous calquer, celle-ci subit un traitement simplifié.
        #Soit l'on prend l'objet correspondant, soit on ne le prend pas.
        if nb == len(tab)-1:
            if itemvaleur[nb]>tab[nb][(len(tab)+1)-itempoid[nb]]: tab[nb][(len(tab)+2)-itempoid[nb]]= itemvaleur[nb]
            
        #Sinon, on viendra se calquer sur les colonnes antérieures. Soit on prend, soit on ne prend pas, toujours en partant des cases remplies de la colonne précédente (principe vu en classe).
        else :
            for i in range((len(tab[0])-1),-1,-1):
                #Si, sur notre ligne, dans la colonne précédente, la case n'est pas vide...
                if tab[nb+1][i] != -1 :
                    #Si l'on peut prendre l'objet correspondant à notre colonne...
                    if i-itempoid[nb]>=0:
                        #Si, une fois remplie, la case a une plus grande valeur qu'avant...
                        if tab[nb+1][i]+itemvaleur[nb] > tab[nb][i-itempoid[nb]]:
                            tab[nb][i-itempoid[nb]] = tab[nb+1][i]+itemvaleur[nb]
                    #On repasse la condition de valeur plus importante, mais c'est ici seulement pour le "on ne prend pas l'objet" (qui passe forcément, en terme de taille de sac)
                    if tab[nb+1][i] > tab[nb][i]:
                        tab[nb][i] =  tab[nb+1][i] 

                print('TAB',tab)

        #On rappelle la fonction (principe récursif), même si le programme aurait pu être fait sous forme d'une boucle        
        tab = remplir_tab(tab,nb-1,itempoid,itemvaleur)
        
    return(tab)


def reconstruction(tab,itempoid,nb,sac):
    '''
    Entree: tab (list), itempoid (list), nb (int), sac (int)
    Sortie: obj (list)

    -> Prend en entrée le tab généré via la fonction 'remplir_tab' et parcourt celui-ci pour déterminer quels objets sont à prendre pour atteindre la valeur max
    '''

    pos_max = -1
    val_max = -1
    #On parcourt la première colonne (indice 0) du tableau, pour y trouver la valeur maximale et conserver, dans 'pos_max', son indice.
    for x in range(sac+1):
        if tab[0][x] > val_max:
            val_max = tab[0][x]
            pos_max = x

    j = 0
    i = pos_max
    obj = []

    #On réalise la reconstruction, en partant de la case, dans la colonne 0, d'indice i (=pos_max). Le principe de reconstruction est le même que celui vu en classe.
    while j <= nb:
        #print(j,i," ",obj)
        
        #Premier cas, on se situe tout en bas à droite du tableau. On ne prend pas l'objet de la colonne finale, et on incrémente j de 1 pour sortir de la boucle.
        if j==nb and i==sac:
            j+=1
        #Deuxième cas, on se situe sur la dernière colonne, mais pas tout en bas. On prend l'objet de la colonne finale, et on incrémente j de 1 pour sortir de la boucle.
        elif j==nb and i<sac:
            obj.append(j)
            j+=1
        #Sinon, on va faire le test classique. Si la valeur voisine, dans la colonne suivante, est la même, on ne prend pas l'objet et on se décalle seulement d'une colonne. Sinon, on prend l'objet, on se
        #décalle d'une colonne, et on descend, dans celle-ci, de la taille de l'objet sélectionné.
        else:
            if tab[j+1][i] == tab[j][i]:
                j+=1
            else:
                obj.append(j)
                i += itempoid[j]
                j+=1
        
    return obj


############################################################################################### Variables

'''
tailleSac = int(input("Quel est la taille du sac ?"))
nbItem = int(input("Combien y a t-il d'item?"))
'''
itempoid = [1,2,3,1,7,3,4,2] 
itemvaleur = [4,3,5,3,8,4,2,4]
tailleSac = 10
nbItem = len(itempoid)

tab = [[-1 for x in range(tailleSac+1)] for y in range (nbItem)]

print(tab)
input()
print(nbItem,nbItem-1,tailleSac,tailleSac-1)
tab[(nbItem-1)][tailleSac] = 0

print('FINI',remplir_tab(tab,nbItem-1,itempoid,itemvaleur))

print('Objets à prendre : ',reconstruction(tab,itempoid,nbItem-1,tailleSac))
