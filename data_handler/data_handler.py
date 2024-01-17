import pandas as pd

class DataHandler:
    def __init__(self):
        # initialize as needed

    def handle_numerical_input(self, user_input):
        """Process user input and extract numerical values

        Parameters:
        - user_input (str): Raw user input.

        Returns:
        - tuple or None: Tuple of numerical values 
            extracted from the input.
        """
        try:
            # Your logic to process user input and extract numerical values
            # Example: Split input into a list and convert each item to a float
            numerical_values = [float(item) for item in user_input.split()]
            return tuple(numerical_values)
        except ValueError:
            print("Error: Invalid input. Please enter numerical values.")
            return None 
        Convert, validate, and return numerical input
        
        
    def read_csv_file(self, file_path):
        """
        Read numerical values from a CSV file.

        Parameters:
        - file_path (str): Path to the CSV file.

        Returns:
        - tuple or None: Tuple of numerical values extracted from the CSV file.
        """
        try:
            df = pd.read_csv(file_path)
            # Assuming the CSV file has a single column of numerical values
            numerical_values = df.iloc[:, 0].tolist()
            return tuple(numerical_values)
        except Exception as e:
            print(f"Error reading CSV file: {e}")
            return None

    def read_excel_file(self, file_path):
        """
        Read numerical values from an Excel file.

        Parameters:
        - file_path (str): Path to the Excel file.

        Returns:
        - tuple or None: Tuple of numerical values extracted from the Excel file.
        """
        try:
            df = pd.read_excel(file_path)
            # Assuming the Excel file has a single column of numerical values
            numerical_values = df.iloc[:, 0].tolist()
            return tuple(numerical_values)
        except Exception as e:
            print(f"Error reading Excel file: {e}")
            return None
        


    