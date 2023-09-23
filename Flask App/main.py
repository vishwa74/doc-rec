from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

# Sample data for dermatologists
dermatologists_data = pd.read_csv('doctordata.csv')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_skin_disease = request.form['skin_disease']
        user_location = request.form['location']

        # Filter dermatologists by the assumed skin disease
        dermatologists_with_skin_disease = dermatologists_data[dermatologists_data['Specialization'] == user_skin_disease]

        # Filter dermatologists by location
        dermatologists_in_user_location = dermatologists_with_skin_disease[dermatologists_with_skin_disease['Location'] == user_location]

        # Sort dermatologists by patient rating
        recommended_dermatologists = dermatologists_in_user_location.sort_values(by='Patient_Rating', ascending=False)

        return render_template('index.html', recommendations=recommended_dermatologists.to_html(classes='table table-striped'))

    return render_template('index.html', recommendations=None)

if __name__ == '__main__':
    app.run(debug=True)
