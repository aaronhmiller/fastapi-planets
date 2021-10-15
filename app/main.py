import platform
from typing import List
from pydantic import BaseModel
from fastapi import FastAPI
app = FastAPI()

planets = [
    {"name": "Mercury", "position": 1, "moons":0},
    {"name": "Venus", "position": 2, "moons":0},
    {"name": "Earth", "position": 3, "moons":1},
    {"name": "Mars", "position": 4, "moons":2},
    {"name": "Jupiter", "position": 5, "moons":79},
    {"name": "Saturn", "position": 6, "moons":62},
    {"name": "Uranus", "position": 7, "moons":27},
    {"name": "Neptune", "position": 8, "moons":14},
]

class Planet(BaseModel):
  name: str
  position: int
  moons: int

@app.get("/")
def read_root():
  return {"FastAPI running " + platform.system() + " on " + platform.machine()}

@app.get("/planets/{planet_id}")
def read_planet(planet_id: int):
  return planets[int(planet_id)-1] 

@app.get("/planets", response_model=List[Planet])
def list_planets():
  return planets
