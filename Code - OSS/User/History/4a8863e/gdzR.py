#!/usr/bin/env python3
import sys
import i3ipc

def navigate_to_workspace_by_position(position):
    i3 = i3ipc.Connection()
    # Get the list of workspaces
    workspaces = i3.get_workspaces()

    # Sort workspaces by their numerical position
    sorted_workspaces = sorted(workspaces, key=lambda ws: ws.num)

    if position < len(sorted_workspaces):
        # Get the name of the workspace at the desired position
        target_workspace = sorted_workspaces[position].name
        # Switch to the desired workspace
        i3.command(f'workspace "{target_workspace}"')
    else:
        # If the desired position is out of the bounds, create a new workspace
        if sorted_workspaces:
            new_workspace_num = sorted_workspaces[-1].num + 1
        else:
            new_workspace_num = 1  # Default to the first workspace if none exist
        i3.command(f'workspace "{new_workspace_num}"')

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