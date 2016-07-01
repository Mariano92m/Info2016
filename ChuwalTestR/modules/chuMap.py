#!/usr/bin/env python
# -*- coding: utf-8 -*-
from gluon import *
from gluon.serializers import loads_json
from applications.ChuwalTestR.modules import chuControll
    
#Controlador para el mapa
def getMarkers(base):
    places = []
    rows = base(base.place.id >0 ).select()

    for row in rows:
        #Color del marcador
        x= chuControll.setMarkerColor(row.cazada)
        #Imagen de la escultura
        imagen= chuControll.showIMG(row.cazada, row.sculpture_id.fileImageC)
        #Boton
        but= chuControll.showBut(row.cazada, row.sculpture_id.fileImageC)
        
        #Codigo html va en este sector
        html =  (
                '<div class="container" style="width: 200px;">'
                    '<center>''<img src=' + imagen + ' style="width: 100%;"/>''</center>'
                    '<center>''<button id="but1">'+ but +'</button>''</center>'
                '</div>'
                ) 
        
        #Setea la informacion de los marcadores
        place = {
            'lat' : row.lat,
            'lng' : row.lng,
            'name' : row.name,
            'cazada':row.cazada,
            'icon': x,
            'infoWindow' : {
                'content' : html,
                'maxWidth' : 200
            },
            'onClick':{}
        }

        #Agrega un marcador a la lista de marcadores
        places.append(place)
    return response.json(places)