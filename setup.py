#!/usr/bin/env python
import sys
import os

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

if sys.version_info < (2, 5):
    sys.exit("requires python 2.5 and up")


here = os.path.dirname(__file__)

exec(open(os.path.join(here, 'memorpy', 'version.py')).read())
setup(name = "memorpy",
    version = 1.7,
    description = "Python library using ctypes to search/edit windows/linux programs memory",
    author = "Victor Dyotte",
    author_email = "vdyotte@gmail.com",
    maintainer_email="vdyotte@gmail.com",
    license = "BSD",
    url = "https://github.com/Kiniamaro/memorpy",
    packages = [
        'memorpy',
    ],
    install_requires = [],
    platforms = ["POSIX", "Windows"],
    use_2to3 = False,
    zip_safe = False,
    long_description = open(os.path.join(here, "README.md"), "r").read(),
)


