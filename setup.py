#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2013 Spotify AB

# This file is part of dh-virtualenv.

# dh-virtualenv is free software: you can redistribute it and/or
# modify it under the terms of the GNU General Public License as
# published by the Free Software Foundation, either version 2 of the
# License, or (at your option) any later version.

# dh-virtualenv is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with dh-virtualenv. If not, see
# <http://www.gnu.org/licenses/>.

import io
import re
import os
import sys
import json

from setuptools import find_packages, setup

version = '0.1.1'
author = u'Runking'
author_email = 'hrunker@gmail.com'
url = 'https://github.com/hackeryard/test'

#version_py = os.path.join(os.path.dirname(__file__), "_version.py")
project = {}
#with io.open(version_py, 'r', encoding='utf-8') as handle:
#    for line in handle:
#        try:
#            key, value = re.match(r"^(\w+) ?= ?u?'(.+?)'$", line).groups()
#        except (AttributeError, TypeError, ValueError):
#            pass
#        else:
#            project[key] = value
#assert all(x in project for x in ('version', 'author', 'author_email', 'url')), 'Bad metadata in _version.py!'


project.update(
    version=version,
    author=author,
    author_email=author_email,
    url=url,
    name='loginserver',
    description='loginserver to providing login services for cmdb.',
    license='GNU General Public License v2 or later',
    #scripts=['manage.py', 'settings.py','wsgi.py', 'urls.py', '__init__.py', 'bking.cert', 'bking.key'],
    scripts=['manage.py', 'config.py', 'settings.py','wsgi.py', 'urls.py', '__init__.py', 'bking.cert', 'bking.key', 'loginserver_config.ini'],
    packages=find_packages(),
    include_package_data=True,
    #data_files=[('templates', ['favicon.ico']), ('static', ['401.html'])],
    classifiers=[
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: GNU General Public License v2 or later (GPLv2+)',
        'Topic :: Software Development :: Build Tools',
        'Topic :: System :: Installation/Setup',
        'Topic :: Utilities',
    ])

# Ensure "setup.py" is importable by other tools, to access the project's metadata
__all__ = ['project']
if __name__ == '__main__':
    if '--metadata' in sys.argv[:2]:
        json.dump(project, sys.stdout, default=repr, indent=4, sort_keys=True)
        sys.stdout.write('\n')
    else:
        setup(**project)
