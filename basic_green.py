# -*- coding: utf-8 -*-
"""
    Programa para generar automaticamente pdf de boletin de sismicidad
    Daniel Siervo, dsiervo@sgc.gov.co
"""

import numpy as np
from pylatex import Document, Section, Subsection, Tabular, Math, TikZ, Axis, \
    Plot, Figure, Matrix, Command, NewPage, MiniPage, LargeText, position, Center, \
    SmallText, PageStyle, StandAloneGraphic, NoEscape, Head, LineBreak, UnsafeCommand, \
    Enumerate, LongTabu
from pylatex.base_classes import Options
from pylatex.utils import italic, bold, NoEscape
import os
from month_to_number import month2num
# Para no tener problemas en la compilacion con las tildes.
import sys
from loc_reg_dis import sc_table, list_events


reload(sys)
sys.setdefaultencoding('utf-8')

#ruta = "/home/camilo/TEMP/scapp/"
#ruta = "/home/Dsiervo/scapp/"
#ruta = "/home/camilo/scapp/"
ruta = os.path.dirname(os.path.abspath(__file__))+"/"

def preamble(doc, year, month1):
    """Add a cover page to the document.

    :param doc: the document
    :type doc: :class:`pylatex.document.Document` instance
    :param year1: year of the seismicity record
    :type year1: :string:
    :param month1: month of the seismicity record
    :type month1: :string:
    """
    #spanish = Command("usepackage","babel","spanish,es-tabla")
    
    doc.preamble.append(Command("input",ruta.strip()+"bulletfiles/structure"))
    doc.preamble.append(NoEscape(r"\usepackage[spanish,es-tabla]{babel}"))
    doc.preamble.append(Command("usepackage","float") )
    #doc.preamble.append(NoEscape(r"\renewcommand{\tablename}{Tabla}"))	


def header_and_footer(doc, year, month1):
    #==================== 
    #  header and footer
    #====================
    insert_logo_command = Command("includegraphics",ruta+"bulletfiles/sgc2","width=120px")
    # add fancy package
    doc.preamble.append( Command("usepackage","fancyhdr") )
    
    # add left header (sgc logo)
    doc.preamble.append( Command("fancyhead",insert_logo_command,"L") )
    # add right header
    doc.preamble.append( Command("fancyhead",Command("small SERVICIO GEOLOGICO COLOMBIANO"),"R") )
    # add page style
    doc.preamble.append( Command("pagestyle","fancy") )
    # add footer line
    doc.preamble.append(UnsafeCommand('renewcommand',r'\footrulewidth', extra_arguments='0.5pt'))
    # clear off all default fancyhdr footers
    doc.preamble.append( Command("fancyfoot",""))
    # add left footer
    doc.preamble.append( Command("fancyfoot",Command("textbf", "Boletin de sismicidad %s %s"%(month1, str(year)) ),"L") )
    # add rigth footer
    doc.preamble.append( Command("fancyfoot",Command("thepage"),"R") ) # \fancyfoot[R]{\thepage}


def cover_page(doc, year1, month1, volume, no):
    """Add a cover page to the document.

    :param doc: the document
    :type doc: :class:`pylatex.document.Document` instance
    :param year1: year of the seismicity record
    :type year1: :string:
    :param month1: month of the seismicity record
    :type month1: :string:
    :param volume: bulletin volume
    :type volume: :string:
    :param no: number of bulletin
    :type no: :string:  
    """
    
    doc.append(NoEscape(r"\let\cleardoublepage\clearpage"))
    doc.append(NoEscape(r"\begingroup"))
    doc.append(NoEscape(r"\thispagestyle{empty}"))
    doc.append(NoEscape(r"\AddToShipoutPicture*{\put(0,0){\includegraphics[scale=1.05]{"+ruta+"bulletfiles/portada1.jpg}}}"))
    #doc.append(NoEscape(r"\centering"))
    doc.append(NoEscape(r"\vspace*{11.8cm}"))
    doc.append(NoEscape(r"{\LARGE \textcolor{white}{\hspace*{1cm}\sffamily\selectfont\hspace*{-0.95cm} %s DE %s}}\par"%(month1.upper(), year1)))
    doc.append(NoEscape(r"\vspace*{0.6cm}"))
    doc.append(NoEscape(r"\par\normalfont\fontsize{35}{35}\sffamily\selectfont"))
    doc.append(NoEscape(r"{\LARGE \textcolor{white}{\hspace*{0.2cm}VOLUMEN %s, No. %s}}"%(volume, no)))
    doc.append(NoEscape(r"\endgroup"))

def tittle_page(doc, year1, year2, month1, month2):
    """Add a tittle page to the document.

    :param doc: the document
    :type doc: :class:`pylatex.document.Document` instance
    :param year1: year of the seismicity record
    :type year1: :string:
    :param year2: year of the bulletin
    :type year2: :string:
    :param month1: month of the seismicity record
    :type month1: :string:
    :param month2: month of the seismicity record
    :type month2: :string: 
    """
    
    doc.append(NoEscape(r"\afterpage{\null}"))
    doc.append(NoEscape(r"\newpage"))
    doc.append(NoEscape(r"~\vfill"))
    doc.append(NoEscape(r"\thispagestyle{empty}"))
    doc.append(NoEscape(r"\afterpage{\null}"))
    doc.append(NoEscape(r"\onecolumn"))
    doc.append(NoEscape(r"\thispagestyle{empty}"))
    doc.append(NoEscape(r"\begin{center}"))
    doc.append(NoEscape(r"\vspace*{3cm}"))
    doc.append(NoEscape(r"\Huge{\textbf{Boletín de sismos: %s %s\\}}"%(month1, year1)))
    doc.append(NoEscape(r"\vspace*{5cm}"))
    doc.append(NoEscape(r"\huge{\textbf{Servicio Geológico Colombiano\\}}"))
    doc.append(NoEscape(r"\vspace*{8cm}"))
    #doc.append(NoEscape(r"\huge{\textsc{República de Colombia}}\\"))
    doc.append(NoEscape(r"\vspace*{1cm}"))
    doc.append(NoEscape(r"\Large{\textsc{bogotá, %s de %s}}"%(month2, year2)))
    doc.append(NoEscape(r"\end{center}"))
    

