#!/bin/bash

# Listen for window events
swaymsg -t subscribe '["window"]' | jq --unbuffered '
  select(.change == "new" or .change == "focus")
  | {
      workspace: .container.workspace.name,
      app_name: .container.app_id // .container.window_properties.class
    }
' |
while read -r event; do
  # Extract workspace and app_name from the parsed event
  workspace=$(echo "$event" | jq -r .workspace)
  app_name=$(echo "$event" | jq -r .app_name)

  # Rename the workspace
  swaymsg workspace "$workspace", rename workspace to "$app_name"
done
