"""This modules contains data about visualisation page"""

# Import necessary modules
import warnings
import matplotlib.pyplot as plt
import seaborn as sns


import streamlit as st


# Import necessary functions from web_functions
from web_functions import train_model

def app(df, X, y):
    """This function create the visualisation page"""
    
    # Remove the warnings
    warnings.filterwarnings('ignore')
    st.set_option('deprecation.showPyplotGlobalUse', False)

    # Set the page title
    st.title("Visualise the Flight Delay Estimatation")

  
    if st.checkbox("Weather_Condition vs Late_Arrivals"):
        sns.color_palette("rocket", as_cmap=True)
        ax=sns.lineplot(x="Weather_Condition",y="Late_Arrivals",data=df)
        st.pyplot()

    if st.checkbox("Technical_Issues vs Late_Arrivals"):
        sns.color_palette("rocket", as_cmap=True)
        ax=sns.lineplot(x="Technical_Issues",y="Late_Arrivals",data=df)
        st.pyplot()

    if st.checkbox("Air_Traffic_Congestion vs Late_Arrivals"):
        sns.color_palette("rocket", as_cmap=True)
        ax=sns.lineplot(x="Air_Traffic_Congestion",y="Late_Arrivals",data=df)
        st.pyplot()

   
