from scipy.sparse import data
import streamlit as st
from openml_gatheringruns import *
from OpenML_connection import *
from PIL import Image
import plotly.express as px
from PIL import Image
from openml.study import get_study

# Runs the missing tasks of both flows
# there are some optional prints left in the code that might be handy
def running_missingtasks(flows_id, missing_tasks1, missing_tasks2):
    #see what runs were run succesfully/unsuccesfully
    cantrun1 = []
    canrun1 = []
    cantrun2 = []
    canrun2 = []
    for j in missing_tasks1:
        try:
            #st.write(f"Trying to run flow_id {flows_id[0]} on task {j}")
            get_flow = openml.flows.get_flow(flows_id[0], reinstantiate=True)
            task_missing = openml.tasks.get_task(j)
            run_missing = openml.runs.run_flow_on_task(flow=get_flow, task=task_missing)
        except ValueError:
            cantrun1.append(j)
            #st.write(f"flow_id {flows_id[0]} cant run on task {j}")
        else:
            canrun1.append(j)
            #st.write("is succesful!")
            #st.write("Publishig run...")
            run_missing.publish()
    st.write(f"flow_id {flows_id[0]} cant run on tasks: ")
    st.write(f"{cantrun1}")

    st.write(f"flow_id {flows_id[0]} did run on tasks: ")
    st.write(f"{canrun1}")

    for j in missing_tasks2:
        try:
            #st.write(f"Trying to run flow_id {flows_id[1]} on task {j}")
            get_flow = openml.flows.get_flow(flows_id[1], reinstantiate=True)
            task_missing = openml.tasks.get_task(j)
            run_missing = openml.runs.run_flow_on_task(flow=get_flow, task=task_missing)
        except ValueError:
            cantrun2.append(j)
            #st.write(f"flow_id {flows_id[1]} cant run on task {j}")
        else:
            canrun2.append(j)
            #st.write("is succesful!")
            #st.write("Publishig run...")
            run_missing.publish()
    st.write(f"flow_id {flows_id[1]} cant run on tasks: ")
    st.write(f"{cantrun2}")

    st.write(f"flow_id {flows_id[1]} did run on tasks: ")
    st.write(f"{canrun2}")
    


# default value = False meaning we do not run missing tasks.
shouldrun = False


evaluation_id = []
# lists for the missing tasks we might need to run
missingtasks1 = []
missingtasks2 = []
#for nr of input boxes
#counter = 3

#header
st.title(""" OpenML Mythbusting """)
st.write(""" This application allows the user to fully experience what a data scientist does.""")
st.write("""This app uses algorithms from OpenML to do the following:\n
        - Running flows on tasks
        - Checks for all task if they are already ran on a flow, else runs them
        - Create multiple plots comparing the flows on the given study
        version 1.0.1""")

st.header("Criterias")
st.write("Please give an input to all of the following:\n  ")

#input fields
study_id = st.number_input("study_id: (ex. 123)",step=1, value=123, min_value = 0, max_value=100000000)
flow_id1 = st.number_input("flow_id1: (ex. 7754)",step=1, value=7754, min_value = 0, max_value=100000000)
flow_id2 = st.number_input("flow_id2: (ex. 7756)",step=1, value=7756, min_value = 0, max_value=100000000)
flows_id = [flow_id1, flow_id2]


#code for a button that adds flows (out of our scope)

#if st.button('add flows'):
#        for i in range(amount_flows):
#                flows_id[i] = st.number_input(f"flow_id{i}: (ex. 7756)",step=1, value=7756, min_value = 0, max_value=100000000)
#if st.button('+'):
 
 #       flow_id4 = st.number_input(f"flow_id{counter}: (ex. 7756)",step=1, value=7756, min_value = 0, max_value=100000000)
 #       counter = counter + 1
 #       flow_id5 = st.number_input(f"flow_id{counter}: (ex. 7756)",step=1, value=7756, min_value = 0, max_value=100000000)
 #       counter = counter + 1
 #       flows_id.append(flow_id4, flow_id5)



 #checkbox should we run missing flows?
if st.checkbox("Do you want to run missing flows (takes longer)?"):
    shouldrun = True
else:
    shouldrun = False

#Collects data needed, and optionally runs missing tasks
if st.button('Run'):
    with st.spinner("Training ongoing"):
        if(shouldrun == True):
            missingtasks1, missingtasks2 = gatheringruns(study_id, flows_id)
        #st.write(f'The missingtasks are:\n {missingtasks}')
        evaluation_id = loadResults(study_id, flows_id)

#log to see progress of program
expander = st.expander("See all logs")
with expander:
    st.write("Here you can see everything that happens")
    if shouldrun:
        st.write(f'The missingtasks of flow {flows_id[0]} are:\n {missingtasks1}')
        st.write(f'The missingtasks of flow {flows_id[1]} are:\n {missingtasks2}')
        running_missingtasks(flows_id,missingtasks1, missingtasks2)
    else:
        st.write("no errors encountered")

#log for results
plots_expander = st.expander("See the plots")
with plots_expander:
        st.header("The plots") 
        image = Image.open('diagplot.png')
        st.image(image, caption='diagplot')
        image = Image.open('barplot.png')
        st.image(image, caption='barplot')
        image = Image.open('splot.png')
        st.image(image, caption='splot')