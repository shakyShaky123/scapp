#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import time

ruta = os.path.dirname(os.path.abspath(__file__))+"/"
#ruta = "/home/camilo/scapp/"

contenido1 = ''

archivo1 = open("sc_destacados.out","r")
lines = archivo1.readlines()
contenido1 += str("#!/usr/bin/env python\n")
contenido1 += "\n"
contenido1 += "b = []\n"
contenido1 += "contenido2 = '""'\n"
i = 0
for line in lines:
	i += 1 
	contenido1 += "a = u'"+line.strip()+"'\n"
	contenido1 += "contenido2 += a.encode('latin1')+'\\n' \n"
	

contenido1 += "archivo1 = open('sc_destacados.out','w')\n"
contenido1 += "archivo1.write(contenido2)\n"
contenido1 += "archivo1.close"



archivo2 = open(ruta+"dest_modif2.py","w")
archivo2.write(contenido1)

os.system("chmod 777 "+ruta+"dest_modif2.py")

archivo2.close()

os.system("dest_modif2.py")





