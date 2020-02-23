# __all__ = ["*", "testbed", "testpost"]
# How does one refer to the ini.py itself within __all__?

from . import testbed

# from .testbed import * allows the importation of all testbed public members
# from importing testPack itself
