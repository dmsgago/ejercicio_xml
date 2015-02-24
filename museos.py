#!/usr/bin/python
# -*- encoding: utf-8 -*-
#Diego Martin Sanchez 1ºASIR, ejercicio_xml

#Importa la clase etree de la librería lxml
from lxml import etree

#Almacena el contenido del fichero XML en una variable
fich=etree.parse("museos.xml")
#Almacena el nombre de espacio utilizado en el fichero xml
raiz=fich.getroot()
nsmap=raiz.tag[:-3]

#Muestra el numero de museos de la provincia de Sevilla
museos=fich.getroot().findall("%sDocument/%sFolder/%sPlacemark"%(nsmap,nsmap,nsmap))
nummuseos=len(museos)
print('Hay %d museos en Sevilla'%nummuseos)
