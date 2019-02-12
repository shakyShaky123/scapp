#!/usr/bin/env python

import os, time, math, tempfile
import numpy 
import sys
import os
import subprocess
from glob import glob


try:
    import Gnuplot, Gnuplot.PlotItems, Gnuplot.funcutils
except ImportError:
    # kludge in case Gnuplot hasn't been installed as a module yet:
    import __init__
    Gnuplot = __init__
    import PlotItems
    Gnuplot.PlotItems = PlotItems
    import funcutils
    Gnuplot.funcutils = funcutils

report=glob("/home/camilo/read_select/codigo/report.out")
archivo=open(report[0],"r")
lines=archivo.readlines()
#print (lines[0])


sum_prof=[0 for i in range(21)]

sum_rms=[0 for i in range(21)]

sum_mag=[0 for i in range(21)]

sum_magM=numpy.zeros((21, 21))

sum_profM=numpy.zeros((21, 21))

sum_profM2=numpy.zeros((21, 21))

#print sum_magM
#print sum_magM[1][:]

sum_magT=[0 for i in range(21)]
sum_profT=[0 for i in range(21)]

vec_prof = numpy.arange(0,210,10)
vec_rms = numpy.arange(0.1,2.2,0.1)
vec_mag = numpy.arange(0,10.5,0.5)

#f = os.fdopen(filename1, 'w')

	##################SUMA PROFUNDIDAD################################
def func_prof():
	if prof == 0:
		sum_prof[0] += 1
	if prof > 0:
		if prof <= 10:
			sum_prof[1] += 1
	if prof > 10:
		if prof <= 20:
			sum_prof[2] += 1
	if prof > 20:
		if prof <= 30:
			sum_prof[3] += 1
	if prof > 30:
		if prof <= 40:
			sum_prof[4] += 1
	if prof > 40:
		if prof <= 50:
			sum_prof[5]  += 1
	if prof > 50:
		if prof <= 60:
			sum_prof[6] += 1	
	if prof > 60:
		if prof <= 70:
			sum_prof[7] += 1
	if prof > 70:
		if prof <= 80:
			sum_prof[8] += 1
	if prof > 80:
		if prof <= 90:
			sum_prof[9] += 1
	if prof > 90:
		if prof <= 100:
			sum_prof[10]  += 1
	if prof > 100:
		if prof <= 110:
			sum_prof[11]  += 1
	if prof > 110:
		if prof <= 120:
			sum_prof[12] += 1
	if prof > 120:
		if prof <= 130:
			sum_prof[13] += 1
	if prof > 130:
		if prof <= 140:
			sum_prof[14] += 1
	if prof > 140:
		if prof <= 150:
			sum_prof[15] += 1
	if prof > 150:
		if prof <= 160:
			sum_prof[16] += 1
	if prof > 160:
		if prof <= 170:
			sum_prof[17] += 1
	if prof > 170:
		if prof <= 180:
			sum_prof[18] += 1
	if prof > 180:
		if prof <= 190:
			sum_prof[19] += 1
	if prof > 190:
		if prof <= 200:
			sum_prof[20] += 1

	######################SUMA RMS####################################
def func_rms():	
	if rms == 0.1:
		sum_rms[0] += 1
	if rms == 0.2:
		sum_rms[1] += 1
	if rms == 0.3:
		sum_rms[2] += 1
	if rms == 0.4:
		sum_rms[3] += 1
	if rms == 0.5:
		sum_rms[4] += 1
	if rms == 0.6:
		sum_rms[5] += 1
	if rms == 0.7:
		sum_rms[6] += 1
	if rms == 0.8:
		sum_rms[7] += 1
	if rms == 0.9:
		sum_rms[8] += 1
	if rms == 1.0:
		sum_rms[9] += 1
	if rms == 1.1:
		sum_rms[10] += 1
	if rms == 1.2:
		sum_rms[11] += 1
	if rms == 1.3:
		sum_rms[12] += 1
	if rms == 1.4:
		sum_rms[13] += 1
	if rms == 1.5:
		sum_rms[14] += 1
	if rms == 1.6:
		sum_rms[15] += 1
	if rms == 1.7:
		sum_rms[16] += 1
	if rms == 1.8:
		sum_rms[17] += 1
	if rms == 1.9:
		sum_rms[18] += 1
	if rms == 2.0:
		sum_rms[19] += 1
	if rms > 2:
		sum_rms[20] += 1
	#####################SUMA MAGNITUD#####################################
