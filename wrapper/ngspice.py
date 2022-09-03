from subprocess import run
from pydantic import FilePath, DirectoryPath
from .spice_wrapper import SpiceWrapper, SupportedSimulator


class NGSpice(SpiceWrapper):
    def __init__(self, sim_path: FilePath):
        SpiceWrapper.__init__(self, name="ngspice", path=sim_path, supported_sim=("ac",))

    def run(self, _spice_file: FilePath, result_folder: DirectoryPath):
        run(
            [
                self.path,
                "-b",
                "-r",
                result_folder + "out.raw",
                _spice_file,
            ]
        )
