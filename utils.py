"""
utils.py
--------
This file contains utility/helper functions
used across the project to avoid code duplication.
"""

import time


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
