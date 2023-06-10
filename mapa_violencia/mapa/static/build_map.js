var map = L.map('map', {zoomSnap: 0.1}).setView([-30.096859, -51.152677], 10.6);

    //Layer
L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png', {
        attribution: '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
    }).addTo(map);

function getData(filtro_bairros) { 
    return $.ajax({
        type: 'POST',
        url: "return_filters/",
        credentials: "same-origin",
        headers: {
        "X-Requested-With": "XMLHttpRequest",
        "X-CSRFToken": $('input[name="csrfmiddlewaretoken"]').val(),
        },
        data: {'filtro_bairros': filtro_bairros},
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

//Get selected neighborhoods

async function getNeighborhoods(filtro_bairros) {
    try {
        var neighborhods = await getData(filtro_bairros);

        var g1 = { "type" : "FeatureCollection",
        "features" : []};

        for (var i = 0; i < neighborhods.lista_bairros.length; i++){
        // console.log(neighborhods.lista_bairros[i])
            g1 = concatGeoJSON(g1, neighborhods.lista_bairros[i].geometry);
        }

        geojson = L.geoJSON(g1, {
            //filter: neighborhoods_filter,
            onEachFeature: onEachFeature
        }).addTo(map);
    
    } catch(err) {
    console.log(err);
    }
}

function create_map(filtro_bairros){

    getNeighborhoods(filtro_bairros);
}

create_map(['All'])
