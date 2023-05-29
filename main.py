from fastapi import FastAPI 
from fastapi.responses import HTMLResponse, JSONResponse
from pydantic import BaseModel
from config.database import engine, Base
from middlewares.error_handler import ErrorHandler
from routers.movie import movie_router
from routers.user import user_router


app = FastAPI()
app.title = "My app with FastAPI"
app.version = '0.0.1'

app.add_middleware(ErrorHandler)

app.include_router(movie_router)
app.include_router(user_router)

Base.metadata.create_all(bind=engine)
        

movies = [
    {
        'id': 1,
        'title': 'Avatar',
        'overview': "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
        'year': '2009',
        'rating': 7.8,
        'category': 'Accion'    
    }, 
        {
        'id': 2,
        'title': 'Avatar 2',
        'overview': "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
        'year': '2022',
        'rating': 7.8,
        'category': 'Accion'    
    }  
]

@app.get('/', tags=['home'])
def message():
    return HTMLResponse('<h1> Hello world! </h1>')


# uvicorn main:app --reload 
# uvicorn main:'Name_of_instance' --reload 
