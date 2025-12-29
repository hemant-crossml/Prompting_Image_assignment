"""
main.py
-------
Application entry point for the LLM text generation project.

This module orchestrates the overall flow by:
- Loading the Gemini client
- Importing model configuration and prompts
- Triggering the text generation process
"""

from client import client
from config import CONFIG, MODEL_NAME
from prompts import system_prompt, user_prompt, form_image
from text_generator import generate_text

def main():
    """
    Summary:
        This is the main entry point script for the Gemini AI text generation application. 
        It orchestrates the text generation process by importing required components (client, 
        configuration, prompts, and generator) and executes the core generation workflow 
        through a protected main function that runs only when the script is directly executed.

    Args:
        None: this function has no argument


    Return:
        None: this  return none
    """
    generate_text(client, MODEL_NAME, system_prompt, user_prompt, form_image, CONFIG)


# Ensures the main function runs only when this file
# is executed directly, not when imported as a module
if __name__ == "__main__":
    main()