def func_mag():
	if mag == 0:
		sum_mag[0] += 1
	if mag > 0:
		if mag <= 0.5:
			sum_mag[1] += 1
	if mag > 0.5:
		if mag <= 1.0:
			sum_mag[2] += 1
	if mag > 1.0:
		if mag <= 1.5:
			sum_mag[3] += 1
	if mag > 1.5:
		if mag <= 2.0:
			sum_mag[4] += 1
	if mag > 2.0:
		if mag <= 2.5:
			sum_mag[5] += 1
	if mag > 2.5:
		if mag <= 3.0:
			sum_mag[6] += 1
	if mag > 3.0:
		if mag <= 3.5:
			sum_mag[7] += 1
	if mag > 3.5:
		if mag <= 4.0:
			sum_mag[8] += 1
	if mag > 4.0:
		if mag <= 4.5:
			sum_mag[9] += 1
	if mag > 4.5:
		if mag <= 5.0:
			sum_mag[10] += 1
	if mag > 5.0:
		if mag <= 5.5:
			sum_mag[11] += 1
	if mag > 5.5:
		if mag <= 6.0:
			sum_mag[12] += 1
	if mag > 6.0:
		if mag <= 6.5:
			sum_mag[13] += 1
	if mag > 6.5:
		if mag <= 7.0:
			sum_mag[14] += 1
	if mag > 7.0:
		if mag <= 7.5:
			sum_mag[15] += 1
	if mag > 7.5:
		if mag <= 8.0:
			sum_mag[16] += 1
	if mag > 8.0:
		if mag <= 8.5:
			sum_mag[17] += 1
	if mag > 8.5:
		if mag <= 9.0:
			sum_mag[18] += 1
	if mag > 9.0:
		if mag <= 9.5:
			sum_mag[19] += 1
	if mag > 9.5:
		if mag <= 10.0:
			sum_mag[20] += 1
##############################Valores de Sumas Total###############################
for line in lines:
	campo = line.split(' ')
	prof = float(line[30:35])
	rms = float(line[43:46])
	mag = float(line[48:51])
	func_prof()
	func_rms()
	func_mag()

#print sum_prof	
#print sum_rms
#print sum_mag
sum_magT[:]=sum_mag[:]
sum_profT[:]=sum_prof[:]
#print sum_magT
#print sum_mag
##############################Valores de Sumas Magnitud por RMS#########################
#del sum_mag
sum_mag=[0 for i in range(21)]
for line in lines:
	campo = line.split(' ')
	prof = float(line[30:35])
	rms = float(line[43:46])
	mag = float(line[48:51])
	if rms==0.1:
		func_mag()
sum_magM[0][:]=sum_mag[:]
#del sum_mag
sum_mag=[0 for i in range(21)]
for line in lines:
	campo = line.split(' ')
	prof = float(line[30:35])
	rms = float(line[43:46])
	mag = float(line[48:51])
	if rms==0.2:
		func_mag()
sum_magM[1][:]=sum_mag[:]
#del sum_mag
sum_mag=[0 for i in range(21)]
for line in lines:
	campo = line.split(' ')
	prof = float(line[30:35])
	rms = float(line[43:46])
	mag = float(line[48:51])
	if rms==0.3:
		func_mag()
sum_magM[2][:]=sum_mag[:]
#del sum_mag
sum_mag=[0 for i in range(21)]
for line in lines:
	campo = line.split(' ')
	prof = float(line[30:35])
	rms = float(line[43:46])
	mag = float(line[48:51])
	if rms==0.4:
		func_mag()
sum_magM[3][:]=sum_mag[:]
#del sum_mag
sum_mag=[0 for i in range(21)]
for line in lines:
	campo = line.split(' ')
	prof = float(line[30:35])
	rms = float(line[43:46])
	mag = float(line[48:51])
	if rms==0.5:
		func_mag()
sum_magM[4][:]=sum_mag[:]
#del sum_mag
sum_mag=[0 for i in range(21)]
for line in lines:
	campo = line.split(' ')
	prof = float(line[30:35])
	rms = float(line[43:46])
	mag = float(line[48:51])
	if rms==0.6:
		func_mag()
sum_magM[5][:]=sum_mag[:]
#del sum_mag
sum_mag=[0 for i in range(21)]
for line in lines:
	campo = line.split(' ')
	prof = float(line[30:35])
	rms = float(line[43:46])
	mag = float(line[48:51])
	if rms==0.7:
		func_mag()
