from os import getcwd
from wrapper.ngspice import NGSpice


def test_ngspice():
    sim = NGSpice(sim_path=f"{getcwd()}/simulators/Spice64/bin/ngspice_con.exe")

    sim.run(f"{getcwd()}/test/schem_test.net", f"{getcwd()}/test/")
