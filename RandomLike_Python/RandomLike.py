#!/usr/bin/python

#Necesario dejarlo en /bin del Arduino Yun
#Se puede usar scp /MiCarpeta/RandomLike.py root@arduino.local:/bin/

import urllib2, json, datetime, random

access_token = ''#Token que acceso a FB
FotoID = ''#ID de la foto 

data = urllib2.urlopen('https://graph.facebook.com/' + FotoID + '?fields=likes.limit(1000)&access_token='+access_token).read()#optiene los ultimos 1000 comentarios de la FotoID
DatosFB = json.loads(data)#Transformar los datos a un areglo JSON

CantidadLike = len(DatosFB['likes']['data'])#Cuanto Like hay en la foto
Ganador = random.randint(0,CantidadLike)#Se escoje uno Rando 

#Se imprimi el numero del gando como el ID y Nombre
print "#" + str(Ganador)
print "$" + DatosFB['likes']['data'][Ganador]['id']
print "@" + DatosFB['likes']['data'][Ganador]['name']
