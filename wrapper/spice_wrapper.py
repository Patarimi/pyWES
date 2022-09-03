"""
Base class for spice simulator
"""
from abc import ABC, abstractmethod
from pydantic import BaseModel, FilePath, DirectoryPath
from enum import Enum
from typing import List


class SupportedSimulator(str, Enum):
    ngsice = "ngspice"


class SimulationType(str, Enum):
    ac = "ac"
    dc = "dc"
    tran = "tran"


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

    def write_result(self):
        """

        :return:
        """
