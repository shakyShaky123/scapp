#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 01:15:08 2017

@author: dsiervo
"""
import sys


def month2num(number):

	months = ["enero","febrero","marzo","abril","mayo","junio","julio","agosto", \
			  "septiembre","octubre","noviembre","diciembre"]
	try:
	  month = months[int(number)-1]
	except IndexError:
		print "\tEl número del mes ingresado no es válido: %s \n"%number
		print "\tDebe ser un número natural entre 1 y 12\n"
		sys.exit()

	return months[int(number)-1]
