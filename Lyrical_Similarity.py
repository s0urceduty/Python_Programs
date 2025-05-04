import nltk
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

# Sample lyrics
lyrics = [
    "I want to hold your hand",
    "Let it be, let it be, let it be, let it be",
    "Hey Jude, don't make it bad",
    "I wanna rock and roll all night",
    "I can't get no satisfaction",
]

# Preprocess and tokenize the lyrics
nltk.download("punkt")
nltk.download("stopwords")
stop_words = set(stopwords.words("english"))

def preprocess_text(text):
    words = nltk.word_tokenize(text)
    words = [word.lower() for word in words if word.isalnum()]
    words = [word for word in words if word not in stop_words]
    return " ".join(words)

preprocessed_lyrics = [preprocess_text(lyric) for lyric in lyrics]

# Calculate TF-IDF vectors for the lyrics
tfidf_vectorizer = TfidfVectorizer()
tfidf_matrix = tfidf_vectorizer.fit_transform(preprocessed_lyrics)

# Calculate cosine similarity between lyrics
cosine_similarities = linear_kernel(tfidf_matrix, tfidf_matrix)

# Find similar lyrics
def find_similar_lyrics(query, lyrics, tfidf_vectorizer, cosine_similarities, top_n=5):
    query = preprocess_text(query)
    query_vector = tfidf_vectorizer.transform([query])
    similarity_scores = cosine_similarities.dot(query_vector.T).toarray().ravel()
    top_indices = similarity_scores.argsort()[::-1][:top_n]
    similar_lyrics = [(lyrics[i], similarity_scores[i]) for i in top_indices]
    return similar_lyrics

# Example usage
query_lyrics = "Let it be"
similar_lyrics = find_similar_lyrics(query_lyrics, lyrics, tfidf_vectorizer, cosine_similarities)

print("Lyrics similar to:", query_lyrics)
for lyric, similarity in similar_lyrics:
    print(f"Similarity: {similarity:.2f}, Lyrics: {lyric}")
