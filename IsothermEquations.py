""" File with all the Isotherm equation functions"""
#from math import exp, expm1, log, log10, pow, sqrt
import numpy as np
#1
def langmuir(x, qm, ka):  
	return qm*ka*x/(1+ka*x)
#2
def freundlich(x, kf, nf):
	return kf*x**(1/nf)
#3	
def jovanovic(x, qm, k):
	return qm**(1-np.exp(k*x))
#4
def harkins(x, a, b):
	return (a/(b-np.log10(x)))**0.5
#5	
def tempkin(x, k, b, t):
	R = 8.3142
	T = 273.15 + t
	return (R*T/b)*log(k*x)
#6
def redlich(x, a, b, g):
	return (a*x)/(1+b*x**g)
#7	
def toth(x, qm, b, n):  
	return qm*x*pow((b+x**n),(-1/n))
#8	
def radke(x, qm, k, m):
	return (k*qm*x)/(1+k*x)**m
#9
def sips(x, qm, k, m):
	return (qm*(k*x)**m)/((1+k*x)**m)
#10	
def vieth(x, qm, k, b):
	return (k*x)+(qm*b*x/(1+b*x))
#11
def brouers(x, qm, k, a):
	return qm*(1-exp(-k*x**a))	