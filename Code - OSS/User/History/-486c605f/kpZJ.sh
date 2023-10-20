# Image previews with kitty
if [[ "$preview_images" == "True" ]]; then
    case "$mimetype" in
        image/*)
            kitty +kitten icat --silent --transfer-mode=file "$path" && exit 6
        ;;
    esac
fi
