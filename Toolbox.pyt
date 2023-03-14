# -*- coding: utf-8 -*-

import arcpy
import toolbox_library.run_tool as run_tool


class Toolbox(object):
    def __init__(self):
        """Define the toolbox (the name of the toolbox is the name of the
        .pyt file)."""
        self.label = "Toolbox"
        self.alias = "toolbox"

        # List of tool classes associated with this toolbox
        self.tools = [Tool]


class Tool(object):
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "Demo Tool"
        self.description = ""
        self.canRunInBackground = True

    def getParameterInfo(self):
        # see for reference
        # https://pro.arcgis.com/en/pro-app/latest/arcpy/geoprocessing_and_python/defining-parameter-data-types-in-a-python-toolbox.htm

        param0 = arcpy.Parameter(
            displayName="Text Example",
            name="text1",
            datatype="GPString",
            parameterType="Optional",
            direction="Input")

        param1 = arcpy.Parameter(
            displayName="Workspace Example",
            name="workspace1",
            datatype="DEWorkspace",
            parameterType="Optional",
            direction="Input")

        params = [param0, param1]
        return params


    def isLicensed(self):
        """Set whether tool is licensed to execute."""
        return True

    def updateParameters(self, parameters):
        """Modify the values and properties of parameters before internal
        validation is performed.  This method is called whenever a parameter
        has been changed."""
        return

    def updateMessages(self, parameters):
        """Modify the messages created by internal validation for each tool
        parameter.  This method is called after internal validation."""
        return

    def execute(self, parameters, messages):
        """The source code of the tool."""

        text1 = parameters[0].valueAsText
        workspace1 = parameters[1].valueAsText

        run_tool.do_execute(text1, workspace1)
        return
