"""
utils.py
--------
This file contains utility/helper functions
used across the project to avoid code duplication.
"""

import time


def print_output(system_prompt:str, user_prompt:str, output:any):
    """
    Formats and prints prompt-output pairs
    for better readability.
    """
    print("\n" + "-" * 60)
    print("PROMPT:")
    print(system_prompt,"\n",user_prompt)
    print("\nOUTPUT:")
    print(output)
    print("-" * 60)

def retry_delay(seconds=2):
    """
    Introduces delay before retrying a failed request.
    """
    time.sleep(seconds)
