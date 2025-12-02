from fastapi import FastAPI

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

@app.post("/chat")
def query(message: str):
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
        stream=False,
    )
    return stream.choices[0].message.content

    # Use with stream=False
    # print(stream.choices[0].message.content)