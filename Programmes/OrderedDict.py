#Créons deux dictionaires similaires
d1 = {}
d2 = {}

#On y ajoute les mèêmes éléments dans un ordre different
d1['a'] = 1
d1['b'] = 2

d2['b'] = 2
d2['a'] = 1

#on les compare:
print('d1=d2?')
print(d1 == d2)
print('\nLa réponse est True car le dictionnaire ne tiens pas compte \nde l\'ordre des données (random mapping).\n Pour cela il faut utiliser OrderedDict() lors de la definition du dictionaire\n')

from collections import OrderedDict

d1 = OrderedDict()
d1['a'] = 1
d1['b'] = 2

d2 = OrderedDict()
d2['b'] = 2
d2['a'] = 1

#Si on les compare maintenant:
print('d1=d2?')
print(d1 == d2)