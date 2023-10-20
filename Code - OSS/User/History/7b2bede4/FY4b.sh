#!/bin/bash

# Function to check for icon (replace with your own logic)
has_icon() {
    # For simplicity, assuming icons are in /usr/share/icons/hicolor/48x48/apps/
    test -e "/usr/share/icons/hicolor/48x48/apps/$1.png"
}

# Generate Rofi menu entries
menu_entries=""
while IFS= read -r app; do
    if has_icon "$app"; then
        # If the app has an icon, use the icon markup
        menu_entries+="{ -i $app, $app },"
    else
        # If the app does not have an icon, use the text markup
        menu_entries+="{ $app, $app },"
    fi
done < <(ls /usr/share/applications | sed 's/\.desktop//')

# Launch Rofi with the generated menu entries
rofi -show drun -dmenu -format i -p "Run: " -mesg "$menu_entries"
