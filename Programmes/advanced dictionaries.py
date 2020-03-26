d = {'k1':1,'k2':2}

"""Créer un dictionnaire auto """
print({x:x**2 for x in range(10)})

print({k:v**2 for k,v in zip(['a','b'],range(10))})

"""récupérer les éléments d'un dictionnaire"""
for k in d.items():
    print(k)
"""récupérer les valeurs d'un dictionnaire"""
for k in d.values():
    print(k)
"""récupérer les clés d'un dictionnaire"""
for k in d.keys():
    print(k)