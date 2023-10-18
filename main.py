import folium
import streamlit as st
from streamlit_folium import st_folium
import csv

def color_detector(height):
    height = int(height)
    if height < 1000:
        color = "green"
    elif 1000 < height <= 3000:
        color = "orange"
    elif height > 3000:
        color = "red"
    return color


if __name__ == "__main__":
    map = folium.Map(zoom_start=10)
    st.title("Volcano Table")
    st.text("Green is up to 1000 m")
    st.text("Orange is for height up to 3000m")
    st.text("Red is for height higher than 3000m")
    with open('volcanoes.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile)
        for volcano in spamreader:
            if all([i != "" for i in volcano]):
                folium.Marker(location=[volcano[3], volcano[4]], popup=f"{volcano[0]} <a href='https://en.wikipedia.org/wiki/{volcano[0]}' target='_blank'>Wikipedia</a>",
                                           icon=folium.Icon(color=color_detector(volcano[5]))).add_to(map)
        st_data = st_folium(map, width=700)
