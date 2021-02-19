demande = int(input("Combien d'items tu veux ? "))
items = dict()
compteur = 1
for i in range(demande):
    taille = int(input("Quelle taille pour l'élément n°{} ? ".format(compteur)))
    valeur = int(input("Quelle valeur pour l'élément n°{} ? ".format(compteur)))
    items[compteur] = {
        "taille": taille,
        "valeur": valeur
    }
    compteur += 1
#items = {1: {'taille': 4, 'valeur': 5}, 2: {'taille': 2, 'valeur': 8}, 3: {'taille': 1, 'valeur': 3}}

def creation_tab(taille_sac,items):
    '''
    :param taille_sac: la taille du sac
    :param items: dictionnaire contenant les items avec leur taille et valeur
    :return: tableau sacado complété
    '''
    nb_items = len(list(items.keys()))
    tab = [[0 if i!=0 else j for i in range(nb_items+1)] for j in range(taille_sac+1)]
    element = nb_items
    while element != 0:
        for i in range(taille_sac):
            if tab[i][element] != 0:
                if i - items[element]["taille"] >= 0 and tab[i][element]+items[element]["valeur"] > tab[i - items[element]["taille"]][element]:
                    tab[i - items[element]["taille"]][element] = tab[i][element]+items[element]["valeur"]
        if tab[taille_sac - items[element]["taille"]][element] < items[element]["valeur"]:
            tab[taille_sac - items[element]["taille"]][element] = items[element]["valeur"]
        if element != 1:
            for i in range(taille_sac):
                if tab[i][element] != 0:
                    tab[i][element - 1] = tab[i][element]
        element -= 1
    for element in tab: print(element)
    return tab
def reconstruction(tab, items):
    '''
    :param tab: tableau sacado complété
    :param items: dictionnaire contenant les items avec leur taille et valeur
    :return: liste optimale des objets à prendre
     '''
    liste_objets = []
    index_max = 0
    for i in range(len(tab)):
        if tab[i][1]>tab[index_max][1]:
            index_max = i
    for i in range(1, len(list(items.keys()))):
        if tab[index_max][i] == tab[index_max][i+1]:
            continue
        liste_objets.append(i)
        index_max += items[i]["taille"]
    if sum(liste_objets) + items[len(tab[-1]) - 1]["taille"] <= len(tab):
        liste_objets.append(len(tab[-1]) - 1)
    return liste_objets

tablo = creation_tab(5, items)
print(reconstruction(tablo, items))

