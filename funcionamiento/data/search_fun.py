#!/usr/bin/env python
import MySQLdb

db = MySQLdb.connect(host='10.100.100.238',    # your host, usually localhost
                     user='consulta',         # your username
                     passwd='consulta',  # your password
                     db="seiscomp3")        # name of the data base
cur = db.cursor()

#cur.execute("show databases")

cur.execute("\
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
			DiskAvailability.date BETWEEN '2017-12-01' AND '2017-12-31' \
			/*AND Network.code = 'CM' */\
			/*AND Station.code = 'HEL' */\
			/*AND Stream.code LIKE 'HHE' */\
			/*AND SensorLocation.code = '00' */\
			group by Station.code,SensorLocation.code,Stream.code  \
			order by Network.code,Station.code,SensorLocation.code,Stream.code asc")

i=0
contenido1 = ''

for fila in cur.fetchall():
	contenido1 += str(fila)+'\n'
	i+=1 
	#print fila

archivo1=open('sc_fun.out','w')
archivo1.write(contenido1)

cur.close()
db.close()






