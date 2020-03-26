année = input ("saississez une année : ")                                               # On demande l'année
année = int (année)                                                                     # Definition variable entier
if année % 400 == 0 or (année % 100 != 0 and année % 4 == 0):                           # Si "multiple de 400" ou "Non multiple de 100 quand multiple de 4"
        print ("année bissextile")                                                      # message réponse positive
else: print (" année non bissextile")                                                   # sinon message réponse négative
