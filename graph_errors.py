# ---- ddsiervop@sgc.gov.co -------
# -*- coding: utf-8 -*-

import pylab as plt
import pandas as pd
import sys

try:
	# con seaborn instalado el histograma queda mas bonito
	import seaborn as sns  
	sns.set()
except:
	print "\nSe requiere la instalación del módulo seabron de python:"
	print "\tPuede instalarse con el comando: pip install seaborn"
	sys.exit()

def location_error_graphics(e_lat, e_lon, e_pro, show=False):
	""" Funcion que grafica los errores en latitud,
	longitud y profundidad en una sola grafica
	en forma de histograma.
	:param e_lat: errores en latitud
	:type e_lat: list or numpy array
	:param e_lon: errores en longitud
	:type e_lat: list or numpy array
	:param e_pro: errores en longitud
	:type e_pro: list or numpy array
	:param show: si es True muestra la grafica. Por defecto False
	:type show: boolean"""
	
	
	#fig, ax = plt.subplots()
	plt.hist([e_lat, e_lon, e_pro], label=["Latitud", "Longitud", "Profundidad"], bins=15, log=True)
	plt.title(u"Errores En Localización")
	#plt.yscale('log', nonposy='clip')
	plt.xlabel("Error (km)")
	plt.ylabel(u'Número de sismos')
	plt.grid(True, which="both")
	plt.legend();
	plt.savefig("loc_err.png")
	plt.show()
	
	if show: plt.show()


def histo(silent=False):
	"""Realiza el histograma de funcionamiento de las estaciones"""

	func_vec = []
	comp_vec = []
	sta_vec = []
	contenido3 = ''
	archivo2=open("sc_fun.out","r")
	lines = archivo2.readlines()
	for line in lines:
		line2 = line.strip().strip("(").strip(")")
		print line2
		campos = line2.split(',')
		campo2 = [campo.strip(" ").strip("\'") for campo in campos]
		new_line = ",".join(campo2) 
		contenido3 += new_line+"\n"
		cont = 0
		for campo in campos:
			cont += 1
			if cont == 5:
				func_vec.append(float(campo))
			if cont == 3:
				comp_vec.append(campo.strip("\'"))
				comp_temp = campo.strip().strip("\'")
			if cont == 2:
				sta_vec.append(campo.strip("\'"))
				sta_temp = campo.strip().strip("\'")

	print len(func_vec)

	archivo2.close()
	archivo2=open("sc_fun2.out","w")
	archivo2.write(contenido3)
	archivo2.close()

	w_graph = float(len(func_vec)*15)

	sns.set(style="whitegrid")
	# style="whitegrid"
	df = pd.read_csv("sc_fun2.out", header=None, dtype=str)
	df["station"] = df[1]+" "+df[2]
	df[4] = df[4].astype(float)

	# Initialize the matplotlib figure
	f, ax = plt.subplots(figsize=(9, 13))

	# Plot the total crashes
	sns.set_color_codes("muted")
	sns.barplot(x=4, y="station", data=df, color="yellowgreen")

	# Add a informative axis label
	ax.set_ylabel("Estaciones", weight='bold')
	ax.set_xlabel("Porcentaje de Funcionamiento", weight='bold')
	sns.despine(left=True, bottom=True)
	plt.savefig('porc_fun.png')
	
	if not silent: plt.show()

if __name__ == "__main__":

	x = 10 + 2.5*plt.randn(1000)
	y = 10 + 2.0*plt.randn(1000)
	z = 10 + 1.5*plt.randn(1000)
	
	location_error_graphics(x, y, z, show=True)
