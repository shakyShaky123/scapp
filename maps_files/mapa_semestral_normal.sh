#!/bin/bash

#rm -rf .gmtdefaults
rm -rf .gmtcommands
rm -f *.ps

gmtset FONT_ANNOT_PRIMARY 5
gmtset FONT_LABEL 5
#gmtset FONT_TITLE 5
gmtset MAP_FRAME_TYPE fancy
gmtset MAP_FRAME_WIDTH 0.1
gmtset PS_MEDIA Custom_525x685
gmtset MAP_ORIGIN_X = 0.6
gmtset MAP_ORIGIN_Y = 0.6
#gmtset DOTS_PR_INCH 100

## Topografia, batimetria
gmt grdimage /home/topo/Col250m_bat30s.grd -I/home/topo/Col250m_bat30s_int.grd -C/home/topo/bati2.cpt -R-82/-67/-5/15 -Ba2f2 -Jm0.45i -K -P >> mapa.ps #grdimage1 
## Divisiones
gmt pscoast -R -Jm -W0.5p -Df  -Ba2f2 -N1/1p -N2/0.3p -O -P  -K >>mapa.ps #pscoast1 
## Coordenadas y magnitud de los sismos (gmtxyz.out) (comando seigmt) 
gmt psxy -R -Jm -O -K -Cpaletteluisa.cpt semestral_normal_gmt.out -Sci -W0.05 >> mapa.ps
## Nombres estaciones
#gmt pstext stations_names_up.txt -R -Jm -O -K >> mapa.ps

## Icono Estaciones
#gmt psxy -R -Jm -O -K formas.d -St0.2 -G255/255/255 -W1  >> mapa.ps #icono_estaciones 

## Icono Capitales
#gmt psxy -R -Jm -O -K capitales.d -Sc0.04 -G0/0/0 -W1 >> mapa.ps #icono_capitales
## Nombres Capitales
#gmt pstext nombresc.d -R -Jm -O -K >> mapa.ps #nombre_capitales

echo -68.5 -3.0 -1.35i 1.8i |psxy -R -Jm -O -K -Sr -Gwhite -W5/black >> mapa.ps #cuadrado_leyenda


## Icono utiliza la leyenda en profundidad (.txt) tiene los parametros del icono
gmt psxy -R -Jm -O -K -Cpalette.cpt escalaP_old.txt -Sci -W0.05 >> mapa.ps #icono_legenda_profundidad
## Leyenta Profundidad (.txt) Texto y parametros del texto de la leyenda
gmt pstext -R -Jm -O  -K textoP_old.txt -W255/255/255  >> mapa.ps #texto_leg_profundidad
## Icono utiliza la leyenda en Magnitud (.txt) tiene los parametros del icono
gmt psxy -R -Jm -O -K -Cpalette.cpt escalaM_old.txt -Sci -W0.05 >> mapa.ps #icono_leg_magnitud
## Leyenta Magnitud (.txt) Texto y parametros del texto de la leyenda
gmt pstext -R -Jm -O  -K textoM_old.txt  -W255/255/255  >> mapa.ps #texto_leg_magnitud
## Icono Leyenda Estaciones
#gmt psxy -R -Jm -O -K -Cpalettestations_all.cpt iconoE.txt -Skantena/0.15i -W0.25 >> mapa.ps #icono_leg_estaciones
## Texto Leyenda Estaciones
#gmt pstext -R -Jm -O -K  textoE.txt  >> mapa.ps #texto_leg_estaciones



gmt pslegend Legend -R -J -Dg-69.9/-1.0+w1.26i/0.59i+jLT -O -K >> mapa.ps #texto_legenda
gmt psimage  Logo-SGC.eps -Dx16.3/2.96+w1.75c+jBR -O -K >> mapa.ps #logo_legenda
gmt psbasemap -R -Jm -Lf-69.4/-4.5/2/100+l+jt -O -K -P >>mapa.ps #escala_legenda

##Mapa pequeno


gmt gmtset MAP_FRAME_WIDTH 0.01



#gmt grdimage /home/topo/bati.grd -C/home/topo/bati2.cpt -R-82/-66.7/-4.3/14 -Bf7 -Jm0.08i -O -P -K -I/home/topo/bati.ilu >> mapa.ps #grdimage_mapa_zoom
#gmt pscoast -R-82/-66.7/-4.3/14 -Jm -W0.3p/200 -Di  -N1/0.4p -O -P -K  >> mapa.ps #pscoast2_mapa_zoom 
#gmt psxy -R -Jm0.10i -O -K -Cvivi.cpt estrella.txt  -Sa0.15 -W0.25 >> mapa.ps 
#gmt psxy -R -Jm -W1p/0/0/0 -L -O -N -A -V -K << END >> mapa.ps #cuadrado_zoom  
#coordenadas_1
#coordenadas_2
#coordenadas_3
#coordenadas_4
END



## Archivos de salida


ps2pdf mapa.ps
#okular mapa.pdf
convert -density 300 mapa.pdf mapa.png
#convert mapa.pdf mapa.png
#convert -density 300 mapa.pdf -quality 100 mapa.jpg
#convert mapa.pdf mapa.jpg
mv mapa.png mapa_semestral_normal.png

rm -rf .gmtdefaults
rm -rf .gmtcommands
