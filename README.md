# Project with FastAPI

This is my first project using FastAPI with python. Currently working as a Data Analyst, exploring new areas of programming. 

During the course I worked using libraries: fastapi, pydantic, typing, uvicorn.

This was an introductory course to backend using FastAPI with Python, some of what I learnt:

- HTTP Methods with FastAPI 
- Path Operations
- Query parameters
- Validations using Pydantic
- Authentication: flow, generate tokens, validate tokens


## Installation

Install libraries with aliases 

```bash
from fastapi import FastAPI, Body, Path, Query, Request, HTTPException, Depends
from fastapi.responses import HTMLResponse, JSONResponse
from pydantic import BaseModel, Field
from typing import Optional, List
from jwt_manager import create_token, validate_token
from fastapi.security import HTTPBearer
```
 of just install the requirements.txt
