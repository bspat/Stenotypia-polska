#!/usr/bin/env python3

from setuptools import setup

from pathlib import Path
this_directory = Path(__file__).parent
long_desc = (this_directory / "README.md").read_text()

setup()
