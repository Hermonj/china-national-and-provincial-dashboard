[# 🏂 china-national-and-provincial-dashboar

A dashboard web app template built in Python using Streamlit.

## Demo App

[![Streamlit App](https://china-s-national-economy-dashboard-pwhbg33mjzupa6kdb94ndp.streamlit.app/)


This code uses the Streamlit library to create a simple web-based dashboard for visualizing key economic indicators related to China's national economy. Here's a breakdown:

Imports:

streamlit is used to create the web application.
pandas and numpy are used for data manipulation.
Dashboard Title and Description:

The title and a header are set for the dashboard using st.title and st.header.
A brief description of the dashboard's purpose is added using st.markdown.
Data Loading:

The code reads a CSV file named "Economy_Dashboard2.csv" using pd.read_csv and stores it in the data variable.
Visualization:

Various economic indicators are visualized using Streamlit's charting functions:
GDP growth is displayed as a line chart.
GDP per capita is displayed as an area chart.
GDP, current prices is displayed as a bar chart.
GDP based on PPP (Purchasing Power Parity) is displayed as a line chart.
Implied PPP conversion rate is displayed as an area chart.
Sidebar:

A sidebar is added using st.sidebar to provide user interaction options.
A radio button is included in the sidebar using st.radio to allow the user to choose between "Standard" and "Express" methods.
This code essentially creates a Streamlit web app with a simple layout that includes charts for various economic indicators and a sidebar for user interaction. The data for visualization is loaded from a CSV file, and the dashboard is designed to be user-friendly by allowing the user to choose between different methods using the radio button in the sidebar.

## Colab notebook
[![Colab Notebook](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1H2kPj2q9buAJQeAs5C59jjNCb4DqgypJ?usp=sharing)

## Prerequisite libraries
Here are the Python libraries used in the creation of this dashboard app

## Data source
(https://github.com/Hermonj/china-national-and-provincial-dashboard/blob/master/data/GDP%20by%20national%20currency%20(renminbi)%20in%20main%20years.csv).

