#!/usr/bin/env python
from Tkinter import *
import tkFileDialog
import datetime
import tkMessageBox
import Tkinter
import sys
import os
import subprocess
import os, time, math, tempfile
import numpy 
from glob import glob
import math


parametros=glob("gmtxyz.out")
archivo=open(parametros[0],"r")
#print "Nombre del archivo : ", archivo.name
#print "Modo de apertura : ", archivo.mode
lines=archivo.readlines()
#print (lines[0])
exp_mag = []
contenido = ''
for line in lines:
	campo = line.split(' ')
	mag = float(line[26:33])
	without_mag = line[0:26]
	#print mag
	exp_mag = str(mag**2.5)
	#print exp_mag
	#print without_mag
	contenido += ''+without_mag+''+exp_mag+'\n'
	#print contenido

archivo.close()
archivo=open(parametros[0],"w")
archivo.write(contenido)
archivo.close()
