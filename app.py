import streamlit as st
import string
import pickle 
st.title("Movie Recommendation System" )

pickle_in = pickle.load(open("model.pkl","rb"))
def similar_movies(movie_name,rating):
    similar_score = pickle_in[movie_name]*(rating-2.5)
    similar_score = similar_score.sort_values(ascending=False)
    return similar_score
movie = str(st.text_input("enter movie"))
rating = st.number_input("enter rating")

if st.button("predict"):
    movies=similar_movies(movie_name=movie,rating=rating)
    st.write(movies)
