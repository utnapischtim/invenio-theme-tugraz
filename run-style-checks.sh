#!/usr/bin/env sh
# -*- coding: utf-8 -*-
#
# Copyright (C) 2020 Graz University of Technology
#
# invenio-theme-tugraz is free software; you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file for more
# details.

pydocstyle **/*.py
isort **/*.py --quiet --check-only --diff
check-manifest --quiet --ignore ".travis-*"
sphinx-build -qnNW docs docs/_build/html
