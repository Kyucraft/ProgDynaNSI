#################################### FONCTIONS ####################################

def cout_replace(x,y,i,j):
    global cout
    if x[i]==y[j]: return 0
    else: return cout['replace']

def remplir_tab(x,y,i,j):
    global cout
    global tab
    global id_j
    
    tab[i][j] = min(
    tab[i+1][j+1]+cout_replace(x,y,i,j),
    tab[i+1][j]+cout['delete'],
    tab[i][j+1]+cout['insert'])

    if i==j==0:
        return None
    elif j==0:
        remplir_tab(x,y,i-1,id_j-1)
    else:
        remplir_tab(x,y,i,j-1)

def cout_min(t):
    return t[0][0]

def prog_edit(x,y,i,j):
    global prog
    global tab
    global cout

    if i==len(x) and j==len(y):
        return ""
    elif i==len(x):
        return prog_edit(x,y,i,j+1)+"I"
    elif j==len(y):
        return prog_edit(x,y,i+1,j)+"D"
    else:
        if (tab[i+1][j+1] == tab[i][j] and cout_replace(x,y,i,j)==0) or (tab[i+1][j+1] == tab[i][j]-cout['replace']):
            return prog_edit(x,y,i+1,j+1)+"R"
        elif tab[i+1][j] == tab[i][j]-cout['delete']:
            return prog_edit(x,y,i+1,j)+"D"
        elif tab[i][j+1] == tab[i][j]-cout['insert']:
            return prog_edit(x,y,i,j+1)+"I"


#################################### CAS PARTICULIERS ####################################

ch_x = "chas"
ch_y = "cabot"
id_i = len(ch_x)
id_j = len(ch_y)
cout = {'delete':2, 'insert':3, 'replace':4}
prog = ""

tab = [[" " for _ in range(id_j+1)] for _ in range(id_i+1)]
tab[id_i][id_j] = 0
ligne_bas = cout['insert']*id_j
ligne_dte = cout['delete']*id_i

for a in range(id_j):
    tab[id_i][a] = ligne_bas
    ligne_bas -= cout['insert']

for b in range(id_i):
    tab[b][id_j] = ligne_dte
    ligne_dte -= cout['delete']

remplir_tab(ch_x,ch_y,id_i-1,id_j-1)
print(cout_min(tab))
print(prog_edit(ch_x,ch_y,0,0))
print(tab)