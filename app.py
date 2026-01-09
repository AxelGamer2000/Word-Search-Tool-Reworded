import sys, api, pathlib, subprocess
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QStyleFactory
from pyui.wst import Ui_SearchWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_SearchWindow()
        self.ui.setupUi(self)
        self.setWindowTitle(api.getSettingsKeyOrDefault("title", "Word Search Tool: Reworded"))

        self.ui.replaceButton.clicked.connect(self.replaceEvent)
        self.ui.removeButton.clicked.connect(self.removeEvent)
        self.ui.searchButton.clicked.connect(self.searchEvent)

        self.ui.editorTabButton.clicked.connect(lambda toEditor: self.ui.stackedWidget.setCurrentIndex(1))
        self.ui.searchTabButton.clicked.connect(lambda toSearch: self.ui.stackedWidget.setCurrentIndex(0))
        self.ui.settingsTabButton.clicked.connect(self.openSettings)

        self.ui.exportButton.clicked.connect(self.exportEvent)
        self.ui.importButton.clicked.connect(self.importEvent)
        self.ui.newButton.clicked.connect(self.newEvent)
        self.ui.saveButton.clicked.connect(self.saveEvent)

        self.isSaved = False
        self.fileSaved: pathlib.Path = None

    def openEditor(self, content:str):
        self.clear()
        self.ui.stackedWidget.setCurrentIndex(1)
        self.ui.editPlainEdit.setPlainText(content)

    def clear(self):
        self.ui.editPlainEdit.setPlainText("")
        self.ui.targetPlainEdit.setPlainText("")
        self.ui.sourcePlainEdit.setPlainText("")
        self.ui.newLineEdit.setText("")

    def replaceEvent(self):
        source = self.ui.sourcePlainEdit.toPlainText()
        new = self.ui.newLineEdit.text()
        target = self.ui.targetPlainEdit.toPlainText()

        targets = target.split(", ")
        news = new.split(", ")

        self.openEditor(api.replaceAll(targets, news, source))

    def removeEvent(self):
        source = self.ui.sourcePlainEdit.toPlainText()
        target = self.ui.targetPlainEdit.toPlainText()

        targets = target.split(", ")

        self.openEditor(api.removeAll(targets, source))

    def searchEvent(self):
        source = self.ui.sourcePlainEdit.toPlainText()
        target = self.ui.targetPlainEdit.toPlainText()

        targets = target.split(", ")

        self.openEditor(api.searchAll(targets, source))

    def exportEvent(self):
        self.isSaved = True
        self.fileSaved = pathlib.Path(QFileDialog.getSaveFileUrl(
            self,
            "Save file"
        )[0].path())

        self.fileSaved.write_text(self.ui.editPlainEdit.toPlainText())
        self.ui.fileNameLabel.setText(self.fileSaved.name)

        self.ui.saveButton.setEnabled(True)

    def importEvent(self):
        self.isSaved = True
        self.fileSaved = pathlib.Path(QFileDialog.getOpenFileUrl(
            self,
            "Open file"
        )[0].path())

        self.ui.editPlainEdit.setPlainText(self.fileSaved.read_text("utf-8"))
        self.ui.fileNameLabel.setText(self.fileSaved.name)

        self.ui.saveButton.setEnabled(True)

    def newEvent(self):
        self.isSaved = False
        self.fileSaved = None

        self.ui.editPlainEdit.setPlainText("")
        self.ui.fileNameLabel.setText("None")

        self.ui.saveButton.setEnabled(False)

    def saveEvent(self):
        if self.isSaved:
            self.fileSaved.write_text(self.ui.editPlainEdit.toPlainText())

    def openSettings(self):
        self.close()
        subprocess.run([sys.executable, "settings.py"], cwd="pyui")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()

    window.show()
    sys.exit(app.exec())