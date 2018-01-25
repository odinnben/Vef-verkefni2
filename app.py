import os
from bottle import route, run, static_file, error, request


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

@route('/page/<n>')
def page(n):
    return '<h3>Þessi síða er ' + n + '</h3>' \
            '<a href="/a">Back</a>'


@route('/Lidurb')
def lidurb():
    return '<h2>Verkefni 2 B</h2>' \
           '<h3>Veldu uppáhalds bókstafurinn þinn :</h3>' \
           '<a href="/favorite?image=A"><img src="/static/A.png" width="150"></a>' \
           '<a href="/favorite?image=B"><img src="/static/B.png" width="150"></a>' \
           '<a href="/favorite?image=C"><img src="/static/C.png" width="150"></a>'

@route('/favorite')
def favorite():
    image = request.query.image

    return '<h2>Uppáhalds bókstafurinn þinn: </h2>' \
           '<img src="/static/' + image +'.png" width="200">' \
           '<h4><a href="/b">Til baka</a></h4>'


@error(404)
def error404(error):
    return '<h1>Síðan sem þú baðst um er ekki til...</h1>'

@route('/static/<filename>')
def server_static(filename):
    return static_file(filename, root="./mYNDIR")

run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