sum_magM[6][:]=sum_mag[:]
#del sum_mag
sum_mag=[0 for i in range(21)]
for line in lines:
	campo = line.split(' ')
	prof = float(line[30:35])
	rms = float(line[43:46])
	mag = float(line[48:51])
	if rms==0.8:
		func_mag()
sum_magM[7][:]=sum_mag[:]
#del sum_mag
sum_mag=[0 for i in range(21)]
for line in lines:
	campo = line.split(' ')
	prof = float(line[30:35])
	rms = float(line[43:46])
	mag = float(line[48:51])
	if rms==0.9:
		func_mag()
sum_magM[8][:]=sum_mag[:]
#del sum_mag
sum_mag=[0 for i in range(21)]
for line in lines:
	campo = line.split(' ')
	prof = float(line[30:35])
	rms = float(line[43:46])
	mag = float(line[48:51])
	if rms==1.0:
		func_mag()
sum_magM[9][:]=sum_mag[:]
#del sum_mag
sum_mag=[0 for i in range(21)]
for line in lines:
	campo = line.split(' ')
	prof = float(line[30:35])
	rms = float(line[43:46])
	mag = float(line[48:51])
	if rms==1.1:
		func_mag()
sum_magM[10][:]=sum_mag[:]
#del sum_mag
sum_mag=[0 for i in range(21)]
for line in lines:
	campo = line.split(' ')
	prof = float(line[30:35])
	rms = float(line[43:46])
	mag = float(line[48:51])
	if rms==1.2:
		func_mag()
sum_magM[11][:]=sum_mag[:]
#del sum_mag
sum_mag=[0 for i in range(21)]
for line in lines:
	campo = line.split(' ')
	prof = float(line[30:35])
	rms = float(line[43:46])
	mag = float(line[48:51])
	if rms==1.3:
		func_mag()
sum_magM[12][:]=sum_mag[:]
#del sum_mag
sum_mag=[0 for i in range(21)]
for line in lines:
	campo = line.split(' ')
	prof = float(line[30:35])
	rms = float(line[43:46])
	mag = float(line[48:51])
	if rms==1.4:
		func_mag()
sum_magM[13][:]=sum_mag[:]
#del sum_mag
sum_mag=[0 for i in range(21)]
for line in lines:
	campo = line.split(' ')
	prof = float(line[30:35])
	rms = float(line[43:46])
	mag = float(line[48:51])
	if rms==1.5:
		func_mag()
sum_magM[14][:]=sum_mag[:]
#del sum_mag
sum_mag=[0 for i in range(21)]
for line in lines:
	campo = line.split(' ')
	prof = float(line[30:35])
	rms = float(line[43:46])
	mag = float(line[48:51])
	if rms==1.6:
		func_mag()
sum_magM[15][:]=sum_mag[:]
#del sum_mag
sum_mag=[0 for i in range(21)]
for line in lines:
	campo = line.split(' ')
	prof = float(line[30:35])
	rms = float(line[43:46])
	mag = float(line[48:51])
	if rms==1.7:
		func_mag()
sum_magM[16][:]=sum_mag[:]
#del sum_mag
sum_mag=[0 for i in range(21)]
for line in lines:
	campo = line.split(' ')
	prof = float(line[30:35])
	rms = float(line[43:46])
	mag = float(line[48:51])
	if rms==1.8:
		func_mag()
sum_magM[17][:]=sum_mag[:]
#del sum_mag
sum_mag=[0 for i in range(21)]
for line in lines:
	campo = line.split(' ')
	prof = float(line[30:35])
	rms = float(line[43:46])
	mag = float(line[48:51])
	if rms==1.9:
		func_mag()
sum_magM[18][:]=sum_mag[:]
#del sum_mag
sum_mag=[0 for i in range(21)]
for line in lines:
	campo = line.split(' ')
	prof = float(line[30:35])
	rms = float(line[43:46])
	mag = float(line[48:51])
	if rms==2.0:
		func_mag()
sum_magM[19][:]=sum_mag[:]
#del sum_mag
sum_mag=[0 for i in range(21)]
for line in lines:
	campo = line.split(' ')
	prof = float(line[30:35])
	rms = float(line[43:46])
	mag = float(line[48:51])
	if rms>2.0:
		func_mag()
sum_magM[20][:]=sum_mag[:]
#del sum_mag

##############################Valores de Sumas Profundidad por RMS######################
del sum_prof
sum_prof=[0 for i in range(21)]
for line in lines:
	campo = line.split(' ')
	prof = float(line[30:35])
	rms = float(line[43:46])
	mag = float(line[48:51])
	if rms==0.1:
		func_prof()
