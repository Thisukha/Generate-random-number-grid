from deffunction import generateGrid
from defftxt import writetotxt
from deffhtml import writetohtml


import sys
from datetime import datetime

def main():
   
    try: #Define number of rows and columns
        grid_size_input = sys.argv[1].upper()
        grid_size = grid_size_input.split('X')
        rows = int(grid_size[0])
        columns = int(grid_size[1])

    except: #Default values
        rows = 5
        columns = 5
  
    if rows< 3 or rows > 9 or columns < 3 or columns > 9: #Check whether Grid size is inside given dimensions 
        sys.exit("Grid dimensions must be between 3 X 3 or 9 X 9.") #If not exit the program
    grid, gridvalues = generateGrid(rows, columns)
    runtime = datetime.now().strftime("%Y%m%d-%H%M%S")
    writetotxt(runtime, grid)
    writetohtml(runtime, gridvalues)


if __name__=="__main__":
    main()
