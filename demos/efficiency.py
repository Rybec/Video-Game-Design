import sys
from pympler.asizeof import asizeof

class Arrays(object):
	def __init__(self, num=100):
		self.pos = [(2, 2) for i in xrange(num)]
		self.name = ["My Name" for i in xrange(num)]
		self.level = [1 for i in xrange(num)]
		self.c = ["fighter" for i in xrange(num)]

class Char(object):
	def __init__(self):
		self.pos = (2, 2)
		self.name = "My Name"
		self.level = 1
		self.c = "fighter"
		
a = Arrays(1000)
c = [Char() for i in xrange(1000)]

print asizeof(a)
print asizeof(c)

