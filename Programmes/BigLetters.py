def print_big(letter):
	"takes in a single letter (between A and F), and returns a 5x5 representation of that letter"

	#Defining lines of chars used to draw the letters
	#			 0       1       2        3      4       5       6      7        8   """
	lignes = ('  *  ',' * * ','*****','*   *','**** ',' *** ','*    ','***  ','*  * ')
	
	#Creating a "letter code" dictionary
	mon_dico = {'a':'01233','b':'43434','c':'53635','d':'78387','e':'26462','f':'26466'}

	#lower user input
	letter=letter.lower()

	#Drawing the letter
	for forme in mon_dico[letter]:
		print ( lignes(forme))
