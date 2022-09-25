from subprocess import run, PIPE
from pydantic import FilePath, DirectoryPath
from .spice_wrapper import SpiceWrapper
from parse.spice3raw import read


class NGSpice(SpiceWrapper):
    def __init__(self, sim_path: FilePath):
        SpiceWrapper.__init__(
            self, name="ngspice", path=sim_path, supported_sim=("ac",)
        )

    def run(self, _spice_file: FilePath, log_folder: DirectoryPath):
        with open(_spice_file, "r") as cir:
            proc = run([self.path, "-s"], stdin=cir, stdout=PIPE, stderr=PIPE)
        with open(log_folder+"sim_server.out", "bw") as f:
            f.write(proc.stdout)
        with open(log_folder+"sim_log.out", "bw") as f:
            f.write(proc.stderr)

    def serialize_result(self, result_file: FilePath):
        return read(result_file)
