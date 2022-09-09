"""
Base class for spice simulator
"""
from abc import ABC, abstractmethod
import h5py
from pydantic import BaseModel, FilePath, DirectoryPath
from enum import Enum
from typing import List, TypedDict
from numpy import ndarray


class SupportedSimulator(str, Enum):
    ngsice = "ngspice"


class SimulationType(str, Enum):
    ac = "ac"
    dc = "dc"
    tran = "tran"


class ResultDict(TypedDict):
    label: str
    array: ndarray


def write_result(result: ResultDict, result_file: FilePath):
    with h5py.File(result_file, "w") as f:
        for keys in result:
            f[keys] = result[keys]


class SpiceWrapper(BaseModel, ABC):
    name: SupportedSimulator
    path: FilePath
    supported_sim: List[SimulationType]

    def add_to_queue(self):
        """
        Not Implemented Yet.
        :return:
        """

    @abstractmethod
    def run(self, _spice_file: FilePath, log_folder: DirectoryPath):
        """
        run the spice simulation describe by the _spice_file
        :param _spice_file: spice file to be simulated
        :param log_folder: directory to write simulation log
        :return: a temp file of the raw out of the simulator (to be process by serialize_result)
        """

    @abstractmethod
    def serialize_result(self, result_file: FilePath):
        """
            Convert simulation output to ResultDict
        :return:
        """
