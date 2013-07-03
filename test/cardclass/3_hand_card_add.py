#Unit Testing - Card class
import modules as mo
rtrn = mo.KeyTracker(mo.sf.Keyboard.RETURN)

class Hand:
	#The player's hand area.
	#Designed to hold multiple cards.
	cards = []; old_cards = []
	box = None

	def __init__(self, player="player"):
		#Position and card size varies between the players.
		if player == "player": scale = 0.25
		if player == "opponent": scale = 0.15
		
		w = 150
		if player == "player":
			self.position = w, mo.SCREEN_HEIGHT - 600*scale
		if player == "opponent":
			self.position = w, 10

		self.size = mo.SCREEN_WIDTH-w*2, 600*scale
		self.scale = scale

	def _check_cards_edit(self):
	#Cards are resozed and aligned every change.
		if self.old_cards != self.cards:
			#Adjust size.
			cards = [c.base for c in self.cards]
			for s in cards:
				s.size = 450*self.scale, 600*self.scale
			#Adjust alignment.
			if len(self.cards) >= 1:
				cards[0].box.position = self.position
				cards[0].box.size = self.size
				cards[0].box.center_row(cards)

		self.old_cards = self.cards[:]

	def draw(self):
		self._check_cards_edit()
		self.cards[0].base.box.draw()###
		for c in self.cards:
			c.draw()

hand = Hand("player")
hand.cards = [mo.Card(0), mo.Card(1), mo.Card(2)]
opponent = Hand("opponent")
opponent.cards = [mo.Card(0), mo.Card(1), mo.Card(2)]
#########################################################
running = True
while running:

	#Logic
	if mo.quit(): running = False
	if rtrn.pressed():
		hand.cards.append(mo.Card(5))

	#Animation
	#

	#Video
	mo.window.clear(mo.sf.Color.WHITE)
	#
	hand.draw()
	opponent.draw()
	#
	mo.window.display()