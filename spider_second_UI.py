# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'spider_second_UI.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1164, 778)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Spider/spider.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget_2 = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget_2.setGeometry(QtCore.QRect(30, 10, 1001, 761))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget_2.sizePolicy().hasHeightForWidth())
        self.tabWidget_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.tabWidget_2.setFont(font)
        self.tabWidget_2.setMovable(True)
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.gridLayout = QtWidgets.QGridLayout(self.tab_3)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.tab_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.tabWidget.setFont(font)
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setStyleSheet("background-color: rgb(255, 255, 238);")
        self.tabWidget.setMovable(True)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(71, 161, 54, 22))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.state_label = QtWidgets.QLabel(self.tab)
        self.state_label.setGeometry(QtCore.QRect(131, 161, 691, 22))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.state_label.sizePolicy().hasHeightForWidth())
        self.state_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.state_label.setFont(font)
        self.state_label.setScaledContents(True)
        self.state_label.setObjectName("state_label")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(70, 240, 55, 22))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.book_list = QtWidgets.QListWidget(self.tab)
        self.book_list.setGeometry(QtCore.QRect(130, 270, 256, 351))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.book_list.sizePolicy().hasHeightForWidth())
        self.book_list.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.book_list.setFont(font)
        self.book_list.setAutoFillBackground(True)
        self.book_list.setResizeMode(QtWidgets.QListView.Fixed)
        self.book_list.setLayoutMode(QtWidgets.QListView.Batched)
        self.book_list.setWordWrap(True)
        self.book_list.setObjectName("book_list")
        self.progressbar = QtWidgets.QProgressBar(self.tab)
        self.progressbar.setGeometry(QtCore.QRect(130, 190, 321, 30))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.progressbar.sizePolicy().hasHeightForWidth())
        self.progressbar.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.progressbar.setFont(font)
        self.progressbar.setProperty("value", 0)
        self.progressbar.setInvertedAppearance(False)
        self.progressbar.setFormat("")
        self.progressbar.setObjectName("progressbar")
        self.label_8 = QtWidgets.QLabel(self.tab)
        self.label_8.setGeometry(QtCore.QRect(750, 70, 71, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("image: url(:/Spider/novel_spider.svg);")
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.search_push_button = QtWidgets.QPushButton(self.tab)
        self.search_push_button.setGeometry(QtCore.QRect(630, 110, 75, 28))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.search_push_button.sizePolicy().hasHeightForWidth())
        self.search_push_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.search_push_button.setFont(font)
        self.search_push_button.setObjectName("search_push_button")
        self.layoutWidget = QtWidgets.QWidget(self.tab)
        self.layoutWidget.setGeometry(QtCore.QRect(61, 111, 267, 28))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.layoutWidget.sizePolicy().hasHeightForWidth())
        self.layoutWidget.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.layoutWidget.setFont(font)
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.book_name_label = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.book_name_label.sizePolicy().hasHeightForWidth())
        self.book_name_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.book_name_label.setFont(font)
        self.book_name_label.setObjectName("book_name_label")
        self.horizontalLayout_3.addWidget(self.book_name_label)
        self.book_name = QtWidgets.QLineEdit(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.book_name.sizePolicy().hasHeightForWidth())
        self.book_name.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.book_name.setFont(font)
        self.book_name.setObjectName("book_name")
        self.horizontalLayout_3.addWidget(self.book_name)
        self.book_source_combobox = QtWidgets.QComboBox(self.tab)
        self.book_source_combobox.setGeometry(QtCore.QRect(430, 110, 121, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.book_source_combobox.sizePolicy().hasHeightForWidth())
        self.book_source_combobox.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.book_source_combobox.setFont(font)
        self.book_source_combobox.setObjectName("book_source_combobox")
        self.book_source_combobox.addItem("")
        self.book_source_combobox.addItem("")
        self.book_source_combobox.addItem("")
        self.source_label = QtWidgets.QLabel(self.tab)
        self.source_label.setGeometry(QtCore.QRect(350, 120, 63, 19))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.source_label.sizePolicy().hasHeightForWidth())
        self.source_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.source_label.setFont(font)
        self.source_label.setObjectName("source_label")
        self.exit_novel_list = QtWidgets.QListWidget(self.tab)
        self.exit_novel_list.setGeometry(QtCore.QRect(450, 230, 256, 401))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.exit_novel_list.sizePolicy().hasHeightForWidth())
        self.exit_novel_list.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.exit_novel_list.setFont(font)
        self.exit_novel_list.setMouseTracking(True)
        self.exit_novel_list.setObjectName("exit_novel_list")
        self.novel_status_list = QtWidgets.QListWidget(self.tab)
        self.novel_status_list.setGeometry(QtCore.QRect(730, 230, 111, 401))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.novel_status_list.sizePolicy().hasHeightForWidth())
        self.novel_status_list.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.novel_status_list.setFont(font)
        self.novel_status_list.setMouseTracking(True)
        self.novel_status_list.setResizeMode(QtWidgets.QListView.Adjust)
        self.novel_status_list.setObjectName("novel_status_list")
        self.label_5 = QtWidgets.QLabel(self.tab)
        self.label_5.setGeometry(QtCore.QRect(460, 200, 241, 21))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.tab)
        self.label_6.setGeometry(QtCore.QRect(730, 200, 91, 21))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.tab_2)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(62, 130, 681, 471))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.horizontalLayoutWidget.setFont(font)
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.content_list1 = QtWidgets.QListWidget(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.content_list1.setFont(font)
        self.content_list1.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.content_list1.setMovement(QtWidgets.QListView.Free)
        self.content_list1.setResizeMode(QtWidgets.QListView.Adjust)
        self.content_list1.setLayoutMode(QtWidgets.QListView.SinglePass)
        self.content_list1.setUniformItemSizes(True)
        self.content_list1.setObjectName("content_list1")
        self.horizontalLayout.addWidget(self.content_list1)
        self.content_list2 = QtWidgets.QListWidget(self.horizontalLayoutWidget)
        self.content_list2.setMaximumSize(QtCore.QSize(108, 469))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.content_list2.setFont(font)
        self.content_list2.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.content_list2.setMovement(QtWidgets.QListView.Free)
        self.content_list2.setResizeMode(QtWidgets.QListView.Adjust)
        self.content_list2.setUniformItemSizes(True)
        self.content_list2.setObjectName("content_list2")
        self.horizontalLayout.addWidget(self.content_list2)
        self.content_list3 = QtWidgets.QListWidget(self.horizontalLayoutWidget)
        self.content_list3.setMaximumSize(QtCore.QSize(115, 469))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.content_list3.setFont(font)
        self.content_list3.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.content_list3.setMovement(QtWidgets.QListView.Free)
        self.content_list3.setResizeMode(QtWidgets.QListView.Adjust)
        self.content_list3.setUniformItemSizes(True)
        self.content_list3.setObjectName("content_list3")
        self.horizontalLayout.addWidget(self.content_list3)
        self.content_list4 = QtWidgets.QListWidget(self.horizontalLayoutWidget)
        self.content_list4.setMaximumSize(QtCore.QSize(122, 469))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.content_list4.setFont(font)
        self.content_list4.setMouseTracking(True)
        self.content_list4.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.content_list4.setMovement(QtWidgets.QListView.Snap)
        self.content_list4.setResizeMode(QtWidgets.QListView.Adjust)
        self.content_list4.setUniformItemSizes(True)
        self.content_list4.setObjectName("content_list4")
        self.horizontalLayout.addWidget(self.content_list4)
        self.content_list5 = QtWidgets.QListWidget(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.content_list5.setFont(font)
        self.content_list5.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.content_list5.setMovement(QtWidgets.QListView.Free)
        self.content_list5.setResizeMode(QtWidgets.QListView.Adjust)
        self.content_list5.setUniformItemSizes(True)
        self.content_list5.setObjectName("content_list5")
        self.horizontalLayout.addWidget(self.content_list5)
        self.content_list6 = QtWidgets.QListWidget(self.horizontalLayoutWidget)
        self.content_list6.setMinimumSize(QtCore.QSize(127, 0))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.content_list6.setFont(font)
        self.content_list6.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.content_list6.setMovement(QtWidgets.QListView.Free)
        self.content_list6.setResizeMode(QtWidgets.QListView.Adjust)
        self.content_list6.setUniformItemSizes(True)
        self.content_list6.setObjectName("content_list6")
        self.horizontalLayout.addWidget(self.content_list6)
        self.gridLayoutWidget = QtWidgets.QWidget(self.tab_2)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(140, 40, 511, 80))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.gridLayoutWidget.setFont(font)
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.rank_label = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.rank_label.setFont(font)
        self.rank_label.setObjectName("rank_label")
        self.gridLayout_2.addWidget(self.rank_label, 1, 0, 1, 1)
        self.source_cobox = QtWidgets.QComboBox(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.source_cobox.setFont(font)
        self.source_cobox.setObjectName("source_cobox")
        self.source_cobox.addItem("")
        self.gridLayout_2.addWidget(self.source_cobox, 1, 1, 1, 1)
        self.rank_button = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.rank_button.setFont(font)
        self.rank_button.setObjectName("rank_button")
        self.gridLayout_2.addWidget(self.rank_button, 1, 2, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.tab_2)
        self.label_9.setGeometry(QtCore.QRect(660, 50, 71, 51))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("image: url(:/Spider/novel_spider.svg);")
        self.label_9.setText("")
        self.label_9.setObjectName("label_9")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.textBrowser = QtWidgets.QTextBrowser(self.tab_5)
        self.textBrowser.setGeometry(QtCore.QRect(0, 0, 961, 621))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(14)
        self.textBrowser.setFont(font)
        self.textBrowser.setAutoFormatting(QtWidgets.QTextEdit.AutoAll)
        self.textBrowser.setObjectName("textBrowser")
        self.preview_button = QtWidgets.QPushButton(self.tab_5)
        self.preview_button.setGeometry(QtCore.QRect(44, 622, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.preview_button.setFont(font)
        self.preview_button.setObjectName("preview_button")
        self.Next_button = QtWidgets.QPushButton(self.tab_5)
        self.Next_button.setGeometry(QtCore.QRect(794, 622, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.Next_button.setFont(font)
        self.Next_button.setObjectName("Next_button")
        self.Menu_button = QtWidgets.QPushButton(self.tab_5)
        self.Menu_button.setGeometry(QtCore.QRect(404, 622, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.Menu_button.setFont(font)
        self.Menu_button.setObjectName("Menu_button")
        self.listWidget_menu = QtWidgets.QListWidget(self.tab_5)
        self.listWidget_menu.setGeometry(QtCore.QRect(0, 0, 961, 621))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.listWidget_menu.setFont(font)
        self.listWidget_menu.setObjectName("listWidget_menu")
        self.tabWidget.addTab(self.tab_5, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        self.tabWidget_2.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.music_listWidget = QtWidgets.QListWidget(self.tab_4)
        self.music_listWidget.setGeometry(QtCore.QRect(80, 140, 311, 451))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.music_listWidget.setFont(font)
        self.music_listWidget.setObjectName("music_listWidget")
        self.label_3 = QtWidgets.QLabel(self.tab_4)
        self.label_3.setGeometry(QtCore.QRect(20, 90, 91, 51))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.tab_4)
        self.label_4.setGeometry(QtCore.QRect(430, 140, 91, 51))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_7 = QtWidgets.QLabel(self.tab_4)
        self.label_7.setGeometry(QtCore.QRect(730, 30, 71, 71))
        self.label_7.setStyleSheet("image: url(:/Spider/novel_spider.svg);")
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.layoutWidget1 = QtWidgets.QWidget(self.tab_4)
        self.layoutWidget1.setGeometry(QtCore.QRect(190, 30, 521, 81))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.layoutWidget1.setFont(font)
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.comboBox_music = QtWidgets.QComboBox(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.comboBox_music.setFont(font)
        self.comboBox_music.setEditable(True)
        self.comboBox_music.setObjectName("comboBox_music")
        self.comboBox_music.addItem("")
        self.horizontalLayout_2.addWidget(self.comboBox_music)
        self.lineEdit_music = QtWidgets.QLineEdit(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_music.setFont(font)
        self.lineEdit_music.setObjectName("lineEdit_music")
        self.horizontalLayout_2.addWidget(self.lineEdit_music)
        self.pushButton_music = QtWidgets.QPushButton(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_music.setFont(font)
        self.pushButton_music.setObjectName("pushButton_music")
        self.horizontalLayout_2.addWidget(self.pushButton_music)
        self.status_music_label = QtWidgets.QLabel(self.tab_4)
        self.status_music_label.setGeometry(QtCore.QRect(530, 140, 421, 51))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.status_music_label.setFont(font)
        self.status_music_label.setText("")
        self.status_music_label.setObjectName("status_music_label")
        self.tabWidget_2.addTab(self.tab_4, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1164, 23))
        self.menubar.setObjectName("menubar")
        self.menuMENU = QtWidgets.QMenu(self.menubar)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.menuMENU.setFont(font)
        self.menuMENU.setObjectName("menuMENU")
        self.menulayout = QtWidgets.QMenu(self.menuMENU)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.menulayout.setFont(font)
        self.menulayout.setObjectName("menulayout")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionclose = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.actionclose.setFont(font)
        self.actionclose.setObjectName("actionclose")
        self.actionsave = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.actionsave.setFont(font)
        self.actionsave.setObjectName("actionsave")
        self.actionwumaomao = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.actionwumaomao.setFont(font)
        self.actionwumaomao.setObjectName("actionwumaomao")
        self.actionauthor = QtWidgets.QAction(MainWindow)
        self.actionauthor.setCheckable(True)
        self.actionauthor.setChecked(True)
        self.actionauthor.setObjectName("actionauthor")
        self.actiongenre = QtWidgets.QAction(MainWindow)
        self.actiongenre.setCheckable(True)
        self.actiongenre.setChecked(True)
        self.actiongenre.setObjectName("actiongenre")
        self.actionstatus = QtWidgets.QAction(MainWindow)
        self.actionstatus.setCheckable(True)
        self.actionstatus.setChecked(True)
        self.actionstatus.setObjectName("actionstatus")
        self.actionname = QtWidgets.QAction(MainWindow)
        self.actionname.setCheckable(True)
        self.actionname.setChecked(True)
        self.actionname.setObjectName("actionname")
        self.actionupdate_chapter = QtWidgets.QAction(MainWindow)
        self.actionupdate_chapter.setCheckable(True)
        self.actionupdate_chapter.setChecked(False)
        self.actionupdate_chapter.setObjectName("actionupdate_chapter")
        self.actionintro = QtWidgets.QAction(MainWindow)
        self.actionintro.setCheckable(True)
        self.actionintro.setChecked(False)
        self.actionintro.setObjectName("actionintro")
        self.menulayout.addAction(self.actionauthor)
        self.menulayout.addAction(self.actiongenre)
        self.menulayout.addAction(self.actionstatus)
        self.menulayout.addAction(self.actionname)
        self.menulayout.addAction(self.actionupdate_chapter)
        self.menulayout.addAction(self.actionintro)
        self.menuMENU.addAction(self.actionclose)
        self.menuMENU.addAction(self.actionsave)
        self.menuMENU.addAction(self.actionwumaomao)
        self.menuMENU.addSeparator()
        self.menuMENU.addAction(self.menulayout.menuAction())
        self.menubar.addAction(self.menuMENU.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget_2.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Spider System"))
        self.label_2.setText(_translate("MainWindow", "status:"))
        self.state_label.setText(_translate("MainWindow", "None"))
        self.label.setText(_translate("MainWindow", "Result:"))
        self.book_list.setToolTip(_translate("MainWindow", "double clicked to download"))
        self.book_list.setStatusTip(_translate("MainWindow", "double clicked to download"))
        self.search_push_button.setText(_translate("MainWindow", "Search"))
        self.search_push_button.setShortcut(_translate("MainWindow", "Return"))
        self.book_name_label.setText(_translate("MainWindow", "KeyWord:"))
        self.book_source_combobox.setItemText(0, _translate("MainWindow", "笔趣阁"))
        self.book_source_combobox.setItemText(1, _translate("MainWindow", "长夜烽火"))
        self.book_source_combobox.setItemText(2, _translate("MainWindow", "落霞"))
        self.source_label.setText(_translate("MainWindow", "Sources:"))
        self.exit_novel_list.setStatusTip(_translate("MainWindow", "double clicked to download"))
        self.novel_status_list.setStatusTip(_translate("MainWindow", "double click to load book"))
        self.label_5.setText(_translate("MainWindow", "Downloaded Files Lists"))
        self.label_6.setText(_translate("MainWindow", "Status"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "HOME"))
        self.content_list1.setToolTip(_translate("MainWindow", "double clicked"))
        self.content_list1.setStatusTip(_translate("MainWindow", "double clicked"))
        self.content_list2.setStatusTip(_translate("MainWindow", "double clicked to open the url"))
        self.content_list3.setStatusTip(_translate("MainWindow", "double clicked to open the url"))
        self.content_list6.setToolTip(_translate("MainWindow", "double clicked"))
        self.content_list6.setStatusTip(_translate("MainWindow", "double clicked"))
        self.rank_label.setText(_translate("MainWindow", "checking ..."))
        self.source_cobox.setItemText(0, _translate("MainWindow", "qidian"))
        self.rank_button.setStatusTip(_translate("MainWindow", "click to get rank info"))
        self.rank_button.setText(_translate("MainWindow", "Search"))
        self.rank_button.setShortcut(_translate("MainWindow", "Return"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "RANK"))
        self.preview_button.setStatusTip(_translate("MainWindow", "last chapter"))
        self.preview_button.setText(_translate("MainWindow", "Preview"))
        self.Next_button.setStatusTip(_translate("MainWindow", "next chapter"))
        self.Next_button.setText(_translate("MainWindow", "Next"))
        self.Menu_button.setStatusTip(_translate("MainWindow", "Menu"))
        self.Menu_button.setText(_translate("MainWindow", "Menu"))
        self.listWidget_menu.setStatusTip(_translate("MainWindow", "double click to change chapter"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("MainWindow", "Browser"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_3), _translate("MainWindow", "小说"))
        self.music_listWidget.setStatusTip(_translate("MainWindow", "double clicked to download"))
        self.label_3.setText(_translate("MainWindow", "Result:"))
        self.label_4.setText(_translate("MainWindow", "Status:"))
        self.comboBox_music.setItemText(0, _translate("MainWindow", "QQmusic"))
        self.lineEdit_music.setText(_translate("MainWindow", "周杰伦"))
        self.pushButton_music.setText(_translate("MainWindow", "Search"))
        self.pushButton_music.setShortcut(_translate("MainWindow", "Return"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_4), _translate("MainWindow", "音乐"))
        self.menuMENU.setTitle(_translate("MainWindow", "MENU"))
        self.menulayout.setTitle(_translate("MainWindow", "layout"))
        self.actionclose.setText(_translate("MainWindow", "close"))
        self.actionclose.setToolTip(_translate("MainWindow", "close the exe"))
        self.actionclose.setStatusTip(_translate("MainWindow", "close the exe"))
        self.actionclose.setShortcut(_translate("MainWindow", "Ctrl+Q"))
        self.actionsave.setText(_translate("MainWindow", "save"))
        self.actionsave.setToolTip(_translate("MainWindow", "save"))
        self.actionsave.setStatusTip(_translate("MainWindow", "save"))
        self.actionsave.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionwumaomao.setText(_translate("MainWindow", "wumaomao"))
        self.actionwumaomao.setToolTip(_translate("MainWindow", "should be handsome"))
        self.actionwumaomao.setStatusTip(_translate("MainWindow", "should be handsome"))
        self.actionauthor.setText(_translate("MainWindow", "author"))
        self.actiongenre.setText(_translate("MainWindow", "genre"))
        self.actionstatus.setText(_translate("MainWindow", "status"))
        self.actionname.setText(_translate("MainWindow", "name"))
        self.actionupdate_chapter.setText(_translate("MainWindow", "update_chapter"))
        self.actionintro.setText(_translate("MainWindow", "intro"))

import spider_rc