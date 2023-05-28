from django.shortcuts import render
from pathlib import Path
import json

def mapa(request):

    src = Path("resources/shapesbairros2016/poa.geojson")

    geojson = json.dumps(json.loads(src.read_text()))

    lista_crimes = ['Teste1', 'Teste2', 'Teste3']
    lista_bairros = ['Teste1', 'Teste2', 'Teste3']

    context = {'lista_crimes': lista_crimes, 'lista_bairros': lista_bairros, 'geojson': geojson}

    return render(request, 'mapa_violencia/index.html', context)

# Called by the js module that builds the leaflet map
def return_filters():
    pass