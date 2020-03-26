from random import *
""" Exemple de fonction utilisant les generateurs"""

#Exemple 1
def square(N):
    """Fonction qui génère le carré des chiffres d'une suite de nombre"""
    for Number in range(N):
        """Ongénère les carrés des chiffres"""
        yield Number**2

for x in square(10):
    """On affiche les carrés des chiffres de la liste"""
    print (x)

#Exemple 2
def rand_num (low,high,n):
    """fonction qui génère n chiffres aléatoires choisit entre deux valeurs fournies"""
    for Number in range(n):
        yield randint(low,high)

for num in rand_num(1,10,5):
    print(num)


#Exemple 3
s = 'hello'

"""la string n'etant pas un objet iterable on utilise la fonction iter(s) pour qu'elle puisse l'être"""
for letter in iter(s):
    print (letter)

#Exemple 4
""" Generator comprehension"""
yourList =[0,1,2,3,4,5,6,7,8,9,10,11]

def allEvens( L ):
    for number in L:
        if number % 2 == 0:
            yield number

evens = allEvens( yourList )

for numbers in evens:
    print (next(evens))
#renvoie la même chose que :

evens = ( number for number in yourList if number % 2 == 0 )
for numbers in evens:
    print (next(evens))
