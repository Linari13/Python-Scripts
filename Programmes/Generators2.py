#Creation fonction qui crée une liste de cube de 1 a n
def creer_cubes(n):
    result = []
    for i in range (n):
        result.append(i**3)
    return result
#La meme fonction avec yield (generateur)
def creer_cube2(n):
    for i in range (n):
        yield i**3

n = int(input('jusqu\'à quel chiffre?'))
#imprimer toute la liste
print(creer_cubes(n))

#imprimer chaque valeur
for x in creer_cubes(n):
    print(x)

for x in creer_cube2(n):
    print(x)

# fonction simple utilisant uin generateur
def simple_gen():
    for x in range(3):
       yield x

# Attribution des chiffrs generés ent utilisation de next pour afficher chaque chiffre
g = simple_gen()
print(next(g))
print(next(g))
print(next(g))

#Convertir un objet en un iterable
#prenons une suite:
s = "hello"

s_iter = iter(s)
print(next(s_iter))
print(next(s_iter))
print(next(s_iter))
print(next(s_iter))
