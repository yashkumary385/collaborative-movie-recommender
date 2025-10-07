import streamlit as st
import string
import pickle 
import numpy as np
import pandas as pd
import requests
st.title("Movie Recommendation System" )

pickle_in = pickle.load(open("model.pkl","rb"))
df1=pd.read_csv("movies (1).csv")
# st.write(df)
movies_list = pickle_in.columns
movies_list = np.array(movies_list)


def similar_movies(movie_name,rating):
    similar_score = pickle_in[movie_name]*(rating-2.5)
    similar_score = similar_score.sort_values(ascending=False)
    
    return similar_score.index

def name_change(movie_name):
    name = movie_name.split()
    name = name[0:len(name)-1]
    name = " ".join(name)
    return name
df1["title"] = df1["title"].apply(name_change)

movies_id =[]
# st.write(df1["title"])

def make_list(movies):
    global df1
    for movie in movies:
        filtered = df1[df1["title"] == movie]
        if not filtered.empty:
            # Take the first movieId if there are duplicates
            data_id = filtered["movieId"].values.item()
            movies_id.append(data_id)
        else:
            st.write(f"⚠️ Movie '{movie}' not found in df1")
    # fetch_poster(movies_id)        
    return movies_id


# ids = make_list(movies_data)
# st.write(ids)
# st.write("Type of df1:", type(df1))
# st.write("Columns:", df1.columns)
# st.write("First few rows:\n", df1.head())

selected_movie = st.selectbox(
    "Which Movie Recommnedation Dou You Want ?",
    (movies_list),
    index=None,
    placeholder="Select a movie...",
)
rating = st.number_input("enter rating",min_value=0,max_value=5,format="%d")
# if selected_movie and rating:
#     movies_items = similar_movies(selected_movie,rating)
# ids = make_list(movies_list)


# movie_posters=[]
# def fetch_poster(movie_id):
#     for movie in movie_id:
#        url = "https://api.themoviedb.org/3/movie/{}?api_key=b9bead723a409353d5ed5ab04f7bc2fa&language=en-US".format(movie)
#        data = requests.get(url)
#        data = data.json()
#        poster_path = data['poster_path']
#        full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
#        movie_posters.append(full_path)
   


if st.button("Recommend"):
        movies_list = similar_movies(selected_movie,rating)[1:6]
        # st.write(movies_list)
        ids = make_list(movies_list)
        st.write(ids)
        # for ans in answer:
        # st.write(ids)
        col1, col2, col3,col4,col5 = st.columns(5)

        with col1:
              st.write(movies_list[0])
            #   st.image(movie_posters[0])

        with col2:
               st.write(movies_list[1])
             


        with col3:
               st.write(movies_list[2])
             
        with col4:
               st.write(movies_list[3])
            

        with col5:
               st.write(movies_list[4])
             
        
        
        
        
        
