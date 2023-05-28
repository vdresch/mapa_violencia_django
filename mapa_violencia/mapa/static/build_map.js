var map = L.map('map', {zoomSnap: 0.1}).setView([-30.096859, -51.152677], 10.6);

//Neighborhoods shape
var porto_alegre = JSON.parse(JSON.parse(document.getElementById('geojson').textContent));

console.log(porto_alegre)

function onEachFeature(feature, layer) {
    // does this feature have a property named popupContent?
    console.log(feature.properties)
    if (feature.properties && feature.properties.popupContent) {
        layer.bindPopup(feature.properties.popupContent);
    }
}

L.geoJSON(porto_alegre, {
    onEachFeature: onEachFeature
}).addTo(map);

//Layer
L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
}).addTo(map);


//Draw
// var drawnItems = new L.FeatureGroup();
// map.addLayer(drawnItems);

// var drawControl = new L.Control.Draw({
//     // position: 'topright',
//     draw: {
//        polygon: {
//         shapeOptions: {
//          color: 'purple'
//         },
//         allowIntersection: true,
//         drawError: {
//          color: 'orange',
//          timeout: 1000
//         },
//        },
//        polyline: {},
//        rect: {},
//        circle: {},
//     },
    
// });
// map.addControl(drawControl);
//  map.on('draw:created', function (e) {
//        var type = e.layerType,
//            layer = e.layer;
//        drawnItems.addLayer(layer);
// });