def copy_page(doc,year2, month2):
    """Add a copyright page to the document.

    :param doc: the document
    :type doc: :class:`pylatex.document.Document` instance
    :param year2: year of the bulletin
    :type year2: :string:
    :param month2: month of the seismicity record
    :type month2: :string: 
    """
    
    doc.append(NoEscape(r"\newpage"))
    doc.append(NoEscape(r"\thispagestyle{empty}"))
    doc.append(NoEscape(r"~\vfill"))
    doc.append(NoEscape(r"\noindent \textsc{BOLETÍN DE SISMOS}\\\\"))
    doc.append(NoEscape(r"\noindent Publicado en %s de %s \\\\ "%(month2,year2)))
    doc.append(NoEscape(r"\noindent \textsc{\textbf{Servicio Geológico Colombiano}}"))
   

def back_template(doc):
    """Add a cover presentation section to the document.
    To modify the names that appear in the presentation, 
    you must edit the document anexos/presentacion2.tex
    
    :param doc: the document
    :type doc: :class:`pylatex.document.Document` instance
    """
    
    doc.append(NoEscape(r"\AddToShipoutPictureBG{{\includegraphics[width=\paperwidth,height=\paperheight]{"+ruta+"bulletfiles/back.jpg}}}"))

def presentation(doc):
    """Add a cover presentation section to the document.
    To modify the names that appear in the presentation, 
    you must edit the document anexos/presentacion2.tex
    
    :param doc: the document
    :type doc: :class:`pylatex.document.Document` instance
    """

    doc.append(NoEscape(r"\newpage"))
    os.system("cp /Rutinas.Seiscomp/scapp/presentacion2.tex .")
    doc.append(Command("input","presentacion2.tex"))
	
	  
def table_of_contents(doc):
    """Add a cover page to the document.

    :param doc: the document
    :type doc: :class:`pylatex.document.Document` instance
    """
    
    #doc.append(NoEscape(r"\chapterimage{"+ruta+"bulletfiles/vidrios.jpg} "))
    doc.append(NoEscape(r"\newpage"))
    doc.append(NoEscape(r"\pagestyle{empty}"))
    doc.append(NoEscape(r"\renewcommand\contentsname{TABLA DE CONTENIDO}"))
    doc.append(NoEscape(r"\renewcommand{\bibname}{Bibliographie}"))
    doc.append(NoEscape(r"\pagestyle{fancy}"))
    doc.append(NoEscape(r"\newpage"))
    doc.append(NoEscape(r"\tableofcontents"))
	

def functioning(doc, sub_list = [["1"],["1"],["1"]]):
    """Add a cover page to the document.

    :param doc: the document
    :type doc: :class:`pylatex.document.Document` instance
    :param fun_map: name of the functioning map
    :type doc: :string:
    """
    
    doc.append(NewPage())
    doc.append(NoEscape(r"\chapter{FUNCIONAMIENTO \\DE LAS ESTACIONES}"))
    #doc.append(NoEscape(r"\chapterimage{"+ruta+"bulletfiles/sgc_blanco2.jpg}"))
    #if sub_list[1][0] == "0":
	#if sub_list[2][0] == "1":
		#doc.append(NoEscape(r"\begin{landscape}"))
    
    
    # =======================================================================
    #  Mapa estaciones
    # =======================================================================
    if sub_list[1][0] == "1":
		doc.append(NoEscape(r"\section{Mapa de las estaciones}"))
		#doc.append(NoEscape(r"\vspace{0.1cm}"))
		doc.append(NoEscape(r"\begin{figure}[h!]"))
		doc.append(NoEscape(r"\begin{minipage}{\textwidth}"))
		
		
		
		file_inspector(sub_list[1][1])

		doc.append(NoEscape(r"\begin{center} "))
		doc.append(NoEscape(r"\vspace{-0.4cm}"))
		doc.append(NoEscape(r"\includegraphics[scale=0.14]{%s}"%sub_list[1][1]))
