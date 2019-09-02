import os #For Clearing Lines
checklist = list() #Creates Check List

# CREATE
def create(item):
    checklist.append(item)

# READ
def read(index):
    print (checklist[index])

# UPDATE
def update(index, item):
    checklist[index] = item

# DESTROY
def destroy(index):
    checklist.pop(index)

#Loops through checklist until all items are printed
def list_all_items():
    index = 0
    for list_item in checklist:
        print("{} {}".format(index, list_item))
        index += 1

#Adds index to checklist
#def mark_completed(index):
#    checklist.append()

def user_input(prompt):
    # the input function will display a message in the terminal
    # and wait for user input.
    user_input = input(prompt)
    return user_input

def select(function_code):
    # Create item
    if function_code == "A" or function_code == "a":
        input_item = user_input("Input item:\n")
        os.system('clear') #Clears terminal
        create(input_item)
    # Read item
    elif ((function_code == "R" or function_code == "r") and len(checklist) > 0): #Takes input and reads the index to print
        while True:
            item_index = user_input("Index Number?\n")
            try:
                os.system('clear')
                read(int(item_index))
            except:
                print("Not a Number or not in Index")
            else:
                break

    elif ((function_code == "D" or function_code == "d") and len(checklist) > 0): #Display list
        os.system('clear')
        list_all_items()

    elif ((function_code == "X" or function_code == "x") and len(checklist) > 0): #If x is selected, destroy the number given in index.
        while True:
            item_index = user_input("Index Number?\n")
            try:
                os.system('clear')
                destroy(int(item_index))
            except:
                print("Not a Number or not in Index")
            else:
                break

    elif ((function_code == "U" or function_code == "u") and len(checklist) > 0): #If u is selected, update the number and object given.
        while True:
            item_index = user_input("Index Number?\n")
            try:
                item_name = user_input("Name\n")
                os.system('clear')
                update(int(item_index),item_name)
            except:
                print("Not a Number or not in Index")
            else:
                break

    elif function_code == "Q" or function_code == "q":
        # This is where we want to stop our loop
        return False
    else:
        #Catch all
        os.system('clear')
        print("Unknown Option or Index is empty")
    return True

#Continuously asks for an input from the list, and uses the select function
#to give a repsonse.
running = True
while running:
    selection = user_input(
        "\nPress A to add to list, R to read from list, D to display list, X to destroy, U to update, and Q to quit\n")
    running = select(selection)
