#import libraries
import streamlit as st
import pandas as pd
import warnings

warnings.filterwarnings("ignore")

import plotly.express as px

#look for more information here https://docs.streamlit.io/library/cheatsheet

# st.title()
# st.write()
# st.header()
# st.markdown()
# st.plotly_chart()

#adding title
st.title("Top Spotify Songs")

#adding discription to your website
st.header('Description of Team')

# add name + bios here
st.header(
  'My name is Erin Kim! I am a junior and I like to play tennis, piano, and paint.'
)

st.header(
  "Hi! I'm Oscar Tiknis, and I am going into freshman year in the fall. I'm in band, and love to play video games"
)

st.header(
  "My name is Shivani Venkatesh, and I am a rising sophmore. I enjoy swimming and doing art."
)

st.markdown("""___""")

# add project description
st.write(
  'We collected our information from Kaggle, a data science platform that allows us to download datasets and analyze them. The dataset we used is called "Best Songs on Spotify for every year (2000-2023)", by Conor Van Eden. This dataset consists of songs that have been popular over past years and provides information about how each song was created. They are ranked based on various categories such as the genre of the song, energy level, popularity, etc.'
)

song_dataframe = pd.read_csv('BestSongsonSpotify.csv', sep=';')
st.write(song_dataframe.head())

# add genre popularity visualization

st.markdown("""___""")
st.header('Hypothesis: Songs that are "pop" will be more popular')
df = song_dataframe.groupby(['top genre']).mean(numeric_only=True).reset_index()
fig = px.bar(df,
             x='top genre',
             y='popularity',
             color='top genre',
             title='Genre Popularity')
st.plotly_chart(fig)

st.write(
  "This graph displays the relationship between the top genre and the highest amount of popularity on spotify. The category of 'genre' can be determined by the style of music played in the song. For example, the more This bar graph shows the popularity of each genre, and the genres with the highest popularity were pop. Our prediction was that pop would have the highest amount of popularity because almost everyone likes pop. Majority of the songs are also some kind of pop, so it isn't unexpected that the most popular song genre is pop. "
)

# liveness over time visualization
st.markdown("""___""")
st.header("Hypothesis: More recent songs will have higher liveness")
df = song_dataframe.groupby(['year']).mean(numeric_only=True).reset_index()
fig = px.line(df,
              x='year',
              y='liveness',
              title='Average Liveness of songs by Year')
st.plotly_chart(fig)
st.write(
  "Liveness is how much an audience is audible in the song. This graph shows than over time liveness in songs has been varied, other than a peak in 1997."
)

st.markdown("""___""")
st.header("Hypothesis: more recent songs will be more popular")
# popularity over time visualization
fig = px.scatter(
  song_dataframe,
  x='year',
  y='popularity',
  title='Popularity of Songs Based on the Year they were Released')
st.plotly_chart(fig)

st.write(
  "This graph determines how over the years, the popularity of a song increases. The popularity of a song is determined by the number of streams that each song gets. It would be expected that the older the songs are, the more views they would get, and the more popular they would get because they had much more time to be seen. But that is not the case in this situation, because the most popular songs are actually the ones that have been released the latest, making them more trendy."
)

st.markdown("""___""")

st.header('Hypothesis: Songs with higher danceability will be more popular.')
# popularity vs danceability visualization
fig = px.scatter(song_dataframe,
                 x='popularity',
                 y='danceability ',
                 title='Popularity vs. Danceability',
                 color='top genre')
st.plotly_chart(fig)

st.write(
  'This graph displays the relationship between song popularity and danceability. The category ‘danceability’ is found using a mixture of beat strength, tempo stability, and overall tempo, to see how easily someone could dance throughout the song. Song popularity is calculated by the number of streams a song gets, how recently it has been played, and how frequently people streamed it. The different colors represent the genre of the songs. The majority of the points are plotted in the range of 60-80, with a danceability of about 50-90. Though it is difficult to prove the hypothesis from this graph alone, it is clear that many songs with high danceability are popular. Considering that many people enjoy upbeat music, tracks with a higher danceability are typically known to be more popular.'
)

# energy vs bpm visualization
st.markdown("""___""")
st.header("Hypothesis: songs with higher bpm will have higher energy")

df = song_dataframe.groupby(['bpm']).mean(numeric_only=True).reset_index()
fig = px.line(df, x='bpm', y='energy', title='Energy of Songs by BPM')
st.plotly_chart(fig)

st.write(
  "bpm is the beats per minute of a song, and for the most part tells the speed at which the song is played. Energy is the amount of power produced by speakers when the song is played, multiplied by the song's length. The hypothesis does not hold true to a high degree, but there is a slight increase in energy at higher bpm, when excused for a few outliers. However, at the highest bpm's, there are also some of the lowest energies, so the hypothesis is not completely true, and it seems that rather than an increase in energy at a higher bpm, there is more range for what the energy can be."
)

# popularity vs speechiness visualization
st.markdown("""___""")
st.header(
  'Hypothesis: Songs with less speechiness will have higher popularity')
df = song_dataframe.groupby(['speechiness ']).mean(numeric_only=True).reset_index()
fig = px.bar(df,
             x='speechiness ',
             y='popularity',
             title='Popularity of Songs by Speechiness')
st.plotly_chart(fig)
st.write(
  "Speechiness is measured by the amount of spoken words in a song. From the graph is appears that the speechiness of a song has little to no correlation with the song's popularity. However, the popularity of songs with high speechiness is more varied than at lower speechiness, which shows there is some form of correlation"
)
st.markdown("""___""")

st.header(
  'Hypothesis: Songs with higher valence will have higher danceability.')
# valence vs danceability visualization
song_dataframe = pd.read_csv('BestSongsonSpotify.csv', sep=';')
print(song_dataframe.head())
fig = px.scatter(song_dataframe,
                 x='valence',
                 y='danceability ',
                 title='Valence vs. Danceability',
                 color='top genre')
st.plotly_chart(fig)
st.write(
  'Valence measures how positive a song is; tracks that are more upbeat have higher valence, while tracks that sound more negative have a lower valence. This graph compares valence with danceability and reveals that there is no inherent relationship between the two variables. This may be due to the wide variety of dances in the world, and how each dance correspons to a different genre of music. However, many points that are scattered across high danceability do end up having a higher valence than most songs.'
)
st.markdown("""___""")

#conclusion

st.header('Conclusion')
st.write(
  "In the end, many of our hypotheses were proven to be correct, even though some were proven otherwise. Based on our visualizations, it is clear to see that there are many relationships between the variables collected, and while some don't have much correlation, many of the variables seem to follow a trend in relationships with one another."
)
