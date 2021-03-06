# -*- coding: utf-8 -*-
"""
    Coleccion de funciones para buscar eventos locales, 
    localizables, regionales, distantes o destacados en
    la base de datos de seisan.
    
    Daniel Siervo, dsiervo@sgc.gov.co
"""
import os
from month_to_number import month2num
import sys

'''
 ========================================================================
 Funcion principal. Devuelve el numero de eventos locales, localizables,
 regionales, distantes y destacados para un mes dado
 ========================================================================
'''
def list_events(report='sc_mensual.out', report_dest = 'sc_destacados.out'):
  archivo1 = open(report)
  lines = archivo1.readlines()
  total_events = 0
  lc = 0
  reg = 0
  pac = 0
  car = 0
  volc = 0
  for line in lines:
	total_events += 1
	campos = line.split(',')
	i = 0
	for campo in campos:
		i += 1
		if i == 8:
			if str(campo.strip()) == "Colombia":
				lc += 1
			elif str(campo.strip()) == "Region Fronteriza":
				reg += 1
		if i == 7:
			if str(campo.strip()) == "Océano Pacífico":
				pac += 1
			elif str(campo.strip()) == "Mar Caribe":
				car += 1
			elif campo[0:7] == "Volcán":
				volc += 1
			campos2 = campo.split(' ')
			j = 0
			for campo2 in campos2:
				j += 1
				if j == 2:
					if str(campo2.strip()) == "Colombia":
						lc += 1
				if j == 6:
					if str(campo2.strip()) == "Colombia":
						reg += 1
				if j == 7:
					if str(campo2.strip()) == "Colombia":
						reg += 1
  archivo1.close()

  archivo2 = open(report_dest)
  lines = archivo2.readlines()
  imp = 0
  for line in lines:
	imp += 1

  return str(total_events), str(lc), str(reg), str(pac), str(car), str(volc), str(imp)

'''
 ===================================================   
 funcion que devuelve la linea, segun su tipo
 ===================================================
'''
def type_line(typ, event, year, month):
  have = False
  #print event
 # for archivo in os.listdir("sfiles/local"):
  sfile = open("/bd/seismo/REA/BDRSN/%s/%s/%s"%(year,month,event)).readlines()
  for line in sfile:
    if line[79] == typ:
      have = True
      break
  return line, have

'''
 ===============================================
 Funcion para contar los eventos localizables
 ===============================================
'''
def count_localizable_events(year,month,l_list):
  l_c = []
  for event in l_list:

    sfile = open("/bd/seismo/REA/BDRSN/%s/%s/%s"%(year,month,event)).readlines()
    
    if sfile[0][44] == "*": pass
    else:
        # agregando evento localizable a la lista 
        l_c.append(event)
  return l_c 

'''
 ================================================================================
 funcion que busca eventos destacados, filtrando por magnitud y linea de sentidos
 ================================================================================
 '''
def important_events(year, month, event_list, regional_list):
  im_events = []
  count = 0
  # se agregan los regionales para buscar sismos regionales sentidos
  event_list = event_list + regional_list
  for event in event_list:
    sfile = open("/bd/seismo/REA/BDRSN/%s/%s/%s"%(year,month,event)).readlines()
    have_2 = False
    #print event
    try:
      # filtrando por magnitud mw, ml y profundidad
      #           Magnitud Mw                      Profundidad                         Magnitud Ml
      if (float(sfile[0][64:67]) > 4.0 and float(sfile[0][38:43]) < 120.0) or (float(sfile[0][56:59]) > 4.0 and float(sfile[0][38:43]) < 120.0) or (float(sfile[0][64:67]) > 5.0):
        #print event.index()
        im_events.append(event)
      
    except ValueError: pass
    
    line_2, have = type_line("2", event, year, month)
    
    # si el evento es sentido
    if have:
      # comprobando que el evento sentido no esta en la lista im_events
      if event not in im_events: 
        im_events.append(event)
        #print event, line_2 
  
  #print im_events, len(im_events)
  return im_events


