import ast
import requests
import pandas as pd
import pickle
import streamlit as st
from sklearn.metrics.pairwise import linear_kernel

# Load model and data
with open("movie_recommender.pkl", "rb") as f:
    df, tfidf_matrix = pickle.load(f)

OMDB_API_KEY = 'b4247444'

# Load CSS based on theme
def load_css(theme="dark"):
    file = "style_dark.css" if theme == "dark" else "style_light.css"
    try:
        with open(file, "r") as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    except FileNotFoundError:
        st.warning(f"{file} not found!")

def fetch_movie_data(imdb_id):
    if not imdb_id or imdb_id == 'nan':
        return {}
    url = f"http://www.omdbapi.com/?i={imdb_id}&apikey={OMDB_API_KEY}"
    try:
        resp = requests.get(url)
        return resp.json()
    except:
        return {}

def get_index_from_title(title):
    if not title.strip():
        raise ValueError("Please enter a movie title.")
    match = df[df['title'].str.lower().str.strip() == title.strip().lower()]
    if match.empty:
        raise ValueError(f"No movie found with title '{title}'.")
    return match.index[0]

def recommend(movie_index):
    sim = linear_kernel(tfidf_matrix[movie_index], tfidf_matrix).flatten()
    indices = sim.argsort()[::-1]
    return [i for i in indices if i != movie_index]

def parse_genres(g):
    try:
        if isinstance(g, str):
            parsed = ast.literal_eval(g)
            if isinstance(parsed, list):
                return ', '.join([d.get('name') for d in parsed])
        elif isinstance(g, list):
            return ', '.join([d.get('name') for d in g])
    except:
        return ''
    return str(g)

# --- Streamlit App ---
theme = st.radio("Choose Theme", ["Dark", "Light"], horizontal=True)
load_css("dark" if theme == "Dark" else "light")

st.markdown("<h1 style='text-align:center;'>🎬 Movie Recommendation System</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align:center;'>Find movies similar to your favorite</h4>", unsafe_allow_html=True)

movie_title = st.text_input("Enter a movie title:")

PAGE_SIZE = 5
if "start" not in st.session_state:
    st.session_state.start = 0

if not movie_title:
    st.subheader("🔥 Popular Movies")
    popular = df.sort_values("vote_average", ascending=False).head(10)
    cols = st.columns(5)
    for i, (_, mv) in enumerate(popular.iterrows()):
        imdb = mv.get('imdb_id', '')
        info = fetch_movie_data(imdb)
        poster = info.get('Poster', '') or 'https://via.placeholder.com/150x225?text=No+Image'
        col = cols[i % 5]
        with col:
            st.markdown(f"""
            <div class="card">
                <img src="{poster}" alt="{mv['title']}">
                <div class="card-title">{mv['title']}</div>
                <div class="card-description">⭐ {mv['vote_average']}</div>
                <a class="card-link" href="https://www.imdb.com/title/{imdb}" target="_blank">IMDb</a>
            </div>
            """, unsafe_allow_html=True)
else:
    try:
        index = get_index_from_title(movie_title)
        movie = df.iloc[index]
        imdb_id = movie.get("imdb_id", "")
        info = fetch_movie_data(imdb_id)
        poster = info.get('Poster', '') or 'https://via.placeholder.com/300x450?text=No+Image'

        # Layout for searched movie
        c1, c2 = st.columns([1, 2])
        with c1:
            st.image(poster, width=300)
        with c2:
            st.markdown(f"<h2>{movie['title']}</h2>", unsafe_allow_html=True)
            st.markdown(f"**Overview**: {movie['overview']}")
            st.markdown(f"**Genres**: {parse_genres(movie['genres'])}")
            st.markdown(f"**Release Year**: {movie['release_date'][:4] if isinstance(movie['release_date'], str) else 'Unknown'}")
            st.markdown(f"**Vote Average**: ⭐ {movie['vote_average']}")
            st.markdown(f"[IMDb](https://www.imdb.com/title/{imdb_id})")

        # Recommendations
        rec_indices = recommend(index)
        total = len(rec_indices)
        paged = rec_indices[st.session_state.start:st.session_state.start + PAGE_SIZE]
        rec_movies = df.iloc[paged]

        st.subheader("🎯 Recommended Movies")

        cols = st.columns(PAGE_SIZE)
        for i, (_, r) in enumerate(rec_movies.iterrows()):
            col = cols[i % PAGE_SIZE]
            imdb = r.get("imdb_id", "")
            info = fetch_movie_data(imdb)
            poster = info.get("Poster", "") or 'https://via.placeholder.com/150x225?text=No+Image'
            with col:
                st.markdown(f"""
                <div class="card">
                    <img src="{poster}" alt="{r['title']}">
                    <div class="card-title">{r['title']}</div>
                    <div class="card-description">⭐ {r['vote_average']}</div>
                    <a class="card-link" href="https://www.imdb.com/title/{imdb}" target="_blank">IMDb</a>
                </div>
                """, unsafe_allow_html=True)

        # Pagination
        prev, _, next = st.columns([1, 1, 1])
        with prev:
            if st.session_state.start >= PAGE_SIZE and st.button("◀ Previous"):
                st.session_state.start -= PAGE_SIZE
        with next:
            if st.session_state.start + PAGE_SIZE < total and st.button("Next ▶"):
                st.session_state.start += PAGE_SIZE

    except ValueError as ve:
        st.error(str(ve))
    except Exception as e:
        st.error("Something went wrong.")
        raise
