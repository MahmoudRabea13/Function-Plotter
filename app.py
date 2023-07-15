from PySide6.QtGui import QPixmap, QImage
from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel, QPushButton
)
from utilities.layout import MainWindow
class WelcomeWindow(QWidget):
    def __init__(self):
        #init the welcome window
        super().__init__()
        self.setWindowTitle("Welcome")
        self.setFixedSize(299, 139)
        layout = QVBoxLayout()
        self.setLayout(layout)
        image_label = QLabel()
        pixmap = QPixmap("assets/welcome.png")
        image_label.setPixmap(pixmap)
        layout.addWidget(image_label)
        #set the welcome window button
        self.button = QPushButton("Use Function Plotter")
        self.button.clicked.connect(self.open_main_window)
        layout.addWidget(self.button)
        self.main_window = None

    def open_main_window(self):
        "function to go from welcome page to main window"
        self.hide()
        self.main_window = MainWindow()
        self.main_window.show()

    def closeEvent(self, event):
        "function to keep main window open till a close event is triggered"
        if self.main_window is not None:
            self.main_window.close()
        event.accept()


if __name__ == '__main__':
    app = QApplication([])
    # Set the welcome icon
    icon = QImage('assets/icon.png')
    pixmap = QPixmap.fromImage(icon)
    app.setWindowIcon(pixmap)
    #init the welcome window
    welcome_window = WelcomeWindow()
    welcome_window.show()
    app.exec()
