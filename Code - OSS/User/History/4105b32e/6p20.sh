#!/bin/bash

# Path to your virtual environment
VENV_PATH=~/.config/sway/venv

# Path to your Python script
PYTHON_SCRIPT=~/.config/sway/dynamic-workspace-naming.py

# Use the Python from the virtual environment to run your script
$VENV_PATH/bin/python $PYTHON_SCRIPT
