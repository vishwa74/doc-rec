import pandas as pd

# Sample data for dermatologists
dermatologists_data = pd.read_csv('doctordata.csv')

# User input: Assumed skin disease and location
user_skin_disease = "Acne"  # Assumed skin disease
user_location = "Chennai"  # User's location

# Filter dermatologists by the assumed skin disease
dermatologists_with_skin_disease = dermatologists_data[dermatologists_data['Specialization'] == user_skin_disease]

# Filter dermatologists by location
dermatologists_in_user_location = dermatologists_with_skin_disease[dermatologists_with_skin_disease['Location'] == user_location]

# Sort dermatologists by patient rating
recommended_dermatologists = dermatologists_in_user_location.sort_values(by='Patient_Rating', ascending=False)

# Display recommended dermatologists
print(recommended_dermatologists[['Name', 'Specialization', 'Location', 'Patient_Rating']])
