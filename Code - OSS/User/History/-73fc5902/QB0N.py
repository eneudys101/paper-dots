import i3ipc

def get_unique_prefix(i3):
    """Fetch a unique prefix for a new workspace name."""
    workspaces = [ws.name for ws in i3.get_workspaces()]
    counter = 1
    while True:
        prefix = f"{counter}:"
        if not any(ws.startswith(prefix) for ws in workspaces):
            return prefix
        counter += 1

def rename_workspace(i3, e):
    print("rename_workspace triggered")
    """Rename the focused workspace based on the last focused app."""
    focused_ws = i3.get_tree().find_focused().workspace().name
    app = i3.get_tree().find_focused().app_id

    # Map application IDs to desired workspace names
    app_name_mapping = {
        "firefox": "Web",
        "kitty": "Terminal"
    }
    new_name = app_name_mapping.get(app, app)

    # Extract the prefix and current name of the workspace
    parts = focused_ws.split(":", 1)
    if len(parts) < 2:  # If the ":" delimiter isn't found in the workspace name
        return  # Exit the function

    prefix = parts[0] + ":"
    current_name = parts[1].strip()

    # Only rename if the name does not match
    if current_name != new_name:
        i3.command(f'rename workspace "{focused_ws}" to "{prefix} {new_name}"')


def name_new_workspace_empty(i3, e):
    print("name_new_workspace_empty triggered")
    """Name a newly created workspace as 'Empty'."""
    prefix = get_unique_prefix(i3)
    i3.command(f'rename workspace "{e.current.name}" to "{prefix} empty"')

i3 = i3ipc.Connection()
i3.on('window::focus', rename_workspace)
i3.on('workspace::init', name_new_workspace_empty)
i3.main()
