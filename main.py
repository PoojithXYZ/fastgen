from fastapi import FastAPI
# import base64
import os
from google import genai
# from google.genai import types
from google.genai.types import Content, Part, GenerateContentConfig, ThinkingConfig

import dotenv
dotenv.load_dotenv()

app = FastAPI()

@app.get("/")
def root_controller():
    return {"status": "u are @ fastgen root page"}

@app.get("/chat")
def generate(prompt: str = "How are you?"):
    try:
        api_key = os.environ["GEMINI_API_KEY"]
    except KeyError:
        raise ValueError(
            "GEMINI_API_KEY environment variable not found. "
            "Please set the environment variable to your key before running."
        )

    client = genai.Client(api_key=api_key)

    model = "gemini-2.5-flash"
    contents = Content(
            role="user",
            parts=[
                Part.from_text(text=prompt),
            ],
        )
    
    generate_content_config = GenerateContentConfig(
        thinking_config = ThinkingConfig(thinking_budget=1000)
    )

    op = []

    for chunk in client.models.generate_content_stream(
        model=model,
        contents=contents,
        config=generate_content_config,
    ):
        op.append(chunk.text)
    
    return {"output": ''.join(op), 'arr':op}

