from django.db.models.signals import post_delete
from fastapi import FastAPI,Response

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