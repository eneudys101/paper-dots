#!/bin/bash

# Get the focused app name
APP_NAME=$(swaymsg -t get_tree | jq '.. | select(.focused?) | .app_id?' | tr -d '"')

# If no app_name, don't rename the workspace
[ -z "$APP_NAME" ] && exit

# Get the current workspace
CURRENT_WORKSPACE=$(swaymsg -t get_workspaces | jq '.[] | select(.focused==true) .name' | tr -d '"')

# Rename the workspace
NEW_NAME="NUMBER:$APP_NAME"

swaymsg workspace rename "$CURRENT_WORKSPACE" to "$NEW_NAME"
