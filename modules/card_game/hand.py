from modules.pysfml_game.window\
	import SCREEN_WIDTH, SCREEN_HEIGHT

class Hand:
	#The player's hand area.
	#Designed to hold multiple cards.
	cards = []; old_cards = []
	box = None

	def __init__(self, player="player"):
		#goto and card size varies between the players.
		if player == "player": scale = 0.25
		if player == "opponent": scale = 0.15
		
		w = 150
		if player == "player":
			self.goto = w, SCREEN_HEIGHT - 600*scale
		if player == "opponent":
			self.goto = w, 10

		self.size = SCREEN_WIDTH-w*2, 600*scale
		self.scale = scale

	def _check_cards_edit(self):
	#Cards are resized and aligned every change.
		if self.old_cards != self.cards:
			#Adjust size.
			cards = [c.base for c in self.cards]
			for s in cards:
				s.size = 450*self.scale, 600*self.scale
			#Adjust alignment.
			if len(self.cards) >= 1:
				cards[0].box.goto = self.goto
				cards[0].box.size = self.size
				cards[0].box.center_row(cards)

		self.old_cards = self.cards[:]

	def draw(self):
		self._check_cards_edit()
		self.cards[0].base.box.draw()###
		for c in self.cards:
			c.draw()