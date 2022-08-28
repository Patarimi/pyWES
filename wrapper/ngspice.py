from subprocess import run
from pydantic import FilePath, DirectoryPath
from .spice_wrapper import SpiceWrapper


class NGSpice(SpiceWrapper):
    path: FilePath

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


