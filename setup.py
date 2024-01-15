#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from os import path

from setuptools import setup

here = path.abspath(path.dirname(__file__))

# Get the long description from the relevant file
with open(path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="furigana",
    version="1.0.0",
    description="Convert Japanese Kanji to Kanji attached with Hiragana. For example, 「澱んだ街角」→「澱(よど)んだ街角(まちかど)」",
    long_description=long_description,
    author="Javi Manzano",
    author_email="javi.manzano.oller@gmail.com",
    url="https://github.com/jgasteiz/furigana",
    packages=["furigana"],
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Text Processing :: Linguistic",
    ],
    keywords="Japanese Language Processing",
)
