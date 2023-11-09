import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_poster(id):

    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

def recommend(movie):
    movie_index = movies[movies['title']==movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x:x[1])[1:6]

    recommended_movies = []
    recommended_movies_posters = []
    for i in movies_list:
        id = movies.iloc[i[0]].id
        # poster fetch from API
        #1st we login TMDB, go to settings in IMDB, go to API there and copy that link
        # then go TMDB API, go to MOVIES section Get Details option, then click on try it
        #copy it and past in web with previously created api key and wih movie id which is
        #given in this imdb dataset, now we get json file, then open online json viewer
        #and paste this text there and you get the details about the movie
        recommended_movies_posters.append(fetch_poster(id))
        recommended_movies.append(movies.iloc[i[0]].title)

    return recommended_movies, recommended_movies_posters


movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl', 'rb'))


st.title ('Movie Recommender System')

selected_movie_name = st.selectbox(
'Popular Shows for You!',
movies['title'].values)

if st.button('Recommend'):
    names, posters = recommend(selected_movie_name)

    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(names[0])
        st.image(posters[0])
    with col2:
        st.text(names[1])
        st.image(posters[1])
    with col3:
        st.text(names[2])
        st.image(posters[2])
    with col4:
        st.text(names[3])
        st.image(posters[3])
    with col5:
        st.text(names[4])
        st.image(posters[4])


