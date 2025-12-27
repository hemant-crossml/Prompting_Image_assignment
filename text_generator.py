from typing import Optional, Union

from PIL import Image
from google.genai import types

from utils import print_output, retry_delay

ImageType=Union[Image.Image, types.Part]

def generate_text(client, model_name: str, System_prompt: str,User_prompt: str,Image: Optional[ImageType], config: Optional[dict] = None,)-> Optional[str]:
   
    
    try:
        # Send the user prompt to the Gemini model for text generation
        response = client.models.generate_content(
            model=model_name,  
            contents=[Image,User_prompt],
            config=config
        )
        # Print formatted output including prompts and model response
        print_output(System_prompt,User_prompt, response.text)

    except Exception as e:
        # Handle runtime or API-related errors gracefully
        print("Error occurred:", e)

        # Apply a delay before retrying or exiting
        retry_delay()