#		doc.append(NoEscape(r"\vspace{-1.0cm}"))
		doc.append(NoEscape(r"\caption{\small{Localizaci\'on de las estaciones de la RSNC. Las antenas rojas y azules representan las estaciones con sensores de banda ancha y corto periodo,  respectivamente. Las antenas negras representan estaciones internacionales.}}%\\"))
		doc.append(NoEscape(r"\end{center}"))	
		doc.append(NoEscape(r"\end{minipage}"))
		doc.append(NoEscape(r"\end{figure}"))
		
		#doc.append(NoEscape(r"\newpage"))
		#doc.append(NoEscape(r"\vspace*{2.0cm}"))
		add_text(sub_list[1][2], doc)

    # =======================================================================
    #  Tabla de funcionamiento de las estaciones
    # =======================================================================
    if sub_list[0][0] == "1":
		doc.append(NoEscape(r"\newpage"))
		doc.append(NoEscape(r"\section{Tabla de funcionamiento de las estaciones}"))
		doc.append(NoEscape(r"\newpage"))

    # =======================================================================
    #  Histograma de funcionamiento de las estaciones
    # =======================================================================
    if sub_list[2][0] == "1":
		file_inspector(sub_list[2][1])
		if sub_list[1][0] == "1":
			doc.append(NoEscape(r"\newpage"))
			#doc.append(NoEscape(r"\begin{landscape}"))
			doc.append(NoEscape(r"\section{Histograma de funcionamiento de las estaciones}"))
			doc.append(NoEscape(r"\vspace{-0.9cm}"))
			doc.append(NoEscape(r"\begin{figure}[H]"))
			doc.append(NoEscape(r"\begin{minipage}{\textwidth}"))
			#doc.append(NoEscape(r"\vspace{-1.0cm}"))
			doc.append(NoEscape(r"\begin{center}"))
			doc.append(NoEscape(r"\includegraphics[scale=0.55]{%s}"%sub_list[2][1]))
			doc.append(NoEscape(r"\caption{\small{El porcentaje de funcionamiento es calculado en términos de la disponibilidad de los datos.}}%\\"))
			doc.append(NoEscape(r"\end{center}"))
			doc.append(NoEscape(r"\end{minipage}"))
			doc.append(NoEscape(r"\end{figure}"))
			
			# Agregando o no texto, sobre histograma de funcionamiento
			#doc.append(NoEscape(r"\newpage"))
			#doc.append(NoEscape(r"\vspace*{1.8cm}"))
			add_text(sub_list[2][2], doc)
			#doc.append(NoEscape(r"\end{landscape}"))


def seismicity(doc, year1, month1, t, lc, reg, pac, car, volc, imp,
               sub_list = [["1"],["1"],["0"],["0"]]):
    """Add seismicity section to the document.

    :param doc: the document
    :type doc: :class:`pylatex.document.Document` instance
    :param fun_map: name of the functioning map
    :type doc: :string:
    """
    print sub_list
    doc.append(NewPage())
    sec_sismicicdad = open(ruta+"bulletfiles/seccion_sismicidad_mes.txt","r").read()
    
    #doc.append(NoEscape(r"\chapterimage{"+ruta+"bulletfiles/sgc_blanco2.jpg}"))
    doc.append(NoEscape(r"\chapter{SISMICIDAD \textcolor{sgc2}{DE %s} \\DE %s}"%(month1.upper(), year1)))
    
    # agregando texto desde archivo
    doc.append(NoEscape(r"\noindent "))
    doc.append(sec_sismicicdad%(month1,t,lc,reg,pac,car,volc,imp))
    with doc.create(Enumerate()) as enum:

	  enum.add_item("El sismo tiene magnitud (M) mayor o\
	  igual a 4.0.")

	  enum.add_item("El sismo es reportado como sentido cerca al epicentro, \
	  sin importar su magnitud.")

	  enum.add_item("El sismo está asociado a sismicidad volcánica con manitud \
	  mayor o igual a 3.0.")
    
    with doc.create(Center()):
		doc.append(NoEscape(r"\sffamily\textcolor{ocre}{Convenciones}"))
    with doc.create(Tabular('ll')) as table:
	  table.add_row((bold('FECHA'), "Año Mes Día"))
	  table.add_row((bold('H:M:S'), SmallText('Hora:Minuto:Segundo. Hora del \
	  evento en tiempo universal (UT).')))
	  table.add_row((bold(''), SmallText("Para la hora local en el territorio Colombiano se restan 5 horas.")))
	  table.add_row((bold(''), SmallText("a la hora UT.")))
	  table.add_row((bold('LAT'), SmallText("Latitud en grados.")))
	  table.add_row((bold('LON'), SmallText("Longitud en grados.")))
	  table.add_row((bold('Z'), SmallText("Profundidad en kilometros.")))
	  table.add_row((bold('M'), SmallText("Promedio ponderado entre las magnitudes de momento")))
	  table.add_row((bold(''), SmallText("Mw(mB), Mwp y la magnitud local MLr.")))
	  table.add_row((bold('UBICACION'), SmallText("Epicentro del evento.")))
	  
    # Texto explicativo sobre la magnitud
    add_text(ruta+"bulletfiles/"+"magnitudes.tex", doc)

    # =======================================================================
    #  tabla de sismicidad destacada
    # =======================================================================
    if sub_list[0][0] == "1":   
		# tabla con eventos destacados
		doc.append(NoEscape(r"\newpage"))
		doc.append(NoEscape(r"\section{Tabla de sismicidad destacada %s de %s}"%(month1, year1)))
		doc.append(NoEscape(r"\vspace{0.8cm}"))
				
		data_list = sc_table("sc_destacados.out")
		
		with doc.create(LongTabu("X[0.4,c] X[1.3,c] X[1.2,c] X[c] X[1.1,c] X[0.4,c] X[0.4,c] X[4,l]",
							 row_height=1)) as data_table:          
		  data_table.add_row(NoEscape(r"\scriptsize\sffamily\bfseries N"), NoEscape(r"\scriptsize\sffamily\bfseries FECHA"),
							NoEscape(r"\scriptsize\sffamily\bfseries H:M:S"),
							NoEscape(r"\scriptsize\sffamily\bfseries LAT"),
							NoEscape(r"\scriptsize\sffamily\bfseries LON"), 
							NoEscape(r"\scriptsize\sffamily\bfseries Z"),
							NoEscape(r"\scriptsize\sffamily\bfseries M"),
							NoEscape(r"\scriptsize\sffamily\bfseries UBICACION"),
						   color="sgc2")
		  #data_table.add_empty_row()
		  data_table.end_table_header()
		  
		  # para cada elemento en la lista list_to_table (lista con info de destacados)
		  for i in range(len(data_list)):
			if (i % 2) == 0:
				data_table.add_row(Command("tiny", str(i+1)),Command("tiny",data_list[i][0]),
						   Command("tiny",data_list[i][1]),Command("tiny",data_list[i][2]),
						   Command("tiny",data_list[i][3]),Command("tiny",data_list[i][4]),
						   Command("tiny",data_list[i][5]),
						   Command("tiny",data_list[i][6]), color="sgc2!20")
			else:
				data_table.add_row(Command("tiny", str(i+1)),Command("tiny",data_list[i][0]),
						   Command("tiny",data_list[i][1]),Command("tiny",data_list[i][2]),
						   Command("tiny",data_list[i][3]),Command("tiny",data_list[i][4]),
						   Command("tiny",data_list[i][5]),
						   Command("tiny",data_list[i][6]))
		  doc.append(NoEscape(r"\caption{Eventos destacados durante %s de %s}"%(month1, year1)))			   

    
    # =======================================================================
    #  mapa de sismicidad destacada 
    # =======================================================================
    if sub_list[1][0] == "1":
		file_inspector(sub_list[1][1])
		doc.append(NoEscape(r"\begin{figure}[H]"))
	        doc.append(NoEscape(r"\begin{minipage}{\textwidth}"))
		doc.append(NoEscape(r"\section{Mapa de sismicidad destacada %s de %s}"%(month1, year1)))
