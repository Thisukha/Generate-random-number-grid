Key Components:

Libraries Used:

random: Generates random numbers.
tabulate: Formats data into tables.
datetime: Works with dates and times.
Functions Created:

generateGrid(rows, columns): Generates a grid of random numbers with specified dimensions and creates a status list based on certain criteria.
writetotxt(runtime, grid): Writes the generated grid data to a text file, including the current date and time in the filename.
writetohtml(runtime, gridvalues): Writes the grid data to an HTML file, incorporating the current date and time in the filename.
Main Function (main()):

Parses command-line arguments to determine the grid size (rows x columns).
Handles default values if no arguments are provided.
Checks if the grid size is within specified dimensions (3x3 to 9x9) and exits if not.
Calls generateGrid() to create the grid and obtain formatted data.
Uses current date and time for file naming and calls file writing functions (writetotxt() and writetohtml()).
Usage:

The program is designed to be run from the command line, with the grid size specified as an argument (e.g., python program.py 4x4 generates a 4x4 grid).
Default values (5x5) are used if no arguments are provided.
