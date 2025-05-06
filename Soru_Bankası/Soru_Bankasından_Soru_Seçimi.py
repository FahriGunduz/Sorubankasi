from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1300, 300)

        # Ana Dikey Layout
        self.main_verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.main_verticalLayout.setObjectName("main_verticalLayout")

        # Tablo Widget
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setRowCount(0)

        # Tablo başlıkları
        for i in range(7):
            item = QtWidgets.QTableWidgetItem()
            self.tableWidget.setHorizontalHeaderItem(i, item)

        # Sütun genişlikleri
        self.tableWidget.setColumnWidth(0, 300)
        self.tableWidget.setColumnWidth(1, 160)
        self.tableWidget.setColumnWidth(2, 160)
        self.tableWidget.setColumnWidth(3, 160)
        self.tableWidget.setColumnWidth(4, 160)
        self.tableWidget.setColumnWidth(5, 160)
        self.tableWidget.setColumnWidth(6, 180)

        self.main_verticalLayout.addWidget(self.tableWidget)

        # Butonlar Layout'u
        self.buttons_horizontalLayout = QtWidgets.QHBoxLayout()
        self.buttons_horizontalLayout.setObjectName("buttons_horizontalLayout")

        # Dosya Seç Butonu
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setObjectName("pushButton")
        self.buttons_horizontalLayout.addWidget(self.pushButton, 1)

        # Yazdır Butonu
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setObjectName("pushButton_2")
        self.buttons_horizontalLayout.addWidget(self.pushButton_2, 1)

        self.main_verticalLayout.addLayout(self.buttons_horizontalLayout)

        self.retranslateUi(Form)

        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))

        # Tablo başlıkları
        header_titles = ["Soru", "1. Seçenek", "2. Seçenek", "3. Seçenek", "4. Seçenek", "5. Seçenek", "Cevap"]
        for i, title in enumerate(header_titles):
            item = self.tableWidget.horizontalHeaderItem(i)
            item.setText(_translate("Form", title))

        # Buton metinleri
        self.pushButton.setText(_translate("Form", "YAZDIRILACAK SORU BANKASINA AİT DOSYAYI SEÇİNİZ"))
        self.pushButton_2.setText(_translate("Form", "Yazdır"))
