#Unit Testing - Card class
	#Loads an image

import modules as mo
rtrn = mo.KeyTracker(mo.sf.Keyboard.RETURN)

class CardLoader:
#Keeps track of all the card textures currently loaded.
	tex_dir = "img/test/cards/"

	ids = [] #current cards being used
	textures = [] #...and corrosponding textures

	def request(self, id):
	#return a texture based on id
	#loads it if it isn't already stored
		found_index = None
		for i in range(len(self.ids)):
			if self.ids[i] == id:
				found_index = i; break

		if found_index == None:
			found_index = len(self.ids)
			self.ids.append(id)
			new_texture = mo.sf.Texture.load_from_file\
				(self.tex_dir + str(id) + ".png")
			self.textures.append(new_texture)

		return self.textures[found_index]


CardLoader = CardLoader()

class Card:
#An individual card object.
	id = None
	#
	base = None

	def __init__ (self, id):
	#Make the sprites.
		self.id = id
		self.make_sprites()

	def make_sprites(self):
		texture = CardLoader.request(self.id)
		self.base = mo.MySprite(texture)

	def draw(self):
		self.base.draw()

card = Card(2)
#########################################################
running = True
while running:

	#Logic
	if mo.quit(): running = False
	if rtrn.pressed():
		pass

	#Animation
	#

	#Video
	mo.window.clear(mo.sf.Color.WHITE)
	#
	card.draw()
	#
	mo.window.display()