s = set()

"""Ajouter au set"""
s.add(1)
print(s)
s.add(2)
print(s)


"""Effacer le set"""
s.clear()
print(s)

"""Copier un set"""
s = {1,2,3}
sc=s.copy()
print(sc)

"""Comparer deux sets"""
s.add(4)
print(s.difference(sc))

"""enlever les éléments d'un set dans un autre"""
s1={1,2,3}
s2={1,4,5}
s1.difference_update(s2)
print(s1)

"""removes an element from a set"""
s.discard(2)
print(s)

"""intersection d'un set (ne modifie pas le set d'origine"""
s1 = {1,2,3}
s2 = {1,2,4}
print(s1.intersection(s2))
print(s1)

"""donne au set la valeur de son intersection avec un autre set"""
print(s1.intersection_update(s2))
print(s1)

"""renvoyer True si deux sets n'ont pas d'intersection"""
s1 = {1,2}
s2 = {1,2,4}
s3 = {5}

print(s1.isdisjoint(s2))
print(s1.isdisjoint(s3))

"""Regarder si un set est contenu dans un autre"""
print(s1.issubset(s2))

"""Regarder si un set en contient un autre"""
print(s2.issuperset(s1))

"""Recuperer les elements differents d'un set à l'autre (existe aussi en version update)"""
print(s1.symmetric_difference(s2))

"""unifier deux set"""
print(s1.union(s2))
print(s1)