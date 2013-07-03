import optparse
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

def determine_player():
	#Grab and return player number from console.
	parser = optparse.OptionParser()
	parser.add_option("--player", type="int")

	options, args = parser.parse_args()
	return vars(options)["player"]

#

class DataGrabber:
	#Stores recieved network data until grabbed.
	data = None

	def grab(self):
		d = self.data
		self.data = None
		return d
datagrabber = DataGrabber()

class myProtocol(Protocol):
	def dataReceived(self, data):
		data = json.loads(data)
		datagrabber.data = data

class myServerProtocol(myProtocol):
	def connectionMade(self):
		print "Connection made to %s"\
		% self.transport.getPeer()

		data = range(15)
		data = json.dumps(data)
		self.transport.write(data)

class myClientProtocol(myProtocol):
	pass

class myServerFactory(ServerFactory):
	protocol = myServerProtocol

class myClientFactory(ClientFactory):
	protocol = myClientProtocol

#########################################################
hand = mo.Hand("player")
hand.cards = [mo.Card(0), mo.Card(1), mo.Card(2)]
opponent = mo.Hand("opponent")
opponent.cards = [mo.Card(0), mo.Card(1), mo.Card(2)]
#########################################################
def set_up_networking(player):
	port = 1000
	print "You are Player %s!" % player

	if player==1:
		print "You're hosting."
		server = myServerFactory()
		reactor.listenTCP(port, server, interface="localhost")
	
	if player==2:
		print "You're connecting."
		client = myClientFactory()
		ip = "127.0.0.1"
		reactor.connectTCP(ip, port, client)

def game_loop():
	
	#Networking
	sent_data = datagrabber.grab()
	if sent_data != None:
		print sent_data

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

player = determine_player()
set_up_networking(player)

tick = LoopingCall(game_loop)
tick.start(1.0/FPS)

reactor.run()