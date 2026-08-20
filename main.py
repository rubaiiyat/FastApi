from fastapi import FastAPI

app=FastAPI()

@app.get('/')
async def home():
    return {'message':'Fastapi is running'}

@app.get('/name')
async def user(name:str):
    return (f'Hello {name}')