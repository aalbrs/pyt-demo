import arcpy


# The main executor, move most logic here.
# This script is used by the debugger as well as the actual toolbox.

def log(message):
    arcpy.AddMessage(message)


def do_execute(map_name: str, project: object):

    log(f"Map name (text): {map_name}")
    if not project:
        log(f"No project supplied. Enter a filepath to a project file (.aprx), or \"CURRENT\" if running from Pro.")
    else:
        log(f"Project file: {project.filePath}")
        log(f"Searching for map in project...")
        m = get_map(project, map_name)
        log(f"Found map \"{m.name}\"")


def get_map(project, map_name):
    maps = [m for m in project.listMaps() if m.name.lower() == map_name.lower()]
    if len(maps) == 0:
        # raising an exception can be useful when input is invalid and we don't want to continue
        raise Exception(f"No map found \"{map_name}\" in this project")
    return maps[0]

