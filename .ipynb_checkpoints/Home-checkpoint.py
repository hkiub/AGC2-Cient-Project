import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Home",
    page_icon="👋",
)

st.write("# Welcome to the AGC2 Dashboard for E583! 👋")

st.sidebar.success("Select a demo above.")

st.markdown(
    """
    This dashboard has been developed for the course at Indiana University Luddy school of
    informatics as part of the Client project called "AGC2: Job and Skill Mapping Dashboard".
    
    **👈 Select a demo from the sidebar** to see some detailed information
    on what this dasboard has to offer!
    ### Team 
    - Harshit Khandelwal - hkhandel@iu.edu
    - Harishanker Brahma Kande - hkande@iu.edu
    - Manognya Katapally - makata@iu.edu
    - Shubhkirti Prasad - shubpras@iu.edu
    ### About the Data
    By examining the technology available in the market, we can determine the state of job openings.
    Through this visualization, we can pinpoint which technologies are in highest demand across
    different regions in the job market.
    When seeking employment with a company, various factors can come into play, including an
    individual's skills, abilities, education, and experience. These factors are often considered by
    employers when evaluating candidates for job openings.
    
    For this dashboard currently only limited tables are being used but in the coming days more tables will be added.
"""
)

