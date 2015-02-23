#!/usr/bin/python
# -*- encoding: utf-8 -*-
#Diego Martín Sánchez 1ºASIR, ejercicio_xml

#Importa la clase etree de la librería lxml
from lxml import etree

#Almacena el contenido del fichero XML en una variable
fichxml=etree.parse("museos.xml")

#Muestra el numero de museos de la provincia de Sevilla
len fichxml.getroot().findall("document/folder/placemark")
