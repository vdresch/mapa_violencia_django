from django.shortcuts import render
from django.http import JsonResponse
import pandas as pd
from datetime import datetime

from .crimes_list import VIOLENT_CRIMES, NON_VIOLENT_CRIMES

#Open DBs
bairros = pd.read_pickle('scripts/data/bairros_metadata.pkl')
crimes = pd.read_pickle('scripts/data/processed_data.pkl')

def mapa(request):

    lista_crimes = list(crimes['Tipo Enquadramento'].unique())
    lista_bairros = list(bairros['Bairro'])

    max_date = max(crimes['Data Fato']).isoformat()

    context = {'lista_crimes': lista_crimes, 'lista_bairros': lista_bairros, 'max_date': max_date}

    return render(request, 'mapa_violencia/index.html', context)

# Called by the js module that builds the leaflet map
from django.http import JsonResponse

def return_filters(request):

    #Get filters
    filtro_bairros = request.POST.getlist('filtro_bairros[]', None)
    filtro_crimes = request.POST.getlist('filtro_crimes[]', None)
    date_min = request.POST.getlist('date_min', None)[0]
    date_max = request.POST.getlist('date_max', None)[0]
    date_min = datetime.strptime(date_min, "%Y-%m-%dT%H:%M:%S.%fZ")
    date_max = datetime.strptime(date_max, "%Y-%m-%dT%H:%M:%S.%fZ")

    #Select neighborghoods
    if filtro_bairros == ['All'] or filtro_bairros == None:
        bairros_mapa = bairros
    #Custom list
    else:
        bairros_mapa = bairros[bairros['Bairro'].isin(filtro_bairros)]

    #Select crimes
    #If custom selection
    if filtro_crimes != ['all'] and filtro_crimes != ['violent'] and filtro_crimes != ['not_violent']:
        crimes_mapa = crimes[crimes['Tipo Enquadramento'].isin(filtro_crimes)]
    #All crimes (none selectet)
    elif filtro_crimes == ['all']:
        crimes_mapa = crimes
    #Only violent crimes (comes from dict)
    elif filtro_crimes == ['violent']:
        crimes_mapa = crimes[crimes['Tipo Enquadramento'].isin(VIOLENT_CRIMES)]
    #Only non violent crimes (comes from dict)
    else:
        crimes_mapa = crimes[crimes['Tipo Enquadramento'].isin(NON_VIOLENT_CRIMES)]

    crimes_mapa = crimes_mapa[(crimes_mapa['Data Fato']  > date_min) & (crimes_mapa['Data Fato']  <= date_max)]

    #Report crimes information to neighborhood
    grouped_crimes = crimes_mapa.groupby('Bairro').agg({'Sequência': 'count'}).reset_index()
    bairros_mapa['n_crimes'] = bairros_mapa['Bairro'].apply(lambda x: grouped_crimes[grouped_crimes['Bairro'] == x]['Sequência'].values[0])

    #Return shapes and crimes
    response_data = bairros_mapa.to_dict(orient='records')
    return JsonResponse(response_data, safe=False)