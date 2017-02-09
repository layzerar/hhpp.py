# -*- coding: utf-8 -*-
#
# Copyright 2017 Melvi Ts <layzerar@gmail.com>.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import sys
import os.path
import setuptools
from setuptools.command.test import test as TestCommand


with open(os.path.join('hhpp', '__init__.py')) as _ver_fp:
    _ver_ctxt = {}
    _ver_line = [line for line in _ver_fp if line.startswith('__version__')][0]
    exec(_ver_line, _ver_ctxt)
    hhpp_version = _ver_ctxt['__version__']


class PyTest(TestCommand):
    # from http://pytest.org/latest/goodpractices.html\
    # #integrating-with-setuptools-python-setup-py-test-pytest-runner
    # TODO: prefer pytest-runner package at some point, however it was
    # not working at the time of this comment.
    user_options = [('pytest-args=', 'a', "Arguments to pass to py.test")]

    default_options = ["-q"]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.pytest_args = ""

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import shlex
        # import here, cause outside the eggs aren't loaded
        import pytest
        errno = pytest.main(self.default_options +
                            shlex.split(self.pytest_args))
        sys.exit(errno)


setuptools.setup(
    name='hhpp',
    version=hhpp_version,
    license='Apache License 2.0',
    author='Melvi Ts',
    author_email='layzerar@gmail.com',
    url='https://github.com/layzerar/hhpp.py',
    description='Happy Hacking Programming Patterns',
    long_description='Happy Hacking Programming Patterns.',
    packages=setuptools.find_packages(include=['hhpp*']),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Software Development :: Libraries',
    ],
    tests_require=[
        'pytest',
        'pytest-cov',
    ],
    cmdclass={
        'test': PyTest,
    }
)
