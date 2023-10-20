#!/bin/bash

output=""

while IFS=';' read -r icon_code app command
do
    output="${output}\u$icon_code\t$app\t$command\n"
done < apps.list

echo -e "$output" | wofi --show dmenu --width 100% --height 100% --style <path_to_css> | awk -F'\t' '{print $3}' | xargs -I {} sh -c "{}"
