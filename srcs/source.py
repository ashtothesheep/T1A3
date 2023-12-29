print("Welcome to knitting app!")

import pandas as pd
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

    df = pd.read_csv("docs/Patterns.csv", encoding="utf-8")
    print(df.to_string())


#definition for option 2
def yarn_stash(yarn_dictionary):
    print("Viewing yarn stash database:")
    # Print header
    print("{:<20} {:<20} {:<20} {:<20}".format('name', 'color', 'type', 'fibre'))

    
    for i in range(len(yarn_dictionary['name'])):
        name = yarn_dictionary['name'][i]
        color = yarn_dictionary['color'][i]
        yarn_type = yarn_dictionary['type'][i]
        fibre = yarn_dictionary['fibre'][i]

        # Print each row of the yarn stash, number indicates column widths
        print("{:<20} {:<20} {:<20} {:<20}".format(name, color, yarn_type, fibre))
    return yarn_dictionary
#definition for option 3

def enter_pattern():
    print("Entering new pattern to database: ")
    
    #user input
    name = input("Enter the pattern name: ")
    designer = input("Enter the designers name: ")
    yarn_weight = input("Enter yarn weight required: ")
    meterage = input ("Enter meterage required: ")
    gauge = input("Enter pattern gauge: ")
    needles = input("Enter needles required: ")
    category = input("Enter pattern category: ")
    
    new_pattern = {
        'Name': [name],
        'Designer': [designer],
        'Yarn Weight': [yarn_weight],
        'Meterage': [meterage],
        'Gauge':[gauge],
        'Needle Sizes':[needles],
        'Category': [category]
    }
    df = pd.DataFrame(columns=['Name', 'Designer', 'Yarn Weight', 'Meterage', 'Gauge', 'Needle Sizes', 'Category'])
    try:
        df_existing = pd.read_csv("docs/Patterns.csv")
        
        # Convert the new pattern data to a DataFrame
        df_new_pattern = pd.DataFrame(new_pattern)
        try:
            df_existing = pd.read_csv("docs/Patterns.csv")
        except FileNotFoundError:
            df_existing = pd.DataFrame(columns=['Name', 'Designer', 'Yarn Weight', 'Meterage', 'Gauge', 'Needle Sizes', 'Category'])

        df_new_pattern = pd.DataFrame(new_pattern)

        df = pd.concat([df_existing, df_new_pattern], ignore_index=True)

        df.to_csv("docs/Patterns.csv", index=False)
        
    
    except FileNotFoundError:
    
        pass
    
    #save file
        df.to_csv("docs/Patterns.csv", index=False)

    print("Pattern added successfully!")

#entering new yarn to stash

def enter_yarn(yarn_dictionary):

    print("Entering new yarn to stash: ")
    attributes = ['name', 'color', 'type', 'fibre']
    new_yarn = {}
    for attribute in attributes:
        new_yarn[attribute] = input("Enter the yarn {}: ".format(attribute))
        
    for key, value in new_yarn.items():
        yarn_dictionary[key].append(value)
    print("Yarn added successfully!")
    return yarn_dictionary


# main script

yarn_dictionary = {
        'name': ['Tweedy', 'Herriot', 'Falklands Merino', 'Alpaca DK', 'Malabrigo Sock', 'Air'],
        'color': ['tweedy', '1073', 'heartfelt', 'fawn', 'irradiant', 'beige'],
        'type': ['8ply', '8ply', '8ply', '4ply', '4ply', '8ply'],
        'fibre': ['wool', 'alpaca', 'wool', 'alpaca', 'wool blend', 'acrylic']
    }
users_choice = ""

while users_choice != "6":
    users_choice = create_menu()
    print(users_choice)

    if users_choice == "1":
        patterns()
    elif users_choice == "2":
        yarn_stash(yarn_dictionary)
    elif users_choice == "3":
        enter_pattern()
    elif users_choice == "4":
        yarn_dictionary = enter_yarn(yarn_dictionary)
    elif users_choice == "5":
        tools()
    elif users_choice == "6":
        break
        
print("Exiting Application...")
        




def tools():
    print("Viewing tools:")
    # Implement the code to display the tools information
    print("Placeholder for viewing tools")


