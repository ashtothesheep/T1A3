print("Welcome to knitting app!")


# menu for launch, provides structure
def create_menu():
    print("1. View pattern database")
    print("2. View yarn stash database")
    print("3. Enter new pattern")
    print("4. Enter new yarn")
    print("5. View tools")
    print("6. Exit application")
    choice = input("Enter your selection: ")
    return choice


# definition for option1
def patterns():
    print("Viewing pattern database:")

    import pandas as pd

    df = pd.read_csv("docs/Patterns.csv", encoding="utf-8")
    print(df.to_string())

def yarn_stash():
    print("Viewing yarn stash database:")
    yarn_dictionary = {
        'name': ['Tweedy', 'Herriot', 'Falklands Merino', 'Alpaca DK', 'Malabrigo Sock', 'Air'],
        'color': ['tweedy', '1073', 'heartfelt', 'fawn', 'irradiant', 'beige'],
        'type': ['8ply', '8ply', '8ply', '4ply', '4ply', '8ply'],
        'fibre': ['wool', 'alpaca', 'wool', 'alpaca', 'wool blend', 'acrylic']
    }
    # Print header
    print("{:<20} {:<20} {:<20} {:<20}".format('name', 'color', 'type', 'fibre'))

    
    for i in range(len(yarn_dictionary['name'])):
        name = yarn_dictionary['name'][i]
        color = yarn_dictionary['color'][i]
        yarn_type = yarn_dictionary['type'][i]
        fibre = yarn_dictionary['fibre'][i]

        # Print each row of the yarn stash, number indicates column widths
        print("{:<20} {:<20} {:<20} {:<20}".format(name, color, yarn_type, fibre))


# main script
users_choice = ""

while users_choice != "6":
    users_choice = create_menu()
    print(users_choice)

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
        break
    
    print("invalid selection, please choose a valid number")
        
print("Exiting Application...")
        



# Placeholder for other functions (yarn_stash(), enter_pattern(), enter_yarn(), tools()) as well



def enter_pattern():
    print("Entering new pattern:")
    # Implement the code to allow the user to enter a new pattern
    print("Placeholder for entering new pattern")


def enter_yarn():
    print("Entering new yarn:")
    # Implement the code to allow the user to enter a new yarn
    print("Placeholder for entering new yarn")


def tools():
    print("Viewing tools:")
    # Implement the code to display the tools information
    print("Placeholder for viewing tools")


