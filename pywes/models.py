from pydantic import BaseModel, Field
from uuid import uuid4, UUID
from pywes.wrapper import SpiceWrapper, SimulationType


class Simulation(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    type: SimulationType
    simulator: SpiceWrapper
