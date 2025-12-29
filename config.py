from google.genai import types

from prompts import system_prompt


# Model Configration
MODEL_NAME="gemini-2.5-flash"

#Generation configuration with System_instruction 
CONFIG=types.GenerateContentConfig(
    system_instruction= system_prompt,
    temperature=0.2,
    top_p=0.5,
    top_k=10,
    max_output_tokens=3000
)
