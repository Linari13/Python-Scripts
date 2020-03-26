## Creer un nouveau fichier texte et le ferme
with open ('/Users/fredericpena/Desktop/Animaux.txt','w') as Le_fichier:
    Le_fichier.write('Homme\n')
    Le_fichier.write('Ours\n')
    Le_fichier.write('Cochon\n')
    Le_fichier.write('Vache\n')
    Le_fichier.write('Canard\n')
    Le_fichier.write('Cheval\n')
    Le_fichier.write('Chien\n')
    Le_fichier.write('Poisson\n')
    
"""## Affiche le contenu du fichier    
with open ('/Users/fredericpena/Desktop/Animaux.txt','r') as Le_fichier:
    print(Le_fichier.read())"""

## Récupère chaque mot dans une liste et la trie
with open ('/Users/fredericpena/Desktop/Animaux.txt','r') as Le_fichier:
    La_liste = []
    for Ligne in Le_fichier:
        La_liste.append(Ligne)
    La_liste.sort()

## Réecrit le fichier dans l'ordre alphabétique    
with open ('/Users/fredericpena/Desktop/Animaux_triés.txt','w') as Le_fichier:
    for Nom_Animal in La_liste:
        Le_fichier.write(Nom_Animal)

"""## Affiche le contenu du fichier
with open ('/Users/fredericpena/Desktop/Animaux.txt','r') as Le_fichier:
    print(Le_fichier.read())"""

"""CORRECTION: --- Inclus un message d'erreur si le fichier ne s'ouvre pas ---

unsorted_file_name = 'animals.txt'
sorted_file_name = 'animals-sorted.txt'
animals = []

try:
    with open(unsorted_file_name) as animals_file:
        for line in animals_file:
            animals.append(line)
    animals.sort()
except:
    print('Could not open {}.'.format(unsorted_file_name))
try:
    with open(sorted_file_name, 'w') as animals_sorted_file:
        for animal in animals:
            animals_sorted_file.write(animal)
except:
    print('Could not open {}.'.format(sorted_file_name))
