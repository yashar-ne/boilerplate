from fastapi import FastAPI

print('Starting Server...')
app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}