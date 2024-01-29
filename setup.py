#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os

from setuptools import find_packages, setup
from setuptools.command.install import install


class inst(install):
    def run(self):
        install.run(self)
        path = os.getcwd().replace(" ", r"\ ").replace("(", r"\(").replace(")", r"\)") + "/bin/"
        os.system("sh " + path + "install_teleservices_package_light_german.sh")


version = "0.0.3"

setup(
    name="teleservices-package-light-german",
    version=version,
    author="iMio",
    author_email="support-ts@imio.be",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[],
    url="https://github.com/IMIO//teleservices-package-light-german",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
    ],
    zip_safe=False,
    cmdclass={
        "inst": inst,
    },
)