#		doc.append(NoEscape(r"\vspace{-1.5cm}"))
		doc.append(NoEscape(r"\begin{center}"))
		doc.append(NoEscape(r"\includegraphics[scale=0.16]{%s}\\"%sub_list[1][1]))
		doc.append(NoEscape(r"\caption{\small{Eventos destacados durante %s de %s}}"%(month1, year1)))
		doc.append(NoEscape(r"\end{center}"))
#		doc.append(NoEscape(r"\vspace{-1.5cm}"))
		doc.append(NoEscape(r"\end{minipage}"))
		doc.append(NoEscape(r"\end{figure}"))
		
		#doc.append(NoEscape(r"\newpage"))
		#doc.append(NoEscape(r"\vspace*{2.0cm}"))
		add_text(sub_list[1][2], doc)


    # =======================================================================
    #  tabla de sismicidad mensual
    # =======================================================================
    if sub_list[2][0] == "1":
		
		doc.append(NoEscape(r"\newpage"))
		doc.append(NoEscape(r"\section{Tabla de sismicidad mensual %s de %s}"%(month1, year1)))
		doc.append(NoEscape(r"\vspace{0.8cm}"))
		data_list = sc_table("sc_mensual.out")
		with doc.create(LongTabu("X[0.4,c] X[1.3,c] X[1.2,c] X[c] X[1.1,c] X[0.4,c] X[0.4,c] X[4,l]",
							 row_height=1)) as data_table:          
		  data_table.add_row(NoEscape(r"\scriptsize\sffamily\bfseries N"),NoEscape(r"\scriptsize\sffamily\bfseries FECHA"),
							NoEscape(r"\scriptsize\sffamily\bfseries H:M:S"),
							NoEscape(r"\scriptsize\sffamily\bfseries LAT"),
							NoEscape(r"\scriptsize\sffamily\bfseries LON"), 
							NoEscape(r"\scriptsize\sffamily\bfseries Z"),
							NoEscape(r"\scriptsize\sffamily\bfseries M"),
							NoEscape(r"\scriptsize\sffamily\bfseries UBICACION"),
						   color="sgc2")
		  #data_table.add_empty_row()
		  data_table.end_table_header()
		  
		  # para cada elemento en la lista list_to_table (lista con info de destacados)
		  for i in range(len(data_list)):
			if (i % 2) == 0:
				data_table.add_row(Command("tiny", str(i+1)),Command("tiny",data_list[i][0]),
						   Command("tiny",data_list[i][1]),Command("tiny",data_list[i][2]),
						   Command("tiny",data_list[i][3]),Command("tiny",data_list[i][4]),
						   Command("tiny",data_list[i][5]),
						   Command("tiny",data_list[i][6]), color="sgc2!20")
			else:
				data_table.add_row(Command("tiny", str(i+1)),Command("tiny",data_list[i][0]),
						   Command("tiny",data_list[i][1]),Command("tiny",data_list[i][2]),
						   Command("tiny",data_list[i][3]),Command("tiny",data_list[i][4]),
						   Command("tiny",data_list[i][5]),
						   Command("tiny",data_list[i][6]), color="white")
		  doc.append(NoEscape(r"\caption{Eventos durante %s de %s}"%(month1, year1)))

    # =======================================================================
    #  mapa de sismicidad mensual 
    # =======================================================================
    if sub_list[3][0] == "1":
		print sub_list[3][1]
		print sub_list[3][2]
		doc.append(NoEscape(r"\newpage"))
		file_inspector(sub_list[3][1])
		doc.append(NoEscape(r"\begin{figure}[H]"))
	        doc.append(NoEscape(r"\begin{minipage}{\textwidth}"))
		doc.append(NoEscape(r"\section{Mapa de sismicidad mensual %s de %s}"%(month1, year1)))
		doc.append(NoEscape(r"\begin{center}"))
		doc.append(NoEscape(r"\includegraphics[scale=0.16]{%s}"%sub_list[3][1]))
		doc.append(NoEscape(r"\caption{\small{Eventos durante %s de %s}}"%(month1, year1)))
		doc.append(NoEscape(r"\end{center}"))
		doc.append(NoEscape(r"\end{minipage}"))
		doc.append(NoEscape(r"\end{figure}"))
		
		add_text(sub_list[3][2], doc)


