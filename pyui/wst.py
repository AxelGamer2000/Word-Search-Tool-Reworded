# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'searchTabohWlaF.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QMenuBar, QPlainTextEdit, QPushButton, QSizePolicy,
    QStackedWidget, QStatusBar, QWidget)

from components import PlainTextEditFile
import darkdetect

darkOrLight = "dark" if darkdetect.isDark() else "light"

class Ui_SearchWindow(object):
    def setupUi(self, SearchWindow):
        if not SearchWindow.objectName():
            SearchWindow.setObjectName(u"SearchWindow")
        SearchWindow.resize(800, 600)
        SearchWindow.setAutoFillBackground(False)
        self.centralwidget = QWidget(SearchWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.searchTabButton = QPushButton(self.centralwidget)
        self.searchTabButton.setObjectName(u"searchTabButton")
        self.searchTabButton.setEnabled(True)
        self.searchTabButton.setGeometry(QRect(0, 0, 91, 91))
        self.searchTabButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon = QIcon()
        icon.addFile(f"icon/{darkOrLight}-search.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.searchTabButton.setIcon(icon)
        self.searchTabButton.setIconSize(QSize(64, 64))
        self.editorTabButton = QPushButton(self.centralwidget)
        self.editorTabButton.setObjectName(u"editorTabButton")
        self.editorTabButton.setGeometry(QRect(0, 90, 91, 91))
        self.editorTabButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(f"icon/{darkOrLight}-editor.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.editorTabButton.setIcon(icon1)
        self.editorTabButton.setIconSize(QSize(64, 64))
        self.settingsTabButton = QPushButton(self.centralwidget)
        self.settingsTabButton.setObjectName(u"settingsTabButton")
        self.settingsTabButton.setGeometry(QRect(0, 180, 91, 91))
        self.settingsTabButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(f"icon/{darkOrLight}-settings.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.settingsTabButton.setIcon(icon2)
        self.settingsTabButton.setIconSize(QSize(64, 64))
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(100, 0, 701, 571))
        self.searchTab = QWidget()
        self.searchTab.setObjectName(u"searchTab")
        self.label = QLabel(self.searchTab)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(230, 20, 66, 18))
        self.label_2 = QLabel(self.searchTab)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(230, 290, 66, 18))
        self.newLineEdit = QLineEdit(self.searchTab)
        self.newLineEdit.setObjectName(u"newLineEdit")
        self.newLineEdit.setGeometry(QRect(230, 230, 241, 26))
        self.label_3 = QLabel(self.searchTab)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(230, 210, 66, 18))
        self.sourcePlainEdit = PlainTextEditFile(self.searchTab)
        self.sourcePlainEdit.setObjectName(u"sourcePlainEdit")
        self.sourcePlainEdit.setGeometry(QRect(230, 40, 241, 111))
        self.removeButton = QPushButton(self.searchTab)
        self.removeButton.setObjectName(u"removeButton")
        self.removeButton.setGeometry(QRect(280, 510, 151, 41))
        self.removeButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.replaceButton = QPushButton(self.searchTab)
        self.replaceButton.setObjectName(u"replaceButton")
        self.replaceButton.setGeometry(QRect(130, 510, 151, 41))
        self.replaceButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.sourcePickFileButton = QPushButton(self.searchTab)
        self.sourcePickFileButton.setObjectName(u"sourcePickFileButton")
        self.sourcePickFileButton.setGeometry(QRect(230, 150, 241, 31))
        self.sourcePickFileButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.searchButton = QPushButton(self.searchTab)
        self.searchButton.setObjectName(u"searchButton")
        self.searchButton.setGeometry(QRect(430, 510, 151, 41))
        self.searchButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.targetPlainEdit = PlainTextEditFile(self.searchTab)
        self.targetPlainEdit.setObjectName(u"targetPlainEdit")
        self.targetPlainEdit.setGeometry(QRect(230, 310, 241, 111))
        self.targetPickFileButton = QPushButton(self.searchTab)
        self.targetPickFileButton.setObjectName(u"targetPickFileButton")
        self.targetPickFileButton.setGeometry(QRect(230, 420, 241, 31))
        self.targetPickFileButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.stackedWidget.addWidget(self.searchTab)
        self.editorTab = QWidget()
        self.editorTab.setObjectName(u"editorTab")
        self.saveButton = QPushButton(self.editorTab)
        self.saveButton.setObjectName(u"saveButton")
        self.saveButton.setEnabled(False)
        self.saveButton.setGeometry(QRect(550, 190, 131, 26))
        self.saveButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.fileNameLabel = QLabel(self.editorTab)
        self.fileNameLabel.setObjectName(u"fileNameLabel")
        self.fileNameLabel.setGeometry(QRect(20, 10, 661, 18))
        self.exportButton = QPushButton(self.editorTab)
        self.exportButton.setObjectName(u"exportButton")
        self.exportButton.setGeometry(QRect(550, 70, 131, 26))
        self.exportButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.editPlainEdit = QPlainTextEdit(self.editorTab)
        self.editPlainEdit.setObjectName(u"editPlainEdit")
        self.editPlainEdit.setGeometry(QRect(20, 30, 511, 521))
        self.newButton = QPushButton(self.editorTab)
        self.newButton.setObjectName(u"newButton")
        self.newButton.setGeometry(QRect(550, 110, 131, 26))
        self.newButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.importButton = QPushButton(self.editorTab)
        self.importButton.setObjectName(u"importButton")
        self.importButton.setGeometry(QRect(550, 30, 131, 26))
        self.importButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.stackedWidget.addWidget(self.editorTab)
        SearchWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(SearchWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 23))
        SearchWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(SearchWindow)
        self.statusbar.setObjectName(u"statusbar")
        SearchWindow.setStatusBar(self.statusbar)

        self.retranslateUi(SearchWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(SearchWindow)
    # setupUi

    def retranslateUi(self, SearchWindow):
        SearchWindow.setWindowTitle(QCoreApplication.translate("SearchWindow", u"MainWindow", None))
        self.searchTabButton.setText("")
        self.editorTabButton.setText("")
        self.settingsTabButton.setText("")
        self.label.setText(QCoreApplication.translate("SearchWindow", u"Source", None))
        self.label_2.setText(QCoreApplication.translate("SearchWindow", u"Target", None))
        self.label_3.setText(QCoreApplication.translate("SearchWindow", u"New", None))
        self.removeButton.setText(QCoreApplication.translate("SearchWindow", u"Remove", None))
        self.replaceButton.setText(QCoreApplication.translate("SearchWindow", u"Replace", None))
        self.sourcePickFileButton.setText(QCoreApplication.translate("SearchWindow", u"Pick file", None))
        self.searchButton.setText(QCoreApplication.translate("SearchWindow", u"Search", None))
        self.targetPickFileButton.setText(QCoreApplication.translate("SearchWindow", u"Pick file", None))
        self.saveButton.setText(QCoreApplication.translate("SearchWindow", u"Save", None))
        self.fileNameLabel.setText(QCoreApplication.translate("SearchWindow", u"None", None))
        self.exportButton.setText(QCoreApplication.translate("SearchWindow", u"Export", None))
        self.newButton.setText(QCoreApplication.translate("SearchWindow", u"New", None))
        self.importButton.setText(QCoreApplication.translate("SearchWindow", u"Import", None))

        self.sourcePlainEdit.setButton(self.sourcePickFileButton)
        self.targetPlainEdit.setButton(self.targetPickFileButton)
    # retranslateUi

