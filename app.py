# Import the required libraries.

import streamlit as st
import pickle
from pathlib import Path

# Set the page configuration.

st.set_page_config(
    page_title="Movie Recommendation System",
    page_icon="🎬",
    layout="centered"
)

# Get the project root directory.

BASE_DIR = Path(__file__).resolve().parent.parent

# Load the saved files.

movies = pickle.load(open(BASE_DIR / "models" / "movies.pkl", "rb"))
similarity = pickle.load(open(BASE_DIR / "models" / "similarity.pkl", "rb"))


# Recommendation function.

def recommend(movie):

    movie_index = movies[movies["title"] == movie].index[0]

    distances = similarity[movie_index]

    movie_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]

    recommended_movies = []

    for movie in movie_list:
        recommended_movies.append(movies.iloc[movie[0]].title)

    return recommended_movies


# App Title.

st.title("🎬 Movie Recommendation System")

st.markdown(
    """
    Discover movies similar to your favorite film using a
    **Content-Based Recommendation System** built with
    Machine Learning and Natural Language Processing.
    """
)

selected_movie = st.selectbox(
    "Select a Movie",
    movies["title"].values
)

if st.button("Recommend Movies"):

    recommendations = recommend(selected_movie)

    st.subheader("Top 5 Recommendations")

    for i, movie in enumerate(recommendations, start=1):
        st.write(f"**{i}. {movie}**")