from os import path, system
def main():
    
    while True:
        system("cls")
        if path.exists("passwords.csv") == False:
            with open("passwords.csv", "w") as file:
                file.close
                
        while True:
            print("Options\n" \
            "1: Add Password\n" \
            "2: Remove Password\n" \
            "3: See all Passwords\n" \
            "4: Exit") # Print options for user
            
            try: 
                user_choice = int(input("Pick Option: "))
                
                if user_choice not in range(1, 5):
                    print("not a valid option")
                    
            except ValueError:
                print("Yeet")
            
            if user_choice == 1:
                add_password()
            elif user_choice == 2:
                remove_password()
            elif user_choice == 3:
                list_passwords()
            elif user_choice == 4:
                return print("Exited Program")
   
def add_password(): # Change ------------- >
    while True:
        print("1: Back\nType your Task")
        task = input("Enter username and password: ")
        if task == "1":
            return # Returns to main()
        else:
            with open("list.csv", "a") as file:
                file.write(f'- {task}\n')

# This function will remove a task from the list
def remove_password():
    temp_list = ["temp"] # temporay list to hold the file values
    row_n = 0 #
    print("Type back to return to start")
    with open("passwords.csv") as file:
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
            with open("passwords.csv", "w") as file:
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

# This function will list all tasks in the list.csv file and print them out
def list_passwords():
    print("Here is your passwords\n")
    with open("passwords.csv") as file:
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
                system("cls")
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

