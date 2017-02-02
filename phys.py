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
def getIntegFunc(_x):
	return 3.0 * (_x ** 2)
class calculusComp(object):
	def derivCalc(self, y):
		self.fx = y
		self.fxprime = self.fx.diff(x)
		print self.fxprime
	def integCalc(self, f, a, b):
		integral = quad(f, a, b)
		print integral
def main():
	calculus = calculusComp()
	_initOpt = input("Calculation type?\n0=derivative\n1=integral\n> ")
	if ( _initOpt == 0 ):
		_fx = input("f(x)> ")
		calculus.derivCalc(_fx)
	elif ( _initOpt == 1 ):
		_fx = input("f(x)> ")
		_fa = input("a---> ")
		_tb = input("b---> ")
		calculus.integCalc(getIntegFunc, 0, 1)
if __name__ == "__main__":
	main()
