# Prompting_assignment
implementing all types of prompting techniques for extracting data from image.
## Project Overview
The project consists of ** different prompt experiments **:
1. **Text Generation Experiments**
   - One shot prompt technique
   - few shot prompt technique
   - Role prompting technique
   - context prompt technique
   - step back prompt technique
   - Chain of thought technique
   - Self consistency technique
   - tree of thought technique

---
##  Tech Stack
- **Language:** Python 3.10+
- **LLM:** Google Gemini
- **SDK:** `google-genai`
- **Environment Management:** `python-dotenv`
---
##  Installation
1. Clone the repository
    ```bash
        git clone https://github.com/hemant-crossml/Prompting_assignment.git
        cd Prompting_assignment
2. Create and activate a virtual environment (recommended)
    ```bash
        python -m venv venv
        source venv/bin/activate
3. Install dependencies
    ```bash
        pip install google-genai python-dotenv
4.  Set up your GEMINI_API_KEY:
    
    Create a file named .env in the root directory of this project. Add the following line to the .env file, replacing YOUR_API_KEY with your actual Gemini API key:
      
        GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
        client = genai.Client(api_key=api_key)
## ▶️ Usage

### 5.1 Text Generation Experiment

This script demonstrates how different **prompt engineering techniques** and **generation parameters** influence the text produced by the Gemini model. By modifying prompts and tuning generation settings, users can observe variations in creativity, coherence, and factual consistency.

```bash
    'python main.py'
```
#### Prompts Used
- All prompts are defined in `prompts.py`
- Prompts should be used **one at a time** to analyze and compare the generated outputs

#### Parameters Tuned
- `temperature`
- `top_p`
- `top_k`
- `max_output_tokens`

       
## Learning Outcomes
  -  Understand the impact of temperature on creativity
  -  Compare top_p vs top_k sampling
  -  Build intuition for prompt engineering
  -  Analyse different prompting technique with output
