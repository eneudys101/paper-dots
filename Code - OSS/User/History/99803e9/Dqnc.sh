#!/bin/bash

# This script switches to a workspace based on its number, 
# regardless of its full name (with icons)

# Desired workspace number
ws_number=$1

# Fetch the name of the workspace starting with the given number
ws_name=$(swaymsg -t get_workspaces | jq -r --arg num "$ws_number:" '.[] | select(.name | startswith($num)) | .name')

# If a workspace with that number is found, switch to it
if [ ! -z "$ws_name" ]; then
    swaymsg workspace "$ws_name"
fi
