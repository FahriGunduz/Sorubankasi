from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(2150, 600)

        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setObjectName("horizontalLayout")

        # Left Side: Add Question Form
        self.verticalLayout_left = QtWidgets.QVBoxLayout()
        self.verticalLayout_left.setObjectName("verticalLayout_left")

        self.groupBox_question = QtWidgets.QGroupBox(Form)
        self.groupBox_question.setObjectName("groupBox_question")
        self.verticalLayout_question = QtWidgets.QVBoxLayout(self.groupBox_question)
        self.verticalLayout_question.setObjectName("verticalLayout_question")
        self.question_textedit = QtWidgets.QTextEdit(self.groupBox_question)
        self.question_textedit.setObjectName("question_textedit")
        self.verticalLayout_question.addWidget(self.question_textedit)
        self.verticalLayout_left.addWidget(self.groupBox_question)

        self.groupBox_answers = QtWidgets.QGroupBox(Form)
        self.groupBox_answers.setObjectName("groupBox_answers")
        self.formLayout_answers = QtWidgets.QFormLayout(self.groupBox_answers)
        self.formLayout_answers.setObjectName("formLayout_answers")

        self.answer_lineedits = []
        self.answer_radios = []
        self.answer_radio_group = QtWidgets.QButtonGroup(Form)
        self.answer_radio_group.setObjectName("answer_radio_group")

        for i in range(1, 6):
            h_layout = QtWidgets.QHBoxLayout()
            h_layout.setObjectName(f"horizontalLayout_answer_{i}")

            radio_button = QtWidgets.QRadioButton(self.groupBox_answers)
            radio_button.setObjectName(f"radioButton_answer_{i}")
            radio_button.setChecked(i == 1)
            h_layout.addWidget(radio_button)
            self.answer_radios.append(radio_button)
            self.answer_radio_group.addButton(radio_button, i)

            answer_input = QtWidgets.QLineEdit(self.groupBox_answers)
            answer_input.setObjectName(f"lineEdit_answer_{i}")
            h_layout.addWidget(answer_input)
            self.answer_lineedits.append(answer_input)

            self.formLayout_answers.addRow(h_layout)

        self.verticalLayout_left.addWidget(self.groupBox_answers)

        self.add_question_button = QtWidgets.QPushButton(Form)
        self.add_question_button.setObjectName("add_question_button")
        self.verticalLayout_left.addWidget(self.add_question_button)

        self.horizontalLayout.addLayout(self.verticalLayout_left, 1)

        # Right Side: Question Bank Table
        self.verticalLayout_right = QtWidgets.QVBoxLayout()
        self.verticalLayout_right.setObjectName("verticalLayout_right")

        self.question_table = QtWidgets.QTableWidget(Form)
        self.question_table.setObjectName("question_table")
        self.question_table.setColumnCount(7)

        self.verticalLayout_right.addWidget(self.question_table)

        self.save_button = QtWidgets.QPushButton(Form)
        self.save_button.setObjectName("save_button")
        self.verticalLayout_right.addWidget(self.save_button)

        self.horizontalLayout.addLayout(self.verticalLayout_right, 2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form - Yeni Soru Ekle/Soru Bankası"))

        self.groupBox_question.setTitle(_translate("Form", "Soru"))
        self.groupBox_answers.setTitle(_translate("Form", "Yanıtlar ve Doğru Şık"))

        self.question_textedit.setPlaceholderText(_translate("Form", "Soruyu buraya yazın..."))
        for i in range(5):
            self.answer_lineedits[i].setPlaceholderText(_translate("Form", f"{i+1}. yanıtı buraya girin..."))
            self.answer_radios[i].setText(_translate("Form", f"{i+1}. Yanıt"))

        self.add_question_button.setText(_translate("Form", "Soru Bankasına Ekle"))
        self.save_button.setText(_translate("Form", "Soru Bankasını Excel Olarak Kaydet"))

        if self.question_table.columnCount() >= 7:
            self.question_table.setHorizontalHeaderItem(0, QtWidgets.QTableWidgetItem(_translate("Form", "Soru")))
            self.question_table.setHorizontalHeaderItem(1, QtWidgets.QTableWidgetItem(_translate("Form", "1. Seçenek")))
            self.question_table.setHorizontalHeaderItem(2, QtWidgets.QTableWidgetItem(_translate("Form", "2. Seçenek")))
            self.question_table.setHorizontalHeaderItem(3, QtWidgets.QTableWidgetItem(_translate("Form", "3. Seçenek")))
            self.question_table.setHorizontalHeaderItem(4, QtWidgets.QTableWidgetItem(_translate("Form", "4. Seçenek")))
            self.question_table.setHorizontalHeaderItem(5, QtWidgets.QTableWidgetItem(_translate("Form", "5. Seçenek")))
            self.question_table.setHorizontalHeaderItem(6, QtWidgets.QTableWidgetItem(_translate("Form", "Cevap")))
