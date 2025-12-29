"""
Gemini Client Initialization Module

This module initializes the Google Gemini client using a securely stored
API key imported from the credentials file. The client object can be reused
across the application to make requests to the Gemini API.
"""

from google import genai

from cred import GEMINI_API_KEY

# Initialize Gemini client with secure API key
client=genai.Client(api_key=GEMINI_API_KEY)