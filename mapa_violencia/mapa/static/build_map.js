var map = L.map('map', {zoomSnap: 0.1}).setView([-30.096859, -51.152677], 10.6);

//Layer
L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png', {
        attribution: '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
    }).addTo(map);

function getData(filtro_bairros, filtro_crimes) { 
    return $.ajax({
        type: 'POST',
        url: "return_filters/",
        credentials: "same-origin",
        headers: {
        "X-Requested-With": "XMLHttpRequest",
        "X-CSRFToken": $('input[name="csrfmiddlewaretoken"]').val(),
        },
        data: {'filtro_bairros': filtro_bairros, 'filtro_crimes': filtro_crimes},
    });    
};

function onEachFeature(feature, layer) {
    layer.on({
        mouseover: highlightFeature,
        mouseout: resetHighlight,
    });
}

function highlightFeature(e) {
    var layer = e.target;

    layer.setStyle({
        weight: 5,
        color: '#666',
        dashArray: '',
        fillOpacity: 0.7
    });

    layer.bringToFront();
}

function resetHighlight(e) {
    geojson.resetStyle(e.target);
}

function concatGeoJSON(g1, g2){
    return { 
        "type" : "FeatureCollection",
        "features": g1.features.concat(g2)
    }
}

function getColor(d) {
    return d > 1000 ? '#800026' :
           d > 500  ? '#BD0026' :
           d > 200  ? '#E31A1C' :
           d > 100  ? '#FC4E2A' :
           d > 50   ? '#FD8D3C' :
           d > 20   ? '#FEB24C' :
           d > 10   ? '#FED976' :
                      '#FFEDA0';
}

function style(feature) {
    return {
        fillColor: getColor(feature.properties.n_crimes),
        weight: 2,
        opacity: 1,
        color: 'white',
        dashArray: '3',
        fillOpacity: 0.7
    };
}

//Get selected neighborhoods

async function getNeighborhoods(filtro_bairros, filtro_crimes) {
    try {
        var neighborhods = await getData(filtro_bairros, filtro_crimes);

        var g1 = { "type" : "FeatureCollection",
        "features" : []};

        for (var i = 0; i < neighborhods.length; i++){
            var neighborhod = {"type":"Feature","id":"01","properties":
            {"Bairro": neighborhods[i].Bairro, 'n_crimes': neighborhods[i].n_crimes},
            "geometry": neighborhods[i].geometry};
            g1 = concatGeoJSON(g1, neighborhod);

        }

        try {
            map.removeLayer(geojson);
        } catch(err) {}

        geojson = L.geoJSON(g1, {
            onEachFeature: onEachFeature,
            style: style
        }).addTo(map);
    
    } catch(err) {
    console.log(err);
    }
}

function create_map(filtro_bairros, filtro_crimes){

    getNeighborhoods(filtro_bairros, filtro_crimes);

}

create_map(['All'], ['all']);
