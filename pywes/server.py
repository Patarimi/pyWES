from os import getcwd
from fastapi import FastAPI
from typing import List
from pywes.wrapper import NGSpice
from pywes.wrapper import SpiceWrapper


Server = FastAPI()
db: List[SpiceWrapper] = [
    NGSpice(sim_path=f"{getcwd()}/simulators/Spice64/bin/ngspice_con.exe"),
]


@Server.get("/")
async def root():
    return {"Hello": "World"}


@Server.get("/api/v1/simulators")
async def fetch_simulators():
    return db


@Server.post("/api/v1/simulators")
async def add_simulator(simulator: SpiceWrapper):
    db.append(simulator)
    return {"name": simulator.name}


@Server.post("api/v1/simulations")
async def add_simulation():
    return {"aaa": "bbb"}
