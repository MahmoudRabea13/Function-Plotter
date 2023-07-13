from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap, QImage
from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QGridLayout,
    QLabel, QLineEdit, QPushButton, QMessageBox,
)
import matplotlib.pyplot as plt
from utilities.functions import FunctionPlotter

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        "This class contains all elements of the main window"
        self.setWindowTitle("Function Plotter")
        main_layout = QVBoxLayout()
        self.setLayout(main_layout)
        self.resize(800, 600)
        # init Upper part(Graph)
        upper_layout = QVBoxLayout()
        self.figure = plt.figure()
        self.canvas = self.figure.canvas
        upper_layout.addWidget(self.canvas)
        main_layout.addLayout(upper_layout)
        # input Lower part (4 boxes layout)
        lower_layout = QGridLayout()
        main_layout.addLayout(lower_layout)

        # First Box (handle first plot)
        first_box = QVBoxLayout()
        lower_layout.addLayout(first_box, 0, 0, 1, 1)

        first_box_title = QLabel("First Plot")
        first_box.addWidget(first_box_title)

        input_section_layout = QVBoxLayout()
        first_box.addLayout(input_section_layout)

        expression_label = QLabel("Enter the mathematical expression (using 'x' as the variable):")
        self.expression_input = QLineEdit()
        input_section_layout.addWidget(expression_label)
        input_section_layout.addWidget(self.expression_input)

        x_min_label = QLabel("Enter the minimum value of x:")
        self.x_min_input = QLineEdit()
        input_section_layout.addWidget(x_min_label)
        input_section_layout.addWidget(self.x_min_input)

        x_max_label = QLabel("Enter the maximum value of x:")
        self.x_max_input = QLineEdit()
        input_section_layout.addWidget(x_max_label)
        input_section_layout.addWidget(self.x_max_input)

        plot_button = QPushButton("Plot")
        plot_button.clicked.connect(self.plot_expression)
        first_box.addWidget(plot_button)

        # Second Box (handle second plot)
        second_box = QVBoxLayout()
        lower_layout.addLayout(second_box, 0, 1, 1, 1)

        second_box_title = QLabel("Second Plot")
        second_box.addWidget(second_box_title)

        input_section_layout2 = QVBoxLayout()
        second_box.addLayout(input_section_layout2)

        expression_label2 = QLabel("Enter the mathematical expression (using 'x' as the variable):")
        self.expression_input2 = QLineEdit()
        input_section_layout2.addWidget(expression_label2)
        input_section_layout2.addWidget(self.expression_input2)

        x_min_label2 = QLabel("Enter the minimum value of x:")
        self.x_min_input2 = QLineEdit()
        input_section_layout2.addWidget(x_min_label2)
        input_section_layout2.addWidget(self.x_min_input2)

        x_max_label2 = QLabel("Enter the maximum value of x:")
        self.x_max_input2 = QLineEdit()
        input_section_layout2.addWidget(x_max_label2)
        input_section_layout2.addWidget(self.x_max_input2)

        plot_button2 = QPushButton("Plot")
        plot_button2.clicked.connect(self.plot_expression2)
        second_box.addWidget(plot_button2)

        # Third Box (handle operations on result plot)
        third_box = QVBoxLayout()
        lower_layout.addLayout(third_box, 0, 2, 1, 1)

        third_box_title = QLabel("Result Plot")
        third_box.addWidget(third_box_title, alignment=Qt.AlignTop)

        divide_button = QPushButton("Divide")
        divide_button.clicked.connect(lambda: self.calculate_result_graph("Divide"))
        third_box.addWidget(divide_button, alignment=Qt.AlignTop)

        multiply_button = QPushButton("Multiply")
        multiply_button.clicked.connect(lambda: self.calculate_result_graph("Multiply"))
        third_box.addWidget(multiply_button, alignment=Qt.AlignTop)

        add_button = QPushButton("Add")
        add_button.clicked.connect(lambda: self.calculate_result_graph("Add"))
        third_box.addWidget(add_button)

        subtract_button = QPushButton("Subtract")
        subtract_button.clicked.connect(lambda: self.calculate_result_graph("Subtract"))
        third_box.addWidget(subtract_button)


        # Fourth Box (options box)
        color_box = QVBoxLayout()
        lower_layout.addLayout(color_box, 1, 0, 1, 3)

        fourth_box_title = QLabel("Options")
        color_box.addWidget(fourth_box_title)

        self.button_color = None
        change_button_color_button = QPushButton("Change Button Color")
        change_button_color_button.clicked.connect(self.change_button_color)
        color_box.addWidget(change_button_color_button)

        self.background_color = None
        change_background_color_button = QPushButton("Change Window Color")
        change_background_color_button.clicked.connect(self.change_background_color)
        color_box.addWidget(change_background_color_button)

        self.text_color = None
        change_text_color_button = QPushButton("Change Text Color")
        change_text_color_button.clicked.connect(self.change_text_color)
        color_box.addWidget(change_text_color_button)

        save_button = QPushButton("Save Graph")
        save_button.clicked.connect(self.save_graph)
        color_box.addWidget(save_button)

        self.ax1 = None  # Reference to the first subplot
        self.ax2 = None  # Reference to the second subplot
        self.ax3 = None  # Reference to the result subplot

        self.function_plotter = FunctionPlotter(self) 

    def plot_expression(self):

        self.function_plotter.plot_expression()

    def plot_expression2(self):
        self.function_plotter.plot_expression2()

    def calculate_result_graph(self, operation):
        self.function_plotter.calculate_result_graph(operation)

    def change_button_color(self):
        self.function_plotter.change_button_color()

    def change_background_color(self):
        self.function_plotter.change_background_color()

    def change_text_color(self):
        self.function_plotter.change_text_color()

    def apply_changes(self):
        self.function_plotter.apply_changes()

    def save_graph(self):
        self.function_plotter.save_graph()

    def show_error_message(self, message):
        self.function_plotter.show_error_message(message)

if __name__ == '__main__':
    app = QApplication([])
    # Set the window icon
    icon = QImage('icon.png')
    pixmap = QPixmap.fromImage(icon)
    #init main window
    app.setWindowIcon(pixmap)
    window = MainWindow()
    window.show()
    app.exec()
