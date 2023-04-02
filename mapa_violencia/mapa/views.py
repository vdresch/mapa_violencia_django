from django.shortcuts import render
import folium

def mapa(request):

    m = folium.Map(location=[45.5236, -122.6750], zoom_start=13)

    # Add a marker to the map
    folium.Marker(
        location=[45.5236, -122.6750],
        popup='Portland, Oregon',
        icon=folium.Icon(icon='cloud')
    ).add_to(m)

    # Render the map in the template
    map_html = m._repr_html_()

    lista_crimes = ['Teste1', 'Teste2', 'Teste3']

    return render(request, 'mapa_violencia/index.html', {'map_html': map_html, 'lista_crimes': lista_crimes})