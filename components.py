from PySide6.QtWidgets import QPlainTextEdit, QPushButton, QFileDialog
from pathlib import Path
from urllib.parse import unquote

class PlainTextEditFile(QPlainTextEdit):
    def __init__(self, parent):
        super().__init__(parent=parent)
        self.setAcceptDrops(True)
        self.button = None

    def setButton(self, button:QPushButton):
        self.button = button
        self.button.clicked.connect(self.onClick)

    def dragEnterEvent(self, e, /):
        e.accept()

    def dropEvent(self, e, /):
        unparse = unquote(e.mimeData().text().replace("file:", "")).strip()
        path = Path(unparse)

        super().dropEvent(e)
        self.setPlainText(path.read_text(encoding="utf-8"))

    def onClick(self):
        filepath, ok = QFileDialog.getOpenFileUrl(
            self,
            "Select a file"
        )

        if ok:
            self.setPlainText(Path(filepath.path()).read_text())