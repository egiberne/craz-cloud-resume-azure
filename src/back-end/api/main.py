# import fastapi library
from fastapi import FastAPI, Request

# create a fastapi instance
app = FastAPI()

# create a path operation aka endpoint or route 
@app.get("/")
# create a endpoint function
def root():
    # return text
    return "Hey there! This is Emerick Giberne's Cloud Resumer Challenge"

# GET request : create a endpoint called, health
@app.get("/health")
# endpoint return message status
def get_health():
    # return jason
    return{"status":"Ok"}
