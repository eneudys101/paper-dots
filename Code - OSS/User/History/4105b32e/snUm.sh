#!/bin/bash

# Function to get the newly opened app's name or class
get_new_app() {
    # Extract the app_id or window_class of the newly opened window from the event data
    echo "$1" | jq -r '.. | select(.change? == "new") | .container.app_id // .container.window_class'
}

# Function to rename the workspace based on the app's name or class
rename_workspace() {
    local app_name="$1"
    local current_ws_name=$(swaymsg -t get_workspaces | jq -r '.[] | select(.focused == true) | .name')
    swaymsg rename workspace -- "$current_ws_name" to "$app_name"
}

# Continuously monitor for new window events and rename the workspace accordingly
swaymsg -t subscribe -- '["window"]' | while read -r event; do
    app_name=$(get_new_app "$event")
    if [ ! -z "$app_name" ]; then
        rename_workspace "$app_name"
    fi
done
