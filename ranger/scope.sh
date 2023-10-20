#!/bin/sh

# ranger will use this script to preview files if it's enabled.

# Environment:
# - $PV_IMAGE_ENABLED: If 'True', ranger is capable of displaying images.
# - $PV_WIDTH, $PV_HEIGHT: The size of the preview pane.
# - $PV_IMAGE_MAX_WIDTH, $PV_IMAGE_MAX_HEIGHT: Maximum dimensions for image previews. Might be smaller than the dimensions of the preview pane.
# - $PV_IMAGE_MAX_OFF_X, $PV_IMAGE_MAX_OFF_Y: The maximum value that the image can be shifted.
# - $PV_IMAGE_OFF_X, $PV_IMAGE_OFF_Y: The value that the image should be shifted by. This can be set to $PV_IMAGE_MAX_OFF_X and ..._OFF_Y to align the image to the bottom right.

# In case of error, this script will output a generic file icon.
# If more than 6 exit codes are used, this might conflict with ranger's error codes.

# Exit codes:
# - 0: success
# - 1: unrecognized file type
# - 2: file not found
# - 3: ranger error
# - 4: missing highlight tool
# - 5: missing helper tool
# - 6: no error, but no action taken
# - 7: the function is not implemented for this type of file

handle_image() {
    if [ "$PV_IMAGE_ENABLED" != True ]; then
        exit 1
    fi

    kitty +kitten icat --silent --transfer-mode=file "$1" && exit 6

    exit 1
}

handle_extension() {
    case "$1" in
        # Archives
        *.tar*) tar tf "$1";;
        *.zip) unzip -l "$1";;
        *.rar) unrar l "$1";;
        *.7z) 7z l "$1";;
        *.pdf) pdftotext "$1" -;;
        # Source code highlighting
        *.c|*.h|*.cpp|*.hpp|*.py|*.rb|*.sh|*.pl|*.lua|*.java|*.go|*.js) highlight -O ansi "$1" || coderay "$1" || cat "$1";;
        *) exit 1;;
    esac
}

handle_mime() {
    case "$1" in
        text/* | */xml)
            highlight -O ansi "$2" || coderay "$2" || cat "$2"
            ;;
        image/*)
            handle_image "$2"
            ;;
        *) exit 1 ;;
    esac
}

if [ ! -r "$1" ]; then
    exit 2
fi

mimetype=$(file --mime-type -Lb "$1")

handle_mime "$mimetype" "$1" || handle_extension "$1"
