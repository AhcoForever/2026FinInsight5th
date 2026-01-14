# 지도 띄우기
import pandas as pd
import folium
import requests

m = folium.Map(location=[33.361936, 126.529165], zoom_start=10, tiles="cartodbpositron")
geojson_data = requests.get(
    "https://raw.githubusercontent.com/python-visualization/folium-example-data/main/world_countries.json"
).json()
tooltip = "Click"

오름 = pd.read_csv("jeju_utf8.csv", encoding="utf-8")
오름.info()

오름["주차장"].value_counts()
# for i in range(오름.shape[0]):
#     folium.Marker(
#         [오름.iloc[i]["위도"], 오름.iloc[i]["경도"]],
#         popup=f'<strong>{오름.iloc[i]["오름명"]}</strong>',
#         tooltip=tooltip,
#     ).add_to(m)
주차장유 = folium.FeatureGroup(name="주차장유").add_to(m)
주차장무 = folium.FeatureGroup(name="주차장무").add_to(m)
for i in range(오름.shape[0]):
    if 오름.iloc[i]["주차장"] == "Y":
        folium.Marker(
            [오름.iloc[i]["위도"], 오름.iloc[i]["경도"]],
            popup=f'<div><strong>{오름.iloc[i]["오름명"]}</strong><br>\
                주차장:{오름.iloc[i]["주차장"]}<br>\
                화장실:{오름.iloc[i]["화장실"]}<br>\
                </div>',
            tooltip=tooltip,
        ).add_to(주차장유)
    else:
        folium.Marker(
            [오름.iloc[i]["위도"], 오름.iloc[i]["경도"]],
            popup=f'<div><strong>{오름.iloc[i]["오름명"]}</strong><br>\
                주차장:{오름.iloc[i]["주차장"]}<br>\
                화장실:{오름.iloc[i]["화장실"]}<br>\
                </div>',
            tooltip=tooltip,
        ).add_to(주차장무)

folium.LayerControl(collapsed=False).add_to(m)

m.save("jeju_utf8.html")
