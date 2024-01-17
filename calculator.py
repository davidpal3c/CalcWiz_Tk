# Example in calculator.py
# from data_handler import read_numeric_input
from calc_operations import calc_op


class Calculator:
    def __init__(self):
        self.data_handler = Data_Handler()
        self.calc_operations = Calc_Operations()
        self.file_io = FileIO()
        self.user_interface = UserInterface()

    def run(self):
        # Main logic for running calcWiz
        user_input = self.user_interface.get_user_input()
        numerical_input = self.data_handler.handle_numerical_input(user_input)
        result = self.calc_operations.perform_calculations(numerical_input)
        self.user_interface.display_output(result)


def main():
    # Handle user input, either from CLI or other sources
    numerical_input = read_numeric_input()

    # Instantiate CalculatorOperations class
    calculator = CalculatorOperations()

    # Determine the type of operation (list, stat, arithmetic, math)
    operation_type = numerical_input[0]

    # Call the appropriate method in CalculatorOperations
    if operation_type == 'list':
        result = calculator.list_operations(numerical_input[1:])
    elif operation_type == 'stat':
        result = calculator.stat_operations(numerical_input[1:])
    elif operation_type == 'arith':
        result = calculator.arith_operations(numerical_input[1:])
    elif operation_type == 'math':
        result = calculator.math_operations(numerical_input[1:])
    else:
        print("Invalid operation type")

    # Further process or display the result as needed
    print("Result:", result)


if __name__ == "__main__":
    calculator = Calculator()
    calculator.run()


