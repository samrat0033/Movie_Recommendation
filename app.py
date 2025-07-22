import streamlit as st
import pickle
import pandas as pd

movies= pickle.load(open("movies2.pkl","rb"))
movies_list= movies['title'].values

def recommend(movie):
  movie_index = movies[movies["title"]==movie].index
  if not movie_index.empty:
      movie_index = movie_index[0] # Handle the case where movie is not found
      distances = similarity[movie_index]
      movies_list = sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:11] # Use distances instead of similarity
      
      recommended_movies=[]
      for i in movies_list:
          recommended_movies.append(movies.iloc[i[0]].title)
      return recommended_movies
  else:
      print(f"Movie '{movie}' not found in the dataset.")

similarity = pickle.load(open("similarity.pkl","rb"))

st.title("Movie Recommendation System")

selected_movie_name = option = st.selectbox(
    "Hello! Samrat here, select a movie you like",
    movies_list
)
if st.button('Recommend'):
    recomendations = recommend(selected_movie_name)
    for i in recomendations:
        st.write(i)