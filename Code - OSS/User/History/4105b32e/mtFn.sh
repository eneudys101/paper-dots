#!/bin/bash

# Function to rename the workspace based on the focused app
rename_workspace() {
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
        workspace_num=$(echo "$current_workspace" | grep -o -E '[0-9]+')
        combined_name="$workspace_num:$new_name"

        swaymsg workspace rename "$current_workspace" "$combined_name"
    fi
}

# Subscribe to workspace and window events
swaymsg -t subscribe '["workspace","window"]' | 
while read -r event; do
    rename_workspace
done
