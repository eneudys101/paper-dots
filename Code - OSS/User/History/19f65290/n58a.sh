#!/bin/bash

# Fetch drun list
APPS=$(rofi -dmenu -format 'i' -p "Run: " -i -show drun -drun-display-format "{name}")

# Check the selection
if [[ $APPS == *Firefox* ]]; then
    # Execute Firefox
    firefox &
else
    # Execute the chosen app (this part can be more refined based on output)
    rofi -show drun | awk 'NR=='$APPS+1'' | xargs -I {} sh -c '{}'
fi
