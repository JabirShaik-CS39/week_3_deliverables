# GET ENDPOINT

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Home Page"}

@app.get("/about")
def about():
    return {"message": "About Page"}

@app.get("/contact")
def contact():
    return {"message": "Contact Page"}