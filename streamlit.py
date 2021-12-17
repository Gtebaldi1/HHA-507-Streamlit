# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import time
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly

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




st.header('Question 1: What are the most common type of hospitals?')
st.subheader('Hospital Types')
bar1 = hospitaldf['hospital_type'].value_counts().reset_index()
st.dataframe(bar1)
st.caption('Acute care hospitals are the most common, followed by critical, and then psychiatric')

st.header('Question 2: Most expensive inpatient DRGs for Stony Brook Hospital?')
sbinpatient = inpatientdf[inpatientdf['provider_id']==330393]
st.header('Inpatient Data for Stony Brook Hospital')
st.dataframe(sbinpatient)

sbdischarges = sbinpatient.pivot_table(index =['drg_definition'],values =['total_discharges'],aggfunc='most')
st.header(' Discharges for DRG Codes at Stony Brook')
st.dataframe(sbdischarges)
st.markdown('Per the table above, you can see that the highest amount of discharges came from drg code 871 - SEPTICEMIA OR SEVERE SEPSIS W/O MV 96+ HOURS W MCC.')








