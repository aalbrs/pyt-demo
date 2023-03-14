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
        self.description = "Demonstrates accessing a map within a project (.aprx file)"
        self.canRunInBackground = True

    def getParameterInfo(self):
        # see for reference
        # https://pro.arcgis.com/en/pro-app/latest/arcpy/geoprocessing_and_python/defining-parameter-data-types-in-a-python-toolbox.htm

        param0 = arcpy.Parameter(
            displayName="Map Name",
            name="map_name",
            datatype="GPString",
            parameterType="Optional",
            direction="Input")

        param1 = arcpy.Parameter(
            displayName="Project Containing Map (Filepath or \"CURRENT\")",
            name="proj_path",
            datatype="GPString",
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

        # gather parameters by index
        map_name = parameters[0].valueAsText
        project_path = parameters[1].valueAsText

        # We want to pass a project object to the main script, rather than text.
        # Note that "CURRENT" will access current project in Pro.
        project = None
        if project_path:
            project = arcpy.mp.ArcGISProject(project_path)

        # call our main script
        run_tool.do_execute(map_name, project)
