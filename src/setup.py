# Available at setup time due to pyproject.toml
from pybind11.setup_helpers import Pybind11Extension, build_ext
from setuptools import setup
from glob import glob


__version__ = "3.0.0"

setup(
    version=__version__,
    ext_modules=[
        Pybind11Extension("SmartCalc",
                          #   ["main.cpp"],
                          sorted(glob("RPN/*.cc")),
                          # Example: passing in the version to the compiled code
                          define_macros=[('VERSION_INFO', __version__)],
                          ),
    ],
    cmdclass={"build_ext": build_ext},
)
