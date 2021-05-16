# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'test.ui'
##
## Created by: Qt User Interface Compiler version 6.0.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from mplwidget import MplWidget


class Ui_Interface(object):
    def setupUi(self, Interface):
        if not Interface.objectName():
            Interface.setObjectName(u"Interface")
        Interface.resize(800, 600)
        self.gridLayout = QGridLayout(Interface)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.widget = MplWidget(Interface)
        self.widget.setObjectName(u"widget")

        self.verticalLayout_3.addWidget(self.widget)


        self.gridLayout.addLayout(self.verticalLayout_3, 0, 2, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.textBrowser = QTextBrowser(Interface)
        self.textBrowser.setObjectName(u"textBrowser")

        self.verticalLayout.addWidget(self.textBrowser)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_5 = QLabel(Interface)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_2.addWidget(self.label_5)

        self.przedzial_linia = QLineEdit(Interface)
        self.przedzial_linia.setObjectName(u"przedzial_linia")

        self.horizontalLayout_2.addWidget(self.przedzial_linia)

        self.przedzial_akcept = QPushButton(Interface)
        self.przedzial_akcept.setObjectName(u"przedzial_akcept")

        self.horizontalLayout_2.addWidget(self.przedzial_akcept)


        self.verticalLayout_4.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_2 = QLabel(Interface)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)

        self.funkcja_linia = QLineEdit(Interface)
        self.funkcja_linia.setObjectName(u"funkcja_linia")

        self.horizontalLayout.addWidget(self.funkcja_linia)

        self.funkcja_akcept = QPushButton(Interface)
        self.funkcja_akcept.setObjectName(u"funkcja_akcept")

        self.horizontalLayout.addWidget(self.funkcja_akcept)


        self.verticalLayout_4.addLayout(self.horizontalLayout)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label = QLabel(Interface)
        self.label.setObjectName(u"label")

        self.horizontalLayout_6.addWidget(self.label)

        self.startowy_linia = QLineEdit(Interface)
        self.startowy_linia.setObjectName(u"startowy_linia")

        self.horizontalLayout_6.addWidget(self.startowy_linia)

        self.startowy_akcept = QPushButton(Interface)
        self.startowy_akcept.setObjectName(u"startowy_akcept")

        self.horizontalLayout_6.addWidget(self.startowy_akcept)


        self.verticalLayout_4.addLayout(self.horizontalLayout_6)


        self.gridLayout.addLayout(self.verticalLayout_4, 3, 0, 1, 1)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.rysuj = QPushButton(Interface)
        self.rysuj.setObjectName(u"rysuj")

        self.verticalLayout_5.addWidget(self.rysuj)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_3 = QLabel(Interface)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_4.addWidget(self.label_3)

        self.dokladnosc_linia = QLineEdit(Interface)
        self.dokladnosc_linia.setObjectName(u"dokladnosc_linia")

        self.horizontalLayout_4.addWidget(self.dokladnosc_linia)

        self.dokladnosc_akcept = QPushButton(Interface)
        self.dokladnosc_akcept.setObjectName(u"dokladnosc_akcept")

        self.horizontalLayout_4.addWidget(self.dokladnosc_akcept)


        self.verticalLayout_5.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_4 = QLabel(Interface)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_5.addWidget(self.label_4)

        self.iteracja_linia = QLineEdit(Interface)
        self.iteracja_linia.setObjectName(u"iteracja_linia")

        self.horizontalLayout_5.addWidget(self.iteracja_linia)

        self.iteracja_akcept = QPushButton(Interface)
        self.iteracja_akcept.setObjectName(u"iteracja_akcept")

        self.horizontalLayout_5.addWidget(self.iteracja_akcept)


        self.verticalLayout_5.addLayout(self.horizontalLayout_5)


        self.gridLayout.addLayout(self.verticalLayout_5, 3, 2, 1, 1)


        self.retranslateUi(Interface)

        QMetaObject.connectSlotsByName(Interface)
    # setupUi

    def retranslateUi(self, Interface):
        Interface.setWindowTitle(QCoreApplication.translate("Interface", u"Interface", None))
        self.label_5.setText(QCoreApplication.translate("Interface", u"Przedzia\u0142 rysowania: ", None))
        self.przedzial_akcept.setText(QCoreApplication.translate("Interface", u"Akceptuj", None))
        self.label_2.setText(QCoreApplication.translate("Interface", u"Funkcja:", None))
        self.funkcja_akcept.setText(QCoreApplication.translate("Interface", u"Akceptuj", None))
        self.label.setText(QCoreApplication.translate("Interface", u"Punkt startowy:", None))
        self.startowy_akcept.setText(QCoreApplication.translate("Interface", u"Akceptuj", None))
        self.rysuj.setText(QCoreApplication.translate("Interface", u"Rysuj", None))
        self.label_3.setText(QCoreApplication.translate("Interface", u"Dok\u0142adno\u015b\u0107:", None))
        self.dokladnosc_akcept.setText(QCoreApplication.translate("Interface", u"Akceptuj", None))
        self.label_4.setText(QCoreApplication.translate("Interface", u"Liczba iteracji:", None))
        self.iteracja_akcept.setText(QCoreApplication.translate("Interface", u"Akceptuj", None))
    # retranslateUi

