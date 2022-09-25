from subprocess import run, PIPE, STDOUT
from pydantic import FilePath, DirectoryPath
from .spice_wrapper import SpiceWrapper
from parse.spice3raw import read


class NGSpice(SpiceWrapper):
    def __init__(self, sim_path: FilePath):
        SpiceWrapper.__init__(
            self, name="ngspice", path=sim_path, supported_sim=("ac",)
        )

    def run(self, _spice_file: FilePath, log_folder: DirectoryPath):
        # TODO : https://docs.python.org/3.9/library/asyncio-subprocess.html
        with open(_spice_file, "r") as cir:
            proc = run([self.path, "-s"], stdin=cir, stdout=PIPE, stderr=PIPE)
        with open(log_folder+"sim_server.out", "bw") as f:
            f.write(proc.stdout)
        with open(log_folder+"sim_log.out", "bw") as f:
            f.write(proc.stderr)
        """
        batch mode keep for perfs test
        proc = run([self.path, "-b", "-r", log_folder+"sim_batch.out", _spice_file], stdout=PIPE, stderr=STDOUT)
        with open(log_folder+"sim.log", "bw") as f:
            f.write(proc.stdout)"""

    def serialize_result(self, result_file: FilePath):
        return read(result_file)
