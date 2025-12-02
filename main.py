from fastapi import FastAPI
from starlette.responses import StreamingResponse
from pydantic import BaseModel

app = FastAPI()

@app.get("/hello")
def hello():
    return {"message": "Hello FastAPI!"}

@app.post("/query")
def query(message:str):
    # pip install openai
    from openai import OpenAI  # openai==1.52.2

    client = OpenAI(
        api_key="up_CQlRUTuZcA4l3YwnD7g9dAdT74hXw",
        base_url="https://api.upstage.ai/v1"
    )
    response = client.embeddings.create(
        input=message,
        model="embedding-query"
    )

    print(response.data[0].embedding)

def upstage_chat(message):
    from openai import OpenAI  # openai==1.52.2

    client = OpenAI(
        api_key="up_CQlRUTuZcA4l3YwnD7g9dAdT74hXw",
        base_url="https://api.upstage.ai/v1"
    )
    stream = client.chat.completions.create(
        model="solar-pro2",
        messages=[
            {
                "role": "user",
                "content": message
            }
        ],
        stream=True,
    )

    for chunk in stream:
        if chunk.choices[0].delta.content is not None:
            yield chunk.choices[0].delta.content

class ChatRequest(BaseModel):
    prompt: str

@app.post("/chat")
def query(message: ChatRequest):
    return StreamingResponse(
        upstage_chat(message.prompt),
        media_type="text/plain; charset=utf-8"
    )
    # Use with stream=False
    # print(stream.choices[0].message.content)