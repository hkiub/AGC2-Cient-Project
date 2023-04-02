import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

OCCU_DATA = 'occu_titles.csv'
TECH_DATA = 'tech_skills.csv'
TOOLS_DATA = 'tools_used.csv'

st.set_page_config(page_title="Compare 2 Occupations", page_icon="🔄")

@st.experimental_memo
def load_data():
    data = pd.read_csv(OCCU_DATA)
    tech_data = pd.read_csv(TECH_DATA)
    tools_data = pd.read_csv(TOOLS_DATA)
    return data, tech_data, tools_data

data, tech_data, tools_data = load_data()

st.title("Comparison Between 2 Occupations")
st.sidebar.write(
    """This page helps in comparing 2 different occupations and presents information which 
    is common between the two occupations. This way we can identify how similar 2 jobs are 
    in the market and make a better informed decision. This tool although naive and simple
    can help a job seeker and other people to make a better decision. So please feel free 
    to explore !!! """
)


val1 = st.selectbox("Select the 1st Occupation Occupation you like to know more about", list(data.title))
val2 = st.selectbox("Select the 2nd Occupation you like to know more about", list(data.title))

st.text("All The values displayed now are the common elements between the 2 Occupations")
col1, col2 = st.columns(2)

with col1:
    agree = st.checkbox('Only Include Hot Tech')
    if agree:
        val1_data = set(tech_data[(tech_data.title == val1) & (tech_data.hot_tech == "Y")]['example'].values)
        val2_data = set(tech_data[(tech_data.title == val2) & (tech_data.hot_tech == "Y")]['example'].values)
        st.write(val1_data & val2_data)
    else:
        val1_data = set(tech_data[(tech_data.title == val1)]['example'].values)
        val2_data = set(tech_data[(tech_data.title == val2)]['example'].values)
        st.write(val1_data & val2_data)

with col2:
    val1_tdata = set(tools_data[(tools_data.title == val1)]['example'].values)
    val2_tdata = set(tools_data[(tools_data.title == val2)]['example'].values)
    st.write(val1_tdata & val2_tdata)
     