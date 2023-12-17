from calc_operations.lst_op import get_sorted, get_filtered_val
from calc_operations.ht_op import get_max, get_min, has_key, get_keys

class CalculatorOperations:
    def __init__(self):
        # Initialize as needed
        pass
    # Helper method to check if there's no input
    def _check_input_list(self, input_list):
        if input_list is None:
            raise ValueError("Input list cannot be None.")
        
    def list_operations(self, numerical_input):
        operation_type, operand_a, operand_b = (*numerical_input, None, None, None)[:3]       
        if operation_type == 'sort_list':
            result = get_sorted(operand_a)
        elif operation_type == 'filter_list':
            result = get_filtered_val(operand_a, operand_b) # Assuming operand is a tuple (list, condition)
        else:
            raise ValueError("Unsupported operation type")

        return result

    def hash_table_operations(self, numerical_input):
        # Assume numerical_input contains the operation type and operands
        operation_type, operand_a, operand_b = numerical_input

        # Perform various hash table operations based on user input
        # Return the result of the calculations
        if operation_type == 'search_key':
            result = has_key(operand_a, operand_b)  # Assuming operand is a tuple (hash_table, key)
        elif operation_type == 'add_key_value':
            result = get_max(operand_a, operand_b)  # Assuming operand is a tuple (hash_table, key_value_pair)
        else:
            raise ValueError("Unsupported operation type for hash table")

        return result


    def perform_addition(self, a, b):
        self._check_input_list(a)
        self._check_input_list(b)
        # Rest of the addition logic
