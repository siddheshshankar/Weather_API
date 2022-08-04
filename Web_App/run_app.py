import streamlit as st
from Get_Details.Create_URL import CreateURL
from Get_Details.Fetch_Details import GetData, StoreData
from Web_App import Create_App


class DisplayDetails:
    """
    Class to initialize value and represent it
    """
    def __init__(self, temperature, humidity, forecast):
        self.temperature = temperature
        self.humidity = humidity
        self.forecast = forecast

    def __repr__(self):
        if st.button('Submit'):
            col1, col2, col3 = st.columns(3)

            col1.metric('Temperature', f'{self.temperature} C')
            col2.metric('Humidity', self.humidity)
            col3.metric('Forecast', self.forecast)


def run():
    # Enter city in web application
    city = Create_App.WebApp().title()

    # Get response from API
    url_cls = CreateURL(city)
    url = url_cls.get_web_url()

    # Required data
    data_cls = GetData(url)

    # Store data
    data = StoreData(
        data_cls.get_celsius(),
        data_cls.get_forecast(),
        data_cls.get_humidity()
    )

    return data

