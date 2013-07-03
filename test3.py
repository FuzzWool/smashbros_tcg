import modules as mo
rtrn = mo.KeyTracker(mo.sf.Keyboard.RETURN)

tex = mo.sf.Texture.load_from_file("img/test/test.png")
sprites = []
def add_sprite():
	i = len(sprites)
	sprite = mo.MySprite(tex)
	sprite.clip.set(25, 25)
	sprite.clip.use(i, 0)
	sprite.position = 100 + (i * 50), 100
	sprites.append(sprite)

for i in range(1):
	add_sprite()

sprites[0].children = sprites[1:]

###Box testing###
box = sprites[0].box
box.boundary = 100, 100, 600, 100
sprites[0].box.center_row()
###

running = True
while running:
	#Logic
	if mo.quit(): running = False
	if rtrn.pressed():
		add_sprite()
		sprites[0].children = sprites[1:]
		sprites[0].box.center_row()

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