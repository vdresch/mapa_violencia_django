var map = L.map('map').setView([51.505, -0.09], 13);
L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
}).addTo(map);

var drawnItems = new L.FeatureGroup();
map.addLayer(drawnItems);
var drawControl = new L.Control.Draw({
    // position: 'topright',
    draw: {
       polygon: {
        shapeOptions: {
         color: 'purple'
        },
        allowIntersection: true,
        drawError: {
         color: 'orange',
         timeout: 1000
        },
       },
       polyline: {},
       rect: {},
       circle: {},
    },
    
});
map.addControl(drawControl);
 map.on('draw:created', function (e) {
       var type = e.layerType,
           layer = e.layer;
       drawnItems.addLayer(layer);
});