"""
Base class for spice simulator
"""
from abc import ABC, abstractmethod
from pydantic import BaseModel, FilePath, DirectoryPath


class SpiceWrapper(BaseModel, ABC):
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