import numpy as np
import sympy as sp
from PySide6.QtWidgets import (QMessageBox,QColorDialog, QFileDialog)
import os 

class FunctionPlotter:
    def __init__(self, window):
        self.window = window
    def plot_expression(self):
        "first plot handler"
        # take inputs (x_min / x_max / expression)
        expr = self.window.expression_input.text() 
        x_min = self.window.x_min_input.text()
        x_max = self.window.x_max_input.text()

        #handle x min/max absence
        if not x_min or not x_max:
            self.window.show_error_message("Please provide both the minimum and maximum values of x.")
            return

        try:
            # handle if x min >= x max
            x_min = float(x_min)
            x_max = float(x_max)
            if x_min >= x_max:
                self.window.show_error_message("Invalid range. The minimum value of x should be less than the maximum value.")
                return
        except ValueError:
            # accept only +ve and -ve numbers only
            self.window.show_error_message("Invalid input. Please enter only positive or negative numbers for the minimum and maximum values.")
            return

        x = sp.symbols('x')
        try:
            # validate mathematical expression
            expr = sp.sympify(expr)
        except sp.SympifyError:
            self.window.show_error_message("Invalid mathematical expression.")
            return

        if not self.validate_expression(expr):
            # accept only x as variable
            self.window.show_error_message("Use 'x' as your only variable.")
            return

        x_vals = np.linspace(x_min, x_max, 100)
        y_vals = [expr.subs(x, val) for val in x_vals]


        if self.window.ax1 is None:
            self.window.ax1 = self.window.figure.add_subplot(131)
        else:
            #clear first plot to avoid overwrite
            self.window.ax1.clear()
        # plot first graph
        self.window.ax1.plot(x_vals, y_vals)
        self.window.ax1.set_xlabel('x')
        self.window.ax1.set_ylabel('y')
        self.window.ax1.set_title('Plot of {}'.format(expr))
        self.window.ax1.grid(True)
        self.window.canvas.draw()

    def plot_expression2(self):
        "second plot handler"
        expr = self.window.expression_input2.text()
        x_min = self.window.x_min_input2.text()
        x_max = self.window.x_max_input2.text()
        # handle x min/max absence
        if not x_min or not x_max:
            self.window.show_error_message("Please provide both the minimum and maximum values of x.")
            return

        try:
            # handle if x min >= x max
            x_min = float(x_min)
            x_max = float(x_max)
            if x_min >= x_max:
                self.window.show_error_message("Invalid range. The minimum value of x should be less than the maximum value.")
                return
        except ValueError:
            # accept only +ve and -ve numbers only
            self.window.show_error_message("Invalid input. Please enter only positive or negative numbers for the minimum and maximum values.")
            return

        x = sp.symbols('x')
        try:
            # validate mathematical expression
            expr = sp.sympify(expr)
        except sp.SympifyError:
            self.window.show_error_message("Invalid mathematical expression.")
            return

        if not self.validate_expression(expr):
            # accept only x as variable 
            self.window.show_error_message("Use 'x' as your only variable.")
            return

        x_vals = np.linspace(x_min, x_max, 100)
        y_vals = [expr.subs(x, val) for val in x_vals]

        if self.window.ax2 is None:
            self.window.ax2 = self.window.figure.add_subplot(132)
        else:
            # clear first plot to avoid overwrite
            self.window.ax2.clear()
        # plot second graph 
        self.window.ax2.plot(x_vals, y_vals)
        self.window.ax2.set_xlabel('x')
        self.window.ax2.set_ylabel('y')
        self.window.ax2.set_title('Plot of {}'.format(expr))
        self.window.ax2.grid(True)
        self.window.canvas.draw()

    def validate_expression(self, expr):
        "validate the mathematical expression and supported operands"
        variables = list(expr.free_symbols)
        if len(variables) != 1:
            return False

        variable = variables[0]
        return variable.name == 'x' and variable.is_Symbol and isinstance(variable, sp.Symbol)




    def calculate_result_graph(self, operation):
        "operations on result graph handler"
        expr1 = self.window.expression_input.text()
        expr2 = self.window.expression_input2.text()

        #handle if any/both graph(s) is/are absence
        if not expr1 or not expr2:
            self.window.show_error_message("Both graphs are required to perform the operation.")
            return

        x = sp.symbols('x')
        try:
            # validate mathematical expressions
            expr1 = sp.sympify(expr1)
            expr2 = sp.sympify(expr2)
        except sp.SympifyError:
            self.window.show_error_message("Invalid mathematical expression.")
            return
        # choose operation
        if operation == "Divide":
            result_expr = expr1 / expr2
        elif operation == "Multiply":
            result_expr = expr1 * expr2
        elif operation == "Add":
            result_expr = expr1 + expr2
        elif operation == "Subtract":
            result_expr = expr1 - expr2

        x_min = self.window.x_min_input.text()
        x_max = self.window.x_max_input.text()
        # recheck on x min/max to perform operation efficiently
        if not x_min or not x_max:
            self.window.show_error_message("Please provide both the minimum and maximum values of x.")
            return

        try:
            x_min = float(x_min)
            x_max = float(x_max)
            if x_min >= x_max:
                self.window.show_error_message("Invalid range. The minimum value of x should be less than the maximum value.")
                return
        except ValueError:
            self.window.show_error_message("Invalid input. Please enter only positive or negative numbers for the minimum and maximum values.")
            return

        x_vals = np.linspace(x_min, x_max, 100)
        y_vals = [result_expr.subs(x, val) for val in x_vals]

        if self.window.ax3 is None:
            self.window.ax3 = self.window.figure.add_subplot(133)
        else:
            # clear result plot to avoid overwrite
            self.window.ax3.clear()
        # plot result graph
        self.window.ax3.plot(x_vals, y_vals)
        self.window.ax3.set_xlabel('x')
        self.window.ax3.set_ylabel('y')
        self.window.ax3.set_title('Result of {}'.format(operation))
        self.window.ax3.grid(True)

        self.window.canvas.draw()


    def change_button_color(self):
        "button color change"
        color = QColorDialog.getColor()
        if color.isValid():
            self.window.button_color = color.name()
            self.window.apply_changes()

    def change_background_color(self):
        "background color change"
        color = QColorDialog.getColor()
        if color.isValid():
            self.window.background_color = color.name()
            self.window.apply_changes()

    def change_text_color(self):
        "text color change"
        color = QColorDialog.getColor()
        if color.isValid():
            self.window.text_color = color.name()
            self.window.apply_changes()

    def apply_changes(self):
        "apply different color changes"
        style_sheet = ""

        if self.window.button_color:
            style_sheet += f"QPushButton {{ background-color: {self.window.button_color}; }}"

        if self.window.background_color:
            style_sheet += f"MainWindow {{ background-color: {self.window.background_color}; }}"

        if self.window.text_color:
            style_sheet += f"QLabel, QLineEdit, QPushButton {{ color: {self.window.text_color}; }}"

        self.window.setStyleSheet(style_sheet)

    def save_graph(self):
        "save graph(s)"
        if not self.window.figure.axes:
            self.window.show_error_message("No graph to be saved.")
            return

        file_path, _ = QFileDialog.getSaveFileName(
            self.window, "Save Graph", os.path.expanduser("~"), "JPEG (*.jpg *.jpeg)"
        )

        if file_path:
            self.window.figure.savefig(file_path, format="jpeg")
            QMessageBox.information(
                self.window, "Graph Saved", "The graph has been saved successfully."
            )
    
    def clear_graph(self):
        "Deletes all plotted graphs"
        if self.window.ax1 is None and self.window.ax2 is None and self.window.ax3 is None:
            self.show_error_message("You don't have anything to clear.")
            return
        if self.window.ax1 is not None:
            self.window.figure.delaxes(self.window.ax1)
            self.window.ax1 = None
        if self.window.ax2 is not None:
            self.window.figure.delaxes(self.window.ax2)
            self.window.ax2 = None
        if self.window.ax3 is not None:
            self.window.figure.delaxes(self.window.ax3)
            self.window.ax3 = None
        self.window.canvas.draw()
        QMessageBox.information(self.window, "Graph cleared", "The graph has been cleared successfully.")
    def show_error_message(self, message):
        "error message handler"
        error_dialog = QMessageBox()
        error_dialog.setWindowTitle("Error")
        error_dialog.setText(message)
        error_dialog.setIcon(QMessageBox.Critical)
        error_dialog.exec()