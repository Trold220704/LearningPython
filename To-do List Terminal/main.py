import sys
import os.path

def main():
    # Impleneted while loop in main function after chatgpt gave advice on it
    # This is to stop calling the main() from other functions and just return to it
    while True:
        os.system("cls")
        print("To-do List")
        
        # Checks if there is a list.csv file and if there isnt it makes one
        if os.path.exists("list.csv") == False:
            with open("list.csv") as file:
                file.close
        
        # While loop for the main function
        while True:
            try:
                #This prints the options that the user has
                print("Options" \
                "1: Add Task\n" \
                "2: Remove Task\n" \
                "3: See all Tasks\n" \
                "4: Exit")
                # This checks for the user input
                user_input = int(input("Which Option do you want: "))

                #This will check if the user input is over 3 and if it is it will continue the program and print "Not a valid option"
                if user_input > 4:
                    print("Not a valid Option")
                    continue
                break
            # This will catch if the user inputs anything other than a number and return a error
            except ValueError:
                print("Not a valid Option try again\n")

        # If the user inputs 2 it will start the  add_task funtion
        if user_input == 1:
            os.system("cls")
            add_task()
        # If the user inputs 2 it will start the remove_task function
        elif user_input == 2:
            os.system("cls")
            remove_task()
        # If the user inputs 2 it will start the list_task function
        elif user_input == 3:
            os.system("cls")
            list_tasks()
        # If the user input 4 it will exit the program
        elif user_input == 4:
            sys.exit("Program Exited")

    
# This function will add a task to the task list
def add_task():
    while True:
        print("1: Back\nType your Task or go back with 1")
        task = input("What task to you want to add: ")
        if task == "1":
            return # Returns to main()
        else:
            with open("list.csv", "a") as file:
                file.write(f'- {task}\n')




# This function will remove a task from the list
def remove_task():
    temp_list = ["temp"] # temporay list to hold the file values
    row_n = 0 #
    print("Type back to return to start")
    with open("list.csv") as file:
        # Removes the trailing \n so that it doesnt give unwatnted spaces in the print and makes the list more clean
        file = [x.strip("\n") for x in file]
        # This loop adds a number to each line in the list and also adds each line to a temp list 
        # so that it can be read and writen again later
        for row in file:
            row_n +=1
            temp_list.append(row)
            print(f"{row_n}: {row}")

    # Essenes of the remove function
    while True:
        user_input = input("Which task do you want to remove?\n")

        #Checks if the user wants to go back to the main menu
        if user_input == "back":
            with open("list.csv", "w") as file:
                temp_list.pop(0)
                for _ in temp_list:
                    file.write(f"{_}\n")
            return
            
        
        # try function to remove what the user selects
        try: 
            # Converts the users input to int so it can be used in the code
            user_input = int(user_input)
            # Checks if the users number is in the range of the list
            if user_input <= row_n:
                # Removes 1 count from the list to update the if statements requirements
                row_n -= 1
                # removes task that the user selcted
                temp_list.pop(user_input)
                #temp number for the for loop that prints the new list after one is removed
                temp_number = 0
                for _ in temp_list[1:]:
                    temp_number +=1
                    print(f"{temp_number}: {_}")
            else:
                # prints if the user selected a number that isnt on the list
                print(f"There is not a task on {user_input}")
        except ValueError:
            # Sends a print if the user selcted something that isnt accpeted in the program
            print("ValueError")    
    



        
    pass


# This function will list all tasks in the list.csv file and print them out
def list_tasks():
    print("Here is your list\n")
    with open("list.csv") as file:
        print(f"{file.read()}\n")
    while True:
        try:
            #This prints the options that the user has
            print("Options\n" \ 
                "1: Back to start\n")
            # This checks for the user input
            user_input = int(input("Which Option do you want: "))
            #This will check if the user input is over 3 and if it is it will continue the program and print "Not a valid option"
            if user_input > 2:
                os.system("cls")
                print("Not a valid Option")
                continue
            break
        # This will catch if the user inputs anything other than a number and return a error
        except ValueError:
            print("Not a valid Option try again\n")
    
    if user_input  == 1:
        return


if __name__ == "__main__":
    main()