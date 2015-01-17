from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QIcon
from MainWindow import MainWindow

if __name__ == '__main__':
    import sys

    application = QApplication(sys.argv)
    application.setApplicationName('Graph Extractor')
    application.setApplicationVersion('0.1')
    application.setOrganizationName('Claudio Mattera')
    application.setOrganizationDomain('http://claudio.no-ip.org/')

    mainWindow = MainWindow()
    mainWindow.setWindowIcon(QIcon(":/images/graph.svg"))
    mainWindow.show()

    sys.exit(application.exec_())
