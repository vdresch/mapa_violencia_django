from django.shortcuts import render
from django.http import JsonResponse
from mapa.models import Bairro

def mapa(request):

    lista_crimes = ['Teste1', 'Teste2', 'Teste3']
    lista_bairros = list(Bairro.objects.values_list('bairro', flat=True).all())

    context = {'lista_crimes': lista_crimes, 'lista_bairros': lista_bairros}

    return render(request, 'mapa_violencia/index.html', context)

# Called by the js module that builds the leaflet map
from django.http import JsonResponse

def return_filters(request):

    print(request.POST.getlist('filtro_bairros[]', None))

    filtro_mapa = request.POST.getlist('filtro_bairros[]', None)

    if filtro_mapa == ['All'] or filtro_mapa == None:
        bairros_mapa = Bairro.objects.all()
    else:
        print('Here')
        bairros_mapa = Bairro.objects.filter(bairro__in=filtro_mapa) 

    # Process the request and prepare the response
    response_data = {
        'lista_bairros': list(bairros_mapa.values()),
    }
    return JsonResponse(response_data)