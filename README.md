# T1A3 Terminal Application

Terminal Application for T1A3 Assignment, CoderAcademy 2023. 
---
## Description and usage

Terminal application designed as a knitting companion, including a database for patterns currently owned and yarn stash details. Designed as an electronic notebook that can produce some basic functions to go through current inventories of yarn and patterns.  
Includes some basic tools to match things and do calculations


## [Source Control](https://github.com/ashtothesheep/T1A3)

## Information about knitting and explanations

Explanation for non-knitters:
- Patterns: "recipes" for creating a knitted object, includes details for materials, size of knitting needles required, amount of yarn, gauge details and step by step instructions. 
- Gauge: Typically a 10xm x 10cm square made up by a specific amount of stitches, they vary depending on thickness of yarn and needles. ex.  it takes approx 20 stitches x 30 rows for an 8ply yarn using 4mm needles, or 12 stitches x 16 rows using 6mm needles for bulky yarn. 
- Yarn: Can be made by different types of fibres and fibre blends. They come in different thicknesses and content depending on use case. They can vary alot. 
- Meterage: Meterage of yarn depends on thickness. Meterage changes in almost every yarn type and within the same yarn types. 
- A pattern database: Helpful tool to sort out different categories of patterns, can be sorted by garment type, yarn type, designer etc. Every knitter usually has a database of patterns, either in electronic form or physical. It's like a library of recipe books. 
- Yarn stash : Most fibre artist like to collect yarn and have different amounts of yarns available. Sometimes you get leftover yarn from a project you want to use for something else. This is where the meterage calculator comes handy, removes all the butcher paper maths from the day-to-day. 


## Features

1. Adding yarn and patterns to database
2. View patterns and yarn database
3. Ability to match yarn from stash to patterns available
4. Tools to make suggestions of what to make and meterage calculator

## Implementation Plan

- [x] Create main menu 
- [x] Structure main ideas of functions around this

### Pattern Database Checklist & Implementation
- [x] Convert Notion database to csv form
- [x] Edit the csv file to be more readable by program, removing unecessary details.
- [x] Write code that can read through the csv file and produce output in terminal
- [x] Add function to main menu options

### Yarn Information Checkling & Implementation
- [x] Create a yarn list using dictionary function
- [x] Categorise the different characteristics
- [x] Format the table for output

### Enter new pattern/yarn Checklist & Implementation
- [x] Create all necessary user inputs
- [x] Add code to create dataframe if one doesn't exist already
- [x] Create code that uses concat or append to combine the input to the current data
- [x] Add error handling
- [x] Two ways of implementing similar functions, one of csv and one for dictionaries

### Styling guide Implementation
- [x] Used flake 8 and black to format to PEP8 

### Tools Checlist & Implementation

- [x] Created tools submenu
- [x] Find yarn for pattern function, used code to take different categories from the two database and match them up
- [x] Make yarn meterage calculator
- [x] Create what can i make function based on stock of patterns and yarn


## Help
 - Installation Steps
    1. Clone the repository:
    ssh
    git clone https://github.com/ashtothesheep/T1A3 
    2. Install requirements found below

 - Requirements
    black==23.12.1
    click==8.1.7
    colorama==0.4.6
    exceptiongroup==1.2.0
    iniconfig==2.0.0
    markdown-it-py==3.0.0
    mdurl==0.1.2
    mypy-extensions==1.0.0
    numpy==1.26.2
    packaging==23.2
    pandas==2.1.4
    pathspec==0.12.1
    platformdirs==4.1.0
    pluggy==1.3.0
    Pygments==2.17.2
    pytest==7.4.3
    python-dateutil==2.8.2
    pytz==2023.3.post1
    rich==13.7.0
    shellingham==1.5.4
    six==1.16.0
    tomli==2.0.1
    typer==0.9.0
    typing_extensions==4.9.0
    tzdata==2023.3



 ## Command lines

 To start the application, the source.py file needs to be run. 
 The application starts off with the main menu. To navigate the main menu you can enter the corresponding number of the options and press 'Enter'. 

 Ex. For Option 1 --> View pattern database , you need to press '1' in the Command line and press 'Enter'. 

 The main menu will cycle back up after selecting an option, with the exception of the Tools sub-menu. 
 
 When adding a pattern or a yarn type, the application will run you through all the inputs needed to update the databases as you go. 


 ## Resources
 https://www.geeksforgeeks.org/load-csv-data-into-list-and-dictionary-using-python/
 https://www.w3schools.com/python/pandas/pandas_getting_started.asp
 http://introtopython.org/terminal_apps.html
 https://realpython.com/python-typer-cli/
 https://www.w3schools.com/python/python_try_except.asp
 https://docs.pytest.org/en/7.4.x/
 https://typer.tiangolo.com/
 https://peps.python.org/pep-0008/
 https://www.geeksforgeeks.org/inserting-data-into-a-new-column-of-an-already-existing-table-in-mysql-using-python/
 http://pandas.pydata.org
https://code.visualstudio.com/docs/python/formatting