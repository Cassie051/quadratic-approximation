import sys
from PyQt5 import QtWidgets

from modules.app import Ui_MainWindow
from modules.plot_widget import MplWidget

def main():
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()