#######################
# Import libraries
import streamlit as st
import pandas as pd
import altair as alt
import plotly.express as px

#######################
# Page configuration
st.set_page_config(
    page_title="China-national-and-provincial-dashboard",
    page_icon="🏂",
    layout="wide",
    initial_sidebar_state="expanded")

alt.themes.enable("dark")

#######################

#######################


#simply plotting a map with no parameters

## Create a sample DataFrame with latitude and longitude values
data = pd.DataFrame({
    'latitude': [35.00000000],
    'longitude': [105.00000000]
})
 
## Create a map with the data
st.map(data)


# Create a DataFrame with the points you want to highlight
highlight = pd.DataFrame({
    'latitude': [37.7749],
    'longitude': [-122.4194]
})
 
# Add the highlight points to the map
st.map(data, highlight)
