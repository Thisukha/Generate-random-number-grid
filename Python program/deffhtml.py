import random
from tabulate import tabulate
from datetime import datetime




#Generating the HTML file
def writetohtml(runtime,gridvalues):
    filenamehtml = "assignment"+str(runtime)+".html"
    filehtml = open(filenamehtml,"w", encoding='utf-8')
    filehtml.write("<html>\n<head>\n<title> \nOutput Assignement Data in to a HTML file \n</title>\n</head>\n<body>")
    filehtml.write(tabulate(gridvalues, tablefmt="html"))
    filehtml.write("\n</body>\n</html>")
    filehtml.close()
