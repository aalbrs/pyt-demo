# ArcGIS Pro Python Toolbox Demo

A starting point for .pyt (Python Toolbox) files for use in ArcGIS Pro, with a separate debugger script to make things easy. 

The debugger can be used directly in PyCharm, VS Code, or your favourite Python IDE. Just set your Python environment to use ArcGIS Pro, for Windows this is usually:  
```
C:\Program Files\ArcGIS\Pro\bin\Python\envs\arcgispro-py3\python.exe
```
Then run/debug the module:  
```
toolbox_debugger.py
```
Where possible logic should be written outside of the .pyt file, such as in the toolbox_library directory.  
