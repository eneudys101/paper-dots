#!/bin/bash

current_workspace=$(swaymsg -t get_workspaces | jq '.[] | select(.focused) | .name' | tr -d '"')
app=$(swaymsg -t get_tree | jq -r '.. | select(.type?) | select(.type=="con") | select(.focused) | .app_id')

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

# Only renaming the workspace if the new name is different from the current name.
if [[ "$new_name" != "$current_workspace" ]]; then
    # Prefix the current workspace number with the new name.
    # This assumes your workspaces are named like "1", "2", etc.
    workspace_num=$(echo "$current_workspace" | grep -o -E '[0-9]+')
    combined_name="$workspace_num:$new_name"

    swaymsg workspace rename "$current_workspace" "$combined_name"
fi
