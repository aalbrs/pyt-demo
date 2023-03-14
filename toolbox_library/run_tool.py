import arcpy

# The main executor, move most logic here.
# This script is used by the debugger as well as the actual toolbox.

def log(message):
    print(message)
    arcpy.AddMessage(message)

def do_execute(text, workspace_path):
    log(f"Text input: {text}")
    log(f"Workspace input: {workspace_path}")

