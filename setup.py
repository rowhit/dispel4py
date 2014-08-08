# Copyright (c) The University of Edinburgh 2014
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "dispel4py",
    version = "0.0.1",
    author = "The University of Edinburgh",
    author_email = "a.krause@epcc.ed.ac.uk",
    description = ("Dispel4py is a Python library used to describe abstract workflows for distributed data-intensive applications."),
    license = "Apache 2",
    keywords = "dispel4py dispel workflows processing elements",
    url = "https://github.com/akrause2014/dispel4py",
    packages=['dispel4py', 'dispel4py.seismo', 'dispel4py.storm', 'dispel4py.examples', 'dispel4py.examples.graph_testing'],
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: Apache 2 License",
    ],
)