def graphics(doc, year, month1, sub_list = [["1"],["1"],["1"],["1"]]):
    """Add a graphics section to the document.

    :param doc: the document
    :type doc: :class:`pylatex.document.Document` instance
    :param fun_map: name of the functioning map
    :type doc: :string:
    """	
    
    # =======================================================================
    #  graphics section 
    # ======================================================================= 

    doc.append(Command("newpage"))
    doc.append(NoEscape(r"\chapter{ESTADÍSTICAS DE LA\\ SISMICIDAD \textcolor{sgc2}{MENSUAL}}"))
    
    # =======================================================================
    #  errores
    # =======================================================================
  
    if sub_list[0][0] == "1":
		print "Creando subsección 'errores'\n"
		doc.append(NoEscape(r"\section{Errores}"))

		# Graficas de errores
		doc.append(NoEscape(r"\begin{figure}[h!]"))
		doc.append(NoEscape(r"\begin{minipage}{\textwidth}"))
		file_inspector('loc_err.png')
		doc.append(NoEscape(r"\begin{center}"))
		doc.append(NoEscape(r"\includegraphics[scale=0.5]{loc_err.png}"))
		doc.append(NoEscape(r"\caption{Error en latitud, longitud y profundidad (km)}"))
		doc.append(NoEscape(r"\end{center}"))
		doc.append(NoEscape(r"\end{minipage}"))
		doc.append(NoEscape(r"\end{figure}"))
		add_text(sub_list[0][2], doc)

    # =======================================================================
    #  no. de sismos
    # =======================================================================
    if sub_list[1][0] == "1": 
		print "Creando subsección 'no. de sismos'\n"
		file_inspector('mag_sismos.png')
		file_inspector('prof_sismos.png')
		file_inspector('rms_sismos.png')
		image_mag_sismos = os.path.join(os.path.dirname(__file__), 'mag_sismos.png')
		image_prof_sismos = os.path.join(os.path.dirname(__file__), 'prof_sismos.png')
		image_prof_mag_sismos = os.path.join(os.path.dirname(__file__), 'rms_sismos.png')
		
		if sub_list[0][0] == "1": doc.append(Command("newpage"))
		doc.append(NoEscape(r"\begin{figure}[h!]"))
		doc.append(NoEscape(r"\begin{minipage}{\textwidth}"))
		doc.append(NoEscape(r"\section{No. de Sismos}"))
		doc.append(NoEscape(r"\begin{multicols}{2}"))
		doc.append(NoEscape(r"\includegraphics[scale=0.5]{mag_sismos.png}"))
		doc.append(NoEscape(r"\includegraphics[scale=0.5]{prof_sismos.png}"))
		doc.append(NoEscape(r"\end{multicols}"))
		doc.append(NoEscape(r"\vspace{0.5cm}"))
		doc.append(NoEscape(r"\begin{center}"))
		doc.append(NoEscape(r"\includegraphics[scale=0.5]{rms_sismos.png}"))
		doc.append(NoEscape(r"\caption{No de eventos por magnitud, profundidad y rms}"))
		doc.append(NoEscape(r"\end{center}"))
		doc.append(NoEscape(r"\vspace{0.5cm}"))
		add_text(sub_list[1][2], doc)
		doc.append(NoEscape(r"\end{minipage}"))
		doc.append(NoEscape(r"\end{figure}"))
    # =======================================================================
    #  evolución temporal
    # =======================================================================
    if sub_list[2][0] == "1":
		print "Creando subsección 'evolución temporal'\n"
		file_inspector('sismos_vs_tiempo_dias.jpg')
		file_inspector('sismos_vs_tiempo_dias_acumulado.jpg')
#		file_inspector('sismos_vs_tiempo_meses.jpg')
		image_sismos_vs_t_d = os.path.join(os.path.dirname(__file__), 'sismos_vs_tiempo_dias.jpg')
		image_sismos_vs_t_d_a = os.path.join(os.path.dirname(__file__), 'sismos_vs_tiempo_dias_acumulado.jpg')
#		image_sismos_vs_t_m = os.path.join(os.path.dirname(__file__), 'sismos_vs_tiempo_meses.jpg')
		
		if sub_list[1][0] == "1":doc.append(Command("newpage"))
		doc.append(NoEscape(r"\begin{figure}[h]"))
		doc.append(NoEscape(r"\begin{minipage}{\textwidth}"))
		doc.append(NoEscape(r"\section{Evolución Temporal}"))
		# histograma sismos registrados por dia      
		doc.append(NoEscape(r"\begin{multicols}{2}"))
		doc.append(NoEscape(r"\includegraphics[scale=0.5]{sismos_vs_tiempo_dias.jpg}"))
		doc.append(NoEscape(r"\includegraphics[scale=0.5]{sismos_vs_tiempo_dias_acumulado.jpg}"))
		doc.append(NoEscape(r"\end{multicols}"))
		doc.append(NoEscape(r"\vspace{-0.5cm}"))
		doc.append(NoEscape(r"\begin{center}"))
