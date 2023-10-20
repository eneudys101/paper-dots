#!/bin/bash

# Generate a list of applications
APPS=$(ls /usr/share/applications/ | sed 's/\.desktop//')

# Display the menu using wofi
CHOSEN_APP=$(echo "$APPS" | wofi --show=dmenu --style="$HOME/.config/wofi/style.css")

# Launch the chosen application
gtk-launch $CHOSEN_APP
