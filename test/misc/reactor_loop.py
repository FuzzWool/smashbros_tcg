from twisted.internet.task \
	import LoopingCall, TaskFinished
from twisted.internet import reactor
FPS = 2.0

import modules as mo
rtrn = mo.KeyTracker(mo.sf.Keyboard.RETURN)

#Network testing
	#! Generate a random hand on both sides.
	# First, print the hand
	# Wait a second and then print the other hand

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