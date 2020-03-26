t = (1,2,3)

print ('On créer un tuple t = (1,2,3) et on appelle la première valeur grace à son index')
print(t[0], '\n')
print('Cependant il peut etre dificile de se souvenir à quel index on a entrer une valeur')
print('Namedtuple assigne un nom en plus de l\'index à chaque membre du tuple\n')

from collections import namedtuple

Dog = namedtuple('Dog','age breed name')
sam = Dog(age=2, breed='Lab', name='Sammy')

print(sam)
print(sam.age)
print(sam[0])