#!/bin/bash

# This gets the list of applications
APPS=$(rofi -dmenu -p "Run: " -i -show drun -drun-display-format "{name}")
echo $APPS
# Check if Firefox is the chosen application
if [[ $APPS == "Firefox" ]]; then
    # Use the Nerd Font icon for Firefox and launch Firefox
    echo -e " Firefox"
    firefox &
else
    # Launch the chosen application
    $APPS &
fi
