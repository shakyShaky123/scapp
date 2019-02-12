#!/usr/bin/env python
import MySQLdb
from graph_errors import histo
from remove_bh_func import modif
import os

def func_semestral(y, no, silent=False):
	
	init_date = ""
	final_date = ""

	if no == "I":
		init_date = str(y)+"0101"
		final_date = str(y)+"0701000000"
	elif no == "II":
		init_date = str(y)+"0701"
		final_date = str(y)+"1231235959"
	
	
	db = MySQLdb.connect(host='10.100.100.238',    # your host, usually localhost
						 user='consulta',         # your username
						 passwd='consulta',  # your password
						 db="seiscomp3")        # name of the data base
	cur = db.cursor()

	print init_date, final_date
	
	sql_query = "\
			SELECT distinct \
				Network.code as red, \
				Station.code as estacion, \
				SensorLocation.code as localizador, \
				Stream.code as channel, \
				round(avg(DiskAvailability.availability),0) as disponibilidad, \
				Stream.code as channel \
			FROM \
				Network left join Station on Network._oid=Station._parent_oid left join SensorLocation on Station._oid=SensorLocation._parent_oid left join Stream on SensorLocation._oid=Stream._parent_oid inner join DiskAvailability on Stream._oid = DiskAvailability.stream_oid \
			WHERE \
				DiskAvailability.date BETWEEN '{0}' AND '{1}' \
				AND (Network.code = 'CM') \
				/*AND Station.code = 'HEL' */\
				AND (Stream.code LIKE '%Z') \
				AND (SensorLocation.code = '00' \
				OR SensorLocation.code = '20' \
				OR SensorLocation.code = '40') \
				group by Station.code,SensorLocation.code,Stream.code  \
				order by Network.code,Station.code,SensorLocation.code,Stream.code asc".format(init_date, final_date)
	cur.execute(sql_query)

	i=0
	contenido1 = ''

	for fila in cur.fetchall():
		contenido1 += str(fila)+'\n'
		i+=1 
		#print fila

	archivo1=open('sc_fun.out','w')
	archivo1.write(contenido1)
	archivo1.close()
	#os.system("gedit sc_fun.out")
	
	cur.close()
	db.close()

	
	# quitando canales BH
	modif(silent)
	# elaborando histograma
	histo(silent)

if __name__ == '__main__':
	func_semestral("2018", "I")