sum_profM[0][:]=sum_prof[:]
del sum_prof
sum_prof=[0 for i in range(21)]
for line in lines:
	campo = line.split(' ')
	prof = float(line[30:35])
	rms = float(line[43:46])
	mag = float(line[48:51])
	if rms==0.2:
		func_prof()
sum_profM[1][:]=sum_prof[:]
del sum_prof
sum_prof=[0 for i in range(21)]
for line in lines:
	campo = line.split(' ')
	prof = float(line[30:35])
	rms = float(line[43:46])
	mag = float(line[48:51])
	if rms==0.3:
		func_prof()
sum_profM[2][:]=sum_prof[:]
del sum_prof
sum_prof=[0 for i in range(21)]
for line in lines:
	campo = line.split(' ')
	prof = float(line[30:35])
	rms = float(line[43:46])
	mag = float(line[48:51])
	if rms==0.4:
		func_prof()
sum_profM[3][:]=sum_prof[:]
del sum_prof
sum_prof=[0 for i in range(21)]
for line in lines:
	campo = line.split(' ')
	prof = float(line[30:35])
	rms = float(line[43:46])
	mag = float(line[48:51])
	if rms==0.5:
		func_prof()
sum_profM[4][:]=sum_prof[:]
del sum_prof
sum_prof=[0 for i in range(21)]
for line in lines:
	campo = line.split(' ')
	prof = float(line[30:35])
	rms = float(line[43:46])
	mag = float(line[48:51])
	if rms==0.6:
		func_prof()
sum_profM[5][:]=sum_prof[:]
del sum_prof
sum_prof=[0 for i in range(21)]
for line in lines:
	campo = line.split(' ')
	prof = float(line[30:35])
	rms = float(line[43:46])
	mag = float(line[48:51])
	if rms==0.7:
		func_prof()
sum_profM[6][:]=sum_prof[:]
del sum_prof
sum_prof=[0 for i in range(21)]
for line in lines:
	campo = line.split(' ')
	prof = float(line[30:35])
	rms = float(line[43:46])
	mag = float(line[48:51])
	if rms==0.8:
		func_prof()
sum_profM[7][:]=sum_prof[:]
del sum_prof
sum_prof=[0 for i in range(21)]
for line in lines:
	campo = line.split(' ')
	prof = float(line[30:35])
	rms = float(line[43:46])
	mag = float(line[48:51])
	if rms==0.9:
		func_prof()
sum_profM[8][:]=sum_prof[:]
del sum_prof
sum_prof=[0 for i in range(21)]
for line in lines:
	campo = line.split(' ')
	prof = float(line[30:35])
	rms = float(line[43:46])
	mag = float(line[48:51])
	if rms==1.0:
		func_prof()
sum_profM[9][:]=sum_prof[:]
del sum_prof
sum_prof=[0 for i in range(21)]
for line in lines:
	campo = line.split(' ')
	prof = float(line[30:35])
	rms = float(line[43:46])
	mag = float(line[48:51])
	if rms==1.1:
		func_prof()
sum_profM[10][:]=sum_prof[:]
del sum_prof
sum_prof=[0 for i in range(21)]
for line in lines:
	campo = line.split(' ')
	prof = float(line[30:35])
	rms = float(line[43:46])
	mag = float(line[48:51])
	if rms==1.2:
		func_prof()
sum_profM[11][:]=sum_prof[:]
del sum_prof
sum_prof=[0 for i in range(21)]
for line in lines:
	campo = line.split(' ')
	prof = float(line[30:35])
	rms = float(line[43:46])
	mag = float(line[48:51])
	if rms==1.3:
		func_prof()
sum_profM[12][:]=sum_prof[:]
del sum_prof
sum_prof=[0 for i in range(21)]
for line in lines:
	campo = line.split(' ')
	prof = float(line[30:35])
	rms = float(line[43:46])
	mag = float(line[48:51])
	if rms==1.4:
		func_prof()
sum_profM[13][:]=sum_prof[:]
del sum_prof
sum_prof=[0 for i in range(21)]
for line in lines:
	campo = line.split(' ')
	prof = float(line[30:35])
	rms = float(line[43:46])
	mag = float(line[48:51])
	if rms==1.5:
		func_prof()
