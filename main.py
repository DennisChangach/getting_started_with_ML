#importing libs
import uvicorn
from fastapi import FastAPI

#creating the App Object
app = FastAPI()

#index route: Opens automaticaly on http://126.0.0.1:8000
@app.get('/')
def index():
    return {'message':'Hello, World'}

# 4. Route with a single parameter, returns the parameter within a message
#    Located at: http://127.0.0.1:8000/AnyNameHere
@app.get('/Welcome')
def get_name(name:str): #expects a string as an input stored in name variable
    return {'Welcome to my Data Science Podcast': f'{name}'}


"""
#Running the API with uvicorn
if __name__ == '__main__':
    uvicorn.run(app,host='127.0.0.1',port=8000)

#Run with: uvicorn main:app --reload
"""