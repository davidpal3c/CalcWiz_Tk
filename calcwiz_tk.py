

class Calculator:
    def __init__(self):
        self.data_handler = Data_Handler()
        self.calc_operations = Calc_Operations()
        self.file_io = FileIO()
        self.user_interface = UserInterface()

    def run(self):
        # Main logic for running calcWiz
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