sum_profM[14][:]=sum_prof[:]
del sum_prof
sum_prof=[0 for i in range(21)]
for line in lines:
	campo = line.split(' ')
	prof = float(line[30:35])
	rms = float(line[43:46])
	mag = float(line[48:51])
	if rms==1.6:
		func_prof()
sum_profM[15][:]=sum_prof[:]
del sum_prof
sum_prof=[0 for i in range(21)]
for line in lines:
	campo = line.split(' ')
	prof = float(line[30:35])
	rms = float(line[43:46])
	mag = float(line[48:51])
	if rms==1.7:
		func_prof()
sum_profM[16][:]=sum_prof[:]
del sum_prof
sum_prof=[0 for i in range(21)]
for line in lines:
	campo = line.split(' ')
	prof = float(line[30:35])
	rms = float(line[43:46])
	mag = float(line[48:51])
	if rms==1.8:
		func_prof()
sum_profM[17][:]=sum_prof[:]
del sum_prof
sum_prof=[0 for i in range(21)]
for line in lines:
	campo = line.split(' ')
	prof = float(line[30:35])
	rms = float(line[43:46])
	mag = float(line[48:51])
	if rms==1.9:
		func_prof()
sum_profM[18][:]=sum_prof[:]
del sum_prof
sum_prof=[0 for i in range(21)]
for line in lines:
	campo = line.split(' ')
	prof = float(line[30:35])
	rms = float(line[43:46])
	mag = float(line[48:51])
	if rms==2.0:
		func_prof()
sum_profM[19][:]=sum_prof[:]
del sum_prof
sum_prof=[0 for i in range(21)]
for line in lines:
	campo = line.split(' ')
	prof = float(line[30:35])
	rms = float(line[43:46])
	mag = float(line[48:51])
	if rms > 2.0:
		func_prof()
sum_profM[20][:]=sum_prof[:]

##############################Valores de Profundidad por Magnitud#####################

del sum_prof
sum_prof=[0 for i in range(21)]
for line in lines:
	campo = line.split(' ')
	prof = float(line[30:35])
	rms = float(line[43:46])
	mag = float(line[48:51])
	if mag == 0:
		func_prof()
sum_profM2[0][:]=sum_prof[:]
del sum_prof
sum_prof=[0 for i in range(21)]
for line in lines:
	campo = line.split(' ')
	prof = float(line[30:35])
	rms = float(line[43:46])
	mag = float(line[48:51])
	if mag > 0:
		if mag <= 0.5:
			func_prof()
sum_profM2[1][:]=sum_prof[:]
del sum_prof
sum_prof=[0 for i in range(21)]
for line in lines:
	campo = line.split(' ')
	prof = float(line[30:35])
	rms = float(line[43:46])
	mag = float(line[48:51])
	if mag > 0.5:
		if mag <= 1.0:
			func_prof()
sum_profM2[2][:]=sum_prof[:]
del sum_prof
sum_prof=[0 for i in range(21)]
for line in lines:
	campo = line.split(' ')
	prof = float(line[30:35])
	rms = float(line[43:46])
	mag = float(line[48:51])
	if mag > 1.0:
		if mag <= 1.5:
			func_prof()
sum_profM2[3][:]=sum_prof[:]
del sum_prof
sum_prof=[0 for i in range(21)]
for line in lines:
	campo = line.split(' ')
	prof = float(line[30:35])
	rms = float(line[43:46])
	mag = float(line[48:51])
	if mag > 1.5:
		if mag <= 2.0:
			func_prof()
sum_profM2[4][:]=sum_prof[:]
del sum_prof
sum_prof=[0 for i in range(21)]
for line in lines:
	campo = line.split(' ')
	prof = float(line[30:35])
	rms = float(line[43:46])
	mag = float(line[48:51])
	if mag > 2.0:
		if mag <= 2.5:
			func_prof()
sum_profM2[5][:]=sum_prof[:]
del sum_prof
sum_prof=[0 for i in range(21)]
for line in lines:
	campo = line.split(' ')
	prof = float(line[30:35])
	rms = float(line[43:46])
	mag = float(line[48:51])
	if mag > 2.5:
		if mag <= 3.0:
			func_prof()
sum_profM2[6][:]=sum_prof[:]
del sum_prof
sum_prof=[0 for i in range(21)]
for line in lines:
	campo = line.split(' ')
	prof = float(line[30:35])
	rms = float(line[43:46])
	mag = float(line[48:51])
	if mag > 3.0:
		if mag <= 3.5:
			func_prof()
