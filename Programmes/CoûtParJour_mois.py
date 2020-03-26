#Calculates the cost per day
coutJour = 0.51*24
coutMois = coutJour*30.5
budget = 918

#Displays cost of 1 server per day then per month (30.5 days)
print ('Coût 1 serveur par jour: {:.2f}'.format(coutJour),'€')
print ('Coût 1 serveur par mois: {:.2f}'.format(coutMois),'€')

#Displays cost of 20 servers per day then per month (30.5 days)
print () #Saut de Ligne
print ('Coût 20 serveur par jour: {:.2f}'.format(coutJour*20),'€')
print ('Coût 20 serveur par mois: {:.2f}'.format(coutMois*20),'€')

#Displays number of days operated according to budget (918€)
print () #Saut de Ligne
print ('un serveur peut opérer {0:.0f} jours avec un budget de {1:.2f}€.'.format(budget/coutJour, budget))

"""petit test
pour voir si les commentaires
marchent"""
