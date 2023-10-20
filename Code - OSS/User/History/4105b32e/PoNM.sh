#!/bin/bash

workspace=$(swaymsg -t get_workspaces | jq '.[] | select(.focused) | .name')
app=$(swaymsg -t get_tree | jq -r '.. | select(.type?) | select(.type=="con") | .app_id')

case "$app" in
    "firefox")
        new_name="Web"
        ;;
    "kitty")
        new_name="Terminal"
        ;;
    *)
        new_name="$app"
        ;;
esac

swaymsg workspace rename "$workspace" "$new_name"
