from sys import path
path.append("./bin/OpenEMS/bin")
path.append("/usr/lib/python3/dist-packages/CSXCAD")

import numpy as np
from pyems.structure import Microstrip, PCB, MicrostripCoupler
from pyems.simulation import Simulation
from pyems.pcb import common_pcbs
from pyems.calc import phase_shift_length, microstrip_effective_dielectric
from pyems.utilities import print_table
from pyems.coordinate import Coordinate2, Axis, Box3, Coordinate3
from pyems.mesh import Mesh
from pyems.field_dump import FieldDump, DumpType
from pyems.kicad import write_footprint

freq = np.linspace(0e9, 18e9, 501)
ref_freq = 5.6e9
unit = 1e-3
sim = Simulation(freq=freq, unit=unit, reference_frequency=ref_freq)
