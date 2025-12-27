from google.genai import types

from prompts import System_Prompt

"""
Summary:
    This script configures and initializes a content generation model using Google's Generative AI API.
    It imports the necessary modules, sets the model name, and defines generation parameters such as 
    temperature, top_p, top_k, and maximum token limit. The model leverages a predefined system prompt 
    to guide content generation behavior and output style.

Args:
    System_Prompt (str): A predefined system prompt imported from the 'prompts' module. It sets the 
                         behavioral and contextual guidelines for content generation.
    MODEL_NAME (str): The name of the Google Generative AI model being used (e.g., "gemini-2.5-flash").
    CONFIG (types.GenerateContentConfig): A configuration object specifying generation parameters 
                                          including system instruction, randomness, and output limits.

Return:
    None: This script sets up model parameters and configuration but does not return any value directly. 
          The defined CONFIG and MODEL_NAME are typically used in subsequent API calls or generation functions.
"""


# Model Configration
MODEL_NAME="gemini-2.5-flash"

#Generation configuration with System_instruction 
CONFIG=types.GenerateContentConfig(
    system_instruction= System_Prompt,
    temperature=0.2,
    top_p=0.5,
    top_k=10,
    max_output_tokens=3000
)
