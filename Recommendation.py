import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

# Load your movies dataset
film_collection = pd.read_csv("movies.csv")
film_collection = film_collection.fillna('')

# Combine all relevant features into one string per movie
film_collection['feature_string'] = (
    film_collection['Genre'] + ' ' +
    film_collection['Lead Studio'] + ' ' +
    film_collection['Audience score %'].astype(str) + ' ' +
    film_collection['Profitability'].astype(str) + ' ' +
    film_collection['Rotten Tomatoes %'].astype(str) + ' ' +
    film_collection['Worldwide Gross'].astype(str) + ' ' +
    film_collection['Year'].astype(str)
)

# Convert features to numerical vectors
vector_creator = TfidfVectorizer(stop_words='english')
feature_vectors = vector_creator.fit_transform(film_collection['feature_string'])

# Calculate similarity between all movies
similarity_grid = linear_kernel(feature_vectors, feature_vectors)

def find_comparable_films(target_film, similarity_data=similarity_grid):
    """Find 3 most similar films based on features"""
    try:
        # Locate the target film
        film_index = film_collection[film_collection['Film'] == target_film].index[0]
        
        # Get similarity scores for all films
        similarity_scores = list(enumerate(similarity_data[film_index]))
        
        # Sort films by similarity
        similarity_scores = sorted(similarity_scores, key=lambda x: x[1], reverse=True)
        
        # Get top 3 similar films (skip the first which is itself)
        similar_films = similarity_scores[1:4]
        similar_indices = [film[0] for film in similar_films]
        
        return film_collection['Film'].iloc[similar_indices].tolist()
    
    except IndexError:
        return ["Film not found in our database"]

# Example 1: Get films by genre
selected_genre = 'Comedy'
genre_based_selection = film_collection[
    film_collection['Genre'].str.contains(selected_genre, case=False)
]['Film'].tolist()

print(f"Top {selected_genre} films:")
for i, film in enumerate(genre_based_selection[:5], 1):
    print(f"{i}. {film}")

# Example 2: Get similar films
example_film = 'Twilight'
print(f"\nFilms similar to '{example_film}':")
for i, similar_film in enumerate(find_comparable_films(example_film), 1):
    print(f"{i}. {similar_film}")
