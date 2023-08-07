import streamlit as st
import pandas as pd
import numpy as np


st.set_page_config(
    page_title="Rocking Recommender",
    page_icon=":robot:"
)
st.header("Rocking Recommender")       
         
data = pd.read_csv("clustered.csv")

#Features Zones
st.subheader("Please, select your favourite genre")
continent2 = st.sidebar.selectbox(label = "genres", options = data["artist_genres"].unique())
continent2 = str("continent2")

#Prediction
if st.button('I want new music!'):
    inputs1 = continent2
    recommender = data[data["artist_genres"] == inputs1]
    a = recommender["cluster"].to_numpy().astype(int)
    cluster = a[0]
    recommendation = data[data["cluster"] == cluster]
    st.write(f"You should explore this artists: {recommendation["artist"].head(2)}")
