# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.title('HHA 504 Streamlit Final Assignment')
st.write('Gina Tebaldi ') 

@st.cache
def load_hospital():
   hospitaldf = pd.read_csv('https://raw.githubusercontent.com/hantswilliams/AHI_DataSci_507/main/Deployment_Streamlit/hospital_info.csv')
   return hospitaldf
@st.cache
def load_inpatient():
    inpatientdf = pd.read_csv('https://raw.githubusercontent.com/hantswilliams/AHI_DataSci_507/main/Deployment_Streamlit/inpatient_2015.csv')
    return inpatientdf
@st.cache
def load_outpatient():
    outpatientdf = pd.read_csv('https://raw.githubusercontent.com/hantswilliams/AHI_DataSci_507/main/Deployment_Streamlit/outpatient_2015.csv')
    return outpatientdf

hospitaldf = load_hospital()
inpatientdf = load_inpatient()
outpatientdf = load_outpatient()  



st.header('Hospital Data')
st.dataframe(load_hospital())

st.header('Inpatient Data')
st.dataframe(load_inpatient())

st.header('Outpatient Data')
st.dataframe(load_outpatient())

st.header('Question 1: How does Stony Brook compare to the rest of New York?')
st.subheader('Hospital Type in New York')
bar1 = hospitaldf['hospital_type'].value_counts().reset_index()
st.dataframe(bar1)
st.caption('Acute care hospitals is the most common hospital type in New York ')