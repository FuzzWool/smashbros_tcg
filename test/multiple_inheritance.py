#! Multiple inheritance - Altering the setter attribute without changing it to a value

class A:
	a = 1
	b = 2

	@property
	def c(self):
		return self.a + self.b
	@c.setter
	def c(self, arg):
		self.a = arg
		self.b = arg

class B:
	a = 1
	b = 2

	@property
	def c(self):
		return self.a + self.b
	@c.setter
	def c(self, arg):
		self.a = arg
		self.b = arg

class C(A, B):
	
	@property
	def c(self):
		return A.c.__get__(A)

c = C()
print c.c