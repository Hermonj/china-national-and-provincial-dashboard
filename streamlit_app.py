import streamlit as st
import pandas as pd
import altair as alt

# Page configuration
st.set_page_config(
    page_title="China Economic Indicators Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded")

# Load data (example data, replace with actual data)
df_gdp = pd.DataFrame({
    'Province': ['Beijing', 'Shanghai', 'Guangdong', 'Zhejiang', 'Jiangsu'],
    'GDP (in Billion USD)': [600, 650, 1200, 700, 900],
    'Population (in Million)': [21, 26, 115, 60, 80],
    'Unemployment Rate (%)': [3.5, 4.2, 4.8, 3.2, 4.5]
})

# Sidebar
with st.sidebar:
    st.title('📊 China Economic Indicators')

# Main Panel
st.title('Key Economic Indicators')

# GDP Ranking Table
st.subheader('GDP Ranking by Province')
st.table(df_gdp[['Province', 'GDP (in Billion USD)']].sort_values(by='GDP (in Billion USD)', ascending=False))

# Line Chart for Population
st.subheader('Population by Province')
population_chart = alt.Chart(df_gdp).mark_bar().encode(
    x='Province',
    y='Population (in Million)',
    color=alt.Color('Population (in Million)', scale=alt.Scale(scheme='blues'))
).properties(width=600, height=400)
st.altair_chart(population_chart)

# Bar Chart for Unemployment Rate
st.subheader('Unemployment Rate by Province')
unemployment_chart = alt.Chart(df_gdp).mark_bar().encode(
    x='Province',
    y='Unemployment Rate (%)',
    color=alt.Color('Unemployment Rate (%)', scale=alt.Scale(scheme='reds'))
).properties(width=600, height=400)
st.altair_chart(unemployment_chart)
