import sys
from PySide6.QtGui import QPixmap, QImage
from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel, QPushButton
)
from utilities.layout import MainWindow
class WelcomeWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Welcome")
        self.setFixedSize(299, 139)

        layout = QVBoxLayout()
        self.setLayout(layout)

        image_label = QLabel()
        pixmap = QPixmap("assets/welcome.png")
        image_label.setPixmap(pixmap)
        layout.addWidget(image_label)

        self.button = QPushButton("Use Function Plotter")
        self.button.clicked.connect(self.open_main_window)
        layout.addWidget(self.button)

        self.main_window = None

    def open_main_window(self):
        self.hide()
        self.main_window = MainWindow()
        self.main_window.show()

    def closeEvent(self, event):
        if self.main_window is not None:
            self.main_window.close()
        event.accept()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    # Set the window icon
    icon = QImage('assets/icon.png')
    pixmap = QPixmap.fromImage(icon)
    app.setWindowIcon(pixmap)

    welcome_window = WelcomeWindow()
    welcome_window.show()

    sys.exit(app.exec())
