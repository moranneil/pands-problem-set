#Neil Moran 27th March 2019
#Solution Question9 second.py

#This imports the sys module to take in the file name as an arguement and assign it to a variable for the filename to be read
import sys

# The line below sys.argv[1] was adapted from the program test.py from this link https://www.tutorialspoint.com/python/python_command_line_arguments.htm
# It used the module sys and the function argv, this takes the name of the program and any text after and creates a list of arguements, the name of the program second.py is sys.argv[0]
# The 1st arguement after the program name sys.argv[1] is the file name, this is assigned to the variable file in line 10 below
file = sys.argv[1]

# the with statement is the recommended way to open a file
with open(file, 'r') as f:
  #linenumber is an integer variable to count or keep track of the current line number this is used to print every 2nd line of the file, linenumbers initial value is 0 so the first line in the file is linenumber 0
  linenumber = 0
  # The for loop reads each line of the file that was opened
  for line in f:
    # The line.rstrip strips the carraige return from each line as its read from the file, this removes the space as the line is read from the file.
    line = line.rstrip("\n")
    #The if statement checks if the linenumber is odd or even, if even it prints the line, therefore printing every 2nd line, ie line 0, 2, 4, 6, etc
    if linenumber % 2 == 0:
      print(line)
    #linenumber is increased by 1 for the next line
    linenumber = linenumber + 1
    