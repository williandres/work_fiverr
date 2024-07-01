from PyQt6 import QtCore, QtGui, QtWidgets
from play import EventReplayer
import sources.ui.base_rc
import record_control
import json

class Ui_Main(object):
        #Test --> Delay bar
        def update_delay_label(self, value):
                self.seconds.setText(f"{value / 10:.1f}")

        #Test --> Play
        def handle_play_button(self):
                filename = self.lineEdit.text()
                executable = self.textBrowser_4.toPlainText()
                extra_delay = float(self.seconds.text())

                if not filename or not executable:
                        QtWidgets.QMessageBox.warning(None, "Error", "Both filename and executable must be filled.")
                        return

                replayer = EventReplayer()
                replayer.replay_events(filename, executable,extra_delay)
                print('Successfull execution')



        #Test --> Browse Files
        def selectFileSearch(self):
                file_dialog = QtWidgets.QFileDialog()
                file_dialog.setDirectory('sources/profiles')
                file_path, _ = file_dialog.getOpenFileName(filter="JSON files (*.json)")

                if file_path:
                        try:
                                with open(file_path, 'r') as file:
                                        data = json.load(file)
                                if isinstance(data, list) and data and 'key' in data[0] and data[0]['key'] == 'RestRobo':
                                        #Filename
                                        self.lineEdit.setText(file_path)
                                        #Description
                                        tittle = data[0]['tittle']
                                        description = data[0]['description']
                                        date = data[0]['creation date']
                                        self.textBrowser.setText(tittle + '\n\n' + description + '\n\n' + date)
                                        #App
                                        self.textBrowser_4.setText(data[0]['app'])
                                else:
                                        QtWidgets.QMessageBox.warning(None, "Error", "The JSON is not in the expected format.")
                        except json.JSONDecodeError:
                                QtWidgets.QMessageBox.warning(None, "Error", "The selected file is not a valid JSON.")
                        except Exception as e:
                                QtWidgets.QMessageBox.warning(None, "Error", f"An error has occurred: {e}")
                #Description
                self.textBrowser
                #App
                self.textBrowser_4

        #Record --> Browse files
        def selectFile(self):
                file_dialog = QtWidgets.QFileDialog()
                file_path, _ = file_dialog.getOpenFileName()
                if file_path:
                       self.iexecutable.setText(file_path)

        #Record --> Button Save
        def handle_save_button(self):
                name = self.iname.text()
                description = self.idescription.toPlainText()
                executable = self.iexecutable.text()
                res = record_control.record_steps(name, description, executable)
                print('RECORD +')
                print(f"Name: {name}, Description: {description}, Executable: {executable}")
                print("Status: ", str(res))
                if res[0] != 5:
                        QtWidgets.QMessageBox.warning(None, "Error", res[1])
                if res[0] == 5:
                        QtWidgets.QMessageBox.warning(None, "Saved", res[1])
                print('________________________________________')

        def setupUi(self, Main):
                #Main window
                Main.setObjectName("Main")
                Main.setEnabled(True)
                Main.resize(569, 521)
                Main.setMinimumSize(QtCore.QSize(569, 521))
                Main.setMaximumSize(QtCore.QSize(569, 521))
                icon = QtGui.QIcon()
                icon.addPixmap(QtGui.QPixmap(":/header/only logo without name.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
                Main.setWindowIcon(icon)
                Main.setAutoFillBackground(True)
                self.centralwidget = QtWidgets.QWidget(parent=Main)
                self.centralwidget.setObjectName("centralwidget")
                self.frame = QtWidgets.QFrame(parent=self.centralwidget)
                self.frame.setGeometry(QtCore.QRect(0, -20, 601, 571))
                self.frame.setStyleSheet("background-color: rgb(35, 35, 35);")
                self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
                self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
                self.frame.setObjectName("frame")


                #Logo center
                self.resttobologo = QtWidgets.QLabel(parent=self.frame)
                self.resttobologo.setGeometry(QtCore.QRect(220, 10, 131, 111))
                self.resttobologo.setStyleSheet("image: url(:/header/second transparent bg.png);\n"
        "background-color: rgba(35, 35, 35, 0);")
                self.resttobologo.setText("")
                self.resttobologo.setObjectName("resttobologo")

                #Settings button
                self.settings = QtWidgets.QPushButton(parent=self.frame)
                self.settings.setGeometry(QtCore.QRect(490, 50, 31, 31))
                self.settings.setAutoFillBackground(False)
                self.settings.setStyleSheet("\n"
        "border-image: url(:/header/settings.png);\n"
        "")
                self.settings.setText("")
                self.settings.setAutoDefault(False)
                self.settings.setObjectName("settings")

                #by Unwirng Tech
                self.textEdit = QtWidgets.QTextEdit(parent=self.frame)
                self.textEdit.setGeometry(QtCore.QRect(0, 520, 191, 31))
                self.textEdit.setStyleSheet("background-color: rgba(0, 0, 0, 0);\n"
        "color: rgb(110, 110, 110);\n"
        "\n"
        "")
                self.textEdit.setObjectName("textEdit")

                #Main line
                self.line = QtWidgets.QFrame(parent=self.frame)
                self.line.setGeometry(QtCore.QRect(-10, 110, 591, 21))
                self.line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
                self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
                self.line.setObjectName("line")

                #Manager
                self.tabWidget = QtWidgets.QTabWidget(parent=self.frame)
                self.tabWidget.setGeometry(QtCore.QRect(30, 140, 511, 361))
                self.tabWidget.setStatusTip("")
                self.tabWidget.setStyleSheet("")
                self.tabWidget.setTabPosition(QtWidgets.QTabWidget.TabPosition.North)
                self.tabWidget.setTabShape(QtWidgets.QTabWidget.TabShape.Rounded)
                self.tabWidget.setIconSize(QtCore.QSize(12, 12))
                self.tabWidget.setElideMode(QtCore.Qt.TextElideMode.ElideMiddle)
                self.tabWidget.setUsesScrollButtons(True)
                self.tabWidget.setDocumentMode(False)
                self.tabWidget.setTabsClosable(False)
                self.tabWidget.setMovable(False)
                self.tabWidget.setTabBarAutoHide(False)
                self.tabWidget.setObjectName("tabWidget")

                #Active Schedule
                self.schedtab = QtWidgets.QWidget()
                self.schedtab.setStyleSheet("\n"
        "background-color: rgba(64, 156, 159, 7);")
                self.schedtab.setObjectName("schedtab")
                        #Table Widget
                self.tableWidget = QtWidgets.QTableWidget(parent=self.schedtab)
                self.tableWidget.setGeometry(QtCore.QRect(30, 20, 451, 261))
                self.tableWidget.setStyleSheet("background-color: rgb(23, 23, 23);")
                self.tableWidget.setObjectName("tableWidget")
                self.tableWidget.setColumnCount(4)
                self.tableWidget.setRowCount(0)
                item = QtWidgets.QTableWidgetItem()
                self.tableWidget.setHorizontalHeaderItem(0, item)
                item = QtWidgets.QTableWidgetItem()
                self.tableWidget.setHorizontalHeaderItem(1, item)
                item = QtWidgets.QTableWidgetItem()
                self.tableWidget.setHorizontalHeaderItem(2, item)
                item = QtWidgets.QTableWidgetItem()
                self.tableWidget.setHorizontalHeaderItem(3, item)
                        #Buttons
                self.horizontalLayoutWidget = QtWidgets.QWidget(parent=self.schedtab)
                self.horizontalLayoutWidget.setGeometry(QtCore.QRect(30, 289, 451, 31))
                self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
                self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
                self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
                self.horizontalLayout.setObjectName("horizontalLayout")
                        #Add
                self.pushButton_2 = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget)
                self.pushButton_2.setStyleSheet("background-color: rgb(62, 62, 62);\n"
        "border-color: rgb(49, 45, 45);")
                icon1 = QtGui.QIcon()
                icon1.addPixmap(QtGui.QPixmap(":/header/file-add_114479.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
                self.pushButton_2.setIcon(icon1)
                self.pushButton_2.setObjectName("pushButton_2")
                self.horizontalLayout.addWidget(self.pushButton_2)
                spacerItem = QtWidgets.QSpacerItem(90, 20, QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Minimum)
                self.horizontalLayout.addItem(spacerItem)
                        #Remove
                self.pushButton_3 = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget)
                self.pushButton_3.setStyleSheet("background-color: rgb(62, 62, 62);\n"
        "border-color: rgb(49, 45, 45);")
                icon2 = QtGui.QIcon()
                icon2.addPixmap(QtGui.QPixmap(":/header/file-delete_114438.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
                self.pushButton_3.setIcon(icon2)
                self.pushButton_3.setObjectName("pushButton_3")
                self.horizontalLayout.addWidget(self.pushButton_3)
                        #Other config
                icon3 = QtGui.QIcon()
                icon3.addPixmap(QtGui.QPixmap(":/header/clock_icon-icons.com_54407.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
                self.tabWidget.addTab(self.schedtab, icon3, "")
                
                #Record
                self.rectab = QtWidgets.QWidget()
                self.rectab.setStyleSheet("\n"
        "background-color: rgba(71, 71, 53, 25);")
                self.rectab.setObjectName("rectab")
                        #Form
                self.formLayoutWidget = QtWidgets.QWidget(parent=self.rectab)
                self.formLayoutWidget.setGeometry(QtCore.QRect(10, 100, 331, 211))
                self.formLayoutWidget.setObjectName("formLayoutWidget")
                self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
                self.formLayout.setContentsMargins(0, 0, 0, 0)
                self.formLayout.setObjectName("formLayout")
                                #Name Label
                self.name = QtWidgets.QLabel(parent=self.formLayoutWidget)
                self.name.setStyleSheet("background-color: rgba(191, 64, 64, 0);\n"
        "font: 12pt \"Ubuntu\";")
                self.name.setObjectName("name")
                self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.name)
                                #Description Label
                self.description = QtWidgets.QLabel(parent=self.formLayoutWidget)
                self.description.setStyleSheet("font: 12pt \"Ubuntu\";\n"
        "background-color: rgba(191, 64, 64, 0);")
                self.description.setObjectName("description")
                self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.description)
                                #Executable Label
                self.executable = QtWidgets.QLabel(parent=self.formLayoutWidget)
                self.executable.setStyleSheet("font: 12pt \"Ubuntu\";\n"
        "background-color: rgba(191, 64, 64, 0);")
                self.executable.setObjectName("executable")
                self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.executable)
                                #Name Input
                self.iname = QtWidgets.QLineEdit(parent=self.formLayoutWidget)
                self.iname.setStyleSheet("")
                self.iname.setText("")
                self.iname.setObjectName("iname")
                self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.iname)
                                #Description Input
                self.idescription = QtWidgets.QTextEdit(parent=self.formLayoutWidget)
                self.idescription.setObjectName("idescription")
                self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.idescription)
                                #Executable Input
                self.iexecutable = QtWidgets.QLineEdit(parent=self.formLayoutWidget)
                self.iexecutable.setObjectName("iexecutable")
                self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.iexecutable)
                                #Executable button
                self.browse = QtWidgets.QPushButton(parent=self.formLayoutWidget)
                self.browse.setStyleSheet("background-color: rgb(62, 62, 62);\n"
        "border-color: rgb(49, 45, 45);")
                icon4 = QtGui.QIcon()
                icon4.addPixmap(QtGui.QPixmap(":/header/lupa2.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
                icon4.addPixmap(QtGui.QPixmap(":/header/lupa.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.On)
                self.browse.setIcon(icon4)
                self.browse.setObjectName("browse")
                self.formLayout.setWidget(3, QtWidgets.QFormLayout.ItemRole.FieldRole, self.browse)
                self.browse.clicked.connect(self.selectFile)
                        #Save button
                self.pushButton = QtWidgets.QPushButton(parent=self.rectab)
                self.pushButton.setGeometry(QtCore.QRect(350, 220, 131, 91))
                font = QtGui.QFont()
                font.setFamily("Ubuntu")
                font.setPointSize(18)
                font.setBold(True)
                font.setItalic(False)
                self.pushButton.setFont(font)
                self.pushButton.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.DefaultContextMenu)
                self.pushButton.setStyleSheet("background-color: rgb(36, 139, 33);\n"
        "font: 700 18pt \"Ubuntu\";")
                icon5 = QtGui.QIcon()
                icon5.addPixmap(QtGui.QPixmap(":/header/save2.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
                self.pushButton.setIcon(icon5)
                self.pushButton.setIconSize(QtCore.QSize(40, 40))
                self.pushButton.setFlat(False)
                self.pushButton.setObjectName("pushButton")
                self.pushButton.clicked.connect(self.handle_save_button)
                        #First text box
                self.textBrowser_2 = QtWidgets.QTextBrowser(parent=self.rectab)
                self.textBrowser_2.setGeometry(QtCore.QRect(20, 10, 311, 81))
                self.textBrowser_2.setStyleSheet("background-color: rgba(0, 0, 0, 0);\n"
        "color: rgb(110, 110, 110);\n"
        "\n"
        "")
                self.textBrowser_2.setObjectName("textBrowser_2")
                        #Vertical line
                self.line_2 = QtWidgets.QFrame(parent=self.rectab)
                self.line_2.setGeometry(QtCore.QRect(340, 20, 1, 61))
                self.line_2.setStyleSheet("background-color: rgba(13, 11, 11, 20);\n"
        "")
                self.line_2.setFrameShape(QtWidgets.QFrame.Shape.VLine)
                self.line_2.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
                self.line_2.setObjectName("line_2")
                        #Second text box
                self.textBrowser_3 = QtWidgets.QTextBrowser(parent=self.rectab)
                self.textBrowser_3.setGeometry(QtCore.QRect(350, 10, 131, 191))
                self.textBrowser_3.setStyleSheet("background-color: rgba(0, 0, 0, 0);\n"
        "color: rgb(110, 110, 110);\n"
        "\n"
        "")
                self.textBrowser_3.setObjectName("textBrowser_3")
                        #Other config
                icon6 = QtGui.QIcon()
                icon6.addPixmap(QtGui.QPixmap(":/header/trafficlight-red_40428.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
                self.tabWidget.addTab(self.rectab, icon6, "")

                #Test
                self.testab = QtWidgets.QWidget()
                self.testab.setObjectName("testab")
                        #Form
                self.formLayoutWidget_2 = QtWidgets.QWidget(parent=self.testab)
                self.formLayoutWidget_2.setGeometry(QtCore.QRect(20, 30, 321, 281))
                self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
                self.formLayout_2 = QtWidgets.QFormLayout(self.formLayoutWidget_2)
                self.formLayout_2.setContentsMargins(0, 0, 0, 0)
                self.formLayout_2.setObjectName("formLayout_2")
                                #Name Label
                self.name_2 = QtWidgets.QLabel(parent=self.formLayoutWidget_2)
                self.name_2.setStyleSheet("font: 12pt \"Ubuntu\";")
                self.name_2.setObjectName("name_2")
                self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.name_2)
                                #Name Input
                self.lineEdit = QtWidgets.QLineEdit(parent=self.formLayoutWidget_2)
                self.lineEdit.setObjectName("lineEdit")
                self.lineEdit.setEnabled(False)
                self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.lineEdit)
                                #Description Label
                self.description_2 = QtWidgets.QLabel(parent=self.formLayoutWidget_2)
                self.description_2.setStyleSheet("font: 12pt \"Ubuntu\";")
                self.description_2.setObjectName("description_2")
                self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.ItemRole.LabelRole, self.description_2)
                                #app label
                self.app = QtWidgets.QLabel(parent=self.formLayoutWidget_2)
                self.app.setStyleSheet("font: 12pt \"Ubuntu\";")
                self.app.setObjectName("app")
                self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.ItemRole.LabelRole, self.app)
                                #Search name button
                self.browse_2 = QtWidgets.QPushButton(parent=self.formLayoutWidget_2)
                self.browse_2.setStyleSheet("background-color: rgb(62, 62, 62);\n"
        "border-color: rgb(49, 45, 45);")
                icon7 = QtGui.QIcon()
                icon7.addPixmap(QtGui.QPixmap(":/header/lupa2.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
                self.browse_2.setIcon(icon7)
                self.browse_2.setObjectName("browse_2")
                self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.browse_2)
                self.browse_2.clicked.connect(self.selectFileSearch)
                                #Description Content Box
                self.textBrowser = QtWidgets.QTextBrowser(parent=self.formLayoutWidget_2)
                self.textBrowser.setObjectName("textBrowser")
                self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.ItemRole.FieldRole, self.textBrowser)
                                #Application Content Box
                self.textBrowser_4 = QtWidgets.QTextBrowser(parent=self.formLayoutWidget_2)
                self.textBrowser_4.setObjectName("textBrowser_4")
                self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.ItemRole.FieldRole, self.textBrowser_4)

                        #Play button
                self.play = QtWidgets.QPushButton(parent=self.testab)
                self.play.setGeometry(QtCore.QRect(350, 220, 131, 91))
                self.play.setStyleSheet("background-color: rgb(201, 29, 29);\n"
        "font: 700 18pt \"Ubuntu\";\n"
        "border-color: rgba(191, 64, 64, 0);")
                icon8 = QtGui.QIcon()
                icon8.addPixmap(QtGui.QPixmap(":/header/play_box_icon_138278.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
                self.play.setIcon(icon8)
                self.play.setIconSize(QtCore.QSize(40, 40))
                self.play.setObjectName("play")
                self.play.clicked.connect(self.handle_play_button)
                        #Delay Bar
                self.delaybar = QtWidgets.QSlider(parent=self.testab)
                self.delaybar.setGeometry(QtCore.QRect(360, 190, 101, 16))
                self.delaybar.setMinimum(1)
                self.delaybar.setMaximum(20)
                self.delaybar.setOrientation(QtCore.Qt.Orientation.Horizontal)
                self.delaybar.setObjectName("delaybar")
                self.delaybar.valueChanged.connect(self.update_delay_label)
                        #Seconds content box
                self.seconds = QtWidgets.QLabel(parent=self.testab)
                self.seconds.setGeometry(QtCore.QRect(405, 170, 67, 17))#QtCore.QRect(380, 170, 67, 17)
                self.seconds.setText("0")
                self.seconds.setObjectName("seconds")
                        #delay by action label
                self.label = QtWidgets.QLabel(parent=self.testab)
                self.label.setGeometry(QtCore.QRect(365, 140, 111, 20))
                self.label.setStyleSheet("color: rgb(110, 110, 110);")
                self.label.setObjectName("label")
                icon9 = QtGui.QIcon()
                icon9.addPixmap(QtGui.QPixmap(":/header/play.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
                self.tabWidget.addTab(self.testab, icon9, "")

                #Configs
                self.settings.raise_()
                self.line.raise_()
                self.textEdit.raise_()
                self.resttobologo.raise_()
                self.tabWidget.raise_()
                Main.setCentralWidget(self.centralwidget)

                self.retranslateUi(Main)
                self.tabWidget.setCurrentIndex(0)
                QtCore.QMetaObject.connectSlotsByName(Main)

        def retranslateUi(self, Main):
                _translate = QtCore.QCoreApplication.translate
                Main.setWindowTitle(_translate("Main", "RestRobo"))

                #by Unwiring Tech
                self.textEdit.setHtml(_translate("Main", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
        "<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
        "p, li { white-space: pre-wrap; }\n"
        "hr { height: 1px; border-width: 0; }\n"
        "li.unchecked::marker { content: \"\\2610\"; }\n"
        "li.checked::marker { content: \"\\2612\"; }\n"
        "</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:7pt; font-weight:700;\">by Unwiring Tech</span></p></body></html>"))
                
                #Active Schedule
                        #Column names
                item = self.tableWidget.horizontalHeaderItem(0)
                item.setText(_translate("Main", "Name"))
                item = self.tableWidget.horizontalHeaderItem(1)
                item.setText(_translate("Main", "Application"))
                item = self.tableWidget.horizontalHeaderItem(2)
                item.setText(_translate("Main", "Execution time"))
                item = self.tableWidget.horizontalHeaderItem(3)
                item.setText(_translate("Main", "Delay(s)"))
                        #Buttons
                self.pushButton_2.setText(_translate("Main", "Add"))
                self.pushButton_3.setText(_translate("Main", "Remove"))
                        #Tab name
                self.tabWidget.setTabText(self.tabWidget.indexOf(self.schedtab), _translate("Main", "Active Schedule"))
                
                #Record
                        #labels
                self.name.setText(_translate("Main", "Name"))
                self.description.setText(_translate("Main", "Description"))
                self.executable.setText(_translate("Main", "Executable"))
                        #buttons
                self.browse.setText(_translate("Main", "Browse"))
                self.pushButton.setText(_translate("Main", "Record"))
                        #first text box
                self.textBrowser_2.setHtml(_translate("Main", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
        "<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
        "p, li { white-space: pre-wrap; }\n"
        "hr { height: 1px; border-width: 0; }\n"
        "li.unchecked::marker { content: \"\\2610\"; }\n"
        "li.checked::marker { content: \"\\2612\"; }\n"
        "</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; font-weight:700;\">Steps</span></p>\n"
        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">-</span></p>\n"
        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">-</span></p>\n"
        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">-</span></p></body></html>"))
                        #Second text box
                self.textBrowser_3.setHtml(_translate("Main", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
        "<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
        "p, li { white-space: pre-wrap; }\n"
        "hr { height: 1px; border-width: 0; }\n"
        "li.unchecked::marker { content: \"\\2610\"; }\n"
        "li.checked::marker { content: \"\\2612\"; }\n"
        "</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; font-weight:700;\">Recommendations</span></p>\n"
        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">-</span></p>\n"
        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">-</span></p>\n"
        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">-</span></p></body></html>"))
                self.tabWidget.setTabText(self.tabWidget.indexOf(self.rectab), _translate("Main", "Record"))
                
                #Test
                        #Labels
                self.name_2.setText(_translate("Main", "Filename"))
                self.description_2.setText(_translate("Main", "Description"))
                self.app.setText(_translate("Main", "Application"))
                        #Buttons
                self.browse_2.setText(_translate("Main", "Browse"))
                self.play.setText(_translate("Main", "Play"))
                self.label.setText(_translate("Main", "delay by action"))
                self.tabWidget.setTabText(self.tabWidget.indexOf(self.testab), _translate("Main", "Test"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Main = QtWidgets.QMainWindow()
    ui = Ui_Main()
    ui.setupUi(Main)
    Main.show()
    sys.exit(app.exec())

    #-----#-------#
