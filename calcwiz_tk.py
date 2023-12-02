

def console_menu():
    print("This is the main menu")



def main():
    while True:
        Welcome = input("Welcome to CalcWiz_Toolkit, press any key to continue...").upper().strip()
        
        if Welcome == "Y":
            console_menu()
        else:
            break

if __name__ == "__main__":
    main()


