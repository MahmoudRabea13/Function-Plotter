from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap, QImage
from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout,
    QLabel, QLineEdit, QPushButton, QMessageBox
)
import matplotlib.pyplot as plt
from utilities.functions import FunctionPlotter

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Function Plotter")
        main_layout = QVBoxLayout()
        self.setLayout(main_layout)
        self.resize(900, 600)

        # Upper part (Graph)
        self.figure = plt.figure()
        self.canvas = self.figure.canvas
        main_layout.addWidget(self.canvas)

        # Lower part (Input and Controls)
        lower_layout = QHBoxLayout()
        main_layout.addLayout(lower_layout)

        # First Plot Box
        first_plot_box = QVBoxLayout()
        first_plot_box.setContentsMargins(10, 10, 10, 10)
        lower_layout.addLayout(first_plot_box)

        first_box_title = QLabel("First Plot")
        first_plot_box.addWidget(first_box_title)

        expression_label = QLabel("Expression (using 'x' as the variable):")
        self.expression_input = QLineEdit()
        first_plot_box.addWidget(expression_label)
        first_plot_box.addWidget(self.expression_input)

        x_min_label = QLabel("x_min:")
        self.x_min_input = QLineEdit()
        first_plot_box.addWidget(x_min_label)
        first_plot_box.addWidget(self.x_min_input)

        x_max_label = QLabel("x_max:")
        self.x_max_input = QLineEdit()
        first_plot_box.addWidget(x_max_label)
        first_plot_box.addWidget(self.x_max_input)

        plot_button = QPushButton("Plot")
        plot_button.clicked.connect(self.plot_expression)
        first_plot_box.addWidget(plot_button)

        # Second Plot Box
        second_plot_box = QVBoxLayout()
        second_plot_box.setContentsMargins(10, 10, 10, 10)
        lower_layout.addLayout(second_plot_box)

        second_box_title = QLabel("Second Plot")
        second_plot_box.addWidget(second_box_title)

        expression_label2 = QLabel("Expression (using 'x' as the variable):")
        self.expression_input2 = QLineEdit()
        second_plot_box.addWidget(expression_label2)
        second_plot_box.addWidget(self.expression_input2)

        x_min_label2 = QLabel("x_min:")
        self.x_min_input2 = QLineEdit()
        second_plot_box.addWidget(x_min_label2)
        second_plot_box.addWidget(self.x_min_input2)

        x_max_label2 = QLabel("x_max:")
        self.x_max_input2 = QLineEdit()
        second_plot_box.addWidget(x_max_label2)
        second_plot_box.addWidget(self.x_max_input2)

        plot_button2 = QPushButton("Plot")
        plot_button2.clicked.connect(self.plot_expression2)
        second_plot_box.addWidget(plot_button2)

        # Plot Operations and Color Picker Box
        operations_color_box = QVBoxLayout()
        operations_color_box.setContentsMargins(10, 10, 10, 10)
        lower_layout.addLayout(operations_color_box)

        # Plot Operations Box
        operations_box = QVBoxLayout()
        operations_color_box.addLayout(operations_box)

        operations_title = QLabel("Plot Operations")
        operations_box.addWidget(operations_title)

        divide_button = QPushButton("Divide")
        divide_button.clicked.connect(lambda: self.calculate_result_graph("Divide"))
        operations_box.addWidget(divide_button)

        multiply_button = QPushButton("Multiply")
        multiply_button.clicked.connect(lambda: self.calculate_result_graph("Multiply"))
        operations_box.addWidget(multiply_button)

        add_button = QPushButton("Add")
        add_button.clicked.connect(lambda: self.calculate_result_graph("Add"))
        operations_box.addWidget(add_button)

        subtract_button = QPushButton("Subtract")
        subtract_button.clicked.connect(lambda: self.calculate_result_graph("Subtract"))
        operations_box.addWidget(subtract_button)

        # Color Picker Box
        color_picker_box = QVBoxLayout()
        operations_color_box.addLayout(color_picker_box)

        color_picker_title = QLabel("Color Picker")
        color_picker_box.addWidget(color_picker_title)

        self.button_color = None
        change_button_color_button = QPushButton("Button Color")
        change_button_color_button.clicked.connect(self.change_button_color)
        color_picker_box.addWidget(change_button_color_button)

        self.background_color = None
        change_background_color_button = QPushButton("Window Color")
        change_background_color_button.clicked.connect(self.change_background_color)
        color_picker_box.addWidget(change_background_color_button)

        self.text_color = None
        change_text_color_button = QPushButton("Text Color")
        change_text_color_button.clicked.connect(self.change_text_color)
        color_picker_box.addWidget(change_text_color_button)

        # Save and Clear Buttons
        save_clear_layout = QHBoxLayout()
        save_clear_layout.setContentsMargins(10, 10, 10, 10)
        main_layout.addLayout(save_clear_layout)

        save_button = QPushButton("Save Graph")
        save_button.clicked.connect(self.save_graph)
        save_clear_layout.addWidget(save_button)

        clear_button = QPushButton("Clear Graph")
        clear_button.clicked.connect(self.clear_graph)
        save_clear_layout.addWidget(clear_button)

        # Function Plotter
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

    def clear_graph(self):
        self.function_plotter.clear_graph()

    def show_error_message(self, message):
        self.function_plotter.show_error_message(message)

if __name__ == '__main__':
    app = QApplication([])
    # Set the window icon
    icon = QImage('icon.png')
    pixmap = QPixmap.fromImage(icon)
    # Init main window
    app.setWindowIcon(pixmap)
    window = MainWindow()
    window.show()
    app.exec()
