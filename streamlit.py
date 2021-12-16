# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import time
import matplotlib.pyplot as plt

st.title('HHA 504 Streamlit Final Assignment')

@st.cache
def load_hospitals():
    hospitaldf = pd.read_csv('https://raw.githubusercontent.com/hantswilliams/AHI_STATS_507/main/Week13_Summary/output/df_hospital.csv')
    return hospitaldf
@st.cache
def load_Outpatient():
    doutpatientdf = pd.read_csv('https://raw.githubusercontent.com/hantswilliams/AHI_STATS_507/main/Week13_Summary/output/df_outpatient.csv')
    return 

@st.cache
def load_Inpatient():
    inpatientdf = pd.read_csv('https://raw.githubusercontent.com/hantswilliams/AHI_STATS_507/main/Week13_Summary/output/df_inpatient.csv')
    return inpatientdf
