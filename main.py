from fastapi.responses import PlainTextResponse,HTMLResponse,JSONResponse
from fastapi.exceptions import HTTPException
from fastapi import FastAPI,status
app=FastAPI()

users=[
  {
    "id": 1,
    "name": "Abir",
    "age": 24,
    "is_student": True,
    "skills": ["Python", "FastAPI", "Django"],
    "address": {
      "city": "Dhaka",
      "country": "Bangladesh"
    }
  },
  {
    "id": 2,
    "name": "Rahim",
    "age": 25,
    "is_student": False,
    "skills": ["JavaScript", "React", "Node.js"],
    "address": {
      "city": "Chittagong",
      "country": "Bangladesh"
    }
  },
  {
    "id": 3,
    "name": "Karim",
    "age": 23,
    "is_student": True,
    "skills": ["C++", "Python", "SQL"],
    "address": {
      "city": "Rajshahi",
      "country": "Bangladesh"
    }
  }
]

@app.get('/')
async def home():
    return {'message':'Fastapi is running'}

@app.get('/name')
async def user(name:str):
    return (f'Hello {name}')

""" @app.get('/users')
async def get_users():
    return users """

@app.post('/string_response')
async def submit_name(name:str):
    return ({'message':f"Your name has been submitted {name}"})


@app.post('/number_response')
async def number_response(number:int):
    return number


numbers=[10,20,30,40]

@app.get('/list_response')
async def list_response():
    return numbers

@app.post('/boolean_response')
async def boolean_response(number:int):
    if number>=18:
        return True
    else: return False

@app.get('/nested_json_response')
async def nested_json_response():
    return users


@app.post('/plain_text_response')
async def plain_text_response(number:int):
    if number>=18:
        return PlainTextResponse('You are eligible')
    else: return PlainTextResponse('You are not eligible')

@app.get('/html_response')
async def html_response():
    return HTMLResponse('<h1>Hello Abir</h1>')

@app.get('/json_response')
async def json_response():
    return JSONResponse({'message':'successful','status':status.HTTP_200_OK})

@app.get('/http_exception')
async def json_response():
    return HTTPException(status_code=404)