#! Inheritance - Overriding, but not replacing, just adding to, a child's property as a parent
# Remember that overriding REPLACES any old functions: they cannot be retained.

class parent(object):

	def __init__(self):
		self._x = 0
	
	@property
	def x(self):
		return self._x
	@x.setter
	def x(self, arg):
		self._x = arg

class child(parent):
	
	@parent.x.getter
	def x(self):
		return self._x
	@parent.x.setter
	def x(self, arg):
		parent.x.fset(self, arg)

c = child()
print c.x
c.x = 100
print c.x