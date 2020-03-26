def titreTicTacToe():
	"""Print game Title"""
	print ('','='*13)
	print ('|','TIC TAC TOE','|')
	print ('','='*13)


def enterNomsEtPieces():

	"""Grab players name and side (X or O)"""
	pieceJoueur1 = ''

	nomJoueur1 = input('Joueur 1 what\'s your name ? ')
	pieceJoueur1 = input ('Choose your side "X" or "O" : ')
	coupsJoueur1=coupsJoueur2=''


	while pieceJoueur1 not in 'XO':
		pieceJoueur1 = input ('Choose your side "X" or "O" : ')

	nomJoueur2  = input('Joueur 2 what\'s your name ? ')
	if pieceJoueur1 == 'X':
		pieceJoueur2 ='O'
	else:
		pieceJoueur2 ='X'

	return {1:[nomJoueur1, pieceJoueur1, coupsJoueur1], 2:[nomJoueur2, pieceJoueur2, coupsJoueur2]}


def cadre(dicoCasesJouees={1:' ', 2:' ',3:' ',4:' ',5:' ',6:' ',7:' ',8:' ',9:' '}):

	"""Print game's chart"""

	print(f' {dicoCasesJouees[7]} | {dicoCasesJouees[8]} | {dicoCasesJouees[9]} ')
	print('-'*11)
	print(f' {dicoCasesJouees[4]} | {dicoCasesJouees[5]} | {dicoCasesJouees[6]} ')
	print('-'*11)
	print(f' {dicoCasesJouees[1]} | {dicoCasesJouees[2]} | {dicoCasesJouees[3]} ')


def afficheRegle():
	
	"""Print game's rules"""

	#from TicTacToeListOfFunc import cadre

	print("\n Rules :\n")
	print("1. The game is played on a grid that's 3 squares by 3 squares as follows:\n")

	cadre({1:'1', 2:'2',3:'3',4:'4',5:'5',6:'6',7:'7',8:'8',9:'9'})

	print("\n2. Each player, turn by turn, choose a case between 1 and 9 to let his mark")
	print("3. The first player to get 3 of his marks in a row (up, down, across, or diagonally) is the winner" )
	print("4. Otherwise when all 9 squares are full, the game is over \n")

	input ('Press enter when ready : ')


def verifierCoup(coupJoueur, dicoCasesJouees):

	"""returns boolean to check whether coupJoueur is a number between 1 and 9  and not in dicoCasesJouees"""

	coupValide = False

	if coupJoueur.isnumeric() == False or int(coupJoueur) not in range(1,10) or dicoCasesJouees[int(coupJoueur)] != ' ':
		print ('Please enter a number between 1 and 9 that hasn\'t been played yet')
	else:
		coupValide = True
	return coupValide



def finPartie(lstCasesJoueur):

	"""returns boolean that indicates whether the game's over"""

	partieFinie = draw = False
	combGagnantes = ('123', '456', '789', '147', '258', '369', '357', '159')

	for comb in combGagnantes:
		if comb[0] in lstCasesJoueur and comb[1] in lstCasesJoueur and comb[2] in lstCasesJoueur:
			partieFinie = True
		elif len(lstCasesJoueur) == 5:
			draw = True

	return (partieFinie, draw)

def nomDuJoueur(BoolJoueur, dicoDuJeu):
	if BoolJoueur == False:
		numJoueur = 1
	else:
		numJoueur = 2

	return numJoueur

def effaceEcran():
	import platform
	import os

	if platform.system() == "Windows":
		os.system("cls")
	elif platform.system() == "Linux":
		os.system("clear")


def TicTacToe ():
	from IPython.display import clear_output

	finDePartie = (False,False)
	BoolJoueur = False
	coupValide = False
	dicoCasesJouees = {1:' ', 2:' ',3:' ',4:' ',5:' ',6:' ',7:' ',8:' ',9:' '}

	titreTicTacToe()
	afficheRegle()

	effaceEcran()

	titreTicTacToe()
	donneesJeu = enterNomsEtPieces()


	# Tant que finDePartie est False
	while finDePartie == (False,False):
		coupValide = False
		numJoueurActif = nomDuJoueur(BoolJoueur, donneesJeu)

		effaceEcran() #Effacer Ecran
		titreTicTacToe() #AfficherTitre
		cadre(dicoCasesJouees)	#Afficher tableau

		while coupValide != True :			
			coupJoué = input (f'{donneesJeu[numJoueurActif][0]} \'s turn. \nwhat\'s your move ? : ') #Demander coup Joueur
			coupValide=verifierCoup(coupJoué, dicoCasesJouees)	#Verifier coup valide

		dicoCasesJouees[int(coupJoué)] = donneesJeu[numJoueurActif][1] #Enregistrer Coup pour affichage
		donneesJeu[numJoueurActif][2] = donneesJeu[numJoueurActif][2] + str(coupJoué) #Enregistrer Coup dans liste coup du joueur

		finDePartie = finPartie(donneesJeu[numJoueurActif][2]) #Verifier fin partie

		BoolJoueur = not BoolJoueur #changer de joueur

	effaceEcran() #Effacer Ecran
	titreTicTacToe() #AfficherTitre
	cadre (dicoCasesJouees) #Afficher tableau
	if  finDePartie == (False,True):
		print('Draw !')
	else:
		print (f'\n{donneesJeu[numJoueurActif][0]} won !\n')

TicTacToe ()