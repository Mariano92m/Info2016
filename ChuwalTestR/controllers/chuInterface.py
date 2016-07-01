from gluon import *
from applications.ChuwalTestR.modules.chuMap import getMarkers


def chuHome():
	return dict()

def chuProfile():
	return dict()

def chuUs():
	return dict()

def chuList():
	return dict()

def chuMap():
	getmark= []
	getmark= getMarkers(db)
	return dict(getmark)

def chuSculptInfo():

	return dict()


@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)

def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    return service()

def somefunction():
    pic = db(db.sculpture).select().first().picture   #select first picture
    return dict(pic=pic)

    