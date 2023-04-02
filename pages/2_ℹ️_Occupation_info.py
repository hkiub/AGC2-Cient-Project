import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

OCCU_DATA = 'occu_titles.csv'
TECH_DATA = 'tech_skills.csv'
TOOLS_DATA = 'tools_used.csv'

st.set_page_config(page_title="More_Info", page_icon="ℹ️")

@st.experimental_memo
def load_data():
    data = pd.read_csv(OCCU_DATA)
    tech_data = pd.read_csv(TECH_DATA)
    tools_data = pd.read_csv(TOOLS_DATA)
    return data, tech_data, tools_data

data, tech_data, tools_data = load_data()

st.title("More information on a Occupation")
st.sidebar.write(
    """Get more information about an occupation on wat tools and technologies
    are being used in a occupation. An additional filter called as hot tech
    can help only identify which technologies are popular and hot in the field!!! """
)

val = st.selectbox("Select A Occupation you like to know more about", list(data.title))
# st.write(val)

col1, col2 = st.columns(2)
hide_table_row_index = """
        <style>
        thead tr th:first-child {display:none}
        tbody th {display:none}
        </style>
        """

# Inject CSS with Markdown
st.markdown(hide_table_row_index, unsafe_allow_html=True)

with col1:
    agree = st.checkbox('Only Include Hot Tech')
    if agree:
        st.table(tech_data[(tech_data.title == val) & (tech_data.hot_tech == "Y") ][['example', 'com_title']].iloc[:10])
    else:
        st.table(tech_data[tech_data.title == val][['example', 'com_title']].iloc[:10])

with col2:
    st.table(tools_data[tools_data.title == val][['example', 'com_title']].iloc[:10])