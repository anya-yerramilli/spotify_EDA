#import libraries
import streamlit as st
import pandas as pd
import warnings

warnings.filterwarnings("ignore")

import matplotlib.pyplot as plt
import numpy as np
import plotly.express as px

#look for more information here https://docs.streamlit.io/library/cheatsheet

# st.title()
# st.text()
# st.header()
# st.markdown()
# st.plotly_chart()

#adding title
st.title("Top Spotify Songs")

#adding discription to your website
st.header('Description of Team')


# add name + bios here
st.header('My name is Erin Kim, I am a junior and I like to play tennis, piano, and paint.')

st.header("Hi! I'm Oscar Tiknis, and I am going into freshman year in the fall. I'm in band, and love to play video games")

st.header("My name is Shivani Venkatesh, and I am a rising sophmore. I enjoy swimming and doing art.") 

# add project description  
song_dataframe = pd.read_csv('BestSongsonSpotify.csv', sep=';')
print(song_dataframe.head())

# add genre popularity visualization 

st.markdown("___")


df = song_dataframe.groupby(['top genre']).mean().reset_index()
fig = px.bar(df, x= 'top genre', y = 'popularity', color = 'top genre', title='genre popularity')
st.plotly_chart(fig)

st.text("This graph displays the relationship between the top genre and the highest amount of popularity on spotify. The category of 'genre' can be determined by the style of music played in the song. For example, the more This bar graph shows the popularity of each genre, and the genres with the highest popularity were pop.")

# liveness over time visualization 
st.markdown("___")
st.text("Hypothesis: more recent songs will have higher liveness")
df = song_dataframe.groupby(['year']).mean().reset_index()
fig = px.line(df, x='year', y='liveness', title = 'average liveness of songs by year')
st.plotly_chart(fig)

st.text("Our prediction")

# popularity over time visualization 
st.markdown("___")
fig = px.scatter(song_dataframe, x = 'year', y = 'popularity', title = 'Popularity of Songs Based on the Year they were Released')
st.plotly_chart(fig)



st.markdown("___")

st.text('Songs with higher danceability will be more popular.')
# popularity vs danceability visualization 
fig = px.scatter(song_dataframe, x = 'popularity', y = 'danceability ', title = 'popularity vs. danceability', color = 'top genre')
st.plotly_chart(fig)

st.text('This graph displays the relationship between song popularity and danceability. The category ‘danceability’ is found using a mixture of beat strength, tempo stability, and overall tempo, to see how easily someone could dance throughout the song. Song popularity is calculated by the number of streams a song gets, how recently it has been played, and how frequently people streamed it. The different colors represent the genre of the songs. The majority of the points are plotted in the range of 60-80, with a danceability of about 50-90. Though it is difficult to prove the hypothesis from this graph alone, it is clear that many songs with high danceability are popular. Considering that many people enjoy upbeat music, tracks with a higher danceability are typically known to be more popular.')

# energy vs bpm visualization
st.markdown("___")
st.text("Hypothesis: songs with higher bpm will have higher energy")

df = song_dataframe.groupby(['bpm']).mean().reset_index()
fig = px.bar(df, x='bpm', y='energy', title='energy of songs by bpm')
st.plotly_chart(fig)

st.text("bpm is the beats per minute of a song, and for the most part tells the speed at which the song is played. Energy is the amount of power produced by speakers when the song is played, multiplied by the song's length. The hypothesis does not hold true to a high degree, but there is a slight increase in energy at higher bpm, when excused for a few outliers. However, at the highest bpm's, there are also some of the lowest energies, so the hypothesis is not completely true.")

# popularity vs speechiness visualization 
st.markdown("___")
df = song_dataframe.groupby(['speechiness ']).mean().reset_index()
fig = px.bar(df, x='speechiness ', y='popularity', title='popularity of songs by speechiness')
st.plotly_chart(fig)

st.markdown("___")


st.text('Songs with higher valence will have higher danceability.')
# valence vs danceability visualization 
song_dataframe = pd.read_csv('BestSongsonSpotify.csv', sep=';')
print(song_dataframe.head())
fig = px.scatter(song_dataframe, x = 'valence', y = 'danceability ', title = 'valence vs. danceability', color = 'top genre')
st.plotly_chart(fig)
st.text('Valence measures how positive a song is; tracks that are more upbeat have higher valence, while tracks that sound more negative have a lower valence. This graph compares valence with danceability and reveals that there is no inherent relationship between the two variables. This may be due to the wide variety of dances in the world, and how each dance correspons to a different genre of music. However, many points that are scattered across high danceability do end up having a higher valence than most songs.')
