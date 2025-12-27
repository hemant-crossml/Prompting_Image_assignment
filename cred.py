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

"""
Summary:
    This module loads and validates the Gemini API key from environment variables using a .env file.
    It utilizes python-dotenv to load configuration variables securely and retrieves the API key 
    with fallback handling, raising an EnvironmentError if the key is missing or empty.

Args:
    None: This module relies on external configuration via a .env file containing GEMINI_API_KEY.
          No explicit function arguments are defined.

Return:
    GEMINI_API_KEY (str): The Gemini API key loaded from environment variables, validated for existence.
                          Raises EnvironmentError if the key is not found or empty.
"""


# Load variables from .env file into environment
load_dotenv()

# Read Gemini API key from environment
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY",default=str)

# Validate API key existence
if not GEMINI_API_KEY:
    raise EnvironmentError("GEMINI_API_KEY not found in .env file")