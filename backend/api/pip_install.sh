#!/bin/bash

venv/Scripts/activate

# Install the package using pip
pip install "$@"

# Update requirements.txt
echo Updating requirements.txt...
pip freeze > requirements.txt