import random
from tabulate import tabulate
from datetime import datetime

#Generating a txt file based on the program runtime and writing the output
def writetotxt(runtime, grid):
    runtime = datetime.now().strftime("%Y%m%d-%H%M%S")
    filenametxt = "assignment"+str(runtime)+".txt"
    with open(filenametxt, 'w', encoding='utf-8') as f:
        f.write(grid)
        f.close()
