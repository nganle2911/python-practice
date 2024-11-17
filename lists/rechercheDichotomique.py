# Recherche dichotomique - Binary search
# Ecrire un programme qui effectue une recherche d’un nombre donné par un utilisateur de manière dichotomique dans le tableau de nombres triés suivant [1,5,7,9,12,13,15,24,56,77,79,89,91,93,99]

listeTriee = [1,5,7,9,12,13,15,24]
nb = 14

i_max = len(listeTriee)
i_min = 0
i_milieu = 0
nb_trouve = False 

print(listeTriee[i_milieu])

while i_max != i_min:
    i_milieu = int((i_max - i_min)/2)

    if nb == listeTriee[i_milieu]:
        nb_trouve = True
        break
    else: 
        if nb < listeTriee[i_milieu]:
            i_max = i_milieu - 1
        elif nb > listeTriee[i_milieu]:
            i_min = i_milieu + 1
        else: 
            nb_trouve = True
            break

if nb_trouve == True:
    print("Votre nombre fait une partie de la liste donnée")
else: 
    print("Votre nombre ne fait pas une partie de la liste donnée")   
