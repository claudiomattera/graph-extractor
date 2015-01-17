from PyQt5.QtCore import QDir
from PyQt5.QtGui import QColor

AXES_COLOR_KEY = 'axesColor'
DEFAULT_AXES_COLOR = QColor.fromRgb(255, 0, 0)

SAMPLES_COLOR_KEY = 'samplesColor'
DEFAULT_SAMPLES_COLOR = QColor.fromRgb(0, 0, 255)

LAST_DIRECTORY_KEY = 'lastDirectory'
DEFAULT_LAST_DIRECTORY = QDir.home().canonicalPath()

DRAW_LINES_BETWEEN_SAMPLES_KEY = 'drawLinesBetweenSamples'
DEFAULT_DRAW_LINES_BETWEEN_SAMPLES = True
