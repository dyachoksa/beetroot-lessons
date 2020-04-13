import sys

# from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5.QtGui import QStandardItemModel, QStandardItem

from notes_ui import Ui_MainWindow

# Form, Window = uic.loadUiType("notes.ui")


# class AppWindow(Window):
#     def __init__(self):
#         super().__init__()

#     def showInfo(self):
#         QMessageBox.about(self, "Notes App", "This is a simple notes app")

#     def onNoteSelected(self, item):
#         print(item)


# class AppForm(Form):
#     def __init__(self):
#         super().__init__()

#         self.window = AppWindow()
#         self.setupUi(self.window)

#         listModel = QStandardItemModel()
#         listModel.appendRow(QStandardItem("First item"))
#         listModel.appendRow(QStandardItem("Second item"))

#         self.listView.setModel(listModel)

#     def showWindow(self):
#         self.window.show()


class ApplicationMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()

        self.setupUi(self)

        listModel = QStandardItemModel()
        listModel.appendRow(QStandardItem("First item"))
        listModel.appendRow(QStandardItem("Second item"))

        self.listView.setModel(listModel)

    def showInfo(self):
        QMessageBox.about(self, "Notes App", "This is a simple notes app")

    def onNoteSelected(self, item):
        print(item)


app = QApplication(sys.argv)

# form = AppForm()
# form.showWindow()

win = ApplicationMainWindow()
win.show()

app.exec_()
