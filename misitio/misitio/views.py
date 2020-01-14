from django.http import HttpResponse, Http404
import datetime

# Mostrar el resultado como una pagina HTML
HTML = """
<!DOCTYPE html>
<html lang="es">
<head>
<meta http­equiv="content­type" content="text/html; charset=utf­8">
<meta name="robots" content="NONE,NOARCHIVE">
<title>Hola mundo</title>
<style type="text/css">
html * { padding:0; margin:0; }
body * { padding:10px 20px; }
body * * { padding:0; }
body { font:small sans­serif; }
body>div { border­bottom:1px solid #ddd; }
h1 { font­weight:normal; }
#summary { background: #e0ebff; }
</style>
</head>
<body>
<div id="summary">
<h1>¡Hola Mundo!</h1>
</div>
</body></html> """

def hola(request):
	# Mostrar un texto sin ningun formato 
	#return HttpResponse("Hola Mundo")
	# Mostrar un texto en HTML
	return HttpResponse(HTML)

# Función para mostrar la fecha y hora actual
def fecha_actual(request):
	ahora = datetime.datetime.now()
	html = '<html><body><h1>Fecha</h1><h3>%s</h3></body></html>'%ahora
	return HttpResponse(html)

# Funcion que devuelve la fecha y la hora sumada segun parametros
def horas_adelante(request, offset):
	try:
		offset = int(offset)
	except ValueError:
		raise Http404()
	dt= datetime.datetime.now()+datetime.timedelta(hours=offset)
	html = "<html><body><h1>En %s hora(s), seran:</h1> <h3>	%s</h3></body></html>" % (offset, dt)
	assert False
	return HttpResponse(html)