import asyncio
from asyncio import StreamReader
from pydantic import FilePath, DirectoryPath
from .spice_wrapper import SpiceWrapper, ResultDict


class NGSpice(SpiceWrapper):
    def __init__(self, sim_path: FilePath):
        SpiceWrapper.__init__(
            self, name="ngspice", path=sim_path, supported_sim=("ac",)
        )

    async def run(self, _spice_file: FilePath, log_folder: DirectoryPath):
        cir = open(_spice_file, "r")
        proc = await asyncio.create_subprocess_shell(f"{self.path} -s",
                                                     stdin=cir,
                                                     stdout=asyncio.subprocess.PIPE,
                                                     stderr=asyncio.subprocess.PIPE)
        std_out_task = asyncio.create_task(self.parse_out(proc.stdout))
        std_err_task = asyncio.create_task(self.parse_err(proc.stderr, log_folder))
        await asyncio.gather(proc.wait(), std_out_task, std_err_task)
        cir.close()

    async def parse_out(self, stdout: StreamReader):
        ind = 0
        var_name = list()
        step = "start"
        self.results = ResultDict()
        while line := await stdout.readline():
            l_str = line.decode()
            if l_str.startswith("Variables"):
                step = "var_name"
            if l_str.startswith("Values"):
                step = "values"
                continue
            l_split = l_str.split()
            # Variables name part
            if step == "var_name" and len(l_split) == 3:
                try:
                    int(l_split[0])
                except ValueError:
                    continue
                var_name.append(l_split[1])
                self.results[l_split[1]] = list()
                continue
            # Values extraction part
            if step == "values":
                if len(l_split) == 2:
                    ind = 0
                    self.results[var_name[ind]].append(float(l_str.split()[1]))
                else:
                    r = float(l_str)
                    ind += 1
                    self.results[var_name[ind]].append(r)

    async def parse_err(self, stderr: StreamReader, log_folder: DirectoryPath):
        with open(log_folder + "err.out", "ab") as err:
            err.write(await stderr.read())