#		doc.append(NoEscape(r"\includegraphics[scale=0.5]{sismos_vs_tiempo_dias_acumulado.jpg}"))
		doc.append(NoEscape(r"\caption{No de eventos por días y acumulado por días}"))
		doc.append(NoEscape(r"\end{center}"))
		doc.append(NoEscape(r"\vspace{0.5cm}"))
		add_text(sub_list[2][2], doc)
		doc.append(NoEscape(r"\end{minipage}"))
		doc.append(NoEscape(r"\end{figure}"))
    # =======================================================================
    #  extras
    # =======================================================================
    if sub_list[3][0] == "1":
		print "Creando subsección 'extras'\n"
		file_inspector('prof_mag_sismos.jpg')
		file_inspector('prof_rms_sismos.jpg')
		file_inspector('mag_rms_sismos.jpg')
		extra1 = os.path.join(os.path.dirname(__file__), 'prof_mag_sismos.jpg')
		extra2 = os.path.join(os.path.dirname(__file__), 'prof_rms_sismos.jpg')
		extra3 = os.path.join(os.path.dirname(__file__), 'mag_rms_sismos.jpg')
		if sub_list[2][0] == "1": doc.append(Command("newpage"))
		doc.append(NoEscape(r"\begin{figure}[h]"))
		doc.append(NoEscape(r"\begin{minipage}{\textwidth}"))
		doc.append(NoEscape(r"\section{Extras}"))
		# histograma sismos registrados por dia acumulado
		doc.append(NoEscape(r"\begin{multicols}{2}"))
		doc.append(NoEscape(r"\includegraphics[scale=0.25]{prof_mag_sismos.jpg}"))
		doc.append(NoEscape(r"\includegraphics[scale=0.25]{prof_rms_sismos.jpg}"))
		doc.append(NoEscape(r"\end{multicols}"))
		doc.append(NoEscape(r"\vspace{-0.5cm}"))
		doc.append(NoEscape(r"\begin{center}"))
		doc.append(NoEscape(r"\includegraphics[scale=0.25]{mag_rms_sismos.jpg}"))
		doc.append(NoEscape(r"\vspace{-0.5cm}"))
		doc.append(NoEscape(r"\caption{No de eventos vs (magnitud y profundidad), (profundidad y rms) y (magnitud y rms)}"))
		doc.append(NoEscape(r"\end{center}"))
		doc.append(NoEscape(r"\vspace{0.5cm}"))
		add_text(sub_list[3][2], doc)
		doc.append(NoEscape(r"\end{minipage}"))
		doc.append(NoEscape(r"\end{figure}"))
    # =======================================================================

def curiosity_section(doc, sub_list = [["1"],["0"]]):
	"""Add special seismicity section to the document.
	
    :param doc: the document
    :type doc: :class:`pylatex.document.Document` instance
	"""
	#doc.append(NoEscape(r"\chapterimage{sgc_blanco2.jpg}"))
	doc.append(NoEscape(r"\chapter{SISMICIDAD ESPECIAL}"))

	# agregando sección ¿sabías qué? 		
	doc.append(NoEscape(r"\begin{definition}"))
	doc.append(NoEscape(r"\sffamily"))
	doc.append(NoEscape(add_text("sismicidad_especial.dat", doc)))
	doc.append(NoEscape(r"\end{definition}"))
	
	# para cada fila donde puede colocarse texto o imagen
	for j in range(1,4):
		
		image_name = sub_list[0][j]
		text_name = sub_list[1][j]
		
		# si hay una imagen en la fila j se agrega al documento
		if image_name != "":
			file_inspector(image_name) 
			doc.append(NoEscape(r"\begin{center}"))
			doc.append(NoEscape(r"\includegraphics[scale=0.4]{%s}"%image_name))
			doc.append(NoEscape(r"\end{center}"))
			
			# si hay un archivo de texto asociado a la imagen de la 
			# misma fila, se agrega
			if text_name != "":
				add_text(text_name, doc)

