#!/usr/bin/python

# everything is in classes and
# a main function is present 
# only for the presence of
# organization in the program

import scipy.special   as special
import sympy           as sp
from   numpy           import *
from   scipy.integrate import *
x = sp.Symbol('x')
class calculusComp(object):
	def getIntegFunc(self, _x):
		return 3.00 * (_x ** 2)
	def derivCalc(self, y):
		self.fx = y
		self.fxprime = self.fx.diff(x)
		print self.fxprime
	def integCalc(self, f, a, b):
		integral = quad(f, a, b)
		print integral
class physicsComp(object):
	def deltaX(self, vn, ti, ax):
		self._deltax = (vn * ti) + ((ax * (ti ** 2)) / 2)
		return self._deltax
	def deltaY(self, vn, ti, ay):
		self._deltay = (vn * ti) + ((ay * (ti ** 2)) / 2)
		return self._deltay
	def getVel(self, infx):
		self._pfx = infx
		self._vfx = self._pfx.diff(x)
		return self._vfx
class setVars(object):
	def setPhysVar(self, _x):
		return _x
	def getVN(self):
		self.vn = self.setPhysVar(3.00)
		return self.vn
	def getTI(self):
		self.ti = self.setPhysVar(5.00)
		return self.ti
	def getAX(self):
		self.ax = self.setPhysVar(4.00)
		return self.ax
	def getAY(self):
		self.ay = self.setPhysVar(-9.80)
		return self.ay
def main():
	calculus = calculusComp()
	physics = physicsComp()
	getvars = setVars()
	print physics.deltaX(getvars.getVN(), getvars.getTI(), getvars.getAX())
	print physics.deltaY(getvars.getVN(), getvars.getTI(), getvars.getAY())
if __name__ == "__main__":
	main()
