from scipy.sparse import data
import streamlit as st
import locale
from openml_gatheringruns import *
from PIL import Image
import plotly.express as px





st.title(""" OpenML Mythbusting """)
st.write("""  An artist or a producer can try this app to get a prediction of the amount of streams his song will get or to get a prediction of how high the song will be in the charts compared to the existing songs on Spotify.""")
st.write("""This app uses a prediction algtorithm based on a data set of spotify songs.
        To make a valid prediction we need a little bit information about the song:\n
        - Artist's number of followers on Spotify
        - Tempo of the song
        - Duration of the song in ms""")

st.header("Criterias")
st.write("Please give an input to all of the following:\n  ")
st.write("(The less information provided the less precise the prediction will be. So please try to answer all of the fields!)")

#inputs
study_id = st.text_input('study_id: (ex. 123)',)
flow_id1 = st.number_input("flow_id1: (ex. 7754)",step=1, value=7754, min_value = 0, max_value=100000000)
flow_id2 = st.number_input("flow_id2: (ex. 7756)",step=1, value=7756, min_value = 0, max_value=100000000)

if st.button('Runmodel'):
    #with st.spinner("Training ongoing"):
    gathered = gatheringruns(study_id, flow_id1, flow_id2)
    st.header(gathered)

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
st.plotly_chart(fig)
"""
