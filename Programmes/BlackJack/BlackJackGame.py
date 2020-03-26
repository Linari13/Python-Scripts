from Cartes import JeuDeCarte
from BlackJackBank import BlackJackBank
from Affichage import *
import time

titre_black_jack()
print ('\nRules:\nBeat the dealer’s hand without going over 21\n\n')

"""Création Instance"""
Bank = BlackJackBank(100)
Jeu = JeuDeCarte()
jouer = True

while jouer:
	"""On demande et traite la mise puis pause 1.5 sec"""
	bet = Bank.ask_amount()
	time.sleep(1.5)

	"""nouveau jeu de carte +  déclaration mains vides des joueurs"""
	jeu = Jeu.make_new_deck()
	jeuDealer = [ ]
	jeuJoueur = [ ]

	"""On tire les 2 premières cartes pour chaque joueurs"""
	for i in range (2):
		jeuDealer.append(str(Jeu.tire_carte(jeu)))
		jeuJoueur.append(str(Jeu.tire_carte(jeu)))

	"""initialisation variable hit (tirer une carte)"""
	hit = True

	"""Tour du joueur tant que hit et score <= 21"""
	while hit:

		affichage_tour_joueur(jeuJoueur,jeuDealer)

		if affichage_score(jeuJoueur) < 21 :
			hit = affichage_hit_or_stand()
			if hit:
				jeuJoueur.append(str(Jeu.tire_carte(jeu)))
		elif affichage_score(jeuJoueur) == 21 :
			print ('Maximum score ! Well done!')
			hit = False
			time.sleep(1.5)
		else:
			print ('YOU BUST!')
			print("YOU LOST !")
			Bank.payoff(0)
			hit = False
			time.sleep(1)

	if affichage_score(jeuJoueur) <= 21:

		affichage_tour_dealer(jeuJoueur, jeuDealer)
		time.sleep(1)

		while affichage_score(jeuDealer) < affichage_score(jeuJoueur) and affichage_score(jeuDealer) < 17:
			"""Le croupier tire une carte"""
			jeuDealer.append(str(Jeu.tire_carte(jeu)))

			affichage_tour_dealer(jeuJoueur,jeuDealer)
			time.sleep(2)

		if affichage_score(jeuJoueur) > affichage_score(jeuDealer) or affichage_score(jeuDealer) > 21:
			print ('YOU WON: CONGRATS !')
			Bank.payoff(bet*2)
		elif affichage_score(jeuJoueur) == affichage_score(jeuDealer):
			print ("DRAW!")
			Bank.payoff(bet)
		else:
			print ("YOU LOST !")
			Bank.payoff(0)

	if Bank.balance > 0:
		jouer = rejouer()
	else:
		print ("You're broke")
		break

print ('Fin de partie')







