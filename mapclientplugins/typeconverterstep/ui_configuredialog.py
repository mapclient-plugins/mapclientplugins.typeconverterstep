# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'configuredialog.ui'
##
## Created by: Qt User Interface Compiler version 6.6.3
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QGridLayout, QGroupBox, QLabel, QLineEdit,
    QSizePolicy, QSpacerItem, QWidget)

class Ui_ConfigureDialog(object):
    def setupUi(self, ConfigureDialog):
        if not ConfigureDialog.objectName():
            ConfigureDialog.setObjectName(u"ConfigureDialog")
        ConfigureDialog.resize(417, 238)
        self.gridLayout = QGridLayout(ConfigureDialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.configGroupBox = QGroupBox(ConfigureDialog)
        self.configGroupBox.setObjectName(u"configGroupBox")
        self.gridLayout_2 = QGridLayout(self.configGroupBox)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label2 = QLabel(self.configGroupBox)
        self.label2.setObjectName(u"label2")
        self.label2.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_2.addWidget(self.label2, 2, 0, 1, 1)

        self.lineEditInputPortType = QLineEdit(self.configGroupBox)
        self.lineEditInputPortType.setObjectName(u"lineEditInputPortType")

        self.gridLayout_2.addWidget(self.lineEditInputPortType, 1, 1, 1, 1)

        self.label1 = QLabel(self.configGroupBox)
        self.label1.setObjectName(u"label1")
        self.label1.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_2.addWidget(self.label1, 1, 0, 1, 1)

        self.lineEdit0 = QLineEdit(self.configGroupBox)
        self.lineEdit0.setObjectName(u"lineEdit0")

        self.gridLayout_2.addWidget(self.lineEdit0, 0, 1, 1, 1)

        self.label0 = QLabel(self.configGroupBox)
        self.label0.setObjectName(u"label0")
        self.label0.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_2.addWidget(self.label0, 0, 0, 1, 1)

        self.lineEditOutputPortType = QLineEdit(self.configGroupBox)
        self.lineEditOutputPortType.setObjectName(u"lineEditOutputPortType")

        self.gridLayout_2.addWidget(self.lineEditOutputPortType, 2, 1, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer, 3, 1, 1, 1)


        self.gridLayout.addWidget(self.configGroupBox, 0, 0, 1, 1)

        self.buttonBox = QDialogButtonBox(ConfigureDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)

        self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 1)


        self.retranslateUi(ConfigureDialog)
        self.buttonBox.accepted.connect(ConfigureDialog.accept)
        self.buttonBox.rejected.connect(ConfigureDialog.reject)

        QMetaObject.connectSlotsByName(ConfigureDialog)
    # setupUi

    def retranslateUi(self, ConfigureDialog):
        ConfigureDialog.setWindowTitle(QCoreApplication.translate("ConfigureDialog", u"ConfigureDialog", None))
        self.configGroupBox.setTitle("")
        self.label2.setText(QCoreApplication.translate("ConfigureDialog", u"Output Port Type:  ", None))
        self.label1.setText(QCoreApplication.translate("ConfigureDialog", u"Input Port Type:  ", None))
        self.label0.setText(QCoreApplication.translate("ConfigureDialog", u"Identifier:  ", None))
    # retranslateUi

