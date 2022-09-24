from subprocess import run, PIPE, STDOUT
from pydantic import FilePath, DirectoryPath
from typing import List
from .spice_wrapper import SpiceWrapper, ResultDict
import numpy as np


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
        num_var: int
        num_pts: int
        var_names: List[str] = list()
        results: ResultDict = dict()
        with open(result_file, 'r') as f:
            for line in f:
                if 'No. Variables:' in line:
                    num_var = int(line.split(' ')[2])
                    print(f"{num_var} variables expected")
                    break
            for line in f:
                if 'No. Points:' in line:
                    num_pts = int(line.split(' ')[2])
                    print(f"{num_pts} points expected")
                    break
            for line in f:
                if 'Variables' in line:
                    continue
                var_names.append(line.split('\t')[2])
                if len(var_names) >= num_var:
                    print(var_names)
                    break
            for name in var_names:
                results[name] = np.zeros(num_pts)
            i = 0
            for line in f:
                if 'Values' in line:
                    continue
                if i == 0:
                    results[var_names[i]] = float(line.split('\t')[2])
                else:
                    results[var_names[i]] = float(line)
                i = 0 if (i >= num_var - 1) else i+1
        return results
