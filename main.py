"""
main.py
-------
Application entry point for the LLM text generation project.

This module orchestrates the overall flow by:
- Loading the Gemini client
- Importing model configuration and prompts
- Triggering the text generation process
"""

from client import Client
from config import CONFIG, MODEL_NAME
from prompts import System_Prompt, User_Prompt, form_image
from text_generator import generate_text

def main():
    """
    Main execution function of the application.

    Calls the text generation pipeline by passing
    the client, model configuration, system prompt,
    user prompt, and generation parameters.
    """
    generate_text(Client, MODEL_NAME, System_Prompt, User_Prompt, form_image, CONFIG)


# Ensures the main function runs only when this file
# is executed directly, not when imported as a module
if __name__ == "__main__":
    main()
