# Movie Recommendation System

---

## Overview 🎬

The **Movie Recommendation System** is an interactive web application that suggests movies similar to a user-provided movie title. Leveraging content-based filtering through TF-IDF vectorization and cosine similarity, along with hybrid recommendations, the system offers personalized suggestions by analyzing movie metadata. It integrates with the OMDB API to fetch detailed movie information and posters, providing users with a visually engaging experience.

---

## Key Features 🚀

- **Movie Search:**  
  Enter any movie title to receive recommendations of similar movies.

- **Content-Based Filtering:**  
  Recommendations based on movie plots, genres, and other metadata using TF-IDF and cosine similarity.

- **Hybrid Recommendations:**  
  Combines content-based filtering with collaborative filtering techniques for improved suggestion accuracy.

- **Movie Details Display:**  
  View detailed information for each movie including overview, genres, release year, vote average, and IMDb link.

- **Dynamic Movie Posters:**  
  Fetches high-quality movie posters dynamically using the OMDB API.

- **User Interface Themes:**  
  Choose between dark and light themes with custom CSS styling.

- **Pagination:**  
  Browse recommended movies with easy navigation through paged results.

---

## Project Architecture 🏗️

### Frontend

- Built with **Streamlit**, providing a responsive, user-friendly interface.
- Uses custom CSS (`style_dark.css` and `style_light.css`) for theme styling.
- Integrates the **OMDB API** for real-time fetching of movie posters and metadata.

### Backend

- Developed in **Python**.
- Employs a pre-trained model stored in a pickle file (`movie_recommender.pkl`) containing:
  - A **Pandas DataFrame** with movie metadata.
  - A **TF-IDF matrix** representing movie plot and metadata vectors.
- Utilizes **scikit-learn's** `linear_kernel` to compute cosine similarity between movie vectors for recommendations.
- Supports error handling for invalid inputs and API issues.

---

## Installation & Setup 🔧

### Prerequisites

- Python 3.7 or higher.
- An **OMDB API Key**:  
  Obtain your free API key from [OMDB API](http://www.omdbapi.com/apikey.aspx).

### Step-by-Step Guide

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/movie-recommendation-system.git
    cd movie-recommendation-system
    ```

2. **Install dependencies:**

    Create a `requirements.txt` file or run:

    ```bash
    pip install pandas numpy scikit-learn requests streamlit fuzzywuzzy
    ```

3. **Configure API Key:**

    - Open `app.py`.
    - Replace the `OMDB_API_KEY` variable with your OMDB API key.

4. **Ensure required files are present:**

    - `movie_recommender.pkl` (pickled model and data).
    - CSS files: `style_dark.css` and `style_light.css`.

5. **Run the application:**

    ```bash
    streamlit run app.py
    ```

6. **Open the browser:**

    The app will launch locally (usually at `http://localhost:8501`).

---

## Usage Guide 🖥️

### Searching for a Movie

- Enter the exact movie title in the search bar.
- If the movie exists in the dataset, the system will display its details and poster.

### Viewing Recommendations

- Browse recommended movies similar to the searched movie.
- Use pagination buttons to navigate through results.

### Theme Selection

- Toggle between **Dark** and **Light** themes using the radio button at the top.

---

## File Structure 📂

    movie-recommendation-system/
    │
    ├── app.py # Main Streamlit app file
    ├── movie_recommender.pkl # Pickled DataFrame and TF-IDF matrix
    ├── style_dark.css # Dark theme CSS styling
    ├── style_light.css # Light theme CSS styling
    ├── requirements.txt # Python dependencies (optional)
    └── README.md # This README file


---

## How It Works 🔍

1. **Input Movie Title:**
   - The user types a movie title into the text input.

2. **Lookup & Validation:**
   - The app searches for the exact title in the pre-loaded DataFrame.
   - If no match is found, it displays an error.

3. **Fetch Movie Details:**
   - Uses the movie's IMDb ID to fetch detailed information and poster from the OMDB API.

4. **Generate Recommendations:**
   - Calculates cosine similarity scores between the input movie’s TF-IDF vector and all others.
   - Sorts movies by similarity and excludes the original movie.

5. **Display Results:**
   - Shows the selected movie’s details and poster.
   - Displays paginated recommended movies with posters, vote averages, and IMDb links.

6. **Theme & Pagination:**
   - Allows users to switch UI themes.
   - Users can navigate between pages of recommendations.

---

## Future Enhancements 🚧

- **Improved Collaborative Filtering:**  
  Incorporate real user ratings to enhance recommendations.

- **Autocomplete Suggestions:**  
  Add real-time movie title suggestions during typing.

- **Expanded Movie Metadata:**  
  Include cast, crew, runtime, and user reviews.

- **User Profiles & Favorites:**  
  Allow users to save preferences and rate movies for personalized recommendations.

- **Caching API Results:**  
  Reduce redundant OMDB API calls for faster performance.

---

## Troubleshooting & FAQ ❓

- **Movie Not Found Error:**  
  Ensure correct spelling and capitalization. The dataset may not contain very recent or obscure titles.

- **Missing Movie Posters:**  
  Some movies might not have posters available via the OMDB API. A placeholder image will appear instead.

- **OMDB API Limits:**  
  The free OMDB API tier has request limits; consider caching responses or upgrading your plan.

- **App Crashes or Errors:**  
  Check your API key validity, internet connection, and ensure all files are present.

---

## License 📄

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Contact & Support 📧

For questions, bug reports, or feature requests, please contact:  

**Shubham Gzppal**  
Email: [shubhamgzppal@gmail.com](mailto:shubhamgzppal@gmail.com)

---

Thank you for using the Movie Recommendation System! Enjoy discovering your next favorite movie. 🎥🍿
