import google.generativeai as genai
import os
from dotenv import load_dotenv

# 1. Load environment variables from .env file
load_dotenv()

# 2. Configure the Gemini API with the key from the environment variable
try:
    # Use os.getenv() for robust access, it returns None if not found,
    # avoiding a KeyError, then we can check for None.
    gemini_api_key = os.getenv("GEMINI_API_KEY")
    if gemini_api_key is None:
        raise ValueError("GEMINI_API_KEY not found in environment variables. Make sure your .env file is correct and loaded.")

    genai.configure(api_key=gemini_api_key)
    print("Gemini API configured successfully.")

except Exception as e:
    print(f"Error configuring Gemini API: {e}")
    print("Please ensure your .env file is in the same directory as this script and contains 'GEMINI_API_KEY=YOUR_KEY'.")
    exit() # Exit the script if configuration fails

# --- Rest of your Gemini API interaction code ---

# Example: List available models
print("\nAvailable Gemini Models supporting generateContent:")
for m in genai.list_models():
    if 'generateContent' in m.supported_generation_methods:
        print(f"  - {m.name} (Display: {m.display_name})")

# Example: Use a supported model (e.g., 'gemini-1.5-flash' or 'gemini-1.5-pro')
# Replace with a model name you found from the list above that supports 'generateContent'
# 'gemini-1.5-flash' is often a good default for general use.
try:
    model_name = "gemini-1.5-flash" # Or "gemini-1.5-pro", etc.
    model = genai.GenerativeModel(model_name)
    print(f"\nUsing model: {model_name}")

    # Generate content
    prompt = "Tell me a short, interesting fact about the universe."
    print(f"Prompt: {prompt}")
    response = model.generate_content(prompt)
    print("\nResponse:")
    print(response.text)

except Exception as e:
    print(f"\nError interacting with Gemini API: {e}")
    print("Ensure the model name used is valid and you have access to it.")