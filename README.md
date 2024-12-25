# Movie_Recommendation_System
 Requirements: Python, ﻿streamlit, request etc
## Goal : 

This approach implements a content-based movie recommendation system using cosine similarity on text features. The dataset (new_df) contains movie information in a tags column, combining descriptions, genres, and keywords.

Steps:
Preprocessing:

Text is cleaned using stemming with PorterStemmer, reducing words to their root forms (e.g., "allowing" → "allow"). Stop words are removed for efficiency.
CountVectorizer converts tags into numerical vectors with a maximum of 5000 features, creating a sparse matrix.
Similarity Calculation:

Cosine similarity computes pairwise similarity between movies, resulting in a matrix where higher values indicate greater similarity.
Recommendations:

For a given movie, the system identifies its index, retrieves similarity scores, and ranks the top 5 most similar movies.
Serialization:

Using pickle, the processed dataset, similarity matrix, and dictionary representation of the data are saved for reuse.
