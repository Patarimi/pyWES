from os import getcwd
from fastapi import FastAPI
from typing import List
from wrapper.ngspice import NGSpice
from wrapper.spice_wrapper import SpiceWrapper


app = FastAPI()
db: List[SpiceWrapper] = [
    NGSpice(sim_path=f"{getcwd()}/simulators/Spice64/bin/ngspice.exe"),
]


@app.get("/")
async def root():
    return {"Hello": "World"}


@app.get("/api/v1/simulators")
async def fetch_simulators():
    return db


@app.post("/api/v1/simulators")
async def add_simulator(simulator: SpiceWrapper):
    db.append(simulator)
    return {"name": simulator.name}


@app.post("api/v1/simulations")
async def add_simulation():
    return {"aaa": "bbb"}
