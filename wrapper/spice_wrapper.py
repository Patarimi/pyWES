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

        :return:
        """

    @abstractmethod
    def run(self, _spice_file: FilePath, result_folder: DirectoryPath):
        """

        :param _spice_file:
        :param result_folder:
        :return:
        """

    @abstractmethod
    def serialize_result(self, result_file: FilePath):
        """
            Convert simulation output to ResultDict
        :return:
        """
