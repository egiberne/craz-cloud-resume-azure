# import fastapi library
from fastapi import FastAPI

# create a fastapi application
app = FastAPI()

# create a endpoint called /health
@app.get("/health")

# endpoint return message status
def health():
    return{"status":"ok"}