#Unit Testing - Card class
	#Loads an image

import modules as mo
rtrn = mo.KeyTracker(mo.sf.Keyboard.RETURN)

# tex_dir = "img/card/"
# tex = mo.sf.Texture.load_from_file(tex_dir + "trophy.png")
# card = mo.MySprite(tex)

class CardTextures:
#Keeps track of all the card textures currently loaded.

	ids = [] #current cards being used
	textures = [] #...and corrosponding textures

	def request(self, id):
	#return a texture based on id

		#See where the texture is in our ids
		found_index = None
		for i in self.ids:
			if self.ids[i] == id:
				found_index = i; break

		#If there is no texture, load it
		if found_index == None:
			#Add id, add texture.
			print "no found_index"
			self.ids.append(id)
		else:
			print "found:	" + str(found_index)
		print


CardTextures = CardTextures()

# class Card:
# #An individual card object.
# 	id = None
# 	#
# 	base = None

# 	def __init__ (self, id):
# 	#Make the sprites.
# 		self.id = id
# 		self.make_sprites()

# 	def make_sprites(self):
# 		texture = CardTextures.request(self.id)
# 		self.base = mo.MySprite(texture)

# 	def draw(self):
# 		self.base.draw()

CardTextures.request(0)
CardTextures.request(1)
CardTextures.request(0)
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

	#
	mo.window.display()