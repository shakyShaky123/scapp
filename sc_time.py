#!/usr/bin/env python

import sys
import os

def sc_time(report):
	year = str
	month = str
	day = str

	contenido = ''

	archivo1 = open(report, 'r')
	lines=archivo1.readlines()
	for line in lines:
		campos = line.split(',')
		i = 0
		for campo in campos:
			i += 1
			if i == 1:
				year = campo[2:6]
				month = campo[7:9]
				day = campo[10:12]
		contenido += " "+year+" "+month+" "+day+" \n"

	archivo1.close
	archivo2 = open('time_sc.out', "w")
	archivo2.write(contenido)
	archivo2.close()
