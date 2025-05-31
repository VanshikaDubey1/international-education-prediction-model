# International Education System Cost Predictor

This web application predicts education costs for international students based on various factors such as country, degree type, and duration of study.

## Features

- Predicts tuition costs based on country and degree type
- Calculates living expenses
- Provides total cost estimation for the entire duration of study
- Simple and intuitive user interface

## Technologies Used

- Frontend: HTML, CSS, JavaScript
- Backend: Python (Flask)
- CORS support for cross-origin requests

## Setup Instructions

1. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Start the backend server:
   ```bash
   python app.py
   ```
   The backend will run on http://localhost:5000

3. Start the frontend server:
   ```bash
   python -m http.server 8000
   ```
   Access the application at http://localhost:8000/education.html

## Project Structure

- `app.py` - Flask backend server with prediction logic
- `education.html` - Frontend HTML interface
- `education.css` - Styling for the frontend
- `script.js` - Frontend JavaScript for form handling and API calls
- `requirements.txt` - Python dependencies

## API Endpoints

### POST /predict
Accepts JSON data with the following fields:
- `country`: String (e.g., "USA", "UK", "Canada")
- `degree`: String ("bachelors", "masters", "phd")
- `field`: String (optional)
- `duration`: Number (years of study)

Returns:
```json
{
    "tuition": float,
    "living": float,
    "total": float
}
``` 