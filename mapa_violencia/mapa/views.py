from django.shortcuts import render
from django.http import JsonResponse
from mapa.models import Bairro

def mapa(request):

    lista_crimes = ['Teste1', 'Teste2', 'Teste3']
    lista_bairros = ['Teste1', 'Teste2', 'Teste3']

    context = {'lista_crimes': lista_crimes, 'lista_bairros': lista_bairros}

    return render(request, 'mapa_violencia/index.html', context)

# Called by the js module that builds the leaflet map
def return_filters(request):

    all_entries = Bairro.objects.all()
    #print(all_entries.values())    

    # Process the request and prepare the response
    response_data = {
        'lista_bairros': list(all_entries.values()),
    }
    return JsonResponse(response_data)