from os import getcwd
from wrapper.ngspice import NGSpice
from wrapper.spice_wrapper import write_result


def test_ngspice():
    sim = NGSpice(sim_path=f"{getcwd()}/simulators/Spice64/bin/ngspice_con.exe")

    sim.run(f"{getcwd()}/test/schem_test.net", f"{getcwd()}/test/")

    res = sim.serialize_result(f"{getcwd()}/test/out.raw")

    write_result(res, f"{getcwd()}/test/out.h5py")
