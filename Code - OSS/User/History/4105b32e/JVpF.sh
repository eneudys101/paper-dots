#!/bin/bash

# Function to get the focused app's name or class
get_focused_app() {
    # Get the focused window's properties using `swaymsg`
    swaymsg -t get_tree | jq -r '.. | select(.focused? == true) | .app_id // .window_class'
}

# Function to rename the workspace based on the focused window's app name or class
rename_workspace() {
    local app_name="$1"
    local current_ws_name=$(swaymsg -t get_workspaces | jq -r '.[] | select(.focused == true) | .name')
    swaymsg rename workspace -- "$current_ws_name" to "$app_name"
}

# Continuously monitor for new window events and rename the workspace accordingly
swaymsg -t subscribe -- '["window::new"]' | while read -r event; do
    app_name=$(get_focused_app)
    if [ ! -z "$app_name" ]; then
        rename_workspace "$app_name"
    fi
done
