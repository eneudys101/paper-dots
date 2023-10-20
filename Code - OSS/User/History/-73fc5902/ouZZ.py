import i3ipc

def get_unique_prefix(i3):
    # Fetch all workspace names
    workspaces = [ws.name for ws in i3.get_workspaces()]
    counter = 1
    while True:
        prefix = f"{counter}:"
        if not any([ws.startswith(prefix) for ws in workspaces]):
            return prefix
        counter += 1

def rename_workspace(i3, e):
    focused_ws = i3.get_tree().find_focused().workspace().name
    app = i3.get_tree().find_focused().app_id

    new_name = {
        "firefox": "Web",
        "kitty": "Terminal"
    }.get(app, app)

    
    print(focused_ws) 

    parts = focused_ws.split(":", 1)
    prefix = parts[0] + ":"
    current_name = parts[1].strip()

    # Only rename if the name does not match
    if current_name != new_name:
        i3.command(f'rename workspace "{focused_ws}" to "{prefix} {new_name}"')



def name_new_workspace_empty(i3, e):
    # Use unique prefix for new workspace and name it "empty"
    prefix = get_unique_prefix(i3)
    i3.command(f'rename workspace "{e.current.name}" to "{prefix} empty"')

i3 = i3ipc.Connection()
i3.on('window::focus', rename_workspace)
i3.on('workspace::init', name_new_workspace_empty)
i3.main()
