#Unit Testing - Card class
import modules as mo
rtrn = mo.KeyTracker(mo.sf.Keyboard.RETURN)

hand = mo.Hand("player")
hand.cards = [mo.Card(0), mo.Card(1), mo.Card(2)]
opponent = mo.Hand("opponent")
opponent.cards = [mo.Card(0), mo.Card(1), mo.Card(2)]
#########################################################
running = True
while running:

	#Logic
	if mo.quit(): running = False
	if rtrn.pressed():
		for c in hand.cards:
			c.flip()

	#Animation
	#

	#Video
	mo.window.clear(mo.sf.Color.WHITE)
	#
	hand.draw()
	opponent.draw()
	#
	mo.window.display()