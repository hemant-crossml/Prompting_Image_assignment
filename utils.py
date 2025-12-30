"""
utils.py
--------
This file contains utility/helper functions
used across the project to avoid code duplication.
"""

import time
import re
from collections import Counter
from typing import Optional


def print_output(system_prompt:str, user_prompt:str, output:any):
    """
    Summary:
        Prints a formatted block that includes the provided prompts and the model/output
        for easier debugging and readability in the console.

    Args:
        system_prompt (str): The system-level prompt/context to display.
        user_prompt (str): The user prompt/query to display.
        output (any): The generated output/result to display. Can be any printable type.

    Return:
        None
    """
    print("\n" + "-" * 60)
    print("PROMPT:")
    print(system_prompt,"\n",user_prompt)
    print("\nOUTPUT:")
    print(output)
    print("-" * 60)

def retry_delay(seconds=2):
    """
    Summary:
        Pauses execution for a specified amount of time, typically used between retry attempts.

    Args:
        seconds (int | float, optional): Number of seconds to sleep before continuing.
            Defaults to 2.

    Return:
        None
    """
    time.sleep(seconds)

def extract_final_answer(text: str) -> str:
    """
    summary:
        Extract the most likely final numeric answer (typically a monetary/tax/total value) from free-form text
        using a small set of regex patterns. Returns the first match found, normalized by removing commas.

    args:
        text (str): Input text that may contain a final/total/answer/result amount (optionally with a $ sign).

    return:
        str: The extracted numeric value as a string (commas removed), or "No answer extracted" if nothing matches.
    """
    patterns = [
        r'(?:total|final|answer|result|liability|amount|tax)[:\s]*\$?([0-9,]+\.?[0-9]*)',
        r'\$([0-9,]+\.?[0-9]*)',
        r'([0-9,]+\.?[0-9]*)\s*(?:total|dollars|tax)'
    ]
    for pattern in patterns:
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            return match.group(1).replace(',', '').strip()
    return "No answer extracted"



def self_consistent_generate(client, model_name: str, contents: list,config: Optional[dict]=None, n_samples: int = 5) -> str:
    """
    summary:
        Generate multiple independent model outputs for the same prompt, extract a final numeric answer from each,
        and return a consensus answer using majority voting over valid extracted answers.

    args:
        client: LLM client instance that exposes a `models.generate_content(...)` method.
        model_name (str): Model identifier/name to use for generation.
        contents (list): Prompt/messages/content payload passed to the model generation call.
        config (Optional[dict]): Optional generation configuration (e.g., temperature, max tokens).
        n_samples (int): Number of independent generation runs ("paths") to sample for self-consistency voting.

    return:
        str: A formatted string containing either:
             - The consensus answer and vote counts when at least one valid answer is extracted, or
             - A no-consensus message with raw path outcomes when voting is not possible.
    """
    answers = []
    for i in range(n_samples):
        config = config
        try:
            response = client.models.generate_content(
                model=model_name,
                contents=contents,
                config=config
            )
            if response and response.text:  # ← SAFE CHECK
                answer = extract_final_answer(response.text)
                answers.append(answer)
                print(f" Path {i+1}: {answer}")
            else:
                print(f" Path {i+1}: Empty response")
                answers.append("Empty")
        except Exception as e:
            print(f" Path {i+1} failed: {str(e)[:50]}...")
            answers.append("Error")
            retry_delay()
        valid_answers = [a for a in answers if a not in ["Error", "Empty", "No answer extracted"]]
    if valid_answers:
        vote = Counter(valid_answers).most_common(1)[0][0]
        return f" Consensus: {vote}\n Votes: {dict(Counter(valid_answers))}"
    return f" No consensus (raw paths: {dict(Counter(answers))})"