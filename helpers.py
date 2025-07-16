import os
import openai
import google.generativeai as genai
from textblob import TextBlob
from dotenv import load_dotenv
import google.api_core.exceptions
import concurrent.futures

load_dotenv()

# Load API keys
openai.api_key = os.getenv("OPENAI_API_KEY")
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# --- Sentiment Detection ---
def detect_sentiment(message):
    blob = TextBlob(message)
    polarity = blob.sentiment.polarity
    if polarity > 0.2:
        return "You sound happy!"
    elif polarity < -0.2:
        return "I'm sensing you're a bit down. Want to talk about it?"
    else:
        return "Hmm, you sound neutral. Let me know how I can help!"

# --- Rule-based fallback ---
def rule_based_reply(message):
    message = message.lower()
    if "hello" in message:
        return "Hi there! 😊"
    elif "bye" in message:
        return "Goodbye! Take care! 👋"
    elif "name" in message:
        return "I'm ChatMind, your virtual buddy!"
    else:
        return None

# --- OpenAI GPT response ---
def get_gpt_response(message):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": message}
            ]
        )
        return response["choices"][0]["message"]["content"]
    except Exception as e:
        # If OpenAI fails, fall back to Gemini
        print("OpenAI failed, using Gemini:", str(e))
        return get_gemini_response(message)

# --- Gemini response ---
import google.generativeai as genai

def get_gemini_response(message):
    try:
        model = genai.GenerativeModel("models/gemini-1.5-flash-latest")
        response = model.generate_content(message)
        return response.text
    except Exception as e:
        return f"Gemini Error: {str(e)}"