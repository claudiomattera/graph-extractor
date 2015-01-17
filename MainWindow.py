from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QMessageBox, QListWidgetItem
from PyQt5.QtCore import pyqtSlot, QDir, Qt, QSettings, QFileInfo
from SettingsDialog import SettingsDialog
from ui_MainWindow import Ui_MainWindow
import math
import Settings

def areaOfPolygon(vertices):
    vertices.append(vertices[0])
    area = lambda a, b: (b[0] - a[0]) * (a[1] + b[1]) / 2.
    areas = map(lambda i: area(vertices[i], vertices[i+1]), range(len(vertices) - 1))
    return sum(areas)

def lengthOfPath(vertices):
    distance = lambda a, b: math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)
    distances = map(lambda i: distance(vertices[i], vertices[i+1]), range(len(vertices) - 1))
    return sum(distances)

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.settings = QSettings()

        self.ui.exitAction.triggered.connect(QApplication.quit)
        self.ui.zoomInAction.triggered.connect(self.ui.imageLabel.zoomIn)
        self.ui.zoomOutAction.triggered.connect(self.ui.imageLabel.zoomOut)

    @pyqtSlot()
    def on_openAction_triggered(self):
        dir = self.settings.value(
            Settings.LAST_DIRECTORY_KEY, Settings.DEFAULT_LAST_DIRECTORY)
        (filename, _) = QFileDialog.getOpenFileName(
            self,
            self.tr('Open Image'),
            dir,
            self.tr('Images (*.png *.jpg)'))
        if filename:
            self.settings.setValue(
                Settings.LAST_DIRECTORY_KEY, QFileInfo(filename).canonicalPath())
            self.ui.imageLabel.loadImage(filename)
            self.statusBar().showMessage(QDir.toNativeSeparators(filename))

    @pyqtSlot()
    def on_settingsAction_triggered(self):
        settingsDialog = SettingsDialog(self)
        if settingsDialog.exec_():
            self.ui.imageLabel.reset()

    @pyqtSlot()
    def on_clearAction_triggered(self):
        self.ui.listWidget.clear()
        self.ui.imageLabel.clearSamples()

    @pyqtSlot()
    def on_aboutQtAction_triggered(self):
        QMessageBox.aboutQt(self)

    @pyqtSlot()
    def on_aboutAction_triggered(self):
        QMessageBox.about(
            self,
            self.tr('About'),
            self.tr('<h1>%s %s</h1>\n' +
                    '<p>Developed by <a href="%s">%s</a></p>') %
                        (QApplication.applicationName(),
                         QApplication.applicationVersion(),
                         QApplication.organizationDomain(),
                         QApplication.organizationName()
                         ))

    @pyqtSlot()
    def on_pathLengthAction_triggered(self):
        items = self.ui.listWidget.findItems('*', Qt.MatchWildcard)
        coordinates = list(map(lambda item: (item.data(Qt.UserRole), item.data(Qt.UserRole + 1)), items))
        totalDistance = lengthOfPath(coordinates)
        QMessageBox.information(
            self,
            self.tr('Path Length'),
            self.tr("The path's length is %f" % totalDistance)
            )

    @pyqtSlot()
    def on_polygonAreaAction_triggered(self):
        items = self.ui.listWidget.findItems('*', Qt.MatchWildcard)
        coordinates = list(map(lambda item: (item.data(Qt.UserRole), item.data(Qt.UserRole + 1)), items))
        totalArea = areaOfPolygon(coordinates)
        QMessageBox.information(
            self,
            self.tr('Polygon Area'),
            self.tr("The polygon's area is %f" % totalArea)
            )

    @pyqtSlot(float, float)
    def on_imageLabel_mouseMoved(self, x, y):
        self.ui.coordinatesLineEdit.setText("%f × %f" % (x, y))

    @pyqtSlot(float, float)
    def on_imageLabel_clicked(self, x, y):
        item = QListWidgetItem("%f × %f" % (x, y))
        item.setData(Qt.UserRole, x)
        item.setData(Qt.UserRole + 1, y)
        self.ui.listWidget.addItem(item)


if __name__ == '__main__':
    vertices = [(0.72, 2.28), (2.66, 4.71), (5., 3.5), (3.63, 2.52), (4., 1.6), (1.9,  1.)]
    expectedArea = 8.3593
    area = areaOfPolygon(vertices)
    print("%f =?=\n%f" % (area, expectedArea))
