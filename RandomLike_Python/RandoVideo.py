#!/usr/bin/python

#Codigo de ALSW bajo GPL v3
#El codigo busca entre los comentario a un ganador para un concurso, siempre que alla etiquedado a otra persona
#Necesario dejarlo en /bin del Arduino Yun
#Se puede usar scp /MiCarpeta/RandomLike.py root@arduino.local:/bin/

import urllib2, json, datetime, random

access_token = ''#Token que acceso a FB
VideoID = ''#ID de la Video 
URL = 'https://graph.facebook.com/' + VideoID + '?fields=comments.limit(1000){message_tags,message}&access_token='+access_token #URL para FB

data = urllib2.urlopen(URL).read()#optiene los ultimos 1000 comentarios de la FotoID
DatosFB = json.loads(data)#Transformar los datos a un areglo JSON

CantidadComentarios  = len(DatosFB['comments']['data'])-1#Cuanto comentarios hay

Encontrado = False#variable para buscar el ganador
Ganador = 0 #ID del ganador

while not Encontrado: ##buscara hasta que encuentre a un ganador que tiene que haber etiquetado a alquien
	Ganador = random.randint(0,CantidadComentarios)#Se escoje uno Rando 
	if 'message_tags' in DatosFB['comments']['data'][Ganador]: #busca si equeto a alquien 
		Encontrado = True 

TrasID = DatosFB['comments']['data'][Ganador]['id'] # guarda el ide del comentario 


#hace de nuevo la busqueda en fb pero esta ves para buscar el nombre del ganador
URL2 = 'https://graph.facebook.com/' + TrasID + '?fields=from&access_token='+access_token
data2 = urllib2.urlopen(URL2).read()
DatosFB2 = json.loads(data2)#Transformar los datos a un areglo JSON

#Se imprimi el numero del gando como el ID y Nombre
print "#" + str(Ganador)
print "$" + DatosFB2['from']['id']
print "@" + DatosFB2['from']['name']
