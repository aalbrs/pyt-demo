import arcpy
import toolbox_library.run_tool as run_tool


# set up variables used for testing/debugging
debug_text = "123"
debug_workspace = "C:/Temp/Data.gdb"


def debug():
    # execute in similar way as toolbox
    run_tool.do_execute(debug_text, debug_workspace)


# this part just makes sure you mean to be calling the debug script
if __name__ == "__main__":
    debug()
