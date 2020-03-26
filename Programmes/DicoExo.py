def display_list(Hobbies):
    #Créer une fonction pour afficher la liste
    for Nom in Hobbies:
        print ('{0} {1}.'.format(Nom, Hobbies[Nom]))
    print()

Hobbies = {
    'Paul' : 'aime faire du vélo',
    'Catherine' : 'a horreur des asperges',
    'Pierre' : 'qui roule n\'amasse pas mousse'
    }
display_list(Hobbies)

Hobbies['Catherine'] = 'ne mange pas de poulet'
Hobbies['Franck'] = 'est pilote de formule 1'


display_list(Hobbies)
