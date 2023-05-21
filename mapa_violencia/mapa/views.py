from django.shortcuts import render

def mapa(request):

    lista_crimes = ['Teste1', 'Teste2', 'Teste3']
    lista_bairros = ['Teste1', 'Teste2', 'Teste3']

    context = {'lista_crimes': lista_crimes, 'lista_bairros': lista_bairros}

    return render(request, 'mapa_violencia/index.html', context)

# Called by the js module that builds the leaflet map
def return_filters():
    pass