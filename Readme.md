Graph Extractor
===============

A simple program that allows to extract coordinates from an image of a graph.

Usage
-----

After opening the image it is possible to right click on a point to bring the contextual menu. Select four points for the minimal / maximal coordinate for x / y axes. After all coordinates are selected, a grid will be shown over the image. The text field on the bottom shows the coordinates at mouse position.

Through the contextual menu it is possible to set the logarithmic scale for one or both axes.

It is possible to select multiple points on the graph by clicking on it. It is possible to compute the length of the path going through all the points, and the area of the corresponding polygon.

Installation
------------

This program depends on [Python][python] and on the library [PyQt 5][pyqt5].

In order to run the program first a couple of files must be processed by PyQt. Run the commands

    pyuic5 MainWindow.ui -o ui_MainWindow.py
    pyuic5 SettingsDialog.ui -o ui_SettingsDialog.py
    pyrcc5 icons.qrc -o icons_rc.py

The the program can be started with the command

    python main.py

or by double clicking the file `main.py`.

[python]: http://www.python.org/
[pyqt5]: http://www.riverbankcomputing.com/software/pyqt/intro
