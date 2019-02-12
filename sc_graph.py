#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os
from sc_time import sc_time
import numpy
import matplotlib.pyplot as plt

def seismic_graph(report="sc_report.out"):

	# creando graph_sc.out
	sc_graph(report)
	# creando time_sc.out
	sc_time(report)

	archivo4=open("graph_sc.out","r")
	name = archivo4.name
	lines=archivo4.readlines()

	vec_prof = numpy.arange(0,800,5)
	vec_rms = numpy.arange(0.1,5.0,0.1)
	vec_mag = numpy.arange(0,10.0,0.1)

	########################### # sismos vs prof, rms, mag#######################
	contador = 0		
	prof = []
	rms = []
	mag = []
	error_lat = []
	error_lon = []
	error_prof = []
	
	for line in lines:
		campos = line.split(" ")
		cont = 0
		for campo in campos:
			cont += 1
			try:
				if cont == 18:
					prof.append(float(campo))
				if cont == 26:
					rms.append(float(campo))
				if cont == 30:
					mag.append(float(campo))
				if cont == 6:
					error_lat.append(float(campo))
				if cont == 14:
					error_lon.append(float(campo))
				if cont == 22:
					error_prof.append(float(campo))
			except:
				pass

	# prof vs num_sismos
	plt.figure()
	plt.hist([prof], label=["Profundidad"],bins=15)
	plt.title(u"Histograma Valores de Profundidad")
	plt.xlabel("Profundidad [km]")
	plt.ylabel(u'Número de sismos')
	plt.legend();
	plt.savefig("prof_sismos.png")

	# rms vs num_sismos
	plt.figure()
	n, bins, patches = plt.hist([rms], label=["RMS"], bins=15, log=True)
	plt.title(u"Histograma Valores de RMS")
	plt.xlabel("RMS")
	plt.ylabel(u'Número de sismos')
	plt.grid(True, which="both")
	plt.legend();
	plt.savefig("rms_sismos.png")

	# mag vs num_sismos
	plt.figure()
	plt.hist([mag], label=["Magnitud"])
	plt.title(u"Histograma Valores de Magnitud")
	plt.xlabel("Magnitud")
	plt.ylabel(u'Número de sismos')
	plt.legend();
	plt.savefig("mag_sismos.png")

	# errores en localización
	plt.figure(figsize=(12, 10))
	plt.hist([error_lat, error_lon, error_prof], label=["Latitud", "Longitud", "Profundidad"], bins=15, log=True)
	plt.title(u"Errores En Localización")
	plt.xlabel("Error (km)")
	plt.ylabel(u'Número de sismos')
	plt.grid(True, which="both")
	plt.legend();
	plt.savefig("loc_err.png")

def sc_graph(report="sc_report.out"):
	lat = float
	e_lat = float
	lon = float
	e_lon = float
	prof = float
	e_prof = float
	rms = float
	mag = float

	contenido = ''

	archivo1 = open(report, 'r')
	lines=archivo1.readlines()
	for line in lines:
		campos = line.split(',')
		i = 0
		for campo in campos:
			i += 1
			if i == 8:
				lon = campo
			if i == 9:
				e_lon = campo
			if i == 6:
				lat = campo
			if i == 7:
				e_lat = campo
			if i == 10:
				prof = campo
			if i == 11:
				e_prof = campo
			if i == 3:
				mag = campo
			if i == 12:
				rms = campo
		contenido += str(lat)+"   "+str(e_lat)+"   "+str(lon)+"   "+str(e_lon)+"   "+str(prof)+"   "+str(e_prof)+"   "+str(rms)+"   "+str(mag)+"\n"

	archivo1.close

	archivo2 = open('graph_sc.out', "w")
	archivo2.write(contenido)
	archivo2.close()

if __name__ == '__main__':
	sc_graph()
