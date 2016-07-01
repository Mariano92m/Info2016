#!/usr/bin/env python
# -*- coding: utf-8 -*-
from gluon import *
#Cambia el color del marcador dependiendo si esta cazada o no
def setMarkerColor(cazada):
    if(cazada =='S' or cazada =='N'):
        if(cazada=='S'):
            return "\Chuwal\static\images\PinVerde.png"
        else:
            return "\Chuwal\static\images\PinRojo.png"


#Muestra una imagen dependiendo si esta cazada o no
def showIMG(condition, imgC):
    if(imgC != "none"):

        if(condition=='S'):
            imagen= '"' + imgC + '"';
        
        elif(condition=='N'):
            imagen= '"' + imgC + '"'; #Blured
    
    else:
        imagen ="https://media.giphy.com/media/pSpmpxFxFwDpC/giphy.gif"
    
    return imagen

#Muestra un boton dependiendo si esta cazada o no
def showBut(condition, imgC):
    if(imgC != "none"):

        if(condition=='S'):
            but='<a href="#" class="btn">Ver info</a>';
        
        elif(condition=='N'):
            but='<a href="#" class="btn">Cazar</a>';
    
    else:
        but='<a href="#" class="btn">Error</a>';
    return but
