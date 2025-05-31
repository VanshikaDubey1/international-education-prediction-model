from flask import Flask, request, jsonify
from flask_cors import CORS
import numpy as np

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Mock prediction function - replace with your actual ML model
def predict_costs(data):
    # This is a simple mock prediction
    # Replace this with your actual ML model predictions
    base_tuition = {
        'bachelors': 15000,
        'masters': 25000,
        'phd': 20000
    }
    
    country_multiplier = {
        'usa': 1.5,
        'uk': 1.3,
        'canada': 1.2,
        'australia': 1.4
    }
    
    # Get base tuition based on degree
    tuition = base_tuition.get(data['degree'].lower(), 20000)
    
    # Apply country multiplier
    country = data['country'].lower()
    multiplier = country_multiplier.get(country, 1.0)
    tuition *= multiplier
    
    # Calculate living expenses (simple estimation)
    living = tuition * 0.4
    
    # Adjust for duration
    total_years = float(data['duration'])
    total = (tuition + living) * total_years
    
    return {
        'tuition': round(tuition, 2),
        'living': round(living, 2),
        'total': round(total, 2)
    }

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        
        # Validate required fields
        required_fields = ['country', 'degree', 'duration']
        for field in required_fields:
            if field not in data:
                return jsonify({'error': f'Missing required field: {field}'}), 400
        
        # Make prediction
        result = predict_costs(data)
        return jsonify(result)
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000) 