from math import *

from pygame.constants import GL_CONTEXT_MAJOR_VERSION

class Vector():
	x = 0
	y = 0
	z = 0

	def __init__(self, x, y, z=0):
		self.x = float(x)
		self.y = float(y)
		self.z = float(z)

    # String represntation
	def __str__(self):
		return "(%s, %s, %s)" % (self.x, self.y, self.z)

	# Produce a copy of itself
	def __copy(self):
		return Vector(self.x, self.y, self.z)

	# Signing
	def __neg__(self):
		return Vector(-self.x, -self.y, -self.z)

	# Scalar Multiplication
	#
	def __mul__(self, number):
		return Vector(self.x * number, self.y * number, self.z * number)

	def __rmul__(self, number):
		return self.__mul__(number)

	# Division
	# /
	def div(self, number):
		self.x /= number
		self.y /= number
		#self.z /= number

	# Arithmetic Operations
	# +
	def __add__(self, operand):
		self.x += operand.x
		self.y += operand.y
		#self.z += operand.z

	# -
	def __sub__(self, operand):
		self.x -= operand.x
		self.y -= operand.y
		#self.z -= operand.z
	
		# -
	def sub(self, operand):
		return Vector(self.x - operand.x, self.y - operand.y)
		#return Vector(self.x - operand.x, self.y - operand.y, self.z - operand.z)


	# Cross product
	# **
	def __pow__(self, operand):
		return Vector(self.y*operand.z - self.z*operand.y, 
			          self.z*operand.x - self.x*operand.z, 
			          self.z*operand.y - self.y*operand.x)

	# Dot Project
	# &
	def __and__(self, operand):
		return (self.x * operand.x) + \
		       (self.y * operand.y)
		""" 		
		return (self.x * operand.x) + \
		       (self.y * operand.y) + \
		       (self.z * operand.z) 
		"""
	
	def dist(self, other):
		return sqrt(pow(self.x - other.x,2)+
					pow(self.y - other.y,2)
					)
		""" 		
		return sqrt(pow(self.x - other.x,2)+
				pow(self.y - other.y,2)+
				pow(self.z - other.z,2)
				) 
		"""
 
	def limit(self,max):
		size = float(self.getMagnitude())

		if(size > max):
			self.x /= size
			self.y /= size
			#self.z /= size

	def setMagnitude(self,newMag):
		currMag = self.getMagnitude()
		new_x = self.x * (newMag/currMag)
		new_y = self.y * (newMag/currMag)
		#new_z = self.z * (newMag/currMag)

		self.x = new_x
		self.y = new_y
		#self.z = new_z


	
	def normalize(self):
		m = self.getMagnitude()
		if(m>0):
			self.x /= m
			self.y /= m
			#self.z /= m

	def getMagnitude(self):
		return (self.x**2 + self.y**2)**(.5)
		#return (self.x**2 + self.y**2 + self.z**2)**(.5)


ZERO = Vector(0,0,0)