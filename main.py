# import json
# import streamlit as st
# from recommend import df, recommend_movies
# from omdb_utils import get_movie_details
# import os
#
# # --- FIX HERE ---
# import os
# BASE_DIR = os.path.dirname(__file__)
# config_path = os.path.join(BASE_DIR, "config.json")
# config = json.load(open(config_path))
#
# # ----------------
#
# # OMDB api key
# OMDB_API_KEY = config["OMDB_API_KEY"]
#
# st.set_page_config(
#     page_title="Movie Recommender",
#     page_icon="🎬",
#     layout="centered"
# )
#
# st.title("🎬 Movie Recommender")
#
# # Using 'title' instead of 'song' now
# movie_list = sorted(df['title'].dropna().unique())
# selected_movie = st.selectbox("🎬 Select a movie:", movie_list)
#
# if st.button("🚀 Recommend Similar Movies"):
#     with st.spinner("Finding similar movies..."):
#         recommendations = recommend_movies(selected_movie)
#         if recommendations is None or recommendations.empty:
#             st.warning("Sorry, no recommendations found.")
#         else:
#             st.success("Top similar movies:")
#             for _, row in recommendations.iterrows():
#                 movie_title = row['title']
#                 plot, poster = get_movie_details(movie_title, OMDB_API_KEY)
#
#                 with st.container():
#                     col1, col2 = st.columns([1, 3])
#                     with col1:
#                         if poster != "N/A":
#                             st.image(poster, width=100)
#                         else:
#                             st.write("❌ No Poster Found")
#                     with col2:
#                         st.markdown(f"### {movie_title}")
#                         st.markdown(f"*{plot}*" if plot != "N/A" else "_Plot not available_")



import json
import streamlit as st
from recommend import df, recommend_movies
from omdb_utils import get_movie_details
import os

st.set_page_config(
    page_title="Movie Recommender",
    page_icon="🎬",
    layout="centered"
)

# --- Load API Key (Works Locally & Deployed) ---
try:
    # 1. Try to load from Streamlit's secrets (for deployment)
    # This uses the .toml format you added in the Streamlit dashboard
    OMDB_API_KEY = st.secrets["OMDB_API_KEY"]
except (KeyError, FileNotFoundError):
    # 2. If not found, load from local config.json (for local)
    try:
        # This code is for your local machine
        # It finds config.json in the same folder as main.py
        BASE_DIR = os.path.dirname(__file__)
        config_path = os.path.join(BASE_DIR, "config.json")
        with open(config_path) as f:
            config = json.load(f)
        OMDB_API_KEY = config["OMDB_API_KEY"]
    except Exception as e:
        st.error(f"API key not found. Please add it to Streamlit Secrets (for deployment) or a local config.json (for local testing). Error: {e}")
        st.stop()
# -----------------------------------------------

st.title("🎬 Movie Recommender")

# Using 'title' instead of 'song' now
movie_list = sorted(df['title'].dropna().unique())
selected_movie = st.selectbox("🎬 Select a movie:", movie_list)

if st.button("🚀 Recommend Similar Movies"):
    with st.spinner("Finding similar movies..."):
        recommendations = recommend_movies(selected_movie)
        if recommendations is None or recommendations.empty:
            st.warning("Sorry, no recommendations found.")
        else:
            st.success("Top similar movies:")
            for _, row in recommendations.iterrows():
                movie_title = row['title']
                plot, poster = get_movie_details(movie_title, OMDB_API_KEY)

                with st.container():
                    col1, col2 = st.columns([1, 3])
                    with col1:
                        if poster != "N/A":
                            st.image(poster, width=100)
                        else:
                            st.write("❌ No Poster Found")
                    with col2:
                        st.markdown(f"### {movie_title}")
                        st.markdown(f"*{plot}*" if plot != "N/A" else "_Plot not available_")
