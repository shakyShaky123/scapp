#!/usr/bin/env python

b = []
contenido2 = ''
a = u'2018/03/05,14:57:11, 4.9, -75.66, -0.0, 3.3,Santa Rosa de Cabal - Risaralda, Colombia'
contenido2 += a.encode('latin1')+'\n' 
a = u'2018/03/17,10:16:12, 12.23, -72.05, 30.0, 5.0,Uribia - la Guajira, Colombia'
contenido2 += a.encode('latin1')+'\n' 
a = u'2018/03/17,15:24:01, 5.32, -77.65, 21.0, 3.9,Oc\xc3\xa9ano Pac\xc3\xadfico'
contenido2 += a.encode('latin1')+'\n' 
a = u'2018/03/21,20:44:00, 0.76, -77.93, 9.0, 3.7,Volc\xc3\xa1n Chiles'
contenido2 += a.encode('latin1')+'\n' 
a = u'2018/03/21,21:21:00, 0.75, -77.92, 9.0, 3.3,Volc\xc3\xa1n Chiles'
contenido2 += a.encode('latin1')+'\n' 
a = u'2018/03/22,04:31:34, 2.92, -76.03, 16.0, 3.9,Volc\xc3\xa1n Nevado del Huila'
contenido2 += a.encode('latin1')+'\n' 
a = u'2018/03/24,16:41:35, 4.09, -73.64, 0.0, 2.2,Villavicencio - Meta, Colombia'
contenido2 += a.encode('latin1')+'\n' 
a = u'2018/03/25,10:56:43, 0.71, -77.81, -0.0, 2.1,Colombia-Ecuador, Region Fronteriza'
contenido2 += a.encode('latin1')+'\n' 
a = u'2018/03/26,08:22:57, 6.8, -73.14, 139.0, 4.5,Los Santos - Santander, Colombia'
contenido2 += a.encode('latin1')+'\n' 
a = u'2018/03/26,17:32:00, 0.76, -77.91, 8.0, 3.4,Volc\xc3\xa1n Chiles'
contenido2 += a.encode('latin1')+'\n' 
a = u'2018/03/28,02:54:00, 0.8, -77.94, 4.0, 2.3,Volc\xc3\xa1n Chiles'
contenido2 += a.encode('latin1')+'\n' 
a = u'2018/03/30,14:29:00, 0.79, -77.95, 8.0, 2.9,Volc\xc3\xa1n Chiles'
contenido2 += a.encode('latin1')+'\n' 
a = u'2018/03/31,21:33:13, 0.78, -77.98, -1.0, 1.4,Colombia-Ecuador, Region Fronteriza'
contenido2 += a.encode('latin1')+'\n' 
archivo1 = open('sc_destacados.out','w')
archivo1.write(contenido2)
archivo1.close