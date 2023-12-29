print("Welcome to knitting app!")

import pandas as pd


######################################################################################################################################
# menu for launch, provides structure
def test_create_menu():
    print("1. View pattern database")
    print("2. View yarn stash database")
    print("3. Enter new pattern")
    print("4. Enter new yarn")
    print("5. View tools")
    print("6. Exit application")
    choice = input("Enter your selection: ")
    return choice


######################################################################################################################################
# definition for option1
def test_patterns():
    print("Viewing pattern database:")

    df = pd.read_csv("docs/Patterns.csv", encoding="utf-8")
    print(df.to_string())


######################################################################################################################################
# definition for option 2
def test_yarn_stash(yarn_dictionary):
    print("Viewing yarn stash database:")
    # Print header
    print("{:<20} {:<20} {:<20} {:<20}".format("name", "color", "type", "fibre"))

    for i in range(len(yarn_dictionary["Name"])):
        name = yarn_dictionary["Name"][i]
        color = yarn_dictionary["Color"][i]
        yarn_type = yarn_dictionary["Yarn Weight"][i]
        fibre = yarn_dictionary["Fibre"][i]

        # Print each row of the yarn stash, number indicates column widths
        print("{:<20} {:<20} {:<20} {:<20}".format(name, color, yarn_type, fibre))
    return yarn_dictionary


######################################################################################################################################
# definition for option 3


def test_enter_pattern():
    print("Entering new pattern to database: ")

    # user input
    name = input("Enter the pattern name: ")
    designer = input("Enter the designers name: ")
    yarn_weight = input("Enter yarn weight required: ")
    meterage = input("Enter meterage required: ")
    gauge = input("Enter pattern gauge: ")
    needles = input("Enter needles required: ")
    category = input("Enter pattern category: ")

    new_pattern = {
        "Name": [name],
        "Designer": [designer],
        "Yarn Weight": [yarn_weight],
        "Meterage": [meterage],
        "Gauge": [gauge],
        "Needle Sizes": [needles],
        "Category": [category],
    }
    df = pd.DataFrame(
        columns=[
            "Name",
            "Designer",
            "Yarn Weight",
            "Meterage",
            "Gauge",
            "Needle Sizes",
            "Category",
        ]
    )
    try:
        df_existing = pd.read_csv("docs/Patterns.csv")

        # Convert the new pattern data to a dataframe
        df_new_pattern = pd.DataFrame(new_pattern)
        try:
            df_existing = pd.read_csv("docs/Patterns.csv")
        except FileNotFoundError:
            df_existing = pd.DataFrame(
                columns=[
                    "Name",
                    "Designer",
                    "Yarn Weight",
                    "Meterage",
                    "Gauge",
                    "Needle Sizes",
                    "Category",
                ]
            )

        df_new_pattern = pd.DataFrame(new_pattern)

        df = pd.concat([df_existing, df_new_pattern], ignore_index=True)

        df.to_csv("docs/Patterns.csv", index=False)

    except FileNotFoundError:
        pass

        # save file
        df.to_csv("docs/Patterns.csv", index=False)

    print("Pattern added successfully!")


######################################################################################################################################

# entering new yarn to stash, option 4


def test_enter_yarn(yarn_dictionary):
    print("Entering new yarn to stash: ")
    attributes = ["Name", "Color", "Yarn Weight", "Fibre"]
    new_yarn = {}
    for attribute in attributes:
        new_yarn[attribute] = input("Enter the yarn {}: ".format(attribute))

    for key, value in new_yarn.items():
        yarn_dictionary[key].append(value)
    print("Yarn added successfully!")
    return yarn_dictionary


######################################################################################################################################
# submenu for tools


def test_tools_submenu():
    print("Viewing tools:")
    print("1. Find yarn for pattern")
    print("2. Yarn meterage calculator")
    print("3. What can I make?")
    print("4. Exit tools")
    return input("Enter your selection: ")


######################################################################################################################################
def test_yarn_match(yarn_dictionary):
    print("Finding yarn for pattern: ")
    patterns_df = pd.read_csv("docs/Patterns.csv", encoding="utf-8")

    pattern_choice = input("Enter the pattern name: ")
    pattern = patterns_df[patterns_df["Name"] == pattern_choice]
    if pattern.empty:
        print("Pattern not found.")
        return
    pattern_yarn_weight = pattern["Yarn Weight"].values[0]

    matching_yarns = []
    for i in range(len(yarn_dictionary["Name"])):
        if yarn_dictionary["Yarn Weight"][i] == pattern_yarn_weight:
            matching_yarns.append(yarn_dictionary["Name"][i])
    if not matching_yarns:
        print("No matching yarn found in stash.")
    else:
        print("Matching yarn(s) found:")
        for yarn in matching_yarns:
            print(yarn)


######################################################################################################################################
def test_yarn_calculator():
    print("Calculating yarn meterage: ")

    yarn_gramms = float(input("Enter weight of skein/ball: "))
    yarn_meterage = float(input("Yarn meterage per skein/ball: "))
    total_qnty = float(input("Enter total quantity in gramms: "))

    total_meterage = total_qnty * (yarn_meterage / yarn_gramms)

    print(f"The total meterage in stash is {total_meterage} meters")


######################################################################################################################################
def test_what_can_i_make(yarn_dictionary):
    print("What can I make?")
    project_type = input("Enter project category you want to make: ")

    patterns_df = pd.read_csv("docs/Patterns.csv", encoding="utf-8")

    matching_patterns = patterns_df[patterns_df["Category"] == project_type]
    if matching_patterns.empty:
        print("No matching patterns found. Browse Ravelry!")
        return

    for index, pattern in matching_patterns.iterrows():
        matching_yarns = []
        for i in range(len(yarn_dictionary["Name"])):
            if yarn_dictionary["Yarn Weight"][i] == pattern["Yarn Weight"]:
                matching_yarns.append(yarn_dictionary["Name"][i])
        if matching_yarns:
            print(f"Suggested pattern: {pattern['Name']}")
            print("Matching yarn(s) from stash:")
            for yarn in matching_yarns:
                print(yarn)
                break


#############main script##############################################################################################################
######################################################################################################################################
######################################################################################################################################
yarn_dictionary = {
    "Name": [
        "Tweedy",
        "Herriot",
        "Falklands Merino",
        "Alpaca DK",
        "Malabrigo Sock",
        "Air",
    ],
    "Color": ["tweedy", "1073", "heartfelt", "fawn", "irradiant", "beige"],
    "Yarn Weight": ["8ply", "8ply", "8ply", "4ply", "4ply", "8ply"],
    "Fibre": ["wool", "alpaca", "wool", "alpaca", "wool blend", "acrylic"],
}
try:
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
            while True:
                tools_choice = tools_submenu()
                if tools_choice == "1":
                    yarn_match(yarn_dictionary)
                elif tools_choice == "2":
                    yarn_calculator()
                    pass
                elif tools_choice == "3":
                    what_can_i_make(yarn_dictionary)
                    pass

                elif tools_choice == "4":
                    print("Back to main menu: ")
                    break
                else:
                    print("Invalid selection, try again: ")

        elif users_choice == "6":
            break
except:
    print("Error occurred. ")
finally:
    print("Exiting Application...")
