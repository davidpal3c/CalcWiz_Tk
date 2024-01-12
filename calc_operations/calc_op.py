from calc_operations.lst_op import get_sorted, get_filtered_val
from calc_operations.ht_op import get_max, get_min, has_key, get_keys


# calcwiz_tk.py

from calc_operations.lst_op import get_sorted, get_filtered_val, get_index, get_slice, is_palindrome
from calc_operations.stat_op import get_lst_mean, get_lst_median, get_sample_std_dev_lst, get_population_std_dev_lst
from calc_operations.arithmetic_op import get_sum, get_average, get_max, get_min, get_product, get_count, get_cumulative_sum, get_add_constant
from calc_operations.math_op import get_exponential_func, get_sin_value, get_cos_value, get_tan_value


class CalculatorOperations:
    def __init__(self):
        # Initialize as needed
        pass

    # Helper method to check if there's no input
    def _check_input_list(self, input_list):
        if input_list is None:
            raise ValueError("Input list cannot be None.")
        # Additional code for the function, if needed

    # Helper method to check if input is a list
    def _check_instance_type(self, input_list):
        # Check if input is a list
        if not isinstance(input_list, list):
            raise TypeError("Input must be a list")

    def list_operations(self, numerical_input):
        """Perform list operations based on user input."""
        operation_type, operand_a, operand_b = (*numerical_input, None, None, None)[:3]
        # Perform various calculator operations based on user input
        # Return the result of the calculations
        if operation_type == 'sort_list':
            result = get_sorted(operand_a)
        elif operation_type == 'filter_list':
            result = get_filtered_val(operand_a, operand_b)
        elif operation_type == 'index_list':
            result = get_index(operand_a, operand_b)
        elif operation_type == 'slice_list':
            result = get_slice(operand_a, operand_b)
        elif operation_type == 'is_palindrome':
            result = is_palindrome(operand_a)
        else:
            raise ValueError(f"Unsupported operation type: {operation_type}")

        return result

    def stat_operations(self, numerical_input):
        """Perform statistical operations based on user input."""
        operation_type, operand_a, operand_b = (*numerical_input, None, None, None)[:3]
        if operation_type == 'mean_list':
            result = get_lst_mean(operand_a)
        elif operation_type == 'median_list':
            result = get_lst_median(operand_a)
        elif operation_type == 'sample_standard_deviation':
            result = get_sample_std_dev_lst(operand_a)
        elif operation_type == 'population_standard_deviation':
            result = get_population_std_dev_lst(operand_a)
        else:
            raise ValueError(f"Unsupported operation type: {operation_type}")

        return result

    def arith_operations(self, numerical_input):
        """Perform arithmetic operations based on user input."""
        operation_type, operand_a, operand_b = (*numerical_input, None, None, None)[:3]
        if operation_type == 'sum_list':
            result = get_sum(operand_a)
        elif operation_type == 'average_list':
            result = get_average(operand_a)
        elif operation_type == 'max_list':
            result = get_max(operand_a)
        elif operation_type == 'min_list':
            result = get_min(operand_a)
        elif operation_type == 'product_list':
            result = get_product(operand_a)
        elif operation_type == 'list_count':
            result = get_count(operand_a)
        elif operation_type == 'cumulative_sum':
            result = get_cumulative_sum(operand_a)
        elif operation_type == 'add_constant':
            result = get_add_constant(operand_a)
        else:
            raise ValueError(f"Unsupported operation type: {operation_type}")

        return result

    def math_operations(self, numerical_input):
        """Perform mathematical operations based on user input."""
        operation_type, operand_a, operand_b = (*numerical_input, None, None, None)[:3]
        if operation_type == 'exponential_function':
            return get_exponential_func(operand_a)
        elif operation_type == 'sin_value':
            return get_sin_value(operand_a)
        elif operation_type == 'cos_value':
            return get_cos_value(operand_a)
        elif operation_type == 'tan_value':
            return get_tan_value(operand_a)
        else:
            raise ValueError(f"Unsupported operation type: {operation_type}")
