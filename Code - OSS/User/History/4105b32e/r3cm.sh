#!/bin/bash

# Listen for window events
swaymsg -t subscribe '["window"]' | jq --unbuffered '
  select(.change == "new" or .change == "focus")
  | {
      workspace: .container.workspace.name,
      app_name: (if .container.app_id != null then .container.app_id else .container.window_properties.class end)
    }
' |
while read -r event; do
  # Extract workspace and app_name from the parsed event
  workspace=$(echo "$event" | jq -r .workspace)
  app_name=$(echo "$event" | jq -r .app_name)

  # Rename the workspace
  swaymsg workspace "$workspace", rename workspace to "$app_name"
done
