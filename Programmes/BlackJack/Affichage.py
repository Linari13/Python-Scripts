def efface_ecran():
	"""Envoie commande de reinitialisation de l'affichage en fonction de l'OS"""
	import platform
	import os

	if platform.system() == "Windows":
		os.system("cls")
	elif platform.system() == "Linux":
		os.system("clear")
if __name__ == '__efface_ecran__':
    efface_ecran()

def titre_black_jack():
	""" Affichage du titre"""
	print ('{:^50}'.format(' ============'))
	print ('{:^50}'.format('| BLACK JACK |'))
	print ('{:^50}'.format(' ============'))
if __name__ == '__titre_black_jack__':
    titre_black_jack()

def affichage_cartes_joueur(jeuJoueur):
	""" Affiche une representation des cartes dans la suite jeuJoueur"""
	ligneHaut = ""
	ligneCote = ""
	ligneMilieu = ""
	ligneBas = ""

	for carte in jeuJoueur:
		if carte == "10":
			ImageCarte = "1 0"
		else:
			ImageCarte = (" "+carte+" ")

		ligneHaut += "  ___ "
		ligneCote += "|   | "
		ligneMilieu += ("|"+ImageCarte+"| ")
		ligneBas += "|___| "

	print (ligneHaut,"\n",ligneCote,"\n",ligneMilieu,"\n",ligneBas)

if __name__ == '__affichage_cartes_joueur__':
    affichage_cartes_joueur(jeuJoueur)

def affichage_score(jeuJoueur):
	""" Affiche le score du joueur en tenant compte de la valeur la plus favorable des As"""

	score = 0
	for carte in jeuJoueur:
		try:
			"""si la carte est un entier on l'ajoute au score"""
			score += int(carte)
		except:
			if carte == "A":
				"""Si erreur sur entier et carte AS on ajoute 11 au score"""
				score += 11
			else:
				"""Si la carte est une figure on ajoutes 10"""
				score += 10

	if "A" in jeuJoueur and score > 21:
		score -= 10

	return score

if __name__ == '__affichage_score__':
    affichage_score(jeuJoueur)

def affichage_hit_or_stand():
	choix = input('Stand (Type \'S\') or Hit (Type \'H\') ? : ').upper()
	while choix != 'S' and choix != 'H':
		choix = input('Error! Please Type \'S\' for Stand or Type \'H\' for Hit : ').upper()

	if choix == 'H':
		return True
	else:
		return False
if __name__ == '__affichage_hit_or_stand__':
    affichage_hit_or_stand()


def affichage_tour_joueur(jeuJoueur,jeuDealer):

	""" Affichage pendant le tour du joueur"""

	efface_ecran()

	"""Affichage titre"""
	titre_black_jack()

	"""Affichage des mains et des scores de chaque joueurs"""
	"""On cache la 2ème carte du dealer"""
	affichage_cartes_joueur([str(jeuDealer[0])," "])
	print (f"Dealer\'s Score > {affichage_score(jeuDealer[0])}")
	print("\n")
	affichage_cartes_joueur(jeuJoueur)
	print (f"Player\'s Score = {affichage_score(jeuJoueur)}")

if __name__ == '__affichage_tour_joueur__':
    affichage_tour_joueur(jeuJoueur,jeuDealer)


def affichage_tour_dealer(jeuJoueur,jeuDealer):
	""" Affichage pendant le tour du dealer"""

	efface_ecran()

	"""Affichage titre"""
	titre_black_jack()

	"""Affichage des mains et des scores de chaque joueurs"""
	affichage_cartes_joueur(jeuDealer)
	print(f"Dealer\'s Score = {affichage_score(jeuDealer)}")
	print("\n")
	affichage_cartes_joueur(jeuJoueur)
	print(f"Player\'s Score = {affichage_score(jeuJoueur)}")

if __name__ == '__affichage_tour_dealer__':
    affichage_tour_dealer(jeuJoueur,jeuDealer)

def rejouer():
	"on demande au joueur si il veut tirer une autre carte ou arreter"
	continuer = input('Do you want to play another game ? (press \'Y\' or \'N\'): ').upper()
	while continuer != 'Y' and continuer != 'N':
		continuer = input('Error! Please Type \'Y\' to continue or \'N\' to stop the game : ').upper()

	if continuer == 'Y':
		return True
	else:
		return False
if __name__ == '__rejouer__':
    rejouer()