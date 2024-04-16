from fastapi import FastAPI

#App instance from FastAPI
app = FastAPI()

#Route to the home
@app.get('/')
def home():
    return {'message': "Hello World"}