from flask import Flask, jsonify, request, send_from_directory, render_template_string
from flask_cors import CORS
from dotenv import load_dotenv
import os
import google.generativeai as genai
import random

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__, static_folder='.')
CORS(app)

# Configure the Gemini API client with the API key from the environment variable
api_key = os.environ.get("GEMINI_API_KEY")
if not api_key:
    raise ValueError("No GEMINI_API_KEY found in environment variables")
genai.configure(api_key=api_key)

@app.route('/')
def index():
    return render_template_string(open('index.html').read(), gemini_api_key=api_key)

@app.route('/get-joke', methods=['GET'])
def get_joke():
    joke_styles = [
    "Tell me a joke about animals.",
    "Give me a joke about technology.",
    "Share a joke about food.",
    "Tell a joke about history.",
    "Give me a joke about sports.",
    "Tell me a joke about science.",
    "Share a joke about movies.",
    "Give me a joke about music.",
    "Tell a joke about school life.",
    "Give me a joke about relationships.",
    "Tell me a joke about doctors.",
    "Give me a joke about teachers.",
    "Share a joke about programming.",
    "Tell a joke about robots.",
    "Give me a joke about artificial intelligence.",
    "Tell me a joke about lawyers.",
    "Give me a joke about bankers.",
    "Share a joke about astronauts.",
    "Tell a joke about space exploration.",
    "Give me a joke about time travel.",
    "Tell me a joke about superheroes.",
    "Give me a joke about pirates.",
    "Share a joke about detectives.",
    "Tell a joke about cowboys.",
    "Give me a joke about weddings.",
    "Tell me a joke about vacations.",
    "Give me a joke about airplanes.",
    "Share a joke about the internet.",
    "Tell a joke about social media.",
    "Give me a joke about texting.",
    "Tell me a joke about video games.",
    "Give me a joke about board games.",
    "Share a joke about office work.",
    "Tell a joke about coffee.",
    "Give me a joke about Mondays.",
    "Tell me a joke about New Year's resolutions.",
    "Give me a joke about dieting.",
    "Share a joke about fitness.",
    "Tell a joke about gym workouts.",
    "Give me a joke about parenting.",
    "Tell me a joke about siblings.",
    "Give me a joke about birthdays.",
    "Share a joke about Christmas.",
    "Tell a joke about Halloween.",
    "Give me a joke about shopping.",
    "Tell me a joke about online dating.",
    "Give me a joke about fashion.",
    "Share a joke about celebrities.",
    "Tell a joke about reality TV.",
    "Give me a joke about conspiracy theories."
]

    
    selected_style = random.choice(joke_styles)
    prompt = f"You are a joke-telling AI. {selected_style}"

    print(f"Generated prompt: {prompt}")  # Debug statement
    
    try:
        model = genai.GenerativeModel("gemini-1.5-pro")
        response = model.generate_content(prompt)
        joke = response.text.strip()

        print(f"Generated joke: {joke}")  # Debug statement
        return jsonify({'joke': joke})
    except Exception as e:
        print(f"Error: {str(e)}")  # Debug statement
        return jsonify({'error': str(e)}), 500

@app.route('/<path:path>')
def send_static(path):
    return send_from_directory('.', path)

@app.route('/test')
def test():
    return "App is working!"

if __name__ == '__main__':
    app.run(debug=True)