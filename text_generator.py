from typing import Optional, Union

from PIL import Image
from google.genai import types

from utils import print_output, retry_delay


def generate_text(client, model_name: str, system_prompt: str,user_prompt: str,image: Optional[Union[Image.Image, types.Part]], config: Optional[dict] = None,):
   
    """
Summary:
    This module provides a robust text generation function for multimodal Gemini AI processing.
    It handles both text and image inputs (PIL Image or Google GenAI Part), sends them to the 
    specified model with configuration, prints formatted output using utilities, and implements 
    error handling with retry delays for reliable API interactions.

Args:
    client: Initialized Google Generative AI client instance for API communication.
    model_name (str): Name of the Gemini model (e.g., "gemini-2.5-flash") to use for generation.
    System_prompt (str): System instruction defining AI role, guidelines, and output format.
    User_prompt (str): User query or instruction to process with the model.
    Image (Optional[ImageType]): PIL Image or Google GenAI Part for multimodal analysis (tax form).
    config (Optional[dict]): Generation configuration (temperature, top_p, max_tokens, etc.).

Return:
     Returns None; generated text is printed via print_output utility. 
     Raises exceptions are caught and handled with retry_delay mechanism.
"""

    try:
        # Send the user prompt to the Gemini model for text generation
        response = client.models.generate_content(
            model=model_name,  
            contents=[image,user_prompt],
            config=config
        )
        # Print formatted output including prompts and model response
        print_output(system_prompt,user_prompt, response.text)

    except Exception as e:
        # Handle runtime or API-related errors gracefully
        print("Error occurred:", e)

        # Apply a delay before retrying or exiting
        retry_delay()
