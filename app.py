from flask import Flask, request, jsonify
import pickle
import numpy as np

# Initialize Flask app
app = Flask(__name__)

# Load trained model and scaler
with open('gb_model.pkl', 'rb') as f:
    model = pickle.load(f)

with open('scaler.pkl', 'rb') as f:
    scaler = pickle.load(f)

# User input features
input_features = [
    'Age', 'Diabetes', 'BloodPressureProblems', 'AnyTransplants', 'AnyChronicDiseases',
    'Height', 'Weight', 'KnownAllergies', 'HistoryOfCancerInFamily', 'NumberOfMajorSurgeries'
]

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json(force=True)

        # Check for all required fields
        if not all(feature in data for feature in input_features):
            return jsonify({'error': 'Missing one or more required input fields.'}), 400

        # Extract values
        Age = data['Age']
        Diabetes = data['Diabetes']
        BloodPressureProblems = data['BloodPressureProblems']
        AnyTransplants = data['AnyTransplants']
        AnyChronicDiseases = data['AnyChronicDiseases']
        Height = data['Height']
        Weight = data['Weight']
        KnownAllergies = data['KnownAllergies']
        HistoryOfCancerInFamily = data['HistoryOfCancerInFamily']
        NumberOfMajorSurgeries = data['NumberOfMajorSurgeries']

        # Derived / Imputed features
        BMI = Weight / ((Height / 100) ** 2)
        MultipleSurgeries = 1 if NumberOfMajorSurgeries > 2 else 0
        OtherHealthConditions = Diabetes + BloodPressureProblems + KnownAllergies + HistoryOfCancerInFamily

        # Categorical features from rules
        AgeGroup_Senior = 1 if Age >= 50 else 0
        AgeGroup_Young = 1 if Age < 30 else 0
        BMIGroup_Obese = 1 if BMI >= 30 else 0
        BMIGroup_Overweight = 1 if 25 <= BMI < 30 else 0
        BMIGroup_Underweight = 1 if BMI < 18.5 else 0

        # Final feature list in model order
        final_features = [
            Age, AnyTransplants, AnyChronicDiseases, BMI,
            MultipleSurgeries, OtherHealthConditions,
            AgeGroup_Senior, AgeGroup_Young, BMIGroup_Obese, BMIGroup_Overweight, BMIGroup_Underweight
        ]

        # Scale features
        input_array = np.array(final_features).reshape(1, -1)
        scaled_input = scaler.transform(input_array)

        # Predict
        prediction = model.predict(scaled_input)

        return jsonify({'predicted_premium': prediction[0]})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
