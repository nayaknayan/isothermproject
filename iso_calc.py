from scipy.optimize import curve_fit
import pandas as pd
import numpy as np
import IsothermEquations as ie

""" Two Parameter Isotherms"""
# Langmuir Calculator
def calc_lang(xdata, ydata, p0):	
	popt, pcov = curve_fit(ie.langmuir, xdata, ydata, p0)
	qm = popt[0]
	k = popt[1]
	y = ie.langmuir(xdata, popt[0], popt[1])
	l_name = 'Langmuir fitted'
	return y, qm, k, pcov, l_name

# Freundlich Calculator
def calc_freund(xdata, ydata, p0):
	popt, pcov = curve_fit(ie.freundlich, xdata, ydata, p0)
	kf = popt[0]
	nf = popt[1]
	y = ie.freundlich(xdata, popt[0], popt[1])
	l_name = 'Freundlich fitted'
	return y, kf, nf, pcov, l_name

#Jovanovich Calculator	
def calc_jovanovic(xdata, ydata, p0):	
	popt, pcov = curve_fit(ie.jovanovic, xdata, ydata, p0, maxfev=10000)
	qmj = popt[0]
	kj = popt[1]
	y = ie.jovanovic(xdata, popt[0], popt[1])
	l_name = 'Jovanovich fitted'
	return y, qm, k, pcov, l_name

#Harkins Calculator
def calc_harkins(xdata, ydata, p0):
	popt, pcov = curve_fit(ie.harkins, xdata, ydata, p0)
	A = popt[0]
	B = popt[1]
	y = ie.harkins(xdata, popt[0], popt[1])
	l_name = 'Harkins-Jura fitted'
	return y, A, B, pcov, l_name

#Tempkin calculator
def calc_tempkin(xdata, ydata, p0):	
	popt, pcov = curve_fit(ie.tempkin, xdata, ydata, p0)
	b = popt[0]
	k = popt[1]
	y = ie.tempkin(xdata, t, popt[0], popt[1])
	l_name = 'Tempkin fitted'
	return y, b, k, pcov, l_name


""" Three Parameter Isotherms"""
#Redlich Peterson isotherm
def calc_redlich(xdata, ydata, p0):
	popt, pcov = curve_fit(ie.redlich, xdata, ydata, p0)
	a = popt[0]
	b = popt[1]
	g = popt[2]
	y = ie.redlich(xdata, popt[0], popt[1], popt[2])
	l_name = 'Redlich-Peterson fitted'
	return y, a, b, g, pcov, l_name

#Toth isotherm
def calc_toth(xdata, ydata, p0):
	popt, pcov = curve_fit(ie.toth, xdata, ydata, p0)
	qm = popt[0]
	b = popt[1]
	n = popt[2]
	y = ie.toth(xdata, popt[0], popt[1], popt[2])
	l_name = 'Toth fitted'
	return y, qm, b, n, pcov, l_name

#Radke-Praustnitz isotherm
def calc_radke(xdata, ydata, p0):
	popt, pcov = curve_fit(ie.radke, xdata, ydata, p0)
	qm = popt[0]
	k = popt[1]
	m = popt[2]
	y = ie.radke(xdata, popt[0], popt[1], popt[2])
	l_name = 'Radke-Prausnitz fitted'
	return y, qm, k, m, pcov, l_name
	
#SIPS isotherm
def calc_sips(xdata, ydata, p0):
	popt, pcov = curve_fit(ie.sips, xdata, ydata, p0)
	qm = popt[0]
	k = popt[1]
	m = popt[2]
	y = ie.sips(xdata, popt[0], popt[1], popt[2])
	l_name = 'SIPS fitted'
	return y, qm, k, m, pcov, l_name
	
#Vieth-Sladek isotherm
def calc_vieth(xdata, ydata, p0):
	popt, pcov = curve_fit(ie.vieth, xdata, ydata, p0)
	qm = popt[0]
	k = popt[1]
	b = popt[2]
	y = ie.vieth(xdata, popt[0], popt[1], popt[2])
	l_name = 'Vieth-Sladek fitted'
	return y, qm, k, b, pcov, l_name
	
#Brouers-Sotolongo isotherm
def calc_brouers(xdata, ydata, p0):
	popt, pcov = curve_fit(ie.brouers, xdata, ydata, p0)
	qm = popt[0]
	k = popt[1]
	a = popt[2]
	y = ie.brouers(xdata, popt[0], popt[1], popt[2])
	l_name = 'Brouers-Sotolongo fitted'
	return y, qm, k, a, pcov, l_name
