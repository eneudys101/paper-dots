import i3ipc

APP_NAME_MAPPING = {
    "firefox": "Web",
    "kitty": "Terminal",
    "code-oss": "Code"
}

def get_workspace_names(i3):
    return [ws.name for ws in i3.get_workspaces()]

def extract_prefix_and_name(workspace_name):
    parts = workspace_name.split(":", 1)
    if len(parts) < 2:
        return None, None
    return int(parts[0]), parts[1].strip()

def rename_workspace_with_prefix(i3, prefix, new_name):
    current_ws_name = i3.get_tree().find_focused().workspace().name
    current_prefix, current_name = extract_prefix_and_name(current_ws_name)
    
    if current_prefix is not None and current_name != new_name:
        i3.command(f'rename workspace "{current_ws_name}" to "{prefix}:{new_name}"')


def get_unique_prefix(i3):
    workspace_names = get_workspace_names(i3)
    counter = 1
    while f"{counter}:" in workspace_names:
        counter += 1
    return f"{counter}:"

def shift_workspaces_up(i3):
    for ws in sorted(i3.get_workspaces(), key=lambda ws: ws.num, reverse=True):
        prefix, name = extract_prefix_and_name(ws.name)
        if prefix is not None:
            i3.command(f'rename workspace "{ws.name}" to "{prefix + 1}:{name}"')

def on_window_focus(i3, e):
    app_name = APP_NAME_MAPPING.get(i3.get_tree().find_focused().app_id, "MysteryBox")
    rename_workspace_with_prefix(i3, get_unique_prefix(i3), app_name)

def on_new_workspace_init(i3, e):
    shift_workspaces_up(i3)
    i3.command(f'rename workspace "{e.current.name}" to "1: Empty"')

def initialize_workspaces(i3):
    for counter, ws in enumerate(sorted(i3.get_workspaces(), key=lambda ws: ws.num), start=1):
        app_node = i3.get_tree().find_by_id(ws.focused)
        desired_app_name = APP_NAME_MAPPING.get(app_node.app_id if app_node else None, "MysteryBox")
        _, current_name = extract_prefix_and_name(ws.name)

        # Rename only if the desired name is different from the current name
        if desired_app_name != current_name:
            rename_workspace_with_prefix(i3, str(counter), desired_app_name)


if __name__ == "__main__":
    i3 = i3ipc.Connection()
    initialize_workspaces(i3)
    i3.on('window::focus', on_window_focus)
    i3.on('workspace::init', on_new_workspace_init)
    i3.main()
