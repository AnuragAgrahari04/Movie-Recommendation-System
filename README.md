# 🎬 Movie Recommendation System

A web application built with **Streamlit** that recommends movies using **content-based filtering**.  
The app suggests **5 movies with similar content** (plot, genres, keywords, etc.) to the one you select.

🔗 **Live App:** [movie-recommendation-system-2004.streamlit.app](https://movie-recommendation-system-2004.streamlit.app/)

---

## 📸 Demo

Here is the app in action, showing recommendations for **"(500) Days of Summer"**:

*(Add a demo GIF or screenshot here, e.g., `![App Demo](assets/demo.gif)`)*

---

## 🌟 Features

- 🎯 **Content-Based Recommendations** — Search for a movie and get 5 similar “movies like this.”
- ⚡ **Real-time API Integration** — Fetches movie posters and summaries from the **OMDB API**.
- 💻 **Simple & Fast UI** — Clean, minimal interface built with **Streamlit**.
- 🧠 **Optimized for Deployment** — Uses precomputed `cosine_sim.pkl` (as float32) to reduce memory and stay under GitHub’s 100 MB limit.
- 🔐 **Secure API Key Handling** — Uses **Streamlit Secrets** for deployment and a local `config.json` for development.

---

## 🛠️ Tech Stack & Libraries

| Category | Tools / Libraries |
|-----------|-------------------|
| **Frontend** | Streamlit |
| **Backend** | Python |
| **Data Processing** | Pandas |
| **Modeling** | Scikit-learn (TF-IDF & Cosine Similarity) |
| **Text Preprocessing** | NLTK |
| **Model Serialization** | Joblib |
| **API Calls** | Requests (OMDB API) |

---

## 📈 How It Works

The recommendation model is built using `src/preprocess.py`, which performs the following steps:

1. **Load Data** — Reads the raw `movies.csv`.
2. **Clean Text** — Cleans and preprocesses the text from `genres`, `keywords`, and `overview`.
3. **Create Tags** — Combines cleaned text into a new `tags` column.
4. **Vectorize Text** — Converts `tags` into a numerical matrix using **TfidfVectorizer** (limited to 5000 features).
5. **Compute Similarity** — Calculates **cosine similarity** between all movies.
6. **Save Models** — Saves the processed DataFrame (`df_cleaned.pkl`) and similarity matrix (`cosine_sim.pkl`) using **Joblib**.

The **Streamlit app** (`src/main.py`) loads these `.pkl` files and the API key to generate recommendations in real time.

---

## 📂 Project Structure

```
movie/
├── .venv
├── config.json 
├── cosine_sim.pkl
├── df_cleaned.pkl
├── main.py 
├── movies.csv 
├── movies-recommendation-system.ipynb 
├── omdb_utils.py 
├── preprocess.log 
├── preprocess.py 
├── recommend.py 
├── requirements.txt 
└── start_app.txt 
```

---

## 🚀 How to Run Locally

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/AnuragAgrahari04/Movie-Recommendation-System.git
cd Movie-Recommendation-System
```

### 2️⃣ Create a Virtual Environment and Install Dependencies
```bash
# Create a virtual environment
python -m venv .venv

# Activate the environment
# On Windows:
.venv\Scripts\activate

# On macOS/Linux:
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 3️⃣ Get Your OMDB API Key

##### => Visit OMDb API to get a free API key.
##### => Create a file named config.json in the project root:

```bash
{
  "OMDB_API_KEY": "YOUR_KEY_GOES_HERE"
}
```
### 4️⃣ (Optional) Rebuild Model Files

If you want to regenerate the .pkl files from scratch:
```bash
python preprocess.py
```
### 5️⃣ Run the Streamlit App
```bash
streamlit run main.py
```
