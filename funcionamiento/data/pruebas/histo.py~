#!/usr/bin/env python

import sys
import os
import numpy 
from glob import glob
from time import *
from datetime import *
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib import cm

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

func_vec = []
sta_vec = []
comp_vec = []
vec_porc = numpy.arange(0,100,1)

archivo2=open("sc_fun.out","r")
lines = archivo2.readlines()
for line in lines:
	campos = line.split(',')
	cont = 0
	for campo in campos:
		cont += 1
		if cont == 5:
			func_vec.append(float(campo))
		if cont == 4:
			comp_vec.append(campo)
		if cont == 2:
			sta_vec.append(campo)
#print func_vec
#print vec_porc

g = Gnuplot.Gnuplot()

g('set ylabel "Porcetaje Funcionamiento" rotate parallel ')
g('set xlabel "Estaciones"')
#g.title('Ocurrencia de Eventos por Meses')
g('set autoscale')
g('set terminal jpeg size 1000,400 ')
g('unset pm3d')
g('set output "porc_fun.jpg"')
#if Var70.get() ==1:
#	g('set xrange ['+v76.get()+':'+v82.get()+']')
#	g('set yrange ['+v88.get()+':'+v94.get()+']')
g('unset key')
g('set boxwidth 0.9 relative')
g('set xtics rotate')
g('set style fill solid 1')
g('set grid')
g('set xtics font ", 10"')
g('plot "sc_fun.out" u 5:xticlabels(2) with boxes')
#raw_input('Please press return to continue...\n')

