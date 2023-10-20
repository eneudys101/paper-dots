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

    if current_name != new_name:
        i3.command(f'rename workspace "{focused_ws}" to "{prefix} {new_name}"')

def shift_workspaces_up(i3):
    # Fetch all workspaces
    workspaces = [ws for ws in i3.get_workspaces()]
    
    # Sort workspaces by their numerical position in descending order
    sorted_workspaces = sorted(workspaces, key=lambda ws: ws.num, reverse=True)
    
    for ws in sorted_workspaces:
        parts = ws.name.split(":", 1)
        if len(parts) < 2:
            continue
        prefix = int(parts[0])  # Convert the prefix to an integer
        new_prefix = prefix + 1
        new_name = f"{new_prefix}:{parts[1].strip()}"
        i3.command(f'rename workspace "{ws.name}" to "{new_name}"')

def name_new_workspace_empty(i3, e):
    shift_workspaces_up(i3)
    i3.command(f'rename workspace "{e.current.name}" to "1: Empty"')

def initialize_workspaces(i3):
    # Fetch all workspaces
    workspaces = [ws for ws in i3.get_workspaces()]
    # Sort workspaces by their numerical position
    sorted_workspaces = sorted(workspaces, key=lambda ws: ws.num)

    app_name_mapping = {
        "firefox": "Web",
        "kitty": "Terminal",
        "code-oss": "Code"
    }

    counter = 1
    for ws in sorted_workspaces:
        app = ws.window_class  # Getting the window class to determine the application
        new_name = app_name_mapping.get(app, "MysteryBox")
        i3.command(f'rename workspace "{ws.name}" to "{counter}:{new_name}"')
        counter += 1

i3 = i3ipc.Connection()
initialize_workspaces(i3)
i3.on('window::focus', rename_workspace)
i3.on('workspace::init', name_new_workspace_empty)
i3.main()