sum_profM2[7][:]=sum_prof[:]
del sum_prof
sum_prof=[0 for i in range(21)]
for line in lines:
	campo = line.split(' ')
	prof = float(line[30:35])
	rms = float(line[43:46])
	mag = float(line[48:51])
	if mag > 3.5:
		if mag <= 4.0:
			func_prof()
sum_profM2[8][:]=sum_prof[:]
del sum_prof
sum_prof=[0 for i in range(21)]
for line in lines:
	campo = line.split(' ')
	prof = float(line[30:35])
	rms = float(line[43:46])
	mag = float(line[48:51])
	if mag > 4.0:
		if mag <= 4.5:
			func_prof()
sum_profM2[9][:]=sum_prof[:]
del sum_prof
sum_prof=[0 for i in range(21)]
for line in lines:
	campo = line.split(' ')
	prof = float(line[30:35])
	rms = float(line[43:46])
	mag = float(line[48:51])
	if mag > 4.5:
		if mag <= 5.0:
			func_prof()
sum_profM2[10][:]=sum_prof[:]
del sum_prof
sum_prof=[0 for i in range(21)]
for line in lines:
	campo = line.split(' ')
	prof = float(line[30:35])
	rms = float(line[43:46])
	mag = float(line[48:51])
	if mag > 5.0:
		if mag <= 5.5:
			func_prof()
sum_profM2[11][:]=sum_prof[:]
del sum_prof
sum_prof=[0 for i in range(21)]
for line in lines:
	campo = line.split(' ')
	prof = float(line[30:35])
	rms = float(line[43:46])
	mag = float(line[48:51])
	if mag > 5.5:
		if mag <= 6.0:
			func_prof()
sum_profM2[12][:]=sum_prof[:]
del sum_prof
sum_prof=[0 for i in range(21)]
for line in lines:
	campo = line.split(' ')
	prof = float(line[30:35])
	rms = float(line[43:46])
	mag = float(line[48:51])
	if mag > 6.0:
		if mag <= 6.5:
			func_prof()
sum_profM2[13][:]=sum_prof[:]
del sum_prof
sum_prof=[0 for i in range(21)]
for line in lines:
	campo = line.split(' ')
	prof = float(line[30:35])
	rms = float(line[43:46])
	mag = float(line[48:51])
	if mag > 6.5:
		if mag <= 7.0:
			func_prof()
sum_profM2[14][:]=sum_prof[:]
del sum_prof
sum_prof=[0 for i in range(21)]
for line in lines:
	campo = line.split(' ')
	prof = float(line[30:35])
	rms = float(line[43:46])
	mag = float(line[48:51])
	if mag > 7.0:
		if mag <= 7.5:
			func_prof()
sum_profM2[15][:]=sum_prof[:]
del sum_prof
sum_prof=[0 for i in range(21)]
for line in lines:
	campo = line.split(' ')
	prof = float(line[30:35])
	rms = float(line[43:46])
	mag = float(line[48:51])
	if mag > 7.5:
		if mag <= 8.0:
			func_prof()
sum_profM2[16][:]=sum_prof[:]
del sum_prof
sum_prof=[0 for i in range(21)]
for line in lines:
	campo = line.split(' ')
	prof = float(line[30:35])
	rms = float(line[43:46])
	mag = float(line[48:51])
	if mag > 8.0:
		if mag <= 8.5:
			func_prof()
sum_profM2[17][:]=sum_prof[:]
del sum_prof
sum_prof=[0 for i in range(21)]
for line in lines:
	campo = line.split(' ')
	prof = float(line[30:35])
	rms = float(line[43:46])
	mag = float(line[48:51])
	if mag > 8.5:
		if mag <= 9.0:
			func_prof()
sum_profM2[18][:]=sum_prof[:]
del sum_prof
sum_prof=[0 for i in range(21)]
for line in lines:
	campo = line.split(' ')
	prof = float(line[30:35])
	rms = float(line[43:46])
	mag = float(line[48:51])
	if mag > 9.0:
		if mag <= 9.5:
			func_prof()
sum_profM2[19][:]=sum_prof[:]
del sum_prof
sum_prof=[0 for i in range(21)]
for line in lines:
	campo = line.split(' ')
	prof = float(line[30:35])
	rms = float(line[43:46])
	mag = float(line[48:51])
	if mag > 9.5:
		if mag <= 10.0:
			func_prof()
sum_profM2[20][:]=sum_prof[:]



