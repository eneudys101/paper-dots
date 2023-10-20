import i3ipc

APP_NAME_MAPPING = {
    "firefox": "\uf269",
    "kitty": "\ue795",
    "code-oss": "\udb80\ude2e"
}

def extract_prefix_and_name(workspace_name):
    parts = workspace_name.split(":", 1)
    if len(parts) < 2:
        return None, None
    return parts[0], parts[1].strip()

def get_app_name(i3):
    app_id = i3.get_tree().find_focused().app_id
    return APP_NAME_MAPPING.get(app_id, "MysteryBox")

def shift_workspaces_up(i3):
    workspaces = sorted(i3.get_workspaces(), key=lambda ws: ws.num, reverse=True)
    for ws in workspaces:
        prefix, name = extract_prefix_and_name(ws.name)
        if prefix:
            new_prefix = str(int(prefix) + 1)
            i3.command(f'rename workspace "{ws.name}" to "{new_prefix}:{name}"')

def on_window_focus(i3, e):
    prefix, _ = extract_prefix_and_name(i3.get_tree().find_focused().workspace().name)
    if prefix:
        new_name = get_app_name(i3)
        i3.command(f'rename workspace to "{prefix}:{new_name}"')

def on_new_workspace_init(i3, e):
    shift_workspaces_up(i3)
    i3.command(f'rename workspace "{e.current.name}" to "1: Empty"')

def initialize_workspaces(i3):
    workspaces = sorted(i3.get_workspaces(), key=lambda ws: ws.num)
    for index, ws in enumerate(workspaces, start=1):
        app_node = i3.get_tree().find_by_id(ws.focused)
        app_name = APP_NAME_MAPPING.get(app_node.app_id if app_node else None, "MysteryBox")
        i3.command(f'rename workspace "{ws.name}" to "{index}:{app_name}"')

if __name__ == "__main__":
    i3 = i3ipc.Connection()
    initialize_workspaces(i3)
    i3.on('window::focus', on_window_focus)
    i3.on('workspace::init', on_new_workspace_init)
    i3.main()
