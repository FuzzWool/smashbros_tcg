from twisted.internet import reactor
from twisted.internet.protocol import \
	Protocol, ServerFactory, ClientFactory
from twisted.internet.task \
	import LoopingCall
import json
FPS = 60.0

import modules as mo
rtrn = mo.KeyTracker(mo.sf.Keyboard.RETURN)
#########################################################
#Networking


#########################################################
hand = mo.Hand("player")
hand.cards = [mo.Card(0), mo.Card(1), mo.Card(2)]
opponent = mo.Hand("opponent")
opponent.cards = [mo.Card(0), mo.Card(1), mo.Card(2)]
#########################################################
def game_loop():
	#Logic
	if mo.quit():
		tick.stop()
		reactor.stop()

	if rtrn.pressed():
		hand.cards[0].flip()

	#Animation
	#

	#Video
	mo.window.clear(mo.sf.Color.WHITE)
	#
	hand.draw()
	opponent.draw()
	#
	mo.window.display()

tick = LoopingCall(game_loop)
tick.start(1.0/FPS)

reactor.run()