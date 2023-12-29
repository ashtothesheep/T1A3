# T1A3 Terminal Application

Terminal Application
---
## Description and usage

Terminal application designed as a knitting companion, including a database for patterns currently owned and yarn stash details. Designed as an electronic notebook that can produce some basic functions to go through current inventories of yarn and patterns.  
Includes some basic tools to match things and do calculations


## [Source Control](/srcs/Control)

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
2. View patterns and sort through relevant via filters
3. Ability to match yarn from stash to patterns available
4. Project section, has gauge calculator and a row counter

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
 pip3 install pandas

 - Dependencies

 - Requirements
 pandas 


 - Command lines

 - Resources
 https://www.geeksforgeeks.org/load-csv-data-into-list-and-dictionary-using-python/
 https://www.w3schools.com/python/pandas/pandas_getting_started.asp
 \http://introtopython.org/terminal_apps.html
 
 https://realpython.com/python-typer-cli/

 used black to reformat the code to follow styling guide
 https://www.w3schools.com/python/python_try_except.asp
 https://docs.pytest.org/en/7.4.x/
 https://typer.tiangolo.com/
