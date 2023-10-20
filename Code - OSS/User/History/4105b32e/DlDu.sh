#!/bin/bash

# Path to your virtual environment
VENV_PATH=~/.config/sway/venv

# Path to your Python script
PYTHON_SCRIPT=~/.config/sway/dynamic-workspace-naming.py

# Activate the virtual environment
source $VENV_PATH/bin/activate

# Use the Python from the virtual environment to run your script
python $PYTHON_SCRIPT