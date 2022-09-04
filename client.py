from os import getcwd
from fastapi import FastAPI
from typing import List
from wrapper.ngspice import NGSpice
from wrapper.spice_wrapper import SpiceWrapper


Client = FastAPI()
db: List[SpiceWrapper] = [
    NGSpice(sim_path=f"{getcwd()}/simulators/Spice64/bin/ngspice_con.exe"),
]


@Client.get("/")
async def root():
    return {"Hello": "World"}


@Client.get("/api/v1/simulators")
async def fetch_simulators():
    return db


@Client.post("/api/v1/simulators")
async def add_simulator(simulator: SpiceWrapper):
    db.append(simulator)
    return {"name": simulator.name}


@Client.post("api/v1/simulations")
async def add_simulation():
    return {"aaa": "bbb"}
