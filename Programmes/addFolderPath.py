"""Ajouter chemin d'accès"""

def modsPersos():
    
    ## Programme pour ajouter le chemin d'accès
    ## du fichier regroupant les modules créés

    import os
    import sys


    ## on vérifie si l'adresse y est déjà ajoutée
    ## on demande confirmation

    print ('Here\'s where you installed python: {}\n'.format(os.environ['PYTHONPATH']))
    Adresse = input('Enter your own modules folder\'s path:\n')

    try:
        if Adresse in sys.path:
            print('\nThis folder\'s path is already registred')
        else:
            Confirm = input('\nAre you sure you want to add this path to python\'s syspath list?\nPlease confirm by pressing \"Y\" and then enter: ')
            if Confirm == 'Y':
                sys.path.append(Adresse)
                print ('\nThe path has been registered successfully')
        print ('-- Good bye! --')
    
    except:
        print ('Error')

if __name__ == '__modsPersos__':
    modsPersos()
