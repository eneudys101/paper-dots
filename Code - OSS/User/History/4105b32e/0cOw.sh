#!/bin/bash

# Path to your virtual environment
VENV_PATH=~/.config/sway/venv

# Path to your Python script
PYTHON_SCRIPT=~/.config/sway/dynamic-workspace-naming.py

# Name or part of the name of your script (for searching processes)
SCRIPT_NAME=dynamic-workspace-naming.py

# Check if the script is already running
#if pgrep -f $SCRIPT_NAME > /dev/null; then
    # Kill it if it is
 #   pkill -f $SCRIPT_NAME
    # Give it a moment to fully terminate
 #   sleep 1
#fi

# Activate the virtual environment
source $VENV_PATH/bin/activate

# Use the Python from the virtual environment to run your script
python $PYTHON_SCRIPT
