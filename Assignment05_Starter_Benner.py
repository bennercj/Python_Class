#-------------------------------------------------#
# Title: Working with Dictionaries
# Dev:   RRoot
# Date:  July 16, 2012
# ChangeLog: (Who, When, What)
#   RRoot, 11/02/2016, Created starting template
#   CBenner, 11/20/2018, Added code to complete assignment 5
#https://www.tutorialspoint.com/python/python_dictionary.htm
#-------------------------------------------------#

#-- Data --#
# declare variables and constants

# objFile = An object that represents a file
objFileName = "ToDo.txt"
# strData = A row of text data from the file
strData = ""
# dicRow = A row of data separated into elements of a dictionary {Task,Priority}
dicRow = ""
# lstTable = A dictionary that acts as a 'table' of rows
lstTable = []
# strMenu = A menu of user options
# strChoice = Capture the user option selection

strchoice = ""

#-- Input/Output --#
# User can see a Menu (Step 2)
# User can see data (Step 3)
# User can insert or delete data(Step 4 and 5)
# User can save to file (Step 6)

#-- Processing --#
# Step 1
# When the program starts, load the any data you have
# in a text file called ToDo.txt into a python Dictionary.

# Step 2
# Display a menu of choices to the user

# Step 3
# Display all todo items to user

# Step 4
# Add a new item to the list/Table

# Step 5
# Remove a new item to the list/Table

# Step 6
# Save tasks to the ToDo.txt file

# Step 7
# Exit program
#-------------------------------

objFileName = "C:\_PythonClass\Assignment05\Todo.txt"
strData = ""
dicRow = {}
lstTable = []
lstRow = []
lstMaster = []

# Step 1 - Load data from a file
    # When the program starts, load each "row" of data
objTextFile = open(objFileName, "r")
for line in objTextFile:
    lstRow = line.split(",")
    dicRow = {"Task": lstRow[0],"Priority":lstRow[1]}
    # in "ToDo.txt" into a python Dictionary.
    # Add the each dictionary "row" to a python list "table"

# Step 2 - Display a menu of choices to the user
while(True):
    print ("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 4] - "))
    print()#adding a new line

    # Step 3 -Show the current items in the table
    if (strChoice.strip() == '1'):
        print("*************************")
        print("Current Data stored in table: ")
        for line in lstMaster:
            lstTemp = []
            for Key, Value in line.items():
                strTemp = myValue
                lstTemp.append(strTemp)
            strDisplay = lstTemp[0] + "," + lstTemp[1]
            print(strDisplay)
        print("*************************")
        continue
    # Step 4 - Add a new item to the list/Table
    elif(strChoice.strip() == '2'):
        strNewTask = input("Enter a new Chore: ")
        strNewPriority = input("What is the chore's priority level?")
        dicNewRow = {"Chore":strNewTask, "Priority Level": strNewPriority}
        lstMaster.append(dicNewRow)
        continue
    # Step 5 - Remove a new item to the list/Table


    elif(strChoice.strip() == '3'):
        strRemoval = str(input("Remove which chore?: "))
        for chore in lstTable:
            lstTemp.remove(strTemp)
        else:
            print(score, "isn't in the high scores list.")

        continue
    # Step 6 - Save tasks to the ToDo.txt file
    elif(strChoice == '4'):
        strSaveit = input('Save data to file? (y/n)')
        if (strSaveit.lower() == 'y'):
            objFile = open(objFileName, 'w')
            for row in lstMaster:
                objFile.write(str(row))
            print("Your Data is Saved!")
        continue
    elif (strChoice == '5'):
        break #and Exit the program

1
