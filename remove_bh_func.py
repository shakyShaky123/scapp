# -*- coding: utf-8 -*-
"""
	Remueve lineas bh de archivo de funcionamiento
 
    Camilo Muñoz 
    Adaptado para elaboración automática del boletín por
    Daniel Siervo, dsiervo@sgc.gov.co
"""
import os

def modif(silent=False):

	archivo2=open("sc_fun.out","r")
	lines = archivo2.readlines()
	contenido2 = ''

	# ignora BH
	for line in lines:
		campos = line.split(',')
		cont2 = 0
		for campo in campos:
			cont2 += 1
			if cont2 == 4:
				if str(campo[1:3]) != "'B":
					contenido2 += line
	archivo2.close()
	archivo2=open("sc_fun.out","w")
	archivo2.write(contenido2)
	archivo2.close()

	archivo3=open("sc_fun.out","r")
	lines = archivo3.readlines()
	contenido3 = ''

	# ignora sub-redes
	for line in lines:
		campos = line.split(',')
		cont3 = 0
		cond = 0
		for campo in campos:
			cont3 += 1
			if cont3 == 2:
				if str(campo[1:6]) == "'AGCC":
					cond = 1
				if str(campo[1:6]) == "'TOLC":
					cond = 1
				if str(campo[1:5]) == "'ACH":
					cond = 1
				if str(campo[1:5]) == "'DRL":
					cond = 1
				if str(campo[1:6]) == "'EZNC":
					cond = 1
				if str(campo[1:4]) == "'HI":
					cond = 1
				if str(campo[1:6]) == "'OCNC":
					cond = 1
				if str(campo[1:5]) == "'PGA":
					cond = 1
				if str(campo[1:7]) == "'SML1C":
					cond = 1
				if str(campo[1:7])== "'SNPBC":
					cond = 1
				if str(campo[1:5]) == "'VMM":
					cond = 1
				if str(campo[1:4]) == "'LL":
					cond = 1

		if cond == 0:
			contenido3 += line
		archivo3.close()
		archivo3=open("sc_fun.out","w")
		archivo3.write(contenido3)
		archivo3.close()

	if not silent: os.system("gedit sc_fun.out")
