#!/usr/bin/env python

import sys
import os

fecha = str
hora = str
lat = str
lon = str
prof = str
mag = str
region = str
municipio = str
departamento = str

contenido1 = ''

archivo1 = open('sc_report.out', 'r')
lines=archivo1.readlines()
eve_cont = 0
cont_col = 0
for line in lines:
	eve_cont += 1
	campos = line.split(',')
	i = 0
	for campo in campos:
		i += 1
		if i == 1:
			fecha = campo[2:12]
		if i == 2:
			hora = campo[2:10]
		if i == 6:
			lat = campo
		if i == 8:
			lon = campo
		if i == 10:
			prof = campo
		if i == 3:
			mag = campo
		if i == 19:
			if str(campo.strip()) == "Colombia')":
				cont_col += 1

	campos2 = line.split("'")
	j=0
	for campo in campos2:
		j += 1
		if j == 18:
			region = campo
#			print campo
	contenido1 += fecha+","+hora+","+lat+","+lon+","+prof+","+mag+","+region+"\n"

cont_dist = eve_cont - cont_col

print eve_cont
print cont_col
print cont_dist

archivo1.close

archivo2 = open(sys.argv[1],"w")
archivo2.write(contenido1)
archivo2.close

