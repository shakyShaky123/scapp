#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Dec 2017

@author: Daniel Siervo <dsiervo@sgc.gov.co>
"""

from basic_green import *
import sys
from search_semestral import *
from tablas2 import report2table
from encoding_modif import encoding_modif
from funcionamiento_semestral import func_semestral
from monthly_map import monthly_map
from scgmt import scgmt
from sc_graph import seismic_graph
import os
import sys
import click


@click.command()
@click.option('-y', "--year", required=True, prompt=True, help='Year of bullet')
@click.option('-s', "--semester", required=True, prompt=True, help='Semester of bullet. 1 or 2')
@click.option('-e', "--elaboration", required=True, prompt="Elaboration month", help="Elaboration month in number.")
@click.option('-q', "--quiet", is_flag=True, help='Quiet mode')

def make_document(year, semester, elaboration, quiet):
    """Create the monthly seismicity bulletin (latex and pdf document) 
    from a year, month of publication, month of elaboration, volume and 
    publication number given.

    :param year: year in which the seismicity to be published was recorded
    :type year: :string:
    
    :param bulletin_month: month of bulletin publication
    :type bulletin_month: :string: natural number from 1 to 12 
    
    :param elaborate_month: month in which the seismicity was recorded
    :type elaborate_month: :string: number from 1 to 12
    
    :param volume: volume of bulletin publication
    :type volume: :string: natural number
    
    :param no: publication number
    :type no: :string: natural number
    """	
    if len(year) != 4:
    	raise ValueError('The value of the year entered "%s" is incorrect'%year)
    	sys.exit()


    bulletin_month = semester
    elaborate_month = elaboration
    final_month = 0
    print "\n\tquiet fue:", quiet, type(quiet)

    bulletin_month = bulletin_month.strip().strip("0")
    volume = str(int(year)-1992)
    no = ""
    if bulletin_month != "1" and bulletin_month != "2":
		print "\nError, el semestre del boletin debe ser 1 o 2\n"
		sys.exit()
    elif bulletin_month == "1": 
    	no = "I"
    	final_month = 6
    elif bulletin_month == "2":
    	no = "II"
    	final_month = 12
		
    year2 = year
    if final_month >= int(elaborate_month): year2 = str(int(year) + 1) 
    boletin_name = 'semestral_'+str(year)+str(bulletin_month)
    month1 = num2dates(no)
    month2 = month2num(elaborate_month)
    
    print "\n Consultando en la base de datos la sismicidad semestral...\n"
    search_normal(year, no)
    print "\n Consultando en la base de datos la sismicidad destacada...\n"
    search_destacados(year, no)

    print "\n Pasando al formato de la tabla la sismicidad semestral...\n"
    report2table("semestral_normal.out", "tabla_normal.out")
    print "\n Pasando al formato de la tabla la sismicidad destacada...\n"
    report2table("semestral_destacados.out", "tabla_destacados.out")

    print "\n Corrigiendo enconding de la tabla de sismicidad semestral...\n"
    encoding_modif("tabla_normal.out")
    print "\n Corrigiendo enconding de la tabla de sismicidad destacada...\n"
    encoding_modif("tabla_destacados.out")

    print "\n Creando mapa de sismicidad semestral...\n"
    # generando report de solo localización y magnitud
    scgmt("semestral_normal.out", auto=True)
    # Ejecutando archivo bash con instrucciones GMT y limpiando el directorio
    make_map("mapa_semestral_normal.sh", quiet)
    print "\n Creando mapa de sismicidad destacada...\n"
    scgmt("semestral_destacados.out", auto=True)
    make_map("mapa_semestral_destacados.sh", quiet)

    print "\n Creando histograma de funcionamiento de las estaciones...\n"
    func_semestral(year, no, quiet)

    print "\n Creando graficas de funcionamiento...\n"
    seismic_graph("semestral_normal.out")
    
    t, lc, reg, pac, car, volc, imp = list_events("tabla_normal.out",
    	                               "tabla_destacados.out")
    section_list, subsections = section_loader()
    
    section_dic =  {"presentation": presentation,
					"functioning": functioning,
					"seismicity": seismicity,
					"graphics": graphics,
					"curiosity_section": curiosity_section}

    # creating doc object
    # , document_options=["extrafontsizes","17pt"]
    print "\n Creando boletin semestral de sismicidad...\n"
    doc = Document(documentclass='book', document_options="11pt")

    # adding preamble
    preamble(doc, year, month1)
    
    # adding cover page
    cover_page(doc, year, month1, volume, no)
    
    # adding tittle page
    tittle_page(doc, year, year2, month1, month2)

    # adding copyright page
    copy_page(doc, year2, month2)

    # adding table of contents
    table_of_contents(doc)

    # adding background of the sheets
    back_template(doc)

    print "\n Agregando la presetacion\n"
    # adding presentation section
    if "presentation" in section_list:
		section_dic["presentation"](doc)
    
    # adding functioning section
    if "functioning" in section_list:
		os.system("cp /Rutinas.Seiscomp/scapp/mapaestaciones.png .")
		section_dic["functioning"](doc, subsections["func"])
    
    print "\n Agregando seccion sismicidad\n"
    # adding seismicity section
    semestral_sismicity(doc, year, month1, t, lc, reg, pac, car,
		                          volc, imp, subsections["sei"])

    print "\n Agregando mapas de sismicidad mensual\n"
    monthly_maps(doc, year, month1, no, quiet)

    # adding graphics
    if "graphics" in section_list:
		print "Creando sección 'estadísticas'"
		section_dic["graphics"](doc, year, month1, subsections["gra"])
 
    print "\n Agregando tabla de sismicidad semestral\n"
    semiannual_seismicity(doc, year, month1)

    # adding special seismicity
    if "curiosity_section" in section_list:
		section_dic["curiosity_section"](doc, subsections["cur"])
    
    try:
	    # generating .pdf and .tex
	    doc.generate_pdf(boletin_name, clean_tex=False, compiler="lualatex")

    except (UnicodeEncodeError, UnicodeDecodeError):
        print "Error UnicodeEncodeError o UnicodeDecodeError, se sigue..."
        pass
    
    directory = "bull_docs"
    os.system("mv mapa.jpg mapa.pdf mapa_*.sh data_map")
    if not os.path.exists(directory):
	    os.makedirs(directory)

    print "Generado el boletin: "+boletin_name+".pdf"
    os.system("evince "+boletin_name+".pdf")

    # Trayendo script de ayuda para compilar
    os.system("cp %scompile_latex.sh"%ruta)

    

def section_loader():
    """Create a python list with sections to load.
    
    :param year: year in which the seismicity to be published was recorded
    :type year: :string:
    """
    
    sections_list = []
    sub_functioning = []
    sub_seismicity = []
    sub_graphics = []
    sub_curiosity = []
    
    # abriendo archivo de entrada como lista
    inp_file = open("semestral.inp").readlines()
    
    # guardando secciones seleccionadas
    if inp_file[0].strip(" ").strip("\n") == "1": sections_list.append("presentation")
    if inp_file[1].strip(" ").strip("\n") == "1": sections_list.append("functioning")
    if inp_file[5].strip(" ").strip("\n") == "1": sections_list.append("seismicity")
    if inp_file[10].strip(" ").strip("\n") == "1": sections_list.append("graphics")
    if inp_file[15].strip(" ").strip("\n") == "1": sections_list.append("curiosity_section")
    
    # guardando subsecciones
    for i in range(2, 5): sub_functioning.append(inp_file[i].strip("\n").split(","))
    for i in range(6, 10): sub_seismicity.append(inp_file[i].strip("\n").split(","))
    for i in range(11, 15): sub_graphics.append(inp_file[i].strip("\n").split(","))
    for i in range(16, len(inp_file)): sub_curiosity.append(inp_file[i].strip("\n").split(","))
    
    subsections = {"func": sub_functioning,
					"sei": sub_seismicity,
					"gra": sub_graphics,
					"cur": sub_curiosity}
	
    print "\n", sections_list, "\n"
    return sections_list, subsections

def num2dates(no):
	if no == "I":
		return "enero-junio"
	elif no == "II":
		return "julio-diciembre"

def make_map(gmt_name, silent=False):
   """
   Ejecuta archivo bash con instrucciones GMT para la generación del mapa y limpia el directorio
   :type gmt_name: str
   :param gmt_name: Can be mapa_semestral_normal.sh or mapa_semestral_destacados.sh
   """
   # trayendo archivos para generar los mapas en GMT
   os.system("cp "+ruta+"maps_files/* .")
   os.system("./"+gmt_name)
   os.system("mkdir data_map")
   os.system("mv Legend Logo-SGC.eps escalaM.txt escalaM2.txt escalaM_old.txt escalaP.txt\
     escalaP2.txt escalaP_old.txt gmt.conf gmt.history iconoE.txt iconoE2.txt iconoE_old.txt\
     mapa mapa~ palette.cpt paletteluisa.cpt palettestations.cpt palettestations_all.cpt\
     textoE.txt textoE2.txt textoE_old.txt textoM.txt textoM2.txt textoM_old.txt textoP.txt\
     textoP2.txt textoP_old.txt stations_up.d stations_names_up.txt antena.def nombresc.d\
     capitales.d estrella.txt data_map")
   # mapa_semestral_destacados.sh"
   if not silent:
	   map_name = gmt_name.split(".")[0]+".png"
	   os.system("eog %s"%map_name)


def monthly_maps(doc, year, month1, no, silent=False):
	"""Crea los 6 mapas mensuales del semestre correspondiente y los agrega
	al documento de latex"""

	months = []
	directory = "monthly_maps/"
	os.system("cp "+ruta+"maps_files/* .")
	#doc.append(NoEscape(r"\section{Mapas de sismicidad mensual durante %s de %s}"%(month1, year)))

	if no == "I":
		months = range(1,7)
	else:
		months = range(7,13)

	if not os.path.exists(directory):
	    os.makedirs(directory)

	for month in months:
		map_name = monthly_map(year, str(month).rjust(2,"0"))
		if not silent: os.system("eog mapa_%s.png"%(map_name))
		os.system("mv mapa_%s.png %s"%(map_name, directory))
		# agrega al documento de latex los mapas mensuales del semestre correspondiente
		monthly_map_page(doc, year, month)

	os.system("mv Legend Logo-SGC.eps escalaM.txt escalaM2.txt escalaM_old.txt escalaP.txt\
	 escalaP2.txt escalaP_old.txt gmt.conf gmt.history iconoE.txt iconoE2.txt iconoE_old.txt\
	 mapa mapa~ palette.cpt paletteluisa.cpt palettestations.cpt palettestations_all.cpt\
	 textoE.txt textoE2.txt textoE_old.txt textoM.txt textoM2.txt textoM_old.txt textoP.txt\
	 textoP2.txt textoP_old.txt stations_up.d stations_names_up.txt antena.def nombresc.d\
	 capitales.d estrella.txt mapa.ps mapa.pdf nombres.txt nombresc.d~ paletteluisa.cpt~ \
	 sgc2.png stations_rsnc_all.d textoM_old.txt~ escalaM_old.txt~ mensual_20*.out data_map")



if __name__ == '__main__':

    os.system("cp /Rutinas.Seiscomp/scapp/bulletfiles/semestral.inp .")
    """archivo1 = open('semestral.inp')
    lines = archivo1.readlines()
    for line in lines:
	campos = line.split(',')
	i = 0
	for campo in campos:
		i+=1
		if i == 1:
			y = campo
		if i == 2:
			m1 = campo
		if i == 3:
			m2 = campo
		if i == 4:
			vol = campo
		if i == 5:
			no = campo
	"""
    #y,m1,m2 = "2018","1","05"
    make_document()