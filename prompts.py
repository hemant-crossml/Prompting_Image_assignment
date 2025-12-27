from PIL import Image


form_image=Image.open("Form.jpg")

System_Prompt="""
You  are a Image analyst.
Your work is to anlyse the image and extract the important details from the image and in a clean format
"""

User_Prompt="I have a give you a form image abd I want you to extract all the details from the image. "