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
        # First switch to the highest-numbered workspace to ensure the new one is on the right.
        if sorted_workspaces:
            highest_workspace = sorted_workspaces[-1].name
            i3.command(f'workspace "{highest_workspace}"')
        # Now, create the new workspace with the name corresponding to its position.
        i3.command(f'workspace "{position + 1}"')

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Provide a workspace position")
        sys.exit(1)

    position = int(sys.argv[1]) - 1  # 0-indexed
    navigate_to_workspace_by_position(position)
