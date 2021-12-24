from scipy.sparse import data
import streamlit as st
import locale
from openml_gatheringruns import *
from OpenML_connection import *
from PIL import Image
import plotly.express as px
import hydralit_components as hc
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

st.title(""" OpenML Mythbusting """)
st.write(""" This application allows the user to fully experience what a data scientist does.""")
st.write("""This app uses a algorithms from OpenMl to do the following:\n
        - Running flows on tasks
        - Checks if all task are runned on a study, if not, tries to do it again
        - Created multiple plots from the study_id""")

st.header("Criterias")
st.write("Please give an input to all of the following:\n  ")

#inputs
name = st.text_input("Type here the name of your algorithm",)
study_id = st.number_input("study_id: (ex. 123)",step=1, value=123, min_value = 0, max_value=100000000)
flow_id1 = st.number_input("flow_id1: (ex. 7754)",step=1, value=7754, min_value = 0, max_value=100000000)
flow_id2 = st.number_input("flow_id2: (ex. 7756)",step=1, value=7756, min_value = 0, max_value=100000000)

flows_id = [flow_id1, flow_id2]
if st.button('Runmodel'):
    #with st.spinner("Training ongoing"):
    missingtasks = gatheringruns(study_id, flow_id1, flow_id2)
    st.header("The log")
    st.write(f'The missingtasks are:\n {missingtasks}')
    evaluation_id = loadResults(study_id, flows_id)

def plots():
        st.header("The plots")
        image = Image.open('barplot.png')
        st.image(image, caption='barplot')
        image = Image.open('diagplot.png')
        st.image(image, caption='diagplot')
        image = Image.open('splot.png')
        st.image(image, caption='splot')

expander = st.expander("See all logs")
with expander:
    st.write("Here you can see everything that happens")
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

"""#    data class
app = SpotifyApp('spotify_dataset.csv')
predict_options = ['Streams', 'Highest Charting Position']
predict = st.selectbox('Select what to predict.',predict_options)
if st.button('Predict'):
    with st.spinner("Training ongoing"):
        if predict == 'Streams':
                streams = app.predict_streams(followers,tempo,duration)
                st.header(f'Following our predicition algorithm we estimated that {name_song} will reach {round(streams[0])} streams!')
        else:
                highest_charting = app.predict_highest_charting_position(followers,tempo,duration)
                st.header(f'Following our predicition algorithm we estimated that {name_song} will reach {round(highest_charting[0])} as the highest charting position!')
#plot
df = app.data #get csv file
st.header ('Scatter Plot') #title
st.write('To get a better understanding of the prediction we have provided a scatterplot of the data set.  ')
st.write('The X  value can be changed using the selectboxes at the top of the plot.')
st.write('We have also provided a local regression line to help us see the relationship between the axes. ')
x_options = ['Artist Followers','Duration (ms)','Tempo'] #selectbox options
x_axis = st.selectbox('Select X-as', x_options)
y_axis = predict
fig = px.scatter(df, 
        x=x_axis,
        y=y_axis,
        hover_name=y_axis,
        title=f'{y_axis} compared to {x_axis}',
        color = "Tempo",
        trendline="lowess")
#creating a scatter plot 
if y_axis == 'Highest Charting Position': fig['layout']['yaxis']['autorange'] = "reversed"

"""




