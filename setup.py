#!/usr/bin/env python
# (C) Copyright 2023 ECMWF.
#
# This software is licensed under the terms of the Apache Licence Version 2.0
# which can be obtained at http://www.apache.org/licenses/LICENSE-2.0.
# In applying this licence, ECMWF does not waive the privileges and immunities
# granted to it by virtue of its status as an intergovernmental organisation
# nor does it submit to any jurisdiction.
#


import io
import os
import platform
import subprocess
import sys

import setuptools


def read(fname):
    file_path = os.path.join(os.path.dirname(__file__), fname)
    return io.open(file_path, encoding="utf-8").read()


version = None
for line in read("ai_models_fuxi/__init__.py").split("\n"):
    if line.startswith("__version__"):
        version = line.split("=")[-1].strip()[1:-1]

assert version


onnxruntime = "onnxruntime-gpu"

setuptools.setup(
    name="ai-models-fuxi",
    python_requires="<3.11",  # For now, does not support Python 3.11
    version=version,
    description="An ai-models plugin to run FuXi",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    author="European Centre for Medium-Range Weather Forecasts (ECMWF)",
    author_email="software.support@ecmwf.int",
    license="Apache License Version 2.0",
    url="https://github.com/tpys/ai-models-fuxi",
    packages=setuptools.find_packages(),
    include_package_data=True,
    setup_requires=["GPUtil"],
    install_requires=[
        "ai-models",
        "onnx",
        os.environ.get("ONNXRUNTIME", onnxruntime),
    ],
    zip_safe=True,
    keywords="tool",
    entry_points={
        "ai_models.model": [
            "fuxi = ai_models_fuxi.model:FuXi",
        ]
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Operating System :: OS Independent",
    ],
)
