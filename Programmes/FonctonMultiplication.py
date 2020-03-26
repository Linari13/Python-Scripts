def tablemult (nb, max=10):                     #Fonction affichant la table de multiplication de nb. Allant de nb*1 à nb*max
	i=0 					#Réinitialisation de i
	while i<=max: 			        #Tant que i<=max
		print(i, "*", nb, "=", i*nb)	#On affiche la multiplication et son résultat
		i += 1 				#Incrémentation de i par 1
