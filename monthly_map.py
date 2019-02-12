#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Jan 2019

@author: Daniel Siervo <dsiervo@sgc.gov.co>
"""
from scgmt import scgmt
from search_monthly import search_monthly
from basic_green import ruta
import os

def monthly_map(year, month):
	"""Genera mapa de sismicidad mensual
	:type year: str
	:param year: Mes para generar mapa de sismicidad
	:type month: str
	:param month: Mes para generar mapa de sismicidad"""

	month = month.rjust(2,"0")

	print "\n Consultando en la base de datos la sismicidad del mes %s de %s...\n"%(month,year)
	search_monthly(year, month)

	print "\n Creando mapa de sismicidad...\n"
	scgmt('mensual_%s_%s.out'%(year, month), auto=True)
	
	map_name = 'mensual_%s_%s_gmt'%(year, month)
	make_monthly_map(map_name)

	return map_name

def make_monthly_map(gmt_file):
   """
   Ejecuta archivo bash con instrucciones GMT para la generación del mapa y limpia el directorio
   :type gmt_name: str
   :param gmt_name: Can be mapa_semestral_normal.sh or mapa_semestral_destacados.sh
   """
   # trayendo archivos para generar los mapas en GMT
   directory = "data_map"
   os.system("./mapa_mensual.sh "+gmt_file)
   if not os.path.exists(directory):
	    os.makedirs(directory)

if __name__ == '__main__':
	monthly_map("2017", "11")
