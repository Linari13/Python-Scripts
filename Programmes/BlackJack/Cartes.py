class JeuDeCarte:

	def __init__(self, deck=[]):
		self.deck = deck

	def make_new_deck(self):
		'''Creation d'un deck complet de 52 cartes'''
		self.deck = (list(range(2,11))+['J','Q','K','A'])*4
		return self.deck

	def tire_carte(self, deck):
		from random import choice
		'''Tire une carte et la supprime du deck
			renvoie la carte tirée'''
		if self.deck != []:
			carte = choice(self.deck)
			self.deck.remove(carte)
			return carte
		else:
			print('Plus de cartes')
