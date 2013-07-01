from twisted.internet import reactor
from twisted.internet.protocol import \
	Protocol, ServerFactory, ClientFactory
from twisted.internet.task \
	import LoopingCall
import json
FPS = 60.0

import modules as mo
rtrn = mo.KeyTracker(mo.sf.Keyboard.RETURN)

#Test
#Hand drawn graphics is the same on both sides, with player and opponent switched.
#All actions are performed at the same time. (Drawing card, showing card)

#! Make card graphics.

#


#

def game_loop():
	#Logic
	if mo.quit():
		tick.stop()
		reactor.stop()

	if rtrn.pressed():
		pass

	#Animation
	#

	#Video
	mo.window.clear(mo.sf.Color.WHITE)
	#

	#
	mo.window.display()

tick = LoopingCall(game_loop)
tick.start(1.0/FPS)

reactor.run()