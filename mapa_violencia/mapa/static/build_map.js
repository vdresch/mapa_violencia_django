var map = L.map('map', {zoomSnap: 0.1}).setView([-30.096859, -51.152677], 10.6);

//Neighborhoods shape
var porto_alegre = JSON.parse(JSON.parse(document.getElementById('geojson').textContent));

//Filter only seleced neighborhoods
var teste = $.ajax({
    url: "return_filters/", // if you don't have dynamic url,
    type: 'GET',
  });

console.log(teste)

function neighborhoods_filter(feature) {
    if (feature.properties.Name === "AGRONOMIA") return true
  }

console.log(porto_alegre)

function onEachFeature(feature, layer) {
    // does this feature have a property named popupContent?
    console.log(feature.properties)
    if (feature.properties && feature.properties.popupContent) {
        layer.bindPopup(feature.properties.popupContent);
    }
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

geojson = L.geoJSON(porto_alegre, {
    filter: neighborhoods_filter,
    onEachFeature: onEachFeature
}).addTo(map);

//Layer
L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
}).addTo(map);