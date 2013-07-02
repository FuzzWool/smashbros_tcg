#Goto is absolute regardless of origin/size

import modules as mo
rtrn = mo.KeyTracker(mo.sf.Keyboard.RETURN)
a = mo.KeyTracker(mo.sf.Keyboard.A)

tex = mo.sf.Texture.load_from_file("img/test/test.png")
sprites = []
for i in range(2):
	i = len(sprites)
	sprite = mo.MySprite(tex)
	sprite.clip.set(25, 25)
	sprite.clip.use(i, 0)
	sprite.origin = sprite.w/2, sprite.h/2###
	if i == 0:
		sprite.scale(2, 2)
		sprite.goto = 200, 200
	else:
		sprite.goto = 200, 200
	sprites.append(sprite)

sprites[0].children = sprites[1:]

for s in sprites:
#!!! - Absolute, so the 0th sprite has it's goto changed.
	print s.goto, s.position

running = True
while running:
	#Logic
	if mo.quit(): running = False
	if rtrn.held():
		sprites[0].w += 1
		sprites[0].h += 1

	if a.pressed():
	#!!! - Absolute, so resizing changes the goto.
		for s in sprites:
			print s.goto, s.size

	#Video
	mo.window.clear(mo.sf.Color.WHITE)
	#
	for s in sprites:
		s.draw()
	#
	mo.window.display()