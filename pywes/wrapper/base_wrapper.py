"""
Base class for spice simulator
"""
from abc import ABC, abstractmethod
from pydantic import BaseModel, FilePath, DirectoryPath
from enum import Enum
from typing import List, Optional
from asyncio import StreamReader
from pywes.parse.results import ResultDict
import h5py


class SupportedSimulator(str, Enum):
    ngsice = "ngspice"


class SimulatorType(str, Enum):
    spice = "spice"
    em = "em"


class SimulationType(str, Enum):
    ac = "ac"
    dc = "dc"
    tran = "tran"


class BaseWrapper(BaseModel, ABC):
    name: SupportedSimulator
    path: FilePath
    supported_sim: List[SimulationType]
    results: Optional[ResultDict]

    def add_to_queue(self):
        """
        Not Implemented Yet.
        :return:
        """

    @abstractmethod
    async def run(
        self,
        sim_file: FilePath,
        log_folder: DirectoryPath,
        config_file: List[FilePath] = (),
    ):
        """
        run the spice simulation describe by the _spice_file
        :param sim_file: input file to be simulated
        :param log_folder: directory to write simulation log
        :param config_file: List of file used to set up the simulator
        :return: a temp file of the raw out of the simulator (to be process by serialize_result)
        """

    @abstractmethod
    async def parse_out(self, stream: StreamReader):
        """
            Convert simulation output to ResultDict
        :return:
        """

    @abstractmethod
    async def parse_err(self, stream: StreamReader, log_folder: DirectoryPath):
        """
            Capture error and print it
        :return:
        """

    def export(self, file: FilePath):
        with h5py.File(file, "w") as f:
            for res in self.results:
                f[f"res/{res}"] = self.results[res]
