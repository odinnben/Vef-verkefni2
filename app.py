import os
from bottle import route, run

@route('/')
def index():
    return "<h2>Verkefni2</h2><br><a href='/Lidura'>lidur a</a>""\n""<a href='/Lidurb'>lidur b</a>"

@route ('/Lidura')
def Lidura():
    return "<h2>Verkefni 2A</h2><br><a href='/site1'>Síða 1</a>""\n""<a href='/site2'>Síða 2</a>""<a href='/site3'>Síða 3</a>"

@route ('/site1')
def site1():
    return "þetta er síða 1<br><a href='/Lidura'>lidur a</a>"

@route ('/site2')
def site2():
    return "þetta er síða 2<br><a href='/Lidura'>lidur a</a>"

@route ('/site3')
def site2():
    return "þetta er síða 3<br><a href='/Lidura'>lidur a</a>"

@route('/Lidurb')
def Lidurb():
    return "Here is biograph from steve jobs"

run()
