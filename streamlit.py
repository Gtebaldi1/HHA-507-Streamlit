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
st.markdown('Answer: Acute care hospitals are the most common, followed by critical, and then psychiatric')


hospitals_ny = hospitaldf[hospitaldf['state'] == 'NY']
st.header('Hospitals in New York')
st.dataframe(hospitals_ny)

st.header('Question 3: What is the most common type of hospital in New York')
table1 = hospitals_ny['hospital_type'].value_counts().reset_index()
st.header('Types of hospitals in New York')
st.markdown('Number of types of hospitals in New York')
st.dataframe(table1)
st.markdown ('Answer: Acute care hospitals are also the most common type of hospital in New York')




st.header('Question 3: What caused the most discharges DRGs for Stony Brook Hospital?')
sbinpatient = inpatientdf[inpatientdf['provider_id']==330393]
st.header('Inpatient Data from Stony Brook Hospital')
st.dataframe(sbinpatient)

sbdischarges = sbinpatient.pivot_table(index =['drg_definition'],values =['total_discharges'],aggfunc='mean')
st.header(' Discharges for DRG Codes at Stony Brook')
st.dataframe(sbdischarges)
st.markdown('Answer: Scrolling through the pivot table the highest amount of discharges came from "SEPTICEMIA OR SEVERE SEPSIS W/O MV 96+ HOURS W MCC" 628 discharges, followed by "MAJOR JOINT REPLACEMENT OR REATTACHMENT OF LOWER EXTREMITY W/O MCC" with 286 discharges.')














