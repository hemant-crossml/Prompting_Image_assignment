"""
cred.py
--------
This file is responsible for loading and validating
all sensitive credentials (API keys).

Best Practice:
- Credentials are NOT hardcoded
- Values are loaded from environment variables
"""

import os

from dotenv import load_dotenv

# Load variables from .env file into environment
load_dotenv()

# Read Gemini API key from environment
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY",default=str)

# Validate API key existence
if not GEMINI_API_KEY:
    raise EnvironmentError("GEMINI_API_KEY not found in .env file")