#print sum_prof
#print sum_profM[5][:]
#print sum_profT
#print sum_profM
g = Gnuplot.Gnuplot()
#########################Grafias 2D Localizacion vs Errores###################
g.title('LATITUD VS ERROR EN LATITUD')
g('set terminal jpeg')
g('set output "late.jpg"')
g.xlabel('LATITUD')
g.ylabel('ERROR')
#g('set yrange [0:100]')
#g('set xrange [-10:200]')
g('unset key')
g('plot "report.out" u 1:2')
#raw_input('Please press return to continue...\n')

g.title('LONGITUD VS ERROR EN LONGITUD')
g('set terminal jpeg')
g('set output "lone.jpg"')
g.xlabel('LONGITUD')
g.ylabel('ERROR')
g('set autoscale')
g('plot "report.out" u 3:4')
#raw_input('Please press return to continue...\n')

g.title('PROFUNDIDAD VS ERROR EN PROFUNDIDAD')
g('set terminal jpeg')
g('set output "profe.jpg"')
g.xlabel('PROFUNDIDAD')
g.ylabel('ERROR')
g('plot "report.out" u 5:6')
#raw_input('Please press return to continue...\n')
	
#########################Grafias 2D Prof,Mag,RMS###################

#g('set xrange [0:200]')
#g('set yrange [0.1:20]')
g.title('PROFUNDIDAD')
g('set terminal jpeg')
g('set output "prof.jpg"')
g.xlabel('Profundidad')
g.ylabel('Numero de Sismos')
g.plot(Gnuplot.Data(vec_prof,sum_profT,inline=1, with_='linespoints'))
#raw_input('Please press return to continue...\n')


g('set boxwidth 0.9 relative')
g('set terminal jpeg')
g('set output "profb.jpg"')
g('set style fill solid 1')
g.plot(Gnuplot.Data(vec_prof,sum_profT,inline=1, with_='boxes'))
#raw_input('Please press return to continue...\n')


#print vec_rms
#g('set xrange [0:2.0]')
#g('set yrange [0.1:20]')
g('set terminal jpeg')
g('set output "rms.jpg"')
g.title('RMS')
g.xlabel('RMS')
g.ylabel('Numero de Sismos')
g.plot(Gnuplot.Data(vec_rms,sum_rms,inline=1, with_='linespoints'))
#raw_input('Please press return to continue...\n')
#print vec_mag

g('set boxwidth 0.9 relative')
g('set style fill solid 1')
g('set terminal jpeg')
g('set output "rmsb.jpg"')
g.plot(Gnuplot.Data(vec_rms,sum_rms,inline=1, with_='boxes'))
#raw_input('Please press return to continue...\n')


#g('set xrange [0:9.0]')
#g('set yrange [0.1:20]')
g('set terminal jpeg')
g('set output "mag.jpg"')
g.title('MAGNITUD')
g.xlabel('Magnitud Ml')
g.ylabel('Numero de Sismos')
g.plot(Gnuplot.Data(vec_mag,sum_magT,inline=1, with_='linespoints'))
#raw_input('Please press return to continue...\n')

g('set boxwidth 0.9 relative')
g('set style fill solid 1')
g('set terminal jpeg')
g('set output "magb.jpg"')
g.plot(Gnuplot.Data(vec_mag,sum_magT,inline=1, with_='boxes'))
#raw_input('Please press return to continue...\n')


#g.splot(Gnuplot.Data(vec_prof,vec_rms,sum_prof, with_='linesp', inline=0))

#x=[0 for i in range(21)]
#y=[0 for i in range(21)]

#hacer un arreglo con numpy
#x = numpy.arange(1,22,1)
#y = numpy.arange(1,22,1)


xm = vec_rms[:,numpy.newaxis]
ym = vec_mag[numpy.newaxis,:]
zm = vec_prof[numpy.newaxis,:]

