def nombres_premiers(num):

	nbr_prem = 0
	ind = 0

	# Check for 0 or 1 input
	if num<2:
		return 0

	# 2 or greater	
	else :

		#number list creation
		liste_num_prem = list(range(2,num+1))
		
		# We stop the algorythm when number used is > to square input
		while not nbr_prem > num**0.5:

			#Store the prime number we're using to shorten the whole number list
			nbr_prem = liste_num_prem [ind]

			# test all list numbers
			for nombre in list(range(2,num+1)):

				# removing number that are not prime numbers from list
				if nombre in liste_num_prem and nombre%nbr_prem == 0 and nombre!= nbr_prem :
					liste_num_prem.remove(nombre)

			#indice incrementation to use next prime number		
			ind+=1

		return (liste_num_prem)

