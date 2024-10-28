pip install folium
import streamlit as st
import folium
from folium import Marker, PolyLine

# Vytvoření základní mapy
st.title("African Adventure of Fila")
st.write("Následuje plán cesty s vyznačenou trasou a body, abys věděla, kde ten tvůj Fíla vězí! ❤️")

# Nastavení výchozího bodu
m = folium.Map(location=[-22.559, 17.083], zoom_start=5)

# Itinerář cesty
itinerary = [
    {"day": 1, "location": "Windhoek", "coords": [-22.559, 17.083], "desc": "Windhoek Lodge - Čas na relax, hodně jídla a pití!"},
    {"day": 2, "location": "Namib Naukluft", "coords": [-24.556, 15.556], "desc": "První zvířata na cestě!"},
    {"day": 3, "location": "Dune 45 & Sossusvlei", "coords": [-24.725, 15.295], "desc": "Libový písečný duny při východu slunce."},
    {"day": 4, "location": "Swakopmund", "coords": [-22.678, 14.526], "desc": "Bůhví, co tady protože jsou tady různý aktivity :D. Takže možná delfíni, sandboarding, nebo tak ;)"},
    {"day": 6, "location": "Spitzkoppe", "coords": [-21.831, 15.190], "desc": "Mega hustý skály."},
    {"day": 7, "location": "Etosha National Park", "coords": [-19.163, 15.917], "desc": "Pár dní jenom zvířataaaaaaaa, pak budou cool fakta ;)!"},
    {"day": 11, "location": "Kasane, Botswana", "coords": [-17.832, 25.153], "desc": "Taky zvířata, ale jinde :D a hustý vodopády"},
    {"day": 13, "location": "Victoria Falls", "coords": [-17.924, 25.856], "desc": "Konečný cíl: Victoria Falls, ty nejvíc hustý vodopády ze všech."},
 {"day": 15, "location": "Domůůůůůůůů", "coords": [49.8175, 15.473], "desc": "Česká republika - Hurá domů!"}
]

# Přidání bodů zájmu do mapy
for point in itinerary:
    Marker(location=point["coords"], popup=f"Day {point['day']}: {point['desc']}").add_to(m)

# Přidání trasy
coords = [point["coords"] for point in itinerary]
PolyLine(coords, color="blue", weight=2.5, opacity=1).add_to(m)

# Šipka zpět do České republiky
folium.Marker(
    location=[49.8175, 15.473],  # Koordináty pro ČR
    popup="Domůůůůůůůů!",
    icon=folium.Icon(icon="home", color="red")
).add_to(m)

# Vykreslení mapy ve streamlitu
st.write("### Mapa cesty")
st.map(m._repr_html_(), width=700, height=500)

