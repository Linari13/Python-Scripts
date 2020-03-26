"""String IO"""
# The StringIO module implements an in-memory file like object.
# This object can then be used as input or output to most functions that would expect a standard file object

from io import StringIO

message = 'voici une phrase simple'

#on utilise la methode stringIO pour configurer comme objet fichier (file object)
f= StringIO(message)
#Noux aves maintenant un object qui peux etre traité comme un fichier

print(f.read())
f.write(' une deuxieme phrase dans mon fichier')
f.seek(0)
print(f.read())
