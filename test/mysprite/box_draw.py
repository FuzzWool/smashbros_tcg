#Remember to check movements with a low FPS!

#Add children to MySprite.
	#Add box.
		#Box will centralize the positioning of sprites.
			#Sprites will remain centered upon any size changes in a box.


import modules as mo
rtrn = mo.KeyTracker(mo.sf.Keyboard.RETURN)

tex = mo.sf.Texture.load_from_file("img/test/test.png")
sprites = []
for i in range(5):
	sprite = mo.MySprite(tex)
	sprite.clip.set(25, 25)
	sprite.clip.use(i, 0)
	sprite.position = 100 + (i * 50), 100
	sprites.append(sprite)

sprites[0].children = sprites[1:]

###Box testing###
sprites[0].box.boundary = 100, 100, 200, 50
###

running = True
while running:
	#Logic
	if mo.quit(): running = False
	if rtrn.pressed():
		sprites[0].box.boundary = 0, 100, 100, 200

	#Animation
	#

	#Video
	mo.window.clear(mo.sf.Color.WHITE)
	#
	sprites[0].box.draw()####
	for s in sprites:
		s.draw()
	#
	mo.window.display()