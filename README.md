# JokeBot

JokeBot is a web application that generates family-friendly jokes using the Gemini API. The jokes are displayed on the web page when the user clicks a button.

## Project Description

This project uses the Gemini API to generate jokes. The jokes are displayed on a web page with a button to fetch a new joke. The application supports light and dark themes.

## Setup and Run Instructions

1. **Clone the repository:**
   ```sh
   git clone https://github.com/your-username/jokebot.git
   cd jokebot
   ```

2. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

3. **Set up environment variables:**
   - Create a .env file in the root directory.
   - Add your Gemini API key to the .env file:
     ```
     GEMINI_API_KEY=your_api_key_here
     ```

4. **Run the application:**
   ```sh
   python app.py
   ```

5. **Open the application in your browser:**
   - Go to `http://localhost:5000`

## API Key Configuration

To use the Gemini API, you need to configure your API key. Follow these steps:

1. Sign up for an API key from the Gemini API provider.
2. Create a `.env` file in the root directory of the project.
3. Add your API key to the `.env` file:
   ```
   GEMINI_API_KEY=your_api_key_here
   ```

## Optional Features

- Light and dark theme support.
- Responsive design for mobile devices.
