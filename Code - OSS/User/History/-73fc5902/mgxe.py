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

    focused_ws = i3.get_tree().find_focused().workspace().name
    app = i3.get_tree().find_focused().app_id

    print(f"Focused Workspace: {focused_ws}")
    print(f"Focused App ID: {app}")

    app_name_mapping = {
        "firefox": "Web",
        "kitty": "Terminal",
        "code-oss": "Code"
    }
    new_name = app_name_mapping.get(app, "MysteryBox")

    parts = focused_ws.split(":", 1)
    if len(parts) < 2:
        return

    prefix = parts[0] + ":"
    current_name = parts[1].strip()

    print(f"New Name: {new_name}")
    print(f"Prefix: {prefix}")
    print(f"Current Name: {current_name}")

    if current_name != new_name:
        i3.command(f'rename workspace "{focused_ws}" to "{prefix} {new_name}"')
        print(f'Renamed workspace "{focused_ws}" to "{prefix} {new_name}"')




def name_new_workspace_empty(i3, e):
    print("name_new_workspace_empty triggered")
    """Name a newly created workspace as 'Empty'."""
    prefix = get_unique_prefix(i3)
    i3.command(f'rename workspace "{e.current.name}" to "{prefix} empty"')

i3 = i3ipc.Connection()
i3.on('window::focus', rename_workspace)
i3.on('workspace::init', name_new_workspace_empty)
i3.main()
