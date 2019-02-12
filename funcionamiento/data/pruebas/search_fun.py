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
			AND Network.code NOT LIKE 'CM' \
			AND Network.code NOT LIKE 'OM' \
			AND Network.code NOT LIKE 'OP' \
			group by Station.code,SensorLocation.code,Stream.code  \
			order by Network.code,Station.code,SensorLocation.code,Stream.code asc")

i=0
contenido1 = ''

#			DATE_FORMAT(DiskAvailability.date, '%Y-%m-%d') as fecha, \
#			round(avg(DiskAvailability.availability),0) as disponibilidad, \

#			CONVERT(DiskAvailability.date, CHAR(50)) LIKE '2017-12-%')
#			group by Station.code,SensorLocation.code,Stream.code  \
#			order by Network.code,Station.code,SensorLocation.code,Stream.code asc")


#			AND (Network.code = 'CM' \
#			OR Network.code = 'BR' \
#			OR Network.code = 'OP') \
#			And (Stream.code LIKE '%Z' \
#			OR Stream.code LIKE 'HHE') \


#			AND Stream.code = 'HHZ' \
#			AND SensorLocation.code = '00' \
#			AND Station.code = 'RUS' \
#			DiskAvailability.availability as disponibilidad, \
#			AND Station.code = 'RUS' \

for fila in cur.fetchall():
	contenido1 += str(fila)+'\n'
	i+=1 
	#print fila

archivo1=open('sc_fun.out','w')
archivo1.write(contenido1)

cur.close()
db.close()


#SERVIDOR,13
#BUSQUEDA,Eventos
#TIME_INI,20171201000000
#TIME_END,20171231235959
#LAT_MIN,
#LAT_MAX,
#LON_MIN,
#LON_MAX,
#DEP_MIN,
#DEP_MAX,
#MAG_MIN,3.5
#MAG_MAX,10.0
#PHASE_MIN,
#PHASE_MAX,
#STA_MIN,
#STA_MAX,
#LAT_ERROR_MIN,
#LAT_ERROR_MAX,
#LON_ERROR_MIN,
#LON_ERROR_MAX,
#DEP_ERROR_MIN,
#DEP_ERROR_MAX,
#RMS_MIN,
#RMS_MAX,
#GAP_MIN,
#GAP_MAX,
#DIST_STA_MIN,
#DIST_STA_MAX,
#MAG_TYPE,
#ESTATUS,
#AGENCIA,
#AUTOR,
#REGION,







