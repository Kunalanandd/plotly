import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px


df = pd.read_csv('India.csv')
list_of_states = list(df['State'].unique())
list_of_states.insert(0,'Overal India')
st.set_page_config(layout='wide')
st.sidebar.title("India Data Viz")
selected_state =st.sidebar.selectbox("Select state",list_of_states)




primary_par = st.sidebar.selectbox("primary_par",sorted(df.columns[5:]))
secondary_par = st.sidebar.selectbox("secondary_par",sorted(df.columns[5:]))

plot = st.sidebar.button('Plot Graph')


if plot:
    st.text("Size represent primary parameter")
    st.text("Color represent Secondary parameter")
    if selected_state=='Overal India':
        fig = px.scatter_mapbox(df,lat='Latitude',lon='Longitude',size=primary_par,color=secondary_par,zoom=4,mapbox_style='carto-positron',size_max=30,width=1200,height=800,hover_name='District')
        st.plotly_chart(fig,use_cantainer_width=True)
    else:
        state_df = df[df['State']==selected_state]
        fig = px.scatter_mapbox(state_df,lat='Latitude',lon='Longitude',size=primary_par,color=secondary_par,zoom=7,mapbox_style='carto-positron',size_max=30,width=1200,height=800,hover_name='District')
        st.plotly_chart(fig,use_cantainer_width=True)
