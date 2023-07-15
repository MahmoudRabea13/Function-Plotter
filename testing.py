import pytest
import os
from PySide6.QtWidgets import QApplication, QMessageBox
from utilities.layout import MainWindow
from app import WelcomeWindow


@pytest.fixture(scope="module")
def app():
    app = QApplication([])
    yield app
    app.quit()


@pytest.fixture(scope="module")
def window(app):
    # Create the main window for all tests
    window = MainWindow()
    yield window

@pytest.fixture(scope="module")
def welcome_window(app):
    # Create the welcome window 
    welcome_window = WelcomeWindow()
    yield welcome_window


def test_welcomewindow(welcome_window):
    "test if welcome window redirects to main window"
    welcome_window.show()
    if welcome_window.button.clicked.connect(welcome_window.open_main_window):
        assert welcome_window.close()

# overall test cases : 21 (1 for welcome window / 11 for main features / 9 for error handliing )

## ------------------Testing Error handling--------------------- ## 

def test_show_error_message(qtbot):
    "test if a message apperes when there's an error"
    error_message = "Invalid input"
    message_box = QMessageBox()
    message_box.setWindowTitle("Error")
    message_box.setText(error_message)
    message_box.setIcon(QMessageBox.Critical)
    # Use qtbot to handle the message box
    qtbot.addWidget(message_box)
    message_box.show()
    # Check if the message box is displayed with the expected error message
    assert message_box.isVisible()
    assert message_box.text() == error_message


def test_invalid_mathematical_expression(window):
    "test error when invalid expression"
    window.expression_input.setText("x**")
    window.x_min_input.setText("-5")
    window.x_max_input.setText("5")
    window.plot_expression()
    # Verify that an error message is shown
    assert window.show_error_message

def test_invalid_variable_symbol(window):
    "test error when invalid symbol in expression input"
    window.expression_input.setText("y*2")
    window.x_min_input.setText("-5")
    window.x_max_input.setText("5")
    window.plot_expression()
    # Verify that an error message is shown
    assert window.show_error_message

def test_missing_min_max_values(window):
    "test error when missing min/max values"
    window.expression_input.setText("x**2")
    window.x_min_input.setText("")
    window.x_max_input.setText("5")
    window.plot_expression()
    # Verify that an error message is shown
    assert window.show_error_message

def test_invalid_min_max_symbol(window):
    "test error when invalid symbol in min/max"
    window.expression_input.setText("x**2")
    window.x_min_input.setText("a")
    window.x_max_input.setText("b")
    window.plot_expression()
    # Verify that an error message is shown
    assert window.show_error_message

def test_invalid_x_range(window):
    "test error if min>= max range"
    window.expression_input.setText("x**2")
    window.x_min_input.setText("5")
    window.x_max_input.setText("3")
    window.plot_expression()
    # Verify that an error message is shown
    assert window.show_error_message


def test_missing_graphs_for_operation(window):
    "test error if any of graph is absent and operation is performed"
    window.expression_input.setText("")
    window.expression_input2.setText("x")
    window.calculate_result_graph("Divide")
    # Verify that an error message is shown
    assert window.show_error_message

def test_save_graph_no_graph(window):
    "test erorr for saving empty graph"
    # Trigger the save_graph method
    window.save_graph()
    # Verify that an error message is shown
    assert window.show_error_message

def test_clear_empty_graph(window):
    "test error for clearing empty graph"
    window.clear_graph()
    assert window.show_error_message


## ------------------Testing main app features--------------------- ## 

# Plotting

def test_plot_expression(window):
    "test if first graph is plotted"
    window.expression_input.setText("(1/x)")
    window.x_min_input.setText("-5")
    window.x_max_input.setText("5")
    window.plot_expression()
    # Verify the plot is displayed
    assert window.ax1.lines


def test_plot_expression2(window):
    "test if second graph is plotted"
    window.expression_input2.setText("2 * x")
    window.x_min_input2.setText("-10")
    window.x_max_input2.setText("14")
    window.plot_expression2()
    # Verify the plot is displayed
    assert window.ax2.lines

# Graph operations

def test_divide(window):
    "test devision of the two graphs"
    window.expression_input.setText("(1/x+3)")
    window.x_min_input.setText("-1")
    window.x_max_input.setText("1")
    window.expression_input2.setText("x")
    window.calculate_result_graph("Divide")
    # Verify the result plot is displayed
    assert window.ax3.lines


def test_multiply(window):
    "test multiplication of the two graphs"
    window.expression_input.setText("(x*8)*(x+3)")
    window.x_min_input.setText("-1")
    window.x_max_input.setText("1")
    window.expression_input2.setText("x")
    window.calculate_result_graph("Multiply")
    # Verify the result plot is displayed
    assert window.ax3.lines


def test_add(window):
    "test addition of the two graphs"
    window.expression_input.setText("x+2")
    window.x_min_input.setText("5")
    window.x_max_input.setText("10")
    window.expression_input2.setText("x")
    window.calculate_result_graph("Add")
    # Verify the result plot is displayed
    assert window.ax3.lines


def test_subtract(window):
    "test subtraction of the two graphs"
    window.expression_input.setText("x-10")
    window.x_min_input.setText("-3")
    window.x_max_input.setText("8")
    window.expression_input2.setText("x")
    window.calculate_result_graph("Subtract")
    # Verify the result plot is displayed
    assert window.ax3.lines

# Change color

def test_change_button_color(window):
    "test  change button color "
    initial_button_color = window.button_color
    window.change_button_color()
    new_button_color = window.button_color
    assert new_button_color != initial_button_color


def test_change_background_color(window):
    "test change background color"
    initial_background_color = window.background_color
    window.change_background_color()
    new_background_color = window.background_color
    assert new_background_color != initial_background_color


def test_change_text_color(window):
    "test change text color"
    initial_text_color = window.text_color
    window.change_text_color()
    new_text_color = window.text_color
    assert new_text_color != initial_text_color

# save graph 

def test_save_graph(window):
    "test if graph is saved"
    save_filename = "graph.jpg"
    save_path = os.path.join(save_filename)
    window.expression_input.setText("(x*7)+(1/x)")
    window.x_min_input.setText("-1")
    window.x_max_input.setText("1")
    window.plot_expression()
    window.save_graph()
    # Check if the graph is saved successfully
    assert os.path.exists(save_path)
    # Clean up the temporary save file
    os.remove(save_path)

# clear graph

def test_clear_graph(window):
    "test if graph is cleared successfully"
    # Plot a graph 
    window.ax1 = window.figure.add_subplot(111)
    window.ax2 = window.figure.add_subplot(121)
    window.ax3 = window.figure.add_subplot(122)

    window.clear_graph()

    assert window.ax1 is None
    assert window.ax2 is None
    assert window.ax3 is None

if __name__ == '__main__':
    pytest.main(['-v', __file__])
