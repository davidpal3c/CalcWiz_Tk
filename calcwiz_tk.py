

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
        pass


def main():
    while True:
        Welcome = input("Welcome to CalcWiz_Toolkit, press any key to continue...").upper().strip()
        
        if Welcome == "Y":
            console_menu()
        else:
            break

if __name__ == "__main__":
    main()


