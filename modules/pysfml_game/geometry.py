class Rectangle(object):
#A class designed to be used with pySFML's transformable.
#Goto is used instead of position, because position cannot be overriden.
	
	position = [0, 0]
	w, h = 0, 0

	@property
	def x(self): return self.position[0]
	@x.setter
	def x(self, arg): self.position[0] = arg

	@property
	def y(self): return self.position[1]
	@x.setter
	def y(self, arg): self.position[1] = arg

	#

	@property
	def boundary(self): return self.goto[0], self.goto[1], self.w, self.h
	@boundary.setter
	def boundary(self, args):
		self.goto = args[:2]
		self.size = args[2:]

	@property
	def goto(self): return self.x, self.y
	@goto.setter
	def goto(self, args):
		self.x, self.y = args

	@property
	def size(self): return self.w, self.h
	@size.setter
	def size(self, args):
		self.w, self.h = args

	@property
	def points(self): return self.goto[0], self.goto[1], self.goto[0] + self.w, self.goto[1] + self.h
	@points.setter
	def points(self, args):
		self.goto = args[0], args[1]
		self.w, self.h = args[2] - args[0], args[3] - args[1]

	@property
	def center(self): return self.goto[0] + (self.w/2), self.goto[1] + (self.h/2)
	@center.setter
	def center(self, args):
		self.goto = args[0] - (self.w/2), args[1] - (self.h/2) 

	def debug(self):
		print "x", self.goto[0], "y", self.goto[1], "w", self.w, "h", self.h
		print "boundary", self.boundary
		print "goto", self.goto, "size", self.size
		print "points", self.points