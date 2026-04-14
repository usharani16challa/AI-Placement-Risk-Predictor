from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle
import numpy as np
import os

app = Flask(__name__)
CORS(app)  # Enable CORS

# ✅ Load model safely
model_path = os.path.join(os.path.dirname(__file__), 'model.pkl')

with open(model_path, 'rb') as f:
    model = pickle.load(f)

# ✅ Home route
@app.route('/')
def home():
    return "API Running Successfully"

# ✅ Prediction route
@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()

        cgpa = float(data['cgpa'])
        internship = int(data['internship'])
        college_tier = int(data['college_tier'])

        # Convert to array
        features = np.array([[cgpa, internship, college_tier]])

        # ML Prediction
        prediction = model.predict(features)[0]

        # Probability (if available)
        try:
            prob = model.predict_proba(features)[0][1]
            prob = round(float(prob) * 100, 2)
        except:
            prob = "N/A"

        # 🔥 SMART REAL-WORLD LOGIC
        if cgpa < 6 and internship == 0:
            result = "High Risk of Unemployment"

        elif cgpa >= 8 and internship == 1:
            result = "High Chance of Placement"

        elif cgpa >= 8 and internship == 0:
            result = "Moderate Chance (Internship Recommended)"

        elif cgpa >= 6:
            result = "Moderate Chance of Placement"

        else:
            result = "Low Chance of Placement"

        # 💡 Suggestions (NEW FEATURE 🔥)
        suggestions = []

        if internship == 0:
            suggestions.append("Complete at least one internship")

        if cgpa < 7:
            suggestions.append("Improve academic performance")

        if college_tier == 3:
            suggestions.append("Build strong projects and skills")

        if not suggestions:
            suggestions.append("Keep improving skills and apply for jobs")

        return jsonify({
            "prediction": result,
            "probability": prob,
            "suggestions": suggestions
        })

    except Exception as e:
        print("Error:", e)
        return jsonify({
            "error": str(e)
        })

# ✅ Run server
if __name__ == "__main__":
    app.run(debug=True)