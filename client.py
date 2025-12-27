"""
Summary:
    Imports the Google GenAI SDK and initializes a Gemini client using an API key
    stored in a separate credentials module.

Args:
    GEMINI_API_KEY (str): Gemini API key imported from `cred`. This key is used to
        authenticate requests made through the GenAI client.

Returns:
    genai.Client: An initialized Gemini client instance authenticated with the
    provided API key.
"""

from google import genai

from cred import GEMINI_API_KEY

# Initialize Gemini client with secure API key
Client=genai.Client(api_key=GEMINI_API_KEY)