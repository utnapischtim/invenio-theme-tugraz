# -*- coding: utf-8 -*-
#
# Copyright (C) 2020 mojib wali.
#
# invenio-theme-tugraz is free software; you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file for more
# details.

"""invenio module for TUGRAZ theme."""

import os

from setuptools import find_packages, setup

readme = open("README.rst").read()
history = open("CHANGES.rst").read()

tests_require = [
    "pytest-invenio>=1.4.0",
    'invenio-app>=1.3.0,<2.0.0',
    "psycopg2-binary>=2.8.6",
]

extras_require = {
    "docs": [
        "Sphinx>=3",
    ],
    "mysql": [
        "invenio-db[mysql]>=1.0.0",
    ],
    "postgresql": [
        "invenio-db[postgresql]>=1.0.0",
    ],
    "sqlite": [
        "invenio-db>=1.0.0",
    ],
    "tests": tests_require,
}

extras_require["all"] = []
for reqs in extras_require.values():
    extras_require["all"].extend(reqs)

setup_requires = [
    "Babel>=1.3",
    "pytest-runner>=3.0.0,<5",
]

install_requires = [
    "Flask-BabelEx>=0.9.4",
    "Flask-WebpackExt>=1.0.0",
    "invenio-assets>=1.2.0",
    "invenio-i18n>=1.2.0",
    "elasticsearch_dsl>=7.2.1",
    "invenio_search>=1.3.1",
]

packages = find_packages()


# Get the version string. Cannot be done with import!
g = {}
with open(os.path.join("invenio_theme_tugraz", "version.py"), "rt") as fp:
    exec(fp.read(), g)
    version = g["__version__"]

setup(
    name="invenio-theme-tugraz",
    version=version,
    description=__doc__,
    long_description=readme + "\n\n" + history,
    keywords="invenio, theme, invenioRDM, TU-Graz, Graz University of Technology, statistics",
    license="MIT",
    author="mojib wali",
    author_email="mojib.wali@tugraz.at",
    url="https://github.com/tu-graz-library/invenio-theme-tugraz",
    packages=packages,
    zip_safe=False,
    include_package_data=True,
    platforms="any",
    entry_points={
        "invenio_base.apps": [
            "invenio_theme_tugraz = invenio_theme_tugraz:InvenioThemeTugraz",
        ],
        "invenio_base.blueprints": [
            "invenio_theme_tugraz = invenio_theme_tugraz.views:blueprint",
        ],
        "invenio_i18n.translations": [
            "messages = invenio_theme_tugraz",
        ],
        "invenio_assets.webpack": [
            "invenio_theme_tugraz_theme = invenio_theme_tugraz.webpack:theme",
        ],
        "invenio_config.module": [
            "invenio_theme_tugraz = invenio_theme_tugraz.config",
        ],
    },
    extras_require=extras_require,
    install_requires=install_requires,
    setup_requires=setup_requires,
    tests_require=tests_require,
    classifiers=[
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Development Status :: 3 - Alpha",
    ],
)
