import json
import folium
import requests
import streamlit as st
from streamlit_folium import st_folium

# とりあえず日本の真ん中くらいの場所を固定しておく。
map = folium.Map(location=(35, 135), zoom_start=5, min_zoom=4, control_scale=True)

# config.jsonによけたAPI_keyの取得
with open('config.json', mode='r', encoding='utf-8') as f:
    jsonfile = json.loads(f.read())
API_key = jsonfile['API_key']

with open('location.json', mode='r', encoding='utf-8') as f:
    selected_cities = json.loads(f.read())

cities_add_weather = []
for city in selected_cities:
    lat = city['lat']
    lon = city['lon']
    url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_key}&lang=ja&units=metric&units=metric'
    jsondata = requests.get(url).json()
    # pprint.pprint(jsondata)

    # selected_citiesの複製を作って、そこにjsondataの内容を追加する
    city_new = dict(city)
    city_new['icon'] = jsondata['weather'][0]['icon']
    city_new['description'] = jsondata['weather'][0]['description']
    city_new['feels_like'] = jsondata['main']['feels_like']
    city_new['humidity'] = jsondata['main']['humidity']
    city_new['sea_level'] = jsondata['main']['sea_level']
    city_new['grnd_level'] = jsondata['main']['grnd_level']

    cities_add_weather.append(city_new)

for city in cities_add_weather:
    url = f'https://openweathermap.org/img/wn/{city["icon"]}@2x.png'

    icon = folium.CustomIcon(
        icon_image=url,
        icon_size=(75, 75),
        icon_anchor=(50, 50),
    )

    folium.Marker(
        location=[city['lat'], city['lon']],
        tooltip=city['name_ja'],
        popup=folium.Popup(
            f'<ul style="list-style: none; text-align: left; font-size: large;">\
                <li>都市名：{city["name_ja"]}</li>\
                <li>天気：{city["description"]}</li>\
                <li>体感気温：{city["feels_like"]}℃</li>\
                <li>湿度：{city["humidity"]}％</li>\
                <li>気圧：{city["sea_level"]}hPa</li>\
            </ul>', max_width=300, offset=(0, -20)),
        icon=icon
    ).add_to(map)

st.title("日本の現在天気マップ")
st_data = st_folium(map, width=900, height=600)