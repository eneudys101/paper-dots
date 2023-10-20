#!/bin/bash

# Function to get the focused app's name or class
get_focused_app() {
    # Get the focused window's properties using `swaymsg`
    swaymsg -t get_tree | jq -r '.. | select(.focused? == true) | .app_id // .window_class'
}

# Function to rename the workspace based on the focused window's app name or class
rename_workspace() {
    local app_name="$1"
    local icon=$(get_app_icon "$app_name")

    # Extract the current workspace's number
    local current_ws_number=$(swaymsg -t get_workspaces | jq -r '.[] | select(.focused == true) | .num')
    if [ -z "$current_ws_number" ]; then
        # Exit the function if the workspace number isn't set
        return
    fi
    
    # Set the new workspace name
    local new_ws_name="${current_ws_number}: ${icon}"

    # Rename the workspace
    swaymsg -- rename workspace to "$new_ws_name"
}


# Continuously monitor for window focus events and rename the workspace accordingly
swaymsg -m -t subscribe '["window"]' | while read -r event; do
    app_name=$(get_focused_app)
    if [ ! -z "$app_name" ]; then
        rename_workspace "$app_name"
    fi
done