import os
import json
import re
from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables from .env
load_dotenv()

app = Flask(__name__)
# Enable CORS globally for all routes
CORS(app)

# Configure the Gemini API Key
api_key = os.getenv("GEMINI_API_KEY")
if api_key:
    genai.configure(api_key=api_key)
else:
    print("WARNING: GEMINI_API_KEY not found in environment variables.")

def clean_gemini_response(text):
    text = re.sub(r'```json\s*', '', text)
    text = re.sub(r'```\s*', '', text)
    text = text.strip()
    start = text.find('{')
    end = text.rfind('}')
    if start != -1 and end != -1:
        text = text[start:end+1]
    return text

@app.route('/analyze', methods=['POST'])
def analyze():
    # Accepts JSON body with fields: scenario (string) and disaster_type (string)
    data = request.get_json(silent=True) or {}
    scenario = data.get("scenario", "")
    disaster_type = data.get("disaster_type", "")

    if not scenario:
        return jsonify({"error": "Scenario is required"}), 400

    # Setup the prompt to send to Gemini
    prompt = f"""You are a disaster response AI assistant for India. Given the following disaster scenario, return ONLY a valid JSON object with no additional text, no markdown, no code blocks, no backticks. Just raw JSON.

Scenario: {scenario}
Disaster Type: {disaster_type}

Return this exact JSON:
{{
  "incident_location": {{ "lat": float, "lng": float }},
  "severity_title": "e.g. CRITICAL DISASTER ALERT — Flood in Assam",
  "severity_level": "RED or ORANGE or YELLOW",
  "population_affected": integer,
  "estimated_response_time": "e.g. 48-72 hours",
  "resources": [ {{ "type": string, "quantity": integer, "unit": string }} ],
  "ndma_phases": {{
    "immediate": ["action 1", "action 2", "action 3"],
    "short_term": ["action 1", "action 2", "action 3"],
    "recovery": ["action 1", "action 2"]
  }},
  "situation_report": "2 paragraph official sitrep",
  "emergency_contacts": [ {{ "name": string, "number": string, "category": string }} ],
  "map_pins": [ {{ "lat": float, "lng": float, "label": string, "color": "hex like #ff4444" }} ]
}}

Use real Indian district names, real agency names like NDRF and SDMA, realistic numbers. severity_level must be exactly RED, ORANGE, or YELLOW. Return ONLY the JSON."""

    try:
        # Call Gemini API using google-generativeai package with gemini-1.5-flash model
        model = genai.GenerativeModel("gemini-3.6-flash")
        response = model.generate_content(prompt)
        raw_text = response.text
        cleaned = clean_gemini_response(raw_text)
        result = json.loads(cleaned)
        return jsonify(result)

    except Exception as e:
        print(f"Raw Gemini response: {raw_text if 'raw_text' in locals() else 'No response received'}")
        print(f"Error: {e}")
        return jsonify({'error': 'Failed to parse AI response'}), 500

if __name__ == '__main__':
    # Run on port 5000
    app.run(host='127.0.0.1', port=5000, debug=True)
