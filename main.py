import streamlit as st
import plotly.express as px
from backend import get_data

st.header("Weather Forecast for the Next Days")
place = st.text_input("Place: ")
days = st.slider("Forecast Days: ", min_value=1, max_value=5, help="Choose the number of forecasted days to show")
option = st.selectbox("Select data to view: ", options=("Temperature", "Sky"))
st.subheader(f"{option} for the next {days} days in {place}")

if place:
    filtered_data = get_data(place, days)
    if option == "Temperature":
        temperatures = [dict["main"]["temp"] for dict in filtered_data]
        dates = [dict["dt_txt"] for dict in filtered_data]
        figure = px.line(x=dates, y=temperatures/10, labels={"x": "Dates", "y": "Temperature (C)"})
        st.plotly_chart(figure)

    if option == "Sky":
        sky_conditions = [dict["weather"][0]["main"] for dict in filtered_data]
        images = {"Clear": "images/clear.png","Rain": "images/rain.png","Clouds": "images/cloud.png",
                  "Snow": "images/snow.png"}
        get_imgs = [ images[condition] for condition in sky_conditions]
        st.image(get_imgs,width=115)
