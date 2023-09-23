import os

import openai 

from fastapi import FastAPI


openai.api_key = os.getenv("OPENAI_API_KEY")

chat_completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "Hello world"}])


app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}
