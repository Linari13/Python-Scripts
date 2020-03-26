s = 'Hello Word'

"""Capitalize first letter in a string"""
print(s.capitalize())

"""Capitalize all letter in string"""
print(s.upper())

"""Lowercase all letters"""
print(s.lower())

"""Compter une lettre"""
print(s.count('o'))

"""find the index of a letter in a string"""
s.find('o')

"""Centrer une string entre des characteres"""
print(s.center(20,'z'))

"""afficher les tabs"""
print('hello\thi')

t= 'hello'

"""verifier si tous les characteres sont alphanumeriques"""
print(t.isalnum())

"""Verifier si tous les characteres sont des lettres"""
print(t.isalpha())

"""Verifier si tous les characteres sont des minuscules"""
print(t.islower())

"""Verifier si tous les characteres sont des espaces"""
print(s.isspace())

"""Verifier si tous les commencent par une majuscule"""
print(s.istitle())

"""Verifier si tous les characteres sont des majuscules"""
print(s.isupper())

"""Verifier si la string fini avec une/des lettre donnée"""
print(s.endswith('o'))

"""Separer la string a un charactere donné"""
print(s.split('l'))

"""Separer la string et afficher l'élement séparant"""
print(s.partition('l'))
