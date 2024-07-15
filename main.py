import os
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pydantic import BaseModel

from get_result import getResult

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

class Individual(BaseModel):
    examType:str
    regulation: int
    heldOn:str
    semester:int
    roll: int

class Inistitution(BaseModel):
    examType:str
    regulation: int
    heldOn:str
    semester:int
    eiin: int

@app.get("/")
async def getExitsData():
    return HTMLResponse( """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Diploma Result API</title>
</head>
<body>
    <h1>Welcome to Diplomat Result API</h1>
    <h3>For documentation, Go to : <a href="https://backend-python-fast-api.onrender.com/docs">https://backend-python-fast-api.onrender.com/docs</a></h3>
</body>
</html>""")

@app.exception_handler(404)
async def custom_404_handler(_, __):
    return HTMLResponse("""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Diploma Result API</title>
</head>
<body>
    <h1>404</h1>
    <h1>Welcome to Diplomat Result API</h1>
    <h3>For documentation, Go to : <a href="https://backend-python-fast-api.onrender.com/docs">https://backend-python-fast-api.onrender.com/docs</a></h3>
</body>
</html>""")

@app.get("/files-list")
async def getExitsData():
    return {"files-list": os.listdir("data")}

@app.post("/individual/")
async def get_individual_data(individual: Individual):
    return getResult(
        examType=individual.examType, 
        regulation= individual.regulation,
        heldOn= individual.heldOn,
        semester= individual.semester,
        roll= individual.roll,
        isIndividual= True,
    )

@app.post("/inistitution/")
async def get_inistitution_data(inistitution: Inistitution):
    return getResult(
        examType=inistitution.examType, 
        regulation= inistitution.regulation,
        heldOn= inistitution.heldOn,
        semester= inistitution.semester,
        isIndividual= False,
        eiin=inistitution.eiin
    )
