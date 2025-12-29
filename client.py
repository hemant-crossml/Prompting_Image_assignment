from google import genai

from cred import GEMINI_API_KEY

# Initialize Gemini client with secure API key
client=genai.Client(api_key=GEMINI_API_KEY)