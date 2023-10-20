#!/bin/bash

while IFS=';' read -r icon_code app command
do
    echo -e "\u$icon_code\t$app\t$command"
done < apps.list | wofi --show dmenu --width 100% --height 100% --style <path_to_css> | awk -F'\t' '{print $3}' | sh
