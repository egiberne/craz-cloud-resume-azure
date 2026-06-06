## import fastapi library
from fastapi import FastAPI, Request



## create a fastapi instance
app = FastAPI()


## GET requests

### create an endpoint at the root
@app.get("/")
### define endpoint function  
def root():
### return message text
    return "Hello World, here is a Cloud Resumer Challenge by Emerick Giberne"

## create an endpoint health
@app.get("/health")
### define endpoint function 
def health():
### return jason
    return'"status":"ok"'

## POST Requests

### create an endpoint /echo
@app.post("/echo")
def echo():
    return '"received":"ok"'

## store number of visits per users based on user id
visit_counter={}

# POST Request : create a endpoint called, visit
@app.post("/counter")
def update_counter(request:Request):
    data = request.text
    user_id=data.get("userId")

    if not user_id:
        return "userId is required"
    
    # Increment  visit count
    if user_id in visit_counter :
        visit_counter[user_id] += 1
    else : 
        visit_counter[user_id] = 1

    return visit_counter[user_id]
    
