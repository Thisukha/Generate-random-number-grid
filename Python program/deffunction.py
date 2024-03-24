import random
from tabulate import tabulate
from datetime import datetime



def generateGrid(rows,columns):
    outside_list = [] #The final list with all the grid values
    perc_list = [] #Status list
    for i in range(columns): 
        perc_list.append("OK") #Default value is "OK" for status list

    for i in range(0, rows, 1):
        nested_list = [] #Create new nested list(s) as per the grid values
        for j in range(0, columns, 1): #Populate the nested list with random numbers
            number = random.randint(1, 99) 
            nested_list.append(number)
        for x in range(len(nested_list)):
            if nested_list[x] < 10:
                nested_list[x] = "  "#Change the value to "  " if the list value is less than 10
                perc_list[x] = "NO" #Change the status to "No" if the number is less than 10
        outside_list.append(nested_list) #Add the nested list to the outside final list
    outside_list.append(perc_list) #Add the stats list to the final list

    grid = tabulate(outside_list, tablefmt="fancy_grid")
    print(grid) #Print Grid
    return grid, outside_list



        





