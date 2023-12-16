#######################
# Import libraries
import streamlit as st
import pandas as pd
import altair as alt
import plotly.express as px
import geopandas as gpd
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable

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






# Load data (replace with your GDP data for each province)
data = {
    "Province": ["Beijing", "Shanghai", "Guangdong", "Zhejiang", "Jiangsu"],
    "GDP": [36103, 39055, 145219, 62352, 102611]  # Example GDP values in billion USD
}

df = pd.DataFrame(data)

# Load China map shapefile
china_map = gpd.read_file("path/to/china_shapefile.shp")  # Replace with the path to your shapefile

# Merge GDP data with China map
merged_data = pd.merge(china_map, df, on="Province", how="left")

# Streamlit app
st.title("China GDP Ranking by Province")

# Create a sidebar for user input
selected_year = st.sidebar.slider("Select Year:", 2023, 2030, 2023, 1)

# Plot the map
fig, ax = plt.subplots(1, 1, figsize=(12, 10))
divider = make_axes_locatable(ax)
cax = divider.append_axes("right", size="5%", pad=0.1)

merged_data.plot(column="GDP", cmap="OrRd", linewidth=0.8, ax=ax, edgecolor="0.8", legend=True, cax=cax)
ax.set_title(f"China GDP by Province - {selected_year}")
ax.set_axis_off()

# Display the map using Streamlit
st.pyplot(fig)


