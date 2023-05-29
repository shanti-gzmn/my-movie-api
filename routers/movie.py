from fastapi import APIRouter
from fastapi import Path, Query, Depends
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
from typing import Optional, List
from config.database import Session
from models.movie import Movie as MovieModel
from fastapi.encoders import jsonable_encoder
from middlewares.jwt_bearer import JWTBearer
from services.movie import MovieService
from schemas.movie import Movie

movie_router = APIRouter()

@movie_router.get('/movies', tags=['movies'], response_model=List[Movie], status_code = 200, dependencies=[Depends(JWTBearer())])
def get_movies() -> List[Movie]:
    db = Session()
    result = MovieService(db).get_movies()
    return JSONResponse(status_code = 200, content=jsonable_encoder(result))

@movie_router.get('/movies/{id}', tags=['movies'], response_model = Movie, status_code=404)
def get_movie(id:int = Path(ge=1, le=2000)) -> Movie:
    db = Session()
    result = MovieService(db).get_movie(id)
    if not result:
        return JSONResponse(status_code = 404, content={'message': 'No encontrado'})
    return JSONResponse(status_code = 200, content = jsonable_encoder(result))
 
@movie_router.get('/movies/', tags=['movies'], response_model = List[Movie])
def get_movies_by_category(category:str = Query(min_length=5, max_length=15)) -> List[Movie]:
    db = Session()
    result = MovieService(db).get_movies_by_category(category)
    return JSONResponse(status_code=200, content = jsonable_encoder(result))

@movie_router.post('/movies', tags=['movies'], response_model = dict, status_code = 201)
def create_movie(movie: Movie) -> dict:
    db = Session()
    new_movie = MovieModel(**movie.dict())
    db.add(new_movie)
    db.commit()
    return JSONResponse(status_code = 201, content = {'message': "Movie registered"}) 

@movie_router.put('/movies/{id}', tags=['movies'], status_code = 200)
def update_movie(id: int, movie: Movie) -> dict:
    db = Session()
    result = db.query(MovieModel).filter(MovieModel.id == id).first()
    if not result:
        return JSONResponse(status_code=404, content={'message': 'No encontrado'})
    result.title = movie.title
    result.overview = movie.overview
    result.year = movie.year
    result.rating = movie.rating
    result.category = movie.category
    db.commit()
    return JSONResponse(status_code = 200, content = {'message': "Movie successfully updated"} )

@movie_router.delete('/movies/{id}', tags=['movies'], response_model = dict, status_code = 200)
def delete_movie(id: int) -> dict:
    db = Session()
    result = db.query(MovieModel).filter(MovieModel.id == id).first()
    if not result:
        return JSONResponse(status_code=404, content={'message': 'No encontrado'})
    db.delete(result)
    db.commit()
    return JSONResponse(status_code = 200, content = {'message': "Movie successfully deleted"})