def semestral_sismicity(doc, year1, month1, t, lc, reg, pac, car, volc, imp,
               sub_list = [["1"],["1"],["0"],["0"]]):
    """Add seismicity section to the document.

    :param doc: the document
    :type doc: :class:`pylatex.document.Document` instance
    :param fun_map: name of the functioning map
    :type doc: :string:
    """
    print sub_list
    doc.append(NewPage())
    sec_sismicicdad = open(ruta+"bulletfiles/seccion_sismicidad_semestral.txt","r").read()
    
    #doc.append(NoEscape(r"\chapterimage{"+ruta+"bulletfiles/sgc_blanco2.jpg}"))
    doc.append(NoEscape(r"\chapter{SISMICIDAD \textcolor{sgc2}{DE %s} \\DE %s}"%(month1.upper(), year1)))
    
    # agregando texto desde archivo
    doc.append(NoEscape(r"\noindent "))
    doc.append(sec_sismicicdad%(month1,t,lc,reg,pac,car,volc,imp))
    with doc.create(Enumerate()) as enum:

	  enum.add_item("El sismo tiene magnitud (M) mayor o\
	  igual a 4.0.")

	  enum.add_item("El sismo es reportado como sentido cerca al epicentro, \
	  sin importar su magnitud.")

	  enum.add_item("El sismo está asociado a sismicidad volcánica con manitud \
	  mayor o igual a 3.0.")
    
    with doc.create(Center()):
		doc.append(NoEscape(r"\sffamily\textcolor{ocre}{Convenciones}"))
    with doc.create(Tabular('ll')) as table:
	  table.add_row((bold('FECHA'), "Año Mes Día"))
	  table.add_row((bold('H:M:S'), SmallText('Hora:Minuto:Segundo. Hora del \
	  evento en tiempo universal (UT).')))
	  table.add_row((bold(''), SmallText("Para la hora local en el territorio Colombiano se restan 5 horas.")))
	  table.add_row((bold(''), SmallText("a la hora UT.")))
	  table.add_row((bold('LAT'), SmallText("Latitud en grados.")))
	  table.add_row((bold('LON'), SmallText("Longitud en grados.")))
	  table.add_row((bold('Z'), SmallText("Profundidad en kilometros.")))
	  table.add_row((bold('M'), SmallText("Promedio ponderado entre las magnitudes de momento")))
	  table.add_row((bold(''), SmallText("Mw(mB), Mwp y la magnitud local MLr.")))
	  table.add_row((bold('UBICACION'), SmallText("Epicentro del evento.")))
	  
    # Texto explicativo sobre la magnitud
    add_text(ruta+"bulletfiles/"+"magnitudes.tex", doc)

    # =======================================================================
    #  tabla de sismicidad destacada
    # =======================================================================
    if sub_list[0][0] == "1":   
		# tabla con eventos destacados
		doc.append(NoEscape(r"\newpage"))
		doc.append(NoEscape(r"\section{Tabla de sismicidad destacada %s de %s}"%(month1, year1)))
		doc.append(NoEscape(r"\vspace{0.8cm}"))
				
		data_list = sc_table("tabla_destacados.out")
		
		with doc.create(LongTabu("X[0.4,c] X[1.3,c] X[1.2,c] X[c] X[1.1,c] X[0.4,c] X[0.4,c] X[4,l]",
							 row_height=1)) as data_table:          
		  data_table.add_row(NoEscape(r"\scriptsize\sffamily\bfseries N"),
							NoEscape(r"\scriptsize\sffamily\bfseries FECHA"),
							NoEscape(r"\scriptsize\sffamily\bfseries H:M:S"),
							NoEscape(r"\scriptsize\sffamily\bfseries LAT"),
							NoEscape(r"\scriptsize\sffamily\bfseries LON"), 
							NoEscape(r"\scriptsize\sffamily\bfseries Z"),
							NoEscape(r"\scriptsize\sffamily\bfseries M"),
							NoEscape(r"\scriptsize\sffamily\bfseries UBICACION"),
						   color="sgc2")
		  #data_table.add_empty_row()
		  data_table.end_table_header()
		  
		  # para cada elemento en la lista list_to_table (lista con info de destacados)
		  for i in range(len(data_list)):
			if (i % 2) == 0:
				data_table.add_row(Command("tiny", str(i+1)), Command("tiny",data_list[i][0]),
						   Command("tiny",data_list[i][1]),Command("tiny",data_list[i][2]),
						   Command("tiny",data_list[i][3]),Command("tiny",data_list[i][4]),
						   Command("tiny",data_list[i][5]),
						   Command("tiny",data_list[i][6]), color="sgc2!20")
			else:
				data_table.add_row(Command("tiny", str(i+1)), Command("tiny",data_list[i][0]),
						   Command("tiny",data_list[i][1]),Command("tiny",data_list[i][2]),
						   Command("tiny",data_list[i][3]),Command("tiny",data_list[i][4]),
						   Command("tiny",data_list[i][5]),
						   Command("tiny",data_list[i][6]))
		  doc.append(NoEscape(r"\caption{Eventos destacados durante %s de %s}"%(month1, year1)))			   

    
    # =======================================================================
    #  mapa de sismicidad destacada 
    # =======================================================================
    if sub_list[1][0] == "1":
		file_inspector(sub_list[1][1])
		doc.append(NoEscape(r"\begin{figure}[H]"))
	        doc.append(NoEscape(r"\begin{minipage}{\textwidth}"))
		doc.append(NoEscape(r"\section{Mapa de sismicidad destacada %s de %s}"%(month1, year1)))
#		doc.append(NoEscape(r"\vspace{-1.5cm}"))
		doc.append(NoEscape(r"\begin{center}"))
		doc.append(NoEscape(r"\includegraphics[scale=0.16]{%s}\\"%sub_list[1][1]))
		doc.append(NoEscape(r"\caption{\small{Sismos destacados localizados por el SGC durante %s de %s.}}"%(month1, year1)))
		doc.append(NoEscape(r"\end{center}"))
#		doc.append(NoEscape(r"\vspace{-1.5cm}"))
		doc.append(NoEscape(r"\end{minipage}"))
		doc.append(NoEscape(r"\end{figure}"))
		
		#doc.append(NoEscape(r"\newpage"))
		#doc.append(NoEscape(r"\vspace*{2.0cm}"))
		add_text(sub_list[1][2], doc)

    # =======================================================================
    #  mapa de sismicidad semestral
    # =======================================================================
    if sub_list[3][0] == "1":
		print sub_list[3][1]
		print sub_list[3][2]
		doc.append(NoEscape(r"\newpage"))
		file_inspector(sub_list[3][1])
		doc.append(NoEscape(r"\begin{figure}[H]"))
	        doc.append(NoEscape(r"\begin{minipage}{\textwidth}"))
		doc.append(NoEscape(r"\section{Mapa de sismicidad semestral %s de %s}"%(month1, year1)))
		doc.append(NoEscape(r"\begin{center}"))