######################Grafica 3D Profundidad####################################
m = (sum_profT+zm-zm+xm-xm)
g('set terminal jpeg')
g('set output "prof3d.jpg"')
g('set pm3d')
g.title('Profundidad')
g('set zlabel "Numero de sismos" rotate parallel ')
g.xlabel('')
g.ylabel('Profundidad')
g('unset xtics')
g('set view 75,75')
g('set palette defined (0 "blue", 4 "white", 9 "red")')
g.splot(Gnuplot.GridData(m,vec_rms,vec_prof, binary=0, inline=0, with_='pm3d'))
#raw_input('Please press return to continue...\n')
############################Grafica 3D RMS####################################
del m
m = (sum_rms+ym-ym+xm-xm)
g('set pm3d')
g('set terminal jpeg')
g('set output "rms3d.jpg"')
g.title('RMS')
g('set zlabel "Numero de sismos" rotate parallel ')
g.xlabel('')
g.ylabel('RMS')
g('unset xtics')
g('set view 75,75')
g('set palette defined (0 "blue", 4 "white", 9 "red")')
g.splot(Gnuplot.GridData(m,vec_mag,vec_rms, binary=0, inline=0, with_='pm3d'))
#raw_input('Please press return to continue...\n')
######################Grafica 3D Magnitud####################################
del m
m = (sum_magT+ym-ym+xm-xm)
#print m
#g('set dgrid3d 50,50')
#g('set isosample 100')
#g('set contour base')
#g('set hidden3d')
g('set terminal jpeg')
g('set output "mag3d.jpg"')
g('set pm3d')
#g('set palette gray')
g.title('Magnitud')
g('set zlabel "Numero de sismos" rotate parallel ')
g.xlabel('')
g.ylabel('Magnitud ML')
#g('set zlabel "Nuemro de Sismos"')
g('unset xtics')
g('set view 75,75')
#g('set xrange [0.1:2.1]')
#g('set yrange [0.0:10.0]')
#g('set zrange [0:10]')
g('set palette defined (0 "blue", 4 "white", 9 "red")')
g.splot(Gnuplot.GridData(m,vec_rms,vec_mag, binary=0, inline=0, with_='pm3d'))
#raw_input('Please press return to continue...\n')
############################Grafica RMS-PROFUNDIDAD-#Sismos##############################
#print sum_profM
#g('set terminal jpeg')
#g('set output "rms-prof-num.jpg"')
g.xlabel('RMS')
g.ylabel('PROFUNDIDAD')
g.title('PROFUNDIDAD vs RMS')
g('set xtics auto')
g('set zlabel "Numero de sismos" rotate parallel ')
#g('set zrange [0:5]')
g('set xrange [0:1.5]')
g('set yrange [0:30]')
g('set grid ytics')
g('set grid xtics')
#g('set dgrid3d 50, 50')
#g('unset surface')
#g('set hidden3d')
g('set view 60,60')  
g('set contour base')
g('unset pm3d')
g('set palette defined (0 "white", 1 "black")')
g.splot(Gnuplot.GridData(sum_profM,vec_rms,vec_prof, binary=0, inline=0, with_='pm3d'))
raw_input('Please press return to continue...\n')


############################Grafica Magnitud-PROFUNDIDAD-#Sismos###################
#print sum_profM2
g.xlabel('MAGNITUD Ml')
g('set terminal jpeg')
g('set output "mag-prof-num.jpg"')
g.ylabel('PROFUNDIDAD')
g.title('Magnitud vs Profundidad')
g('set xtics auto')
g('set zlabel "Numero de sismos" rotate parallel ')
#g('set zrange [0:6000]')
g('set xrange [0:5.0]')
g('set yrange [0:30]')
g('set grid ytics')
g('set grid xtics')
#g('set dgrid3d 50, 50')
#g('unset surface')
#g('set hidden3d')
g('set view 60,60')  
g('set contour base')
g('unset pm3d')
g('set palette defined (0 "white", 1 "black")')
g.splot(Gnuplot.GridData(sum_profM2,vec_mag,vec_prof, binary=0, inline=0, with_='pm3d'))
#raw_input('Please press return to continue...\n')



############################Grafica RMS-MAGNITUD-#Sismos##############################
#print sum_magM
g.xlabel('RMS')
g('set terminal jpeg')
g('set output "rms-mag-num.jpg"')
g.ylabel('MAGNITUD Ml')
g.title('Magnitud vs RMS')
g('set xtics auto')
g('set zlabel "Numero de sismos" rotate parallel ')
#g('set zrange [0:5]')
g('set xrange [0.1:1.0]')
g('set yrange [0.0:5]')
g('set grid ytics')
g('set grid xtics')
#g('set dgrid3d 50, 50')
#g('unset surface')
#g('set hidden3d')
g('set view 60,60')  
g('set contour base')
g('unset pm3d')
g('set palette defined (0 "white", 1 "black")')
g.splot(Gnuplot.GridData(sum_magM,vec_rms,vec_mag, binary=0, inline=0, with_='pm3d'))
#raw_input('Please press return to continue...\n')

############################Grafica Sismos-Tiempo##############################





#Gnuplot.Data(vec_prof,sum_prof,inline=1, with_='linespoints', filename=filename1) #Guardar archivo

