import modules as mo

path = "img/card/"
card_tex = mo.sf.Texture.load_from_file(path + "trophy.png")
class Card:
	type = None

	def __init__(self):
		self.g = mo.MySprite(card_tex)
		self.g.position(100, 100)
		self.g.resize.h(100)

	def draw(self):
		self.g.draw()