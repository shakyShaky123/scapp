#!/usr/bin/env python

import sys
import os

lat = float
e_lat = float
lon = float
e_lon = float
prof = float
e_prof = float
rms = float
mag = float

if len(sys.argv) > 1:
	report_file = sys.argv[1]
else:
	report_file = 'sc_report.out'


contenido = ''

archivo1 = open(report_file, 'r')
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
		if i == 16:
			i_d = campo
		if i == 1:
			date = campo[1:13]
		if i == 2:
			time = campo
		if i == 18:
			reg = campo.strip()

	contenido += str(lat)+"   "+str(e_lat)+"   "+str(lon)+"   "+str(e_lon)+"   "+str(prof)+"   "+str(e_prof)+"   "+str(rms)+"   "+str(mag)+"   "+str(reg)+"   "+str(i_d)+"   "+str(date)+str(time)+"\n"

archivo1.close

archivo2 = open('rev_sc.out', "w")
archivo2.write(contenido)
archivo2.close
