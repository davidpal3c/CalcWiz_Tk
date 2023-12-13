
class CalculatorOperations:
    def __init__(self):
        # Initialize as needed

    # helper method to check if there's no input
    def _check_input_list(self, input_list):
        if input_list is None:
            raise ValueError("Input list cannot be None. ")
        
    def perform_addition(self, a, b):
        self._check_input_list(a)
        self._check_input_list(b)

    def perform_calculations(self, numerical_input):
        # Perform various calculator operations based on user input
        # Return the result of the calculations

