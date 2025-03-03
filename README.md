# JokeBot

A fun Flask-based web application that generates random jokes using Google's Gemini AI API.

## Live Demo
[https://jokebot-iota.vercel.app/](https://jokebot-iota.vercel.app/)

## Features
- Generates random jokes based on different themes
- Simple and responsive UI using Bootstrap
- Dark mode and light mode support
- Deployed on Vercel

## Tech Stack
- Python (Flask)
- HTML, CSS, JavaScript
- Bootstrap
- Google Gemini AI API
- Vercel (for deployment)

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/jokebot.git
   cd jokebot
   ```
2. Create a virtual environment:
   ```sh
   python -m venv venv
   source venv/bin/activate   # On Windows use: venv\\Scripts\\activate
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
4. Set up the environment variables:
   - Create a `.env` file in the root directory and add:
   ```sh
   GEMINI_API_KEY=your_api_key_here
   ```
5. Run the Flask app:
   ```sh
   python app.py
   ```
6. Open your browser and go to `http://127.0.0.1:5000/`

## Deployment
- The app is deployed using Vercel.
- Ensure you have a `vercel.json` file configured for deployment.
- Install Vercel CLI and run:
  ```sh
  vercel
  ```

## Directory Structure
```
.vercel/
.env
app.py
index.html
README.md
requirements.txt
style.css
vercel.json
```

## License
This project is licensed under the MIT License.

## Author
[GIRISH R V](https://github.com/GIRISHRV)
