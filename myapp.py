from scipy.sparse import data
import streamlit as st
import locale
from openml_gatheringruns import *
from OpenML_connection import *
from PIL import Image
import plotly.express as px
from PIL import Image

def running_missingtasks(flows_id, missing_tasks):
    for i in flows_id:
        for j in missing_tasks:
            try:
                st.write(f"Trying to run flow_id {i} on task {j}")
                get_flow = openml.flows.get_flow(i, reinstantiate=True)
                task_missing = openml.tasks.get_task(j)
                run_missing = openml.runs.run_flow_on_task(flow=get_flow, task=task_missing)
            except ValueError:
                st.write(f"flow_id {i} cant run on task {j}")
            else:
                st.write("is succesful!")

evaluation_id = []
missingtasks = []
counter = 3

st.title(""" OpenML Mythbusting """)
st.write(""" This application allows the user to fully experience what a data scientist does.""")
st.write("""This app uses a algorithms from OpenMl to do the following:\n
        - Running flows on tasks
        - Checks if all task are runned on a study, if not, tries to do it again
        - Created multiple plots from the study_id""")

st.header("Criterias")
st.write("Please give an input to all of the following:\n  ")

#inputs
study_id = st.number_input("study_id: (ex. 123)",step=1, value=123, min_value = 0, max_value=100000000)
flow_id1 = st.number_input("flow_id1: (ex. 7754)",step=1, value=7754, min_value = 0, max_value=100000000)
flow_id2 = st.number_input("flow_id2: (ex. 7756)",step=1, value=7756, min_value = 0, max_value=100000000)
amount_flows = st.number_input("How many flows do you want to input? (steps of 2)",step=2, value=2, min_value = 0, max_value=100000000)
flows_id = [flow_id1, flow_id2]

#if st.button('add flows'):
#        for i in range(amount_flows):
#                flows_id[i] = st.number_input(f"flow_id{i}: (ex. 7756)",step=1, value=7756, min_value = 0, max_value=100000000)

if st.button('+'):
        #(kaas,('counter')) = st.number_input(f"flow_id{counter}: (ex. 7754)",step=1, value=7754, min_value = 0, max_value=100000000)
        flow_id4 = st.number_input(f"flow_id{counter}: (ex. 7756)",step=1, value=7756, min_value = 0, max_value=100000000)
        counter = counter + 1
        flow_id5 = st.number_input(f"flow_id{counter}: (ex. 7756)",step=1, value=7756, min_value = 0, max_value=100000000)
        counter = counter + 1
        flows_id.append(flow_id4, flow_id5)

if st.button('Runm'):
    #with st.spinner("Training ongoing"):
    missingtasks = gatheringruns(study_id, flows_id)
    #st.write(f'The missingtasks are:\n {missingtasks}')
    evaluation_id = loadResults(study_id, flows_id)







expander = st.expander("See all logs")
with expander:
    st.write("Here you can see everything that happens")
    st.write(f'The missingtasks are:\n {missingtasks}')
    running_missingtasks(flows_id,missingtasks)

plots_expander = st.expander("See the plots")
with plots_expander:
        st.header("The plots")
        image = Image.open('barplot.png')
        st.image(image, caption='barplot')
        image = Image.open('diagplot.png')
        st.image(image, caption='diagplot')
        image = Image.open('splot.png')
        st.image(image, caption='splot')






