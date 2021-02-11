import pprint

tailleSac = int(input("Quel est la taille du sac ?"))
nbItem = int(input("Combien y a t-il d'item?"))
#colonne = (tailleSac+1)*[None]
tab = [[-1 for x in range(tailleSac+1)] for y in range (nbItem)]
#tab=[[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1]]
print(tab)
input()
tab[(nbItem-1)][tailleSac-1] = 0
print(tab)
itempoid = [1,2,3,1,7,3,4,2] 
itemvaleur = [4,3,5,3,8,4,2,4] 
print(itempoid,itemvaleur)
#############


def initColonne (list,nb):
    '''
    Input : list : list nb:Int
    Fonctionnement :Prend le tableau et deplace 
        les valeurs de la derniere collonne etudié dans la suivante)
    Output : list:list
    '''
    tab[nb-1] = tab[nb]
    return(tab)

def remplir_tab(tab,nb,itempoid,itemvaleur):
    print('NB',nb)
    if nb==-1:
        return(tab)
    else:
        if nb == len(tab)-1:
            if itemvaleur[nb]>tab[nb][(len(tab)+1)-itempoid[nb]]: tab[nb][(len(tab)+1)-itempoid[nb]]= itemvaleur[nb]
            #tab[nb-1] = tab[nb]
            
        else :
            for i in range((len(tab[0])-1),-1,-1):
                #print('NB',nb)
                if tab[nb+1][i] != -1 :
                    if i-itempoid[nb]>=0:
                        if tab[nb+1][i]+itemvaleur[nb] > tab[nb][i-itempoid[nb]]:
                            tab[nb][i-itempoid[nb]] = tab[nb+1][i]+itemvaleur[nb]
                    if tab[nb+1][i] > tab[nb][i]:
                        tab[nb][i] =  tab[nb+1][i] 

                print('TAB',tab)
        remplir_tab(tab,nb-1,itempoid,itemvaleur)


    
        



        
    return(tab)

print('FINI',remplir_tab(tab,nbItem-1,itempoid,itemvaleur))





            





