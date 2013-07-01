import modules as mo
import random
rtrn = mo.KeyTracker(mo.sf.Keyboard.RETURN)

#! Flip the cards.
	#! Flipped card needs to follow base as child.
#! Positions for player 1 and player 2.
###

#Load all card textures in advance.
def load_cards():
	card_texs = []
	for i in range(10):
		string = "img/card/test/%s.png" % i
		tex = mo.sf.Texture.load_from_file(string)
		card_texs.append(tex)
	return card_texs

card_texs = load_cards()
card_back = mo.sf.Texture.load_from_file("img/card/test/back.png")

class Card:
	#Each individual card.
	name = ""

	#gfx
	base = None
	base_flip = None

	def __init__ (self, id = 0):
	#Grab the card id and grab the respective graphics for it.
		self.id = id

		self.base = mo.MySprite(card_texs[id])
		self.base.w = 100
		self.base.position = 100, 100
		self.base_flip = mo.MySprite(card_back)

	def flip(self):
	#Flip the graphic for the card over.
		print "flipped"

	def draw(self):
		self.base.draw()


class Deck:
	#Each player's deck.
	cards = []

	def __init__(self):
	#Generate the cards.
		for i in range(9):
			self.cards.append(Card(i))
		self.shuffle()

	def shuffle(self):
	 #Shuffle the deck, randomizing the card positions.
		random.shuffle(self.cards)

	def deal(self):
	#Deal a card, remove it from the deck.
		if len(self.cards) > 0:
			card = self.cards[0]
			del self.cards[0]
			return card
		return None


class Hand:
	#Each player's hand.
	cards = []
	_Deck = None

	def __init__ (self, Deck):
		self._Deck = Deck

	def deal(self, amt=1):
	#Deals card(s) from the deck and puts it in the hand.
		for i in range(amt):
			card = self._Deck.deal()
			if card != None:
				self.cards.append(card)
		self.organize()

	def organize(self):
	#Organizes the cards in the hand.
		#Creates the boundary for the hand.
		x = 50
		box = (x, 450, mo.SCREEN_WIDTH - (x*2), 100)
		self.cards[0].base.box.boundary = box

		#Neatens the cards in the boundary.
		card_gfx = [c.base for c in self.cards]
		self.cards[0].base.box.spread_x(card_gfx)

	#

	def draw(self):
		for c in self.cards:
			c.draw()

###

#Create deck.
d = Deck()
print [i.id for i in d.cards]
#Add cards to hand.
h = Hand(d)
h.deal(100)
print [i.id for i in h.cards]

for c in h.cards:
	c.flip()


running = True
while running:
	#Logic
	if mo.quit(): running = False
	if rtrn.pressed():
		pass

	#Animation
	#

	#Video
	mo.window.clear(mo.sf.Color.BLACK)
	#
	h.cards[0].base.box.draw()
	h.draw()
	#
	mo.window.display()