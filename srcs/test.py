print("Welcome to knitting app!")

def main_menu():
    print("1. View pattern database")
    print("2. View yarn stash database")
    print("3. Enter new pattern")
    print("4. Enter new yarn")
    print("5. View tools")
    print("6. Exit application")
    choice = input("Enter your selection: ")
    return choice

def sub_menu():
    print("1. Sub-Option 1")
    print("2. Sub-Option 2")
    print("3. Back to main menu")
    choice = input("Select: ")
    return choice

def patterns():
    print("Viewing pattern database:")
    # Your pattern database code here...

def yarn_stash():
    print("Viewing yarn stash database:")
    # Your yarn stash code here...

def enter_pattern():
    print("Entering new pattern:")
    # Your enter pattern code here...

def enter_yarn():
    print("Entering new yarn:")
    # Your enter yarn code here...

def tools():
    print("Viewing tools:")
    # Your tools code here...

in_sub_menu = False

while True:
    if in_sub_menu:
        users_choice = sub_menu()
        if users_choice == "3":
            in_sub_menu = False  # Back to the main menu
    else:
        users_choice = main_menu()

        if users_choice == "1":
            patterns()
        elif users_choice == "2":
            yarn_stash()
        elif users_choice == "3":
            enter_pattern()
        elif users_choice == "4":
            enter_yarn()
        elif users_choice == "5":
            tools()
        elif users_choice == "6":
            print("Exiting Application...")
            break
        elif users_choice == "7":  # Go to the sub-menu
            in_sub_menu = True
        else:
            print("Invalid selection, please choose a valid number")
