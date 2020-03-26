#Programme notes

#Enregistre et affiche une liste de choses à faire

#Variables
index = 0
continuer = 'O'
choses_a_faire =[] 

#On demande les entrées et de valider pour continuer
try:
    while (continuer == 'O' or continuer == 'o'):
        tache = input('que voulez vous ajouter à la liste ? Appuyer sur entrée pour valider : ')
        choses_a_faire.append(tache)
        continuer = input ('Appuyez sur O puis valider avec entrée pour ajouter autre chose à la liste ')
except:
    print('une erreur c\'est produite')

#Affichage de la liste
print (' ')
print('_'*30)
print ('Votre liste de Choses à faire')
print('_'*30)

for tache in choses_a_faire:
    print ('{0}. {1}'.format(index+1, tache))
    index += 1
