#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Dec 2017

@author: Daniel Siervo <dsiervo@sgc.gov.co>
"""

from basic_green import *


def make_document(year, bulletin_month, elaborate_month, volume = "24", no = "12"):
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



    year2 = year
    if int(bulletin_month) > int(elaborate_month): year2 = str(int(year) + 1) 
    boletin_name = 'b_'+str(year)+str(bulletin_month)
    month1 = month2num(bulletin_month)
    month2 = month2num(elaborate_month)
    
    t, lc, reg, pac, car, volc, imp = list_events()
    
    section_list, subsections = section_loader()
    
    section_dic =  {"presentation": presentation,
					"functioning": functioning,
					"seismicity": seismicity,
					"graphics": graphics,
					"curiosity_section": curiosity_section}

    # creating doc object
    # , document_options=["extrafontsizes","17pt"]
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
    
    # adding presentation section
    if "presentation" in section_list:
		section_dic["presentation"](doc)
    
    # adding functioning section
    if "functioning" in section_list:
		section_dic["functioning"](doc, subsections["func"])
    
    # adding seismicity section
    if "seismicity" in section_list: 
		section_dic["seismicity"](doc, year, month1, t, lc, reg, pac, car,
		                          volc, imp, subsections["sei"])
    
    # adding graphics
    if "graphics" in section_list:
		print "Creando sección 'estadísticas'"
		section_dic["graphics"](doc, year, month1, subsections["gra"])
    
    # add latex code from other file
    #doc.append(Command("input","main2.tex"))
    
    # adding special seismicity
    if "curiosity_section" in section_list:
		section_dic["curiosity_section"](doc, subsections["cur"])
    
    try:
	    # generating .pdf and .tex
	    doc.generate_pdf(boletin_name, clean_tex=False)


    except (UnicodeEncodeError, UnicodeDecodeError):
        print "Error UnicodeEncodeError o UnicodeDecodeError, se sigue..."
        pass
    
    print "Generado el boletin: "+boletin_name
    

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
    inp_file = open("boletin.inp").readlines()
    
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
    
if __name__ == '__main__':

    archivo1 = open('boletin2.inp')
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

    make_document(y,m1,m2,vol,no)
    os.system("evince b_"+str(y)+str(m1)+".pdf")

