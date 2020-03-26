""" Jeu : Remplir les vides """

def Demander_mot(type_de_mot):
    """ Demande un nom puis renvoie chaine dans variable nom"""
    return input('Entrez un {} : '.format(type_de_mot))

def Ecrire_histoire ():
    """demande les entrées"""
    nom = Demander_mot('nom')
    verbe = Demander_mot('verbe')
    adj = Demander_mot('adjectif')
    
    """Écrit une histoire en fonction des entrées"""
    print ('{0} est {2}. {0} {1} la voiture.'.format(nom, verbe, adj))

Ecrire_histoire()


                                                        

                                                         
    
        
                
