import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow

from main_screen import Ui_Form as MainScreen_Ui
from yeni_soru_ekle_logic import YeniSoruEkleLogic
from soru_secimi_logic import SoruSecimiLogic


class MainApp(QMainWindow):
    def __init__(self):
        super().__init__()

        # Ana ekran UI'ını yükle
        self.main_screen_ui = MainScreen_Ui()
        self.main_screen_widget = QWidget()
        self.main_screen_ui.setupUi(self.main_screen_widget)

        # Buton bağlantılarını yap
        self.main_screen_ui.pushButton.clicked.connect(self.open_yeni_soru_ekle_screen)
        self.main_screen_ui.pushButton_2.clicked.connect(self.open_soru_secimi_screen)

        # Ana pencereyi ayarla
        self.setCentralWidget(self.main_screen_widget)
        self.setWindowTitle("Ana Ekran")
        self.resize(self.main_screen_widget.size())  # Pencere boyutunu UI boyutuna ayarla

        # Diğer pencereler için referansları tut
        self.yeni_soru_ekle_window = None
        self.soru_secimi_window = None

    # "Yeni Soru Ekle" penceresini açan metot
    def open_yeni_soru_ekle_screen(self):
        if self.yeni_soru_ekle_window is None:
            self.yeni_soru_ekle_window = YeniSoruEkleLogic(self)
            self.yeni_soru_ekle_window.resize(2150, 600)  # Pencereyi ilk boyutta ayarlayın
            self.yeni_soru_ekle_window.show()

    # "Soru Seç" penceresini açan metot
    def open_soru_secimi_screen(self):
        if self.soru_secimi_window is None:
            self.soru_secimi_window = SoruSecimiLogic(self)
            self.soru_secimi_window.resize(1300, 300)  # Pencereyi ilk boyutta ayarlayın
            self.soru_secimi_window.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_app = MainApp()
    main_app.show()
    sys.exit(app.exec_())