#		doc.append(NoEscape(r"\vspace{-1.5cm}"))
		doc.append(NoEscape(r"\includegraphics[scale=0.16]{%s}"%sub_list[3][1]))
		doc.append(NoEscape(r"\caption{\small{Eventos localizados por el SGC durante %s de %s}}"%(month1, year1)))
		doc.append(NoEscape(r"\end{center}"))
#		doc.append(NoEscape(r"\vspace{-1.5cm}"))
		doc.append(NoEscape(r"\end{minipage}"))
		doc.append(NoEscape(r"\end{figure}"))
		
		#doc.append(NoEscape(r"\newpage"))
		#doc.append(NoEscape(r"\vspace*{2.0cm}"))
		add_text(sub_list[3][2], doc)

def file_inspector(file_name):
	"""Inspecciona que en el directorio exista el archivo a cargar
	:param file_name: nombre del archivo a cargar
	:type file_name: string
	"""
	
	try:
		temp_file = open(file_name)
		print "Inspeccionando> ",file_name
		temp_file.close()
	except IOError as e:
		print "\n",e,"\n"
		sys.exit()

def add_text(file_name, doc):
	"""Agrega o no texto según la selección del usuario
	:param file_name: nombre del archivo a cargar
	:type file_name: string
    :param doc: the document
    :type doc: :class:`pylatex.document.Document` instance
	"""
	# Agregando o no texto, sobre mapa de funcionamiento
	if file_name != "":
		file_inspector(file_name)
		with open(file_name, "r") as text:
			doc.append(NoEscape(text.read().strip()))

def monthly_map_page(doc, year, m):
	"""Agrega sección con sismicidad mensual en boletín semestral
	"""
	month = month2num(m)
	map_dir = "monthly_maps/mapa_mensual_%s_%s_gmt.png"%(year,str(m).rjust(2,"0"))
	doc.append(NoEscape(r"\newpage"))
	file_inspector(map_dir)
	doc.append(NoEscape(r"\begin{figure}[H]"))
	doc.append(NoEscape(r"\begin{minipage}{\textwidth}"))
	doc.append(NoEscape(r"\section{Mapa de sismicidad mensual %s de %s}"%(month, year)))
	doc.append(NoEscape(r"\begin{center}"))
	doc.append(NoEscape(r"\includegraphics[scale=0.16]{%s}"%map_dir))
	doc.append(NoEscape(r"\caption{\small{Eventos durante %s de %s}}"%(month, year)))
	doc.append(NoEscape(r"\end{center}"))
	doc.append(NoEscape(r"\end{minipage}"))
	doc.append(NoEscape(r"\end{figure}"))

def semiannual_seismicity(doc, year1, month1):
    # =======================================================================
    #  tabla de sismicidad semestral
    # =======================================================================
	doc.append(NoEscape(r"\newpage"))
	doc.append(NoEscape(r"\section{Tabla de sismicidad semestral %s de %s}"%(month1, year1)))
	doc.append(NoEscape(r"\vspace{0.8cm}"))
	file_inspector("tabla_normal.out")
	data_list = sc_table("tabla_normal.out")
	
	m = len(data_list)/2
	semiannual_table(doc, year1, month1, data_list, 0, m)
	semiannual_table(doc, year1, month1, data_list, m, len(data_list))
	
def semiannual_table(doc, year1, month1, data_list, init, final):
	
	with doc.create(LongTabu("X[0.4,c] X[1.3,c] X[1.2,c] X[c] X[1.1,c] X[0.4,c] X[0.4,c] X[4,l]",
						 row_height=1)) as data_table:          
	  data_table.add_row(NoEscape(r"\scriptsize\sffamily\bfseries N"),NoEscape(r"\scriptsize\sffamily\bfseries FECHA"),
						NoEscape(r"\scriptsize\sffamily\bfseries H:M:S"),
						NoEscape(r"\scriptsize\sffamily\bfseries LAT"),
						NoEscape(r"\scriptsize\sffamily\bfseries LON"), 
						NoEscape(r"\scriptsize\sffamily\bfseries Z"),
						NoEscape(r"\scriptsize\sffamily\bfseries M"),
						NoEscape(r"\scriptsize\sffamily\bfseries UBICACION"),
					   color="sgc2")
	  #data_table.add_empty_row()
	  data_table.end_table_header()
	  
	  # para cada elemento en la lista list_to_table (lista con info de sismos)
	  for i in range(init, final):
		if (i % 2) == 0:
			data_table.add_row(Command("tiny", str(i+1)),Command("tiny",data_list[i][0]),
					   Command("tiny",data_list[i][1]),Command("tiny",data_list[i][2]),
					   Command("tiny",data_list[i][3]),Command("tiny",data_list[i][4]),
					   Command("tiny",data_list[i][5]),
					   Command("tiny",data_list[i][6]), color="sgc2!20")
		else:
			data_table.add_row(Command("tiny", str(i+1)),Command("tiny",data_list[i][0]),
					   Command("tiny",data_list[i][1]),Command("tiny",data_list[i][2]),
					   Command("tiny",data_list[i][3]),Command("tiny",data_list[i][4]),
					   Command("tiny",data_list[i][5]),
					   Command("tiny",data_list[i][6]), color="white")
