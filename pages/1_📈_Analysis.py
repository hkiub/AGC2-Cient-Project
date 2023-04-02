import streamlit as st
import time
import numpy as np

st.set_page_config(page_title="Analysis", page_icon="📈")

st.markdown("# Visualizations on Jobs and skills")
st.sidebar.write(
    """After going through all the tables and selecting a few for the visualization herr.
    This part provides the visual depiction of the conclusions that we have drawn from the 
    data. For this purpose we have used various kinds of visualizations like the chloroppleth map,
    Tree map, Bubble graph, scatter graph and others which helps summarize the data well."""
)

st.image('imgs/img1.png')
st.write("This graph utilizes the geographic locations of states in the US from BLS Salaries Data for all the employed individuals(annually). The above visualizations represent the distribution of annual salaries of individuals employed in different states of the United States. The color in the graph represents the median annual salary of employees in the state. The label in the graph shows the state name and mean & median annual salaries in a particular state.")

st.image('imgs/img2.png')
st.write("This graph is visualized by utilizing the tech skills table from O*NET Data. The data is further filtered to get tech_skills which are in hot-tech and in-demand for most of the roles/titles in the job market. The above visualization represents the skills required for an individual to secure a job at present market trends. Word cloud is the best visualization to represent the name of the tech skill and size of the rectangular box represents the number of titles required that skill from the data.")

st.image('imgs/img3.png')
st.write("This graph is visualized by utilizing the tools table from O*NET Data. The data represent the tools required for most of the roles/titles in the job market. The above visualization represents the tools required for a job title in the present market. Word cloud is the best visualization to represent the tool and size of the rectangular box represents the number of titles required for that tool from the data.")

st.image('imgs/img4.png')
st.write("In the BLS projection table of ONET data, We have compared the work experience and the ion Jon training required for different Titles/roles. Size of the bubble represents the median annual wages for the Title/ role.")

st.image('imgs/img5.png')
st.write("The above tree map uses BLS salaries data of the year 2021 to represent the annual mean salaries of people in all the US states.")

st.image('imgs/img6.png')
st.write("""
The Abilities table provides information on the required abilities for different occupations, which can be visualized using scatter plots based on the 'Importance' and 'Level' columns.
The scatter plots help to illustrate the relative significance of each ability for different job titles.
On average, Physicists require the highest level of ability for their jobs, while models require the least.
Another graph shows the average importance of different abilities across all jobs, with 'Oral Comprehension' being the most desired ability at the highest level, and 'Dynamic flexibility' being the least important.
""")