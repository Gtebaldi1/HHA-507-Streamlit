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

st.header(' Question 2: What are the most expensive APC for Stony Brook Hopsital?')
st.subheader('Pivot APC for SBU Hospital')
dataframe_pivot = df_merged_clean_SB.pivot_table(index=['provider_id','apc'],values=['average_total_payments'],aggfunc='mean')
st.dataframe(dataframe_pivot)
st.markdown('Answer:The most expensive average total cost for APC in the outpatient and hospital dataframe with SBU hospital are the following')
st.markdown('1. Level IV endoscopy 2307.21, 2. Level IV Nerver Injections 1325.64, 3. Level II Cardiac Imaging 1300.67')








