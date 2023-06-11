from django.shortcuts import render
from django.http import JsonResponse
from mapa.models import Bairro, Crime

def mapa(request):

    lista_crimes = list(Crime.objects.values_list('enquadramento', flat=True).distinct())
    lista_bairros = list(Bairro.objects.values_list('bairro', flat=True).all())

    context = {'lista_crimes': lista_crimes, 'lista_bairros': lista_bairros}

    return render(request, 'mapa_violencia/index.html', context)

# Called by the js module that builds the leaflet map
from django.http import JsonResponse

def return_filters(request):

    print(request.POST.getlist('filtro_bairros[]', None))
    print(request.POST.getlist('filtro_crimes[]', None))

    filtro_bairros = request.POST.getlist('filtro_bairros[]', None)
    filtro_crimes = request.POST.getlist('filtro_crimes[]', None)

    if filtro_bairros == ['All'] or filtro_bairros == None:
        bairros_mapa = Bairro.objects.all()
        if filtro_crimes != ['all'] or filtro_crimes != ['violent'] or filtro_crimes != ['not_violent']:
            crimes_mapa = Crime.objects.filter(enquadramento__in=filtro_crimes).count()
            print(crimes_mapa)
        
    else:
        bairros_mapa = Bairro.objects.filter(bairro__in=filtro_bairros) 

    # Process the request and prepare the response
    response_data = {
        'lista_bairros': list(bairros_mapa.values()),
    }
    return JsonResponse(response_data)