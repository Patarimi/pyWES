from wrapper.ngspice import NGSpice


def test_ngspice():
    sim = NGSpice(path="./simulators/ngspice-37_64/Spice64/bin/ngspice.exe")

    sim.run(".test/schem_test.net", "./test/")
