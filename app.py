import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

OCCU_DATA = 'occu_titles.csv'
TECH_DATA = 'tech_skills.csv'
TOOLS_DATA = 'tools_used.csv'

@st.experimental_memo
def load_data():
    data = pd.read_csv(OCCU_DATA)
    tech_data = pd.read_csv(TECH_DATA)
    tools_data = pd.read_csv(TOOLS_DATA)
    return data, tech_data, tools_data

data, tech_data, tools_data = load_data()

analysis = st.sidebar.checkbox('Only Include Analysis and Graphs')
comp = st.sidebar.checkbox('Compare 2 Occupations')

if comp:
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
        
elif analysis:
    st.subheader('Top 10 Tools used')
    grp1 = tools_data.example.value_counts()
    # hist_values = plt.bar(grp1.index, grp1.values)
    st.bar_chart(grp1.sort_values(ascending = False).head(10))
else:
    val = st.selectbox("Select A Occupation you like to know more about", list(data.title))
    st.write(val)

    col1, col2 = st.columns(2)

    with col1:
        agree = st.checkbox('Only Include Hot Tech')
        if agree:
            st.table(tech_data[(tech_data.title == val) & (tech_data.hot_tech == "Y") ][['example', 'com_title']].iloc[:10])
        else:
            st.table(tech_data[tech_data.title == val][['example', 'com_title']].iloc[:10])

    with col2:
        st.table(tools_data[tools_data.title == val][['example', 'com_title']].iloc[:10])