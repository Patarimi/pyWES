from pydantic import BaseModel, FilePath, Field
from uuid import uuid4, UUID
from typing import List
from enum import Enum


class SimulationType(str, Enum):
    ac = "ac"
    dc = "dc"
    tran = "tran"


class SupportedSimulator(str, Enum):
    ngsice = "ngspice"


class Simulator(BaseModel):
    name: SupportedSimulator
    path: FilePath
    supported_sim_type: List[SimulationType]


class Simulation(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    type: SimulationType
    simulator: Simulator
