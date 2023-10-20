#!/bin/sh

kitty -e cmatrix &

# Grab the last kitty window ID
KITTY_WINDOW=$(swaymsg -t get_tree | jq -r '.. | select(.type?=="con" and .app_id?=="kitty")? | .id' | tail -1)

# Wait for a moment to ensure the kitty window is ready
sleep 0.5

# Make it full screen
swaymsg [con_id="$KITTY_WINDOW"] fullscreen

wait # This will wait for the kitty process to end before ending the script
