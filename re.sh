#!/bin/bash

set -e
# add __init__.py
(cd static && touch __init__.py)

(cd templates && touch __init__.py)

(dpkg-buildpackage -us -uc -b ; dpkg -i ../*.deb)
#( deactivate ; dpkg-buildpackage -us -uc -b ; dpkg -i ../*.deb)
