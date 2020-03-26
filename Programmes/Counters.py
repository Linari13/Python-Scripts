#Counters
from collections import Counter

"""on créer une liste"""
l =(1,1,1,1,1,2,2,2,3,3,2,4,5,6,7,5,4,6,3,9,5,7,1,2,9,7,8,5,5,4,4)

"""la fonction Çounter renvoie un dictionaire indiquant le nombre d'utterance pour chaque chiffre"""
print(Counter(l))

"""meme chose pour une chaine"""
s = "J'ai la patate"
print(Counter(s))

"""compter le nombre d'utterance de chaque mot dans une phrase(chaine)"""
s = "je vais bien, super bien, je vais mieux"
mots = s.split() #on isole chaque mots
print(Counter(mots)) #on compte et on affiche l'utterance de chaque mots

c = Counter(mots) #on affecte le resultat du compteur de mot a une variable (Dic)
print(c.most_common(3)) #on affiche les 3 mots les plus utilisés

"""total de mots"""
print(sum(c.values()))

""" Autre fonction avec les compteurs"""
c.clear()                       #reset all counts
list(c)                         #list unique elements
set(c)                          #convert to a set
dict(c)                         #Convert to a dictionary
c.items()                       #convert to a list of (elem, cnt) pairs
Counter(dict(list_of_pairs))    #convert from a list of (elem, cnt)
c.most_common()[:-n-1:-1]       #n least common elements
c += Counter()                  # remove zero and negative counts