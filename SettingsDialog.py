from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from ui_SettingsDialog import Ui_SettingsDialog
import math
import Settings

class SettingsDialog(QDialog):

    DEFAULT_AXES_COLOR = QColor.fromRgb(255, 0, 0)
    DEFAULT_SAMPLES_COLOR = QColor.fromRgb(0, 0, 255)

    def __init__(self, parent=None):
        super(SettingsDialog, self).__init__(parent)

        self.ui = Ui_SettingsDialog()
        self.ui.setupUi(self)

        self.settings = QSettings()
        self.axesColor = self.settings.value(
            Settings.AXES_COLOR_KEY, Settings.DEFAULT_AXES_COLOR)
        self.samplesColor = self.settings.value(
            Settings.SAMPLES_COLOR_KEY, Settings.DEFAULT_SAMPLES_COLOR)
        self.drawLinesBetweenSamples = self.settings.value(
            Settings.DRAW_LINES_BETWEEN_SAMPLES_KEY, Settings.DEFAULT_DRAW_LINES_BETWEEN_SAMPLES)
        if self.drawLinesBetweenSamples.__class__ == str:
            self.drawLinesBetweenSamples = self.drawLinesBetweenSamples == 'true'

        self.ui.drawLinesCheckBox.setChecked(self.drawLinesBetweenSamples)
        self.colorizeButtons()

    @pyqtSlot()
    def on_axesColorButton_clicked(self):
        color = QColorDialog.getColor(
            self.axesColor, self, '', QColorDialog.ShowAlphaChannel)
        if color.isValid():
            self.axesColor = color
            self.colorizeButtons()

    @pyqtSlot()
    def on_samplesColorButton_clicked(self):
        color = QColorDialog.getColor(
            self.samplesColor, self, '', QColorDialog.ShowAlphaChannel)
        if color.isValid():
            self.samplesColor = color
            self.colorizeButtons()

    @pyqtSlot(bool)
    def on_drawLinesCheckBox_toggled(self, value):
        self.drawLinesBetweenSamples = value

    @pyqtSlot('QAbstractButton*')
    def on_buttonBox_clicked(self, button):
        if self.ui.buttonBox.standardButton(button) == QDialogButtonBox.Save:
            self.settings.setValue(Settings.AXES_COLOR_KEY, self.axesColor)
            self.settings.setValue(Settings.SAMPLES_COLOR_KEY, self.samplesColor)
            self.settings.setValue(Settings.DRAW_LINES_BETWEEN_SAMPLES_KEY,
                self.drawLinesBetweenSamples)

    def colorizeButtons(self):
        pixmap = QPixmap(32, 32)

        pixmap.fill(self.axesColor)
        self.ui.axesColorButton.setIcon(QIcon(pixmap))

        pixmap.fill(self.samplesColor)
        self.ui.samplesColorButton.setIcon(QIcon(pixmap))
