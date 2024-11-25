Install with terminal the following command:

pip install pygubu-designer

After installed, in your terminal, type the following command:

pygubu-designer

The Pygubu Designer will open. In the Pygubu Designer, you can create a GUI by dragging and dropping widgets.
You can also generate the Python code for the GUI you created.

You will need a directory with the following files:
EXAMPLE.ui
EXAMPLE.py

You will use the generated .ui code from the pygubu-designer to create the GUI in Python.

The EXAMPLE.py file will contain the following code at the start:

#!/usr/bin/python3
import pathlib
import pygubu

PROJECT_PATH = pathlib.Path(__file__).parent
PROJECT_UI = PROJECT_PATH / "demo1.ui"

____________________________________________________________________________________________________________________