'''
 ===============================================================================================
 funcion que busca datos de los eventos para crear tabla en boletin, devuelve lista de una tupla
 ===============================================================================================
 '''
def event_to_table(year, month, event_list):
  
  dic_for_table = {}
  list_dup_table = []
  for event in event_list:
    sfile = open("/bd/seismo/REA/BDRSN/%s/%s/%s"%(year,month,event)).readlines()
    line1 = sfile[0]
    epicentro = ""
    gap = ""
    n = "254"
    nf = "64"
    try:
      y, M, d, h, m, s = line1[1:5].strip(), line1[6:8].strip(), line1[8:10].strip(), line1[11:13].strip(), line1[13:15].strip(), line1[16:20].strip()
      lat, lon, z, rms, mw  = line1[23:30].strip(), line1[30:38].strip(), line1[38:43].strip(), line1[51:55].strip(), line1[64:67].strip()
      float(mw)
    except ValueError:
      mw = line1[56:59] 
      print "Tomando magnitud local! ",mw
      pass
    
    if z == "0.0": z = "Sup"
    # encontrando epicentro del sfile y formateandolo con parentesis 
    for line in sfile:
      if line[1:10] == "Epicentro": 
        epicentro = line.split(":")[1][0:65].strip()
        break
    print epicentro, mw
    try:
     municipio = epicentro.split("-")[0].strip()
     departamento = epicentro.split("-")[1].strip()
     epicentro = municipio+" ("+departamento+")"
    except IndexError:
     pass
    
    
    # encontrando NF
    nf_list = []
    nf_line = 0
    for line in sfile:
      if line[79] == 7:
        nf_line = sfile.index(line)
        break
    for i in range(nf_line, len(sfile)):
      
      if sfile[i][9:11] == "EP" or sfile[i][9:11] == "IP" or sfile[i][9:11] == "ES" or sfile[i][9:11] == "IS":
        nf_list.append(sfile[i])
    
    nf = len(nf_list) - 1
    
    
    
    # encontrando gap
    for line in sfile:
      if line[1:4] == "GAP":
        gap = line[5:8].strip()
    
    date = month2num(M)[0:3]+" "+d+" "+y
    hour = h+":"+m+":"+s
    
    # agregando datos para cada evento
    row_for_table = [n, date, hour, lat, lon, z, mw, rms, gap, nf, epicentro]
    list_dup_table.append((int(d),row_for_table))
    dic_for_table[event] = row_for_table
    # ordenando la tabla por el primer item de la dupla (el día)
    list_dup_table.sort(key = lambda seism: seism[0])
  return list_dup_table


def sc_table(file_name):
	"""Make table from seicomp report. Report line example:
	    
	   2017/02/01,00:18:28, 6.8, -73.17, 141.0, 5.3,LOS SANTOS - SANTANDER

	:param file_name: name of the file that contains the data
	:type file_name: :string:
	:param fun_map: name of the functioning map
	:type doc: :string:
	"""	
	try:
	  data = open(file_name).readlines()
	except IOError as e:
		print "No se encuentra el archivo de entrada con los datos de los eventos"
		print "\n",e,"\n"
		sys.exit(0)
	final_data = []
		
	for line in data:
			
		camps = line.split(",")
		row = [camps[i].replace("\\xc3\\x8d", "I").replace("\\xc3\\x81", "A") for i in range(7)]
		final_data.append(row)
		
	return final_data

"""
if __name__ == "__main__":

    give_me_my_sfiles(y,m,l)
    
    # recorrierndo todos los arhivos en el directorio sfiles
    for archivo in os.listdir("sfiles"):
      
      # abriendo cada sfile
      sfile = open("sfiles/"+archivo).readlines()
      
      # recoriendo todas las lineas por sfile
      for line in sfile:
      
        # verificando que el caracter 79 sea 6 (linea tipo 6)
        if line[79] == "6":
          # tomando el nombre de la forma de onda
          wf_name = line[1:30]
          #
          os.system("cp /bd/seismo/WAV/OPERA/%s/%s/%s ./waveforms"%(y,m,wf_name))
"""    
