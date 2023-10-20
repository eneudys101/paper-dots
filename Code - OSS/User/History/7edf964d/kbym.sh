#!/bin/bash

# Exit if no arguments are provided
[[ -z "$1" ]] && exit 1

# Using kitty's icat to preview
kitty +kitten icat --place=${3}x${4}@${1}x${2} "$5"
