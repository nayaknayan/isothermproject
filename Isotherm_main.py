"""Retrieving, Calculating and plotting isotherm data for batch adsorption kinetics"""
import csv
import urllib2
import matplotlib.pyplot as plt
import numpy as np
import xlrd
from scipy.optimize import curve_fit
import pandas as pd
#import IsothermEquations as ie
import iso_calc as ic

 
# Read data from csv file
table = pd.read_csv('iso_test.csv')

# Store data into variables
xdata = np.array(table.astype(float)['Ce'])
ydata = np.array(table.astype(float)['Qe'])

# Read and store guess parameters for two parameter isotherms
pl0 = table['lang'][0:2]
pf0 = table['freund'][0:2]
ph0 = table['harkins'][0:2]

# Read and store guess parameters for three parameter isotherms
pr0 = table['redlich'][0:3]
prp0 = table['radke'][0:3]
ps0 = table['sips'][0:3]

# Unsolved Isotherms declared variables

#pv0 = table['vieth'][0:3]
#pb0 = table['brouers'][0:3]
#pto0 = table['toth'][0:3]
#pt0 = table['tempkin'][0:2]
#pj0 = table['jovanovic'][0:2]

# Initialize legend name for plots
leg_name1 = ['Experimental data']
leg_name2 = ['Experimental data']

# Generalized Plotting function
def pl_gen(xdata, ydata, y1, y2, y3, leg_name, p_name):
	""" Generates plots for 3 parameters along with experimental data"""
	plt.plot(xdata,ydata,'bo')
	plt.plot(xdata,y1,'--')
	plt.plot(xdata,y2,'-.')
	plt.plot(xdata,y3,'*-')
	plt.xlabel('Ce [mg/L]')
	plt.ylabel('Qe[mg/g]')
	plt.legend(leg_name,loc='lower right',
				ncol=2, fontsize='small',frameon=False)
	plt.savefig(p_name+'.png')
	plt.clf()
	return p_name

#Two parameter Isotherms	
yl,qml,kl,pcov_l, name_l = ic.calc_lang(xdata,ydata,pl0)
leg_name1.append (name_l)

yf,k,n,pcov_f, name_l = ic.calc_freund(xdata,ydata,pf0)
leg_name1.append (name_l)

yh,a,b,pcov_h, name_l = ic.calc_harkins(xdata,ydata,ph0)
leg_name1.append (name_l)

lang_freu_p = pl_gen(xdata,ydata,yl,yf,yh,leg_name1, p_name = 'lang_freund_harkins')


# Three parameter Isotherms
y_red,a_red,b_red,g_red, pcov_red, name_l = ic.calc_redlich(xdata,ydata,pr0)
leg_name2.append (name_l)

y_sips,qm_sips,k_sips,m_sips, pcov_sips, name_l = ic.calc_sips(xdata,ydata,ps0)
leg_name2.append (name_l)

y_rp,qm_rp,k_rp,m_rp, pcov_rp, name_l = ic.calc_radke(xdata,ydata,prp0)
leg_name2.append (name_l)

red_radke_sips_p = pl_gen(xdata,ydata,y_red,y_sips,y_rp,leg_name2, p_name = 'redlich_sips_radke')

"""
Generation of the result CSV file
"""
with open('isotherm_solutions.csv', 'wb') as csvfile:
	report = csv.writer(csvfile)
	report.writerow(["Ce","Qe","Qe_Langmuir","Qe_Freundlich","Qe_Harkins","Qe_Redlich","Qe_Sips","Qe_Radke"])
	rows = zip(xdata,ydata,yl,yf,yh,y_red,y_sips,y_rp)
	for row in rows:
		report.writerow(row)
	report.writerow(["Langmuir parameters"])
	report.writerow(["Qm"])
	report.writerow([qml.astype(str)])
	report.writerow(["Kl"])
	report.writerow([kl.astype(str)])
	report.writerow(["Freundlich parameters"])
	report.writerow(["Kf"])
	report.writerow([k.astype(str)])
	report.writerow(["Harkins -Jura parameters"])
	report.writerow(["A"])
	report.writerow([a.astype(str)])
	report.writerow(["B"])
	report.writerow([b.astype(str)])
	report.writerow(["Redlich-Peterson parameters"])
	report.writerow(["A"])
	report.writerow([a_red.astype(str)])
	report.writerow(["B"])
	report.writerow([b_red.astype(str)])
	report.writerow(["g"])
	report.writerow([g_red.astype(str)])
	report.writerow(["Sips parameters"])
	report.writerow(["Qm"])
	report.writerow([qm_sips.astype(str)])
	report.writerow(["Ks"])
	report.writerow([k_sips.astype(str)])	
	report.writerow(["m"])
	report.writerow([m_sips.astype(str)])	
	report.writerow(["Radke-Praustnitz parameters"])
	report.writerow(["Qm"])
	report.writerow([qm_rp.astype(str)])
	report.writerow(["Krp"])
	report.writerow([k_rp.astype(str)])	
	report.writerow(["m"])
	report.writerow([m_rp.astype(str)])	
csvfile.close()


