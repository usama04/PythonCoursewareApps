import folium
mapo = folium.Map(location=[30.656,104.062], zoom_start=5, tiles="Mapbox Bright")
import pandas as pd
data = pd.read_csv("Volcanos.csv")
data.drop('Unnamed: 0', axis=1, inplace=True)
data_lat = data["Volcanos_Latitude"]
data_lon = data["Volcanos_Longitude"]
data_lat = list(data_lat)
data_lon = list(data_lon)
data_names = list(data["Volcanos_Name"])
data_elev = list(data["Volcanos_Elev"])
def color_ret(elev):
    if elev <=1000:
        return "green"
    elif elev <= 3000 and elev>1000:
        return "blue"
    else:
        return "red"

fgv = folium.FeatureGroup(name = "Volcano Map")

for lt, ln, vn, el in zip(data_lat, data_lon, data_names, data_elev):
    fgv.add_child(folium.Marker(location=[lt, ln], popup=vn, icon=folium.Icon(color=color_ret(el))))

fgp = folium.FeatureGroup(name="Population")

fgp.add_child(folium.GeoJson(data=open("world.json", 'r', encoding='utf-8-sig').read(),
style_function=lambda x: {'fillColor':'blue' if x['properties']['POP2005']<10000000 else 'green' if 10000000<=x['properties']['POP2005']<100000000 else 'red'}))

mapo.add_child(fgv)
mapo.add_child(fgp)
mapo.add_child(folium.LayerControl())
mapo.save("Map1.html")