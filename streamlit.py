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

st.header('Question 2: What is the most common type of hospital in New York')
table1 = hospitals_ny['hospital_type'].value_counts().reset_index()
st.header('Types of hospitals in New York')
st.markdown('Number of types of hospitals in New York')
st.dataframe(table1)
st.markdown ('Answer: Acute care hospitals are also the most common type of hospital in New York')

st.subheader('PIE Chart of hospital type in NY:')
fig = px.pie(bar1, values='hospital_type', names='index')
st.plotly_chart(fig)


st.header('Question 3: What caused the most discharges DRGs for Stony Brook Hospital?')
sbinpatient = inpatientdf[inpatientdf['provider_id']==330393]
st.header('Inpatient Data from Stony Brook Hospital')
st.dataframe(sbinpatient)
sbdischarges = sbinpatient.pivot_table(index =['drg_definition'],values =['total_discharges'],aggfunc='mean')
st.header(' Discharges for DRG Codes at Stony Brook')
st.dataframe(sbdischarges)
st.markdown('Answer: Scrolling through the pivot table the highest amount of discharges came from "SEPTICEMIA OR SEVERE SEPSIS W/O MV 96+ HOURS W MCC" 628 discharges, followed by "MAJOR JOINT REPLACEMENT OR REATTACHMENT OF LOWER EXTREMITY W/O MCC" with 286 discharges.')

st.header ('Question 4: What is the most expensive inpatient DRG at SBUH?')
costpivotdrg = sbinpatient.pivot_table(index=['provider_name','drg_definition'],values=['average_total_payments'],aggfunc='mean')
##costpivotdrg = sbinpatient.sort_values(['average_total_payments'], ascending=False)
st.header('Average Total Payments for DRG Codes at SBUH')
st.dataframe(costpivotdrg)
st.markdown('Answer: The highest average total payment came from drg code 003 - ECMO OR TRACH W MV >96 HRS OR PDX EXC FACE, MOUTH & NECK W MAJ O.R.')
st.markdown('Followed by the second highest of code 004- TRACH W MV 96+ HRS OR PDX...')




st.header ('Question 5: What is the most DRG for NY hospitals?')
inpatient_ny = inpatientdf[inpatientdf['provider_state'] == 'NY']
total_inpatient_count = sum(inpatient_ny['total_discharges'])


costs_condition_hospital = inpatient_ny.groupby(['provider_name', 'drg_definition'])['average_total_payments'].sum().reset_index()
st.header("Costs by Condition and Hospital in NY - Average Total Payments")
st.dataframe(costs_condition_hospital)
st.header("Most Common DRG in NY hospitals")
table2 = costs_condition_hospital['drg_definition'].value_counts().reset_index()
st.dataframe (table2)

sboutpatient = outpatientdf[outpatientdf['provider_id']==330393]
st.header('Outpatient Data for Stony Brook')
st.dataframe(sboutpatient)

st.header('Question 6: What is the most expensive inpatient APCs code for SBUH?')
sboutpatientdrg = sboutpatient.pivot_table(index=['provider_id','provider_name','apc'],values=['average_total_payments'])
sboutpatientapcs= sboutpatientdrg.sort_values(['average_total_payments'], ascending=False)
st.markdown('Answer the most expensive APC for SBUH is Level IV Endoscopy Upper Airway')
st.dataframe(sboutpatientapcs)









