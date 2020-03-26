l = [1,2,3]

"""Ajouter un élément à une liste"""
l.append(4)
print(l)

"""Compter le nombre d'occurence d'un élément dans ma liste"""
print(l.count(10))
print(l.count(1))

"""rajouter les éléments d'une list à une autre (sans rajouter la liste elle même"""
x = [1,2,3]
x.append([4,5,6])
print(x)

x = [1,2,3]
x.extend([4,5,6])
print(x)

"""renvoie l'index d'un element"""
print(l.index(2))

"""insert un élément à l'index specifié en premier"""
l.insert(2,'inséré')
print(l)

"""enlève et renvoie l'élément correspondant à l'index specifié d'une liste"""
"""si l'indice n'est pas specifié : enlève et renvoie le dernier élément"""
ele = l.pop(2)
print(ele)
print(l)

"""enlève la premiere occurence d'un élement de la liste"""
l.remove(4)
print(l)

l.insert(1, 3)
print(l)
l.remove(3)
print(l)

"""inverse la liste"""
l.reverse()
print(l)

"""Trie la liste"""
l.sort()
print(l)