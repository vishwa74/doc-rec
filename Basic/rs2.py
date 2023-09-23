import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

# Sample data for dermatologists and skin diseases
dermatologists_data = pd.DataFrame({
    'Dermatologist_ID': [1, 2, 3],
    'Name': ['Dr. Smith', 'Dr. Johnson', 'Dr. Brown'],
    'Specialization': ['Acne', 'Eczema', 'Psoriasis'],
    'Location': ['New York', 'Los Angeles', 'Chicago'],
    'Patient_Rating': [4.8, 4.5, 4.7]
})

skin_diseases_data = pd.DataFrame({
    'Skin_Disease_ID': [101, 102, 103],
    'Name': ['Acne', 'Eczema', 'Psoriasis'],
    'Symptoms': ['Pimples, blackheads, oily skin', 'Itchy, red patches', 'Thick, scaly skin'],
    'Treatments': ['Topical creams', 'Corticosteroids', 'Immunosuppressants']
})

# Input from the user describing their skin disease
user_input_symptoms = "Pimples, blackheads, oily skin"

# Calculate TF-IDF vectors for dermatologists' specializations
tfidf_vectorizer = TfidfVectorizer()
dermatologists_data['Specialization'] = dermatologists_data['Specialization'].fillna('')
tfidf_matrix = tfidf_vectorizer.fit_transform(dermatologists_data['Specialization'])

# Calculate cosine similarity between user input and dermatologists' specializations
cosine_similarities = linear_kernel(tfidf_vectorizer.transform([user_input_symptoms]), tfidf_matrix)

# Get the top recommended dermatologists
dermatologists_data['Cosine_Similarity'] = cosine_similarities[0]
recommended_dermatologists = dermatologists_data.sort_values(by='Cosine_Similarity', ascending=False)

# Display recommended dermatologists
print(recommended_dermatologists[['Name', 'Specialization', 'Location', 'Patient_Rating']])
