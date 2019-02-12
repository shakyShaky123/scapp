#!/usr/bin/env python

import sys
import os


lon = float
lat = float
prof = float
mag = float
mag_gmt = float

#ruta = "/home/camilo/TEMP/scapp/"
ruta = "/Rutinas.Seiscomp/scapp/"
#ruta = "/home/camilo/scapp/"

contenido = ''

archivo1 = open('sc_report.out', 'r')
lines=archivo1.readlines()
for line in lines:
	campos = line.split(',')
	i = 0
	for campo in campos:
		i += 1
		if i == 8:
			lon = campo
		if i == 6:
			lat = campo
		if i == 10:
			prof = -float(campo)
		if i == 3:
			mag = float(campo)
			mag_gmt = mag*0.03
	contenido += str(lon)+"   "+str(lat)+"   "+str(prof)+"   "+str(mag_gmt)+"\n"

archivo1.close

archivo2 = open('gmt_sc.out', "w")
archivo2.write(contenido)
archivo2.close

