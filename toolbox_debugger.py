import arcpy
import toolbox_library.run_tool as run_tool


# set up variables used for testing/debugging
# 1) a map name:
debug_map_name = "Map"
# 2) point to a project containing map above
debug_project_path = None


def debug():
    # main debug method, start with a breakpoint here

    # first get project from path above, if provided
    project = None
    if debug_project_path:
        arcpy.mp.ArcGISProject(debug_project_path)
    # execute in similar way as toolbox
    run_tool.do_execute(debug_map_name, project)


# this part just makes sure you mean to be calling the debug script
if __name__ == "__main__":
    debug()
