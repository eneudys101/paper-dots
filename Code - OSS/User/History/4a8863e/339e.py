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
        # If the desired position is out of the bounds, create a new workspace.
        # The new workspace name corresponds to its position + 1 (because of 0-index).
        new_workspace_name = str(position + 1)
        i3.command(f'workspace "{new_workspace_name}"')

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Provide a workspace position")
        sys.exit(1)

    position = int(sys.argv[1]) - 1  # 0-indexed
    navigate_to_workspace_by_position(position)
