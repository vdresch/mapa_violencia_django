from django.shortcuts import render
from django.http import JsonResponse
import pandas as pd

bairros = pd.read_pickle('scripts/data/bairros_metadata.pkl')
crimes = pd.read_pickle('scripts/data/processed_data.pkl')

def mapa(request):

    lista_crimes = list(crimes['Tipo Enquadramento'].unique())
    lista_bairros = list(bairros['Bairro'])

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
        bairros_mapa = bairros
        if filtro_crimes != ['all'] or filtro_crimes != ['violent'] or filtro_crimes != ['not_violent']:
            crimes_mapa = crimes[crimes['Tipo Enquadramento'].isin(filtro_crimes)]
            bairros_mapa['n_crimes'] = [len(crimes_mapa[crimes_mapa['Bairro'] == i]) for i in bairros_mapa['Bairro']]
        
    else:
        bairros_mapa = bairros[bairros['Bairro'].isin(filtro_bairros)]

    
    response_data = bairros_mapa.to_dict(orient='records')

    return JsonResponse(response_data, safe=False)