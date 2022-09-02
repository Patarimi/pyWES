from os import getcwd
from fastapi import FastAPI, HTTPException
from uuid import uuid4, UUID
from typing import List
from models import Simulator, SimulationType, Simulation


app = FastAPI()
db: List[Simulator] = [
    Simulator(
        name="ngspice",
        path=f"{getcwd()}/simulators/Spice64/bin/ngspice.exe",
        supported_sim_type=("dc", "ac", "tran"),
    ),
]


@app.get("/")
async def root():
    return {"Hello": "World"}


@app.get("/api/v1/simulators")
async def fetch_simulators():
    return db


@app.post("/api/v1/simulators")
async def add_simulator(simulator: Simulator):
    db.append(simulator)
    return {"name": simulator.name}
