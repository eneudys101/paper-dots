import sys
import i3ipc

def navigate_to_workspace_by_position(position):
     i3 = i3ipc.Connection()
    # Get the list of workspaces
    workspaces = i3.get_workspaces()

    # Sort workspaces by their numerical position
    sorted_workspaces = sorted(workspaces, key=lambda ws: ws.num)

    try:
        # Get the name of the workspace at the desired position
        target_workspace = sorted_workspaces[position].name
    except IndexError:
        # Create a new workspace with a unique name
        last_workspace_num = sorted_workspaces[-1].num if sorted_workspaces else 0
        target_workspace = f"Workspace-{last_workspace_num + 1}"

    # Switch to the desired workspace
    i3.command(f'workspace "{target_workspace}"')

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Provide a workspace position")
        sys.exit(1)

    position = int(sys.argv[1]) - 1  # 0-indexed
    navigate_to_workspace_by_position(position)
