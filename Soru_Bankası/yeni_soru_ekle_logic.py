import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QTableWidget, QTableWidgetItem,
                             QHeaderView, QFileDialog, QMessageBox)
from PyQt5.QtCore import Qt
from Yeni_Soru_Ekle import Ui_Form as YeniSoruEkle_Ui
import pandas as pd

class YeniSoruEkleLogic(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.resize(2150, 600)
        self.ui = YeniSoruEkle_Ui()
        self.ui.setupUi(self)
        self.setFixedSize(2150, 600)
        self.setWindowTitle("Yeni Soru Ekle / Soru Bankası")

        self.ui.add_question_button.clicked.connect(self.add_question_to_table)
        self.ui.save_button.clicked.connect(self.save_question_bank_to_excel)

        self.ui.question_table.horizontalHeader().setSectionResizeMode(0, QHeaderView.Stretch)
        for i in range(1, self.ui.question_table.columnCount()):
            self.ui.question_table.horizontalHeader().setSectionResizeMode(i, QHeaderView.ResizeToContents)

    def add_question_to_table(self):
        question_text = self.ui.question_textedit.toPlainText().strip()
        answers = [lineedit.text().strip() for lineedit in self.ui.answer_lineedits]
        correct_answer_id = self.ui.answer_radio_group.checkedId()

        if not question_text or all(not ans for ans in answers):
            QMessageBox.warning(self, "Uyarı", "Lütfen soru metnini ve en az bir şıkkı doldurun.")
            return

        correct_answer_text = ""
        if 1 <= correct_answer_id <= 5:
            correct_answer_text = answers[correct_answer_id - 1]

        row_position = self.ui.question_table.rowCount()
        self.ui.question_table.insertRow(row_position)

        self.ui.question_table.setItem(row_position, 0, QTableWidgetItem(question_text))
        for i in range(5):
            self.ui.question_table.setItem(row_position, i + 1, QTableWidgetItem(answers[i]))
        self.ui.question_table.setItem(row_position, 6, QTableWidgetItem(correct_answer_text))

        self.ui.question_textedit.clear()
        for lineedit in self.ui.answer_lineedits:
            lineedit.clear()
        if self.ui.answer_radios:
            self.ui.answer_radios[0].setChecked(True)

    def save_question_bank_to_excel(self):
        if self.ui.question_table.rowCount() == 0:
            QMessageBox.information(self, "Bilgi", "Kaydedilecek herhangi bir soru bulunmamaktadır.")
            return

        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getSaveFileName(self, "Soru Bankasını Kaydet", "soru_bankasi.xlsx",
                                                   "Excel Dosyaları (*.xlsx);;Tüm Dosyalar (*)", options=options)

        if file_path:
            try:
                row_count = self.ui.question_table.rowCount()
                column_count = self.ui.question_table.columnCount()
                data = []
                headers = [self.ui.question_table.horizontalHeaderItem(i).text() for i in range(column_count)]

                for row in range(row_count):
                    row_data = []
                    for col in range(column_count):
                        item = self.ui.question_table.item(row, col)
                        row_data.append(item.text() if item else "")
                    data.append(row_data)

                df = pd.DataFrame(data, columns=headers)
                df.to_excel(file_path, index=False)

                QMessageBox.information(self, "Başarılı", f"Soru bankası başarıyla kaydedildi:\n{file_path}")
            except Exception as e:
                QMessageBox.critical(self, "Hata", f"Dosya kaydedilirken bir hata oluştu:\n{e}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = YeniSoruEkleLogic()
    main_window.show()
    sys.exit(app.exec_())
