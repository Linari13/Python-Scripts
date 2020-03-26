#Creation liste de tupples
Aeroports = [('Aeroport Paris Charles de Gaules', 'CDG'), ('O\'Hare International Airport', 'ORD'), ('Denver International', 'DEN')]

#Affichage des détails
"""for Aeroport in Aeroports:
    Nom_Aeroport = Aeroport[0]
    Code_Aeroport = Aeroport[1]
    print ('le codet pour {0}est : {1}'.format(Nom_Aeroport, Code_Aeroport))"""

for (Aeroport, Code) in Aeroports:
    print ('le codet pour {0} est : {1}'.format(Aeroport, Code))
