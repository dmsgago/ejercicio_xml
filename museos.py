#!/usr/bin/python
# -*- encoding: utf-8 -*-
#Diego Martin Sanchez 1ºASIR, ejercicio_xml

#Importa la clase etree de la librería lxml
from lxml import etree

#Declara las variables utilizadas
nsmap=''
museos=[]
nummuseos=0
nombremuseo=''
propiedad=[]

#Almacena el contenido del fichero XML en una variable
fich=etree.parse("museos.xml")
#Almacena el nombre de espacio utilizado en el fichero xml
raiz=fich.getroot()
nsmap=raiz.tag[:-3]

#Muestra el numero de museos de la provincia de Sevilla
museos=fich.getroot().findall("%sDocument/%sFolder/%sPlacemark"%(nsmap,nsmap,nsmap))
nummuseos=len(museos)
print('\nHay %d museos en Sevilla'%nummuseos)

#Muestra el nombre de todos los museos
print('\nLos nombres de los distintos museos son:')
for museo in museos:
    propiedades=museo.findall('%sExtendedData/%sSchemaData/%sSimpleData'%(nsmap,nsmap,nsmap))
    for propiedad in propiedades:
        if propiedad.attrib["name"] == "NOMBRE":
            print('\t%s'%propiedad.text)

