from dotenv import load_dotenv
from fastapi import FastAPI
import sqlalchemy
import uvicorn

load_dotenv()
app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)