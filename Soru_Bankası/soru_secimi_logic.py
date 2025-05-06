import sys
import os
import pandas as pd
from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog, QMessageBox, QAbstractItemView, QTableWidgetItem, QHeaderView
from PyQt5.QtCore import Qt, QRectF, QSizeF
from PyQt5.QtGui import QPainter, QTextDocument, QPen, QColor, QFont
from PyQt5.QtPrintSupport import QPrinter
from PyQt5.QtGui import QAbstractTextDocumentLayout

from Soru_Bankasından_Soru_Seçimi import Ui_Form as SoruSecimi_Ui


class SoruSecimiLogic(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = SoruSecimi_Ui()
        self.ui.setupUi(self)
        self.setFixedSize(1300, 300)
        self.setWindowTitle("Soru Bankasından Soru Seçimi")

        # Sinyaller
        self.ui.pushButton.clicked.connect(self.open_file_and_load_questions)
        self.ui.pushButton_2.clicked.connect(self.print_selected_questions)

        # Tablo ayarları
        self.ui.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.ui.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)

        # Sütun başlıkları
        headers = ["Seç", "Soru", "1. Seçenek", "2. Seçenek", "3. Seçenek", "4. Seçenek", "5. Seçenek", "Cevap"]
        self.ui.tableWidget.setColumnCount(len(headers))
        for i, h in enumerate(headers):
            self.ui.tableWidget.setHorizontalHeaderItem(i, QTableWidgetItem(h))

        self.ui.tableWidget.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeToContents)
        self.ui.tableWidget.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)
        for i in range(2, len(headers)):
            self.ui.tableWidget.horizontalHeader().setSectionResizeMode(i, QHeaderView.ResizeToContents)

    def open_file_and_load_questions(self):
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getOpenFileName(
            self, "Soru Bankası Dosyasını Seçin", "",
            "Excel Dosyaları (*.xlsx);;Tüm Dosyalar (*)", options=options)

        if file_path:
            try:
                df = pd.read_excel(file_path)
                if df.shape[1] != 7:
                    QMessageBox.warning(self, "Hata",
                        f"Dosyada beklenenden farklı sayıda sütun var ({df.shape[1]} yerine 7 bekleniyordu).")
                    return

                self.ui.tableWidget.setRowCount(0)
                self.ui.tableWidget.setRowCount(df.shape[0])

                for row in range(df.shape[0]):
                    checkbox_item = QTableWidgetItem()
                    checkbox_item.setFlags(Qt.ItemIsUserCheckable | Qt.ItemIsEnabled)
                    checkbox_item.setCheckState(Qt.Unchecked)
                    self.ui.tableWidget.setItem(row, 0, checkbox_item)

                    for col in range(df.shape[1]):
                        text = str(df.iloc[row, col]) if pd.notna(df.iloc[row, col]) else ""
                        item = QTableWidgetItem(text.strip())
                        item.setFlags(item.flags() & ~Qt.ItemIsEditable)
                        self.ui.tableWidget.setItem(row, col + 1, item)

                QMessageBox.information(self, "Başarılı", f"Soru bankası başarıyla yüklendi:\n{file_path}")

            except Exception as e:
                QMessageBox.critical(self, "Hata", f"Dosya okunurken bir hata oluştu:\n{e}")

    def print_selected_questions(self):
        selected_data = []

        for row in range(self.ui.tableWidget.rowCount()):
            select_item = self.ui.tableWidget.item(row, 0)
            if select_item and select_item.checkState() == Qt.Checked:
                row_data = []
                for col in range(1, self.ui.tableWidget.columnCount()):
                    item = self.ui.tableWidget.item(row, col)
                    cell_text = item.text().strip() if item else ""
                    row_data.append(cell_text)
                selected_data.append(row_data)

        if not selected_data:
            QMessageBox.information(self, "Bilgi", "Yazdırmak için herhangi bir soru seçilmedi.")
            return

        printer = QPrinter(QPrinter.HighResolution)
        printer.setOutputFormat(QPrinter.PdfFormat)

        options = QFileDialog.Options()
        pdf_path, _ = QFileDialog.getSaveFileName(
            self, "PDF Olarak Kaydet", "secili_sorular.pdf",
            "PDF Dosyaları (*.pdf);;Tüm Dosyalar (*)", options=options)

        if not pdf_path:
            return

        printer.setOutputFileName(pdf_path)
        painter = QPainter()

        if not painter.begin(printer):
            QMessageBox.critical(self, "Hata", "PDF yazdırma başlatılamadı.")
            return

        try:
            document = QTextDocument()
            painter.setPen(QPen(QColor(Qt.black)))

            document.setDefaultFont(QFont("Arial", 72))

            page_rect = printer.pageRect(QPrinter.DevicePixel)
            margin = 50
            dpi = printer.resolution()
            ppp = 72.0 / dpi

            printable_rect = QRectF(
                page_rect.x() + margin,
                page_rect.y() + margin,
                page_rect.width() - 2 * margin,
                page_rect.height() - 2 * margin
            )

            width_pt = printable_rect.width() * ppp
            height_pt = printable_rect.height() * ppp
            document.setPageSize(QSizeF(width_pt, height_pt))

            html = "<style>"
            html += "body { font-family: Arial; font-size: 14pt; margin: 0; padding: 0; }"
            html += "p { margin-top: 0.5em; margin-bottom: 0.5em; }"
            html += "ul { margin-top: 0.5em; margin-bottom: 0.5em; padding-left: 1.5em; }"
            html += "li { margin-bottom: 0.3em; }"
            html += ".question { font-weight: bold; font-size: 20pt; margin-bottom: 0.8em; }"
            html += ".answer { font-style: italic; margin-top: 0.5em; }"
            html += "</style><body>"

            letters = ["A)", "B)", "C)", "D)", "E)"]

            for i, q in enumerate(selected_data):
                question_text = q[0]
                options_list = q[1:6]
                answer = q[6]

                html += f"<p class='question'>{i+1}. {question_text.strip()}</p><ul>"
                for j, opt in enumerate(options_list):
                    if opt.strip():
                        html += f"<li>{letters[j]} {opt.strip()}</li>"
                html += "</ul>"
                answer_text = answer.strip() if answer.strip() else "Belirtilmemiş"
                html += f"<p class='answer'>Doğru Cevap: {answer_text}</p>"

            html += "</body>"
            document.setHtml(html)

            context = QAbstractTextDocumentLayout.PaintContext()
            context.clipRect = printable_rect
            document.documentLayout().draw(painter, context)

        except Exception as e:
            QMessageBox.critical(self, "Yazdırma Hatası", f"PDF oluşturulurken hata oluştu:\n{e}")

        finally:
            painter.end()

        QMessageBox.information(self, "Yazdırma Tamamlandı", f"PDF kaydedildi:\n{pdf_path}")

    def closeEvent(self, event):
        event.accept()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = SoruSecimiLogic()
    main_window.show()
    sys.exit(app.exec_())
