"""


basic quantum chemistry softwares data including:



* cp2k
    - POTENTIAL
    - BASIS_SET
* vasp
    - potpaw
    - potpaw_GGA
    - potpaw_PBE
* adf
    - atomicdata(exclude Molecules & DFTB)

"""


import os


__version__ = '1.1.0'


def version():
    return __version__


basedir = os.path.dirname(os.path.realpath(__file__))
cp2k = os.path.join(basedir, 'cp2k')
vasp = os.path.join(basedir, 'vasp')
adf = os.path.join(basedir, 'adf')
