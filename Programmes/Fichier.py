
## Creer un nouveau fichier texte et le ferme
with open ('/Users/fredericpena/Desktop/Fichier_Exercice_Python.txt','w') as Le_fichier:
    Le_fichier.write('Ceci est la première ligne.\n')
    Le_fichier.write('Ceci est la deuxième ligne.\n')
    Le_fichier.write('Et finalement, voici la troisième et dernière ligne du fichier.\n')

with open ('/Users/fredericpena/Desktop/Fichier_Exercice_Python.txt','r') as Le_fichier:
    ## Défini variable Numero_ligne
    Numero_ligne = 1
    ## Lit le fichier et affiche son contenu ligne par ligne en insérant le numero de ligne avant chaque ligne
    for line in Le_fichier:
        print('{0}: {1}'.format(Numero_ligne, line.rstrip()))
        Numero_ligne += 1

