
from setuptools import setup

__project__ = "passwordGenerator"
__version__ = "0.0.1"
__description__ = "a Python module from the Raspberry projects to generate a complex random password"
__packages__ = ["pwdGenerator"]
__author__ = "Raspberry"
__classifiers__ = "classifiers"


setup(
    name = __project__,
    version = __version__,
    description = __description__,
    packages = __packages__,
    author = __author__,
    classifiers = __classifiers__,

)

"""Create a list of classifiers and pass it to the set up function"""

__classifiers__ = [
    "Development Status :: 3 - Alpha",
    "Intended Audience :: Education",
    "Programming Language :: Python :: 3",
]
