import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

# Load dataset
film_data = pd.read_csv("C:/Users/HAPPY/Downloads/movies.csv")
film_data = film_data.fillna('')

# Combine attributes into a single string
film_data['movie_attributes'] = (
    film_data['Genre'] + ' ' + 
    film_data['Lead Studio'] + ' ' +
    film_data['Audience score %'].astype(str) + ' ' +
    film_data['Profitability'].astype(str) + ' ' +
    film_data['Rotten Tomatoes %'].astype(str) + ' ' +
    film_data['Worldwide Gross'].astype(str) + ' ' +
    film_data['Year'].astype(str)
)

# Calculate TF-IDF vectors
vectorizer = TfidfVectorizer(stop_words='english')
attribute_vectors = vectorizer.fit_transform(film_data['movie_attributes'])

# Compute similarity scores
similarity_matrix = linear_kernel(attribute_vectors, attribute_vectors)

def find_similar_films(input_title, similarity_scores=similarity_matrix):
    """Returns similar films based on content"""
    try:
        film_index = film_data[film_data['Film'] == input_title].index[0]
        film_similarities = list(enumerate(similarity_scores[film_index]))
        film_similarities = sorted(film_similarities, key=lambda x: x[1], reverse=True)
        similar_indices = [i[0] for i in film_similarities[1:4]]
        return film_data['Film'].iloc[similar_indices]
    except:
        return ["Film not found in database"]

# Example usage
preferred_genre = 'Comedy'
genre_matches = film_data[film_data['Genre'].str.contains(preferred_genre, case=False)]['Film'].tolist()
print(f"Recommended {preferred_genre} films:")
for match in genre_matches[:5]:  # Show top 5
    print(f"- {match}")

sample_film = 'Twilight'
print(f"\nFilms similar to '{sample_film}':")
for similar in find_similar_films(sample_film):
    print(f"- {similar}")
