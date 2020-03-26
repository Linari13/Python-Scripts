from random import *
from VerifNombre import VerifNombreDansPlage

#On récupère un entier aléatoire compris entre 1 et 100
num = randint(1,101)
#On fixe guess=0 (en dehors de la plage)
guess = 0
# Variable stockage coup précédent
previous = 0
#Initialisation Compteur coups
NbCoups = 0

while int(guess) != num:
   
    previous = int(guess)
    #print(f'Num is{num}, Guess is {guess}, Previous is {previous}, Coups are {NbCoups}')
    
    guess = input('Entrer un nombre entier et tapez Entrée : ')
    #On demande le nombre et on vérifie si l'entrée est correcte
    guess = VerifNombreDansPlage(guess,1,100)

    NbCoups += 1
    
    if (guess-num)**2 > 0:
        if NbCoups == 1:
            if (guess-num)**2 <= 100:
                print ('Warm')
            else:
                print ('Cold')
        else:
            if (guess-num)**2 <= (previous-num)**2:
                print ('Warmer')
            else:
                print('Colder')
                
print (f'Bravo!\nVous avez réussi en {NbCoups} coup(s)')