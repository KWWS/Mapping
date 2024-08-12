import folium
import pandas

data = pandas.read_csv("Volcanoes-USA.txt")

lon = list(data["LON"])
lat = list(data["LAT"])
elev = list(data["ELEV"])

def color_producer(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000 <= elevation < 3000:
        return 'orange'
    else:
        return 'red'
# Crie um objeto Map com a localização centralizada
map = folium.Map(location=[38.58, -99.09], zoom_start=6, titles="Mapbox Bright")

fgv = folium.FeatureGroup(name="Volcanoes")

for lt, ln, el in zip(lat, lon, elev):
    fgv.add_child(folium.CircleMarker(location=[lt, ln], radius=6, popup=str(el)+" m", fill_color=color_producer(el), color = 'grey', fill=True, fill_opacity=0.7))

fgp = folium.FeatureGroup(name="Population")

fgp.add_child(folium.GeoJson(data=(open('countries.geo.json', 'r', encoding='utf-8-sig').read())))

map.add_child(fgv)
# Salve o mapa em um arquivo HTML
map.add_child(fgp)

map.add_child(folium.LayerControl())

map.save("map1.html")
