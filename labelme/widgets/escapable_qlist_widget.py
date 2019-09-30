from qtpy.QtCore import Qt
from qtpy import QtWidgets


class EscapableQListWidget(QtWidgets.QListWidget):

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.clearSelection()

if __name__ == '__main__':

    import sys
    from PyQt5.QtWidgets import *

    app = QtWidgets.QApplication(sys.argv)
    win = QtWidgets.QMainWindow()
    list = EscapableQListWidget()
    list.addItem(QListWidgetItem('显示'))
    win.setCentralWidget(list)
    win.show()
    win.raise_()
    sys.exit(app.exec_())