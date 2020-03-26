import re

""" Prenons un exemple ou l'on cherce un mot dans une phrase"""

mots = ['premier', 'second']
phrase = 'Voici une phrase avec le mot premier, mais pas avec l\'autre mot'

print(re.search(mots[0], phrase))
print(re.search(mots[1], phrase))

for mot in mots:
    print(f'\nRecherche \"{mot}\" dans : \n \"{phrase}\"')

    #on recherche les mots:
    if re.search(mot, phrase):
        #print('\n')
        print(f'Le mot {mot} est présent')
    else:
        #print('\n')
        print(f'Le mot {mot} n\'est pas présent')

""" Séparer un phrase """
split_term = '@'
phrase = 'Votre adresse mail est-elle bien Salut@gmail.com ?'

print('\n', re.split(split_term, phrase))

"""re.findall va trouver tous des élements dans une chaine :"""

#prenons la fonction suivante:
def multi_re_find(mots, phrase):
    """affiche les mots recherchés dans un liste à partir d'une suite de charactères"""

    for mot in mots:
        print("recherche dans la phrase en utilisant le \"re check\"")
        print(re.findall(mot, phrase))
        print('\n')

test_phrase = 'sdsd..sssddd...sdddsddd...dsds...dsssss...sdddd'

test_mots = ['sd*',     #s suivi de 0 ou + d
            'sd+',      #s suivi de 1 ou + d
            'sd?',      #s suivi de 0 ou 1 d
            'sd{3}',    #s suivi de 3 d
            'sd{2,3}'   #s suivi de 2 ou 3 d
            ]

multi_re_find(test_mots, test_phrase)

test_lettres= ['[sd]',      # s ou d
               's[sd]+'     #s suivi de  1 ou plus s ou d
               ]

multi_re_find(test_lettres, test_phrase)

"""Si on veut isoler chaque mot"""
#utliser ^ avant les crochet pour trouver tout ce qui ne correspond pas aux charactères/ symboles entre les crochet
# (ex: [^!.? ] pour trouver tout ce qui n'est pas !, ., ?, ou espace)
#en ajoutant un + on va isoler des mot car on cherche la presence d'un ou plusieur charactere procscrit la la chaine

test_phrase= 'Ceci est une chaine de charactere! il y a des ponctuations. Comment les enlever?'
print(re.findall('[^!.,? ]+', test_phrase))

"""Character Ranges"""
#Pour cela des characteres compris en une lettre de l'alphabet (start)
# et une autre (end) on utilise la syntaxe suivante: [a-f]
test_phrase = 'Ceci est un exemple de phrase. Voyons su no pouvons y trouver quelques lettres.'

type_de_recherche = ['[a-z]+',      #sequence de minuscules
                    '[A-Z]+',       #sequence de majuscules
                    '[a-zA-Z]+',    #sequence de minuscules ou majuscules
                    '[A-Z][a-z]+']  #une majuscule suivie d'une minuscule

multi_re_find(type_de_recherche, test_phrase)

"""Espace codes"""
#   Code           Meaning
#   \d             a digit
#   \D             a non-digit
#   \s             Whitespace (tab, space, newline, etc.)
#   \S             non-whitespace
#   \w             alphanumeric
#   \W             non-alphanumeric

#Escapes are indicated by prefixing the character with a backslash.
#Unfortunately a backslahmust itself be escaped in normal Python strings,
# and that result in expressions that are difficult to read
#Using raw strings, created by prefixing the literal value of r, for  creationg expressions eliminates this issue

test_phrase = 'Ceci est une chaine avec des chiffres 1234 et un symbole #hashtag'
type_de_recherche = [r'\d+',    #sequence of digits
                    r'\D+',     #sequence of non-digits
                    r'\s+',     #sequence of whitespace
                    r'\S+',     #sequence of non-whitespace
                    r'\w+',     #alphanumeric characters
                    r'\W+']     #non alphanumeric

multi_re_find(type_de_recherche, test_phrase)