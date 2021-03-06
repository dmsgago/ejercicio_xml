#!/usr/bin/python
# -*- coding: utf-8 -*-
#Diego Martin Sanchez 1ºASIR, ejercicio_xml

#Importa la clase etree de la librería lxml
from lxml import etree

#Declara las variables utilizadas
nsmap = ''
museos = []
nummuseos = 0
nombremuseo = ''
propiedad = []
petmuseo = ''

#Almacena el contenido del fichero XML en una variable
fich = etree.parse("museos.xml")
#Almacena el nombre de espacio utilizado en el fichero xml
raiz = fich.getroot()
nsmap = raiz.tag[:-3]

#Muestra el numero de museos de la provincia de Sevilla
museos = fich.getroot().findall("%sDocument/%sFolder/%sPlacemark"%(nsmap,nsmap,nsmap))
nummuseos = len(museos)
print ('\nHay %d museos en Sevilla'%nummuseos)

raw_input('\n(Haga clic para continuar...)')

#Muestra el nombre de todos los museos
print ('\nLos nombres de los distintos museos son:')
for museo in museos:
    propiedades = museo.findall('%sExtendedData/%sSchemaData/%sSimpleData'%(nsmap,nsmap,nsmap))
    for propiedad in propiedades:
        if propiedad.attrib["name"] == "NOMBRE":
            print('\t%s'%propiedad.text)

raw_input('\n(Haga clic para continuar...)')

#Pide al usuario el nombre de un museo y muestra su direccion, telefono y horario
petmuseo = raw_input('\nIntroduce el nombre de un museo: ')
listadatos = []
datos = {}
for museo in museos:
    propiedades = museo.findall('%sExtendedData/%sSchemaData/%sSimpleData'%(nsmap,nsmap,nsmap))
    datos = {}
    for propiedad in propiedades:
        datos[propiedad.attrib['name']] = propiedad.text
    listadatos.append(datos)

#Recorre la lista de datos y muestra solo los datos del museo introducido por el usuario.
museoencontrado=True
print('\nDatos del museo %s:'%petmuseo)
for museo in listadatos[:]:
    if museo['NOMBRE'].lower() == petmuseo.lower():
        print ('\tNombre: %s\n\tDireccion: %s\n\tTelefono: %s\n\tHorario: %s'%(museo['NOMBRE'],museo['DIRECCION'],museo['TELEFONO'],museo['HORARIO']))
        museoencontrado=False
if museoencontrado:
    print ('\tMuseo desconocido: %s'%petmuseo)

#Muestra la url de la web y de la foto del museo introducido anteriormente
for museo in listadatos[:]:
    if museo['NOMBRE'].lower() == petmuseo.lower():
        print ('\tWeb: %s\n\tFoto: %s\n'%(museo['WEB'],museo['Foto']))

raw_input('\n(Haga clic para continuar...)')

#Muestra la ubicacion del museo sobre OpenStreetMap
print ('\nLos nombres de los distintos museos son:')
for museo in museos:
    if museo[0][0][1].text.lower() == petmuseo.lower():
        ubicacion=museo[1][0].text.split(',')
print ('http://www.openstreetmap.org/#map=18/%s/%s'%(ubicacion[1],ubicacion[0